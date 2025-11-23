#!/usr/bin/env python3
"""
Organize markdown study notes into a GitHub-ready folder structure
based on their topics and Table of Contents.
"""

import os
import shutil
from pathlib import Path
import re

# Define the folder structure and file mappings
FOLDER_STRUCTURE = {
    "web-development": {
        "frontend": {
            "html": ["- -HyperText Markup Language Tutorial- -.md"],
            "css": ["Cascading Style Sheet.md"],
            "javascript": ["JavaScript Introduction.md"],
            "react": ["React@JS-Framework.md"],
            "jquery": ["jQuery@JS-libraries.md"]
        },
        "backend": {
            "php": ["PHP DOCUMENTATION.md"]
        }
    },
    "programming-languages": {
        "python": ["PYTHON.md"]
    },
    "networking": {
        "protocols": ["Networking Protocols.md"],
        "cloud-networking": ["AZ-700 (Azure Network Engineer Associate) && AWS Certified Advanced….md"],
        "virtual-networking": ["From Packet Tracer to Multi-Vendor Labs: Understanding Virtual….md"],
        "system-administration": ["Unix Fundamentals.md"]
    },
    "security": {
        "ethical-hacking": ["CyberSecurity &Ethical Hacking.md"],
        "web-security": ["OWASP -> Open Web Application Security Project TOP-10 Vulnerabilities.md"]
    },
    "system-architecture": {
        "reverse-engineering": ["Reverse Engineering & System Architecture.md"]
    }
}

# Map all files to their categories (for verification)
ALL_FILES = {
    "- -HyperText Markup Language Tutorial- -.md": ("web-development", "frontend", "html"),
    "Cascading Style Sheet.md": ("web-development", "frontend", "css"),
    "JavaScript Introduction.md": ("web-development", "frontend", "javascript"),
    "React@JS-Framework.md": ("web-development", "frontend", "react"),
    "jQuery@JS-libraries.md": ("web-development", "frontend", "jquery"),
    "PHP DOCUMENTATION.md": ("web-development", "backend", "php"),
    "PYTHON.md": ("programming-languages", "python"),
    "Networking Protocols.md": ("networking", "protocols"),
    "AZ-700 (Azure Network Engineer Associate) && AWS Certified Advanced….md": ("networking", "cloud-networking"),
    "From Packet Tracer to Multi-Vendor Labs: Understanding Virtual….md": ("networking", "virtual-networking"),
    "Unix Fundamentals.md": ("networking", "system-administration"),
    "CyberSecurity &Ethical Hacking.md": ("security", "ethical-hacking"),
    "OWASP -> Open Web Application Security Project TOP-10 Vulnerabilities.md": ("security", "web-security"),
    "Reverse Engineering & System Architecture.md": ("system-architecture", "reverse-engineering")
}

def create_folder_structure(base_path):
    """Create the folder structure."""
    for category, subcategories in FOLDER_STRUCTURE.items():
        category_path = base_path / category
        category_path.mkdir(exist_ok=True)
        
        for subcategory, files in subcategories.items():
            subcategory_path = category_path / subcategory
            subcategory_path.mkdir(exist_ok=True)

def move_files(base_path):
    """Move files to their appropriate folders."""
    moved_files = []
    
    # Use the ALL_FILES mapping for simpler logic
    for filename, (category, *path_parts) in ALL_FILES.items():
        source_file = base_path / filename
        if source_file.exists():
            # Build target path
            target_dir = base_path / category
            for part in path_parts:
                target_dir = target_dir / part
            
            target_file = target_dir / filename
            # Ensure target directory exists
            target_dir.mkdir(parents=True, exist_ok=True)
            
            shutil.move(str(source_file), str(target_file))
            relative_path = target_dir.relative_to(base_path)
            moved_files.append((filename, str(relative_path)))
            print(f"✓ Moved: {filename} → {relative_path}/")
        else:
            print(f"✗ Not found: {filename}")
    
    return moved_files

def create_readme(base_path, moved_files):
    """Create a comprehensive README.md file."""
    readme_content = """# Study Notes Repository

A comprehensive collection of study notes organized by topic and category.

## 📚 Table of Contents

"""
    
    # Generate navigation structure
    for category, subcategories in FOLDER_STRUCTURE.items():
        category_name = category.replace("-", " ").title()
        readme_content += f"\n### {category_name}\n\n"
        
        for subcategory, files in subcategories.items():
            subcategory_name = subcategory.replace("-", " ").title()
            readme_content += f"#### {subcategory_name}\n\n"
            
            for filename in files:
                # Clean filename for display
                display_name = filename.replace(".md", "").replace("-", " ").replace("_", " ")
                # Find the actual path
                file_path = f"{category}/{subcategory}/{filename}"
                readme_content += f"- [{display_name}]({file_path})\n"
            readme_content += "\n"
    
    readme_content += """
## 📖 Categories

### Web Development
Frontend and backend web development technologies including HTML, CSS, JavaScript, React, jQuery, and PHP.

### Programming Languages
Core programming language documentation and tutorials.

### Networking
Network protocols, cloud networking, virtual networking, and system administration.

### Security
Cybersecurity, ethical hacking, and web application security best practices.

### System Architecture
Reverse engineering and system architecture concepts.

---

## 🚀 Getting Started

Browse the folders above to find notes on specific topics. Each markdown file contains:
- Summary
- Table of Contents
- Detailed content

## 📝 Notes

All notes were converted from PDF format and organized for easy navigation and study.

---
*Last updated: Auto-generated*
"""
    
    readme_path = base_path / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"\n✓ Created README.md")

def create_category_readmes(base_path):
    """Create README files for each category."""
    category_descriptions = {
        "web-development": {
            "title": "Web Development",
            "description": "Frontend and backend web development technologies, frameworks, and best practices."
        },
        "programming-languages": {
            "title": "Programming Languages",
            "description": "Core programming language documentation, syntax, and concepts."
        },
        "networking": {
            "title": "Networking",
            "description": "Network protocols, cloud networking, virtual networking, and system administration."
        },
        "security": {
            "title": "Security",
            "description": "Cybersecurity, ethical hacking, web application security, and vulnerability assessment."
        },
        "system-architecture": {
            "title": "System Architecture",
            "description": "Reverse engineering, system architecture, and low-level programming concepts."
        }
    }
    
    for category, subcategories in FOLDER_STRUCTURE.items():
        category_path = base_path / category
        readme_content = f"# {category_descriptions[category]['title']}\n\n"
        readme_content += f"{category_descriptions[category]['description']}\n\n"
        readme_content += "## Topics\n\n"
        
        for subcategory, files in subcategories.items():
            subcategory_name = subcategory.replace("-", " ").title()
            readme_content += f"### {subcategory_name}\n\n"
            
            for filename in files:
                display_name = filename.replace(".md", "").replace("-", " ").replace("_", " ")
                file_path = f"{subcategory}/{filename}"
                readme_content += f"- [{display_name}]({file_path})\n"
            readme_content += "\n"
        
        readme_path = category_path / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"✓ Created {category}/README.md")

def main():
    """Main function to organize the study notes."""
    base_path = Path('.')
    
    print("Creating folder structure...")
    create_folder_structure(base_path)
    
    print("\nMoving files to appropriate folders...")
    moved_files = move_files(base_path)
    
    print("\nCreating README files...")
    create_readme(base_path, moved_files)
    create_category_readmes(base_path)
    
    print(f"\n✅ Organization complete! {len(moved_files)} files organized.")
    print("\nFolder structure created:")
    for category, subcategories in FOLDER_STRUCTURE.items():
        print(f"  📁 {category}/")
        for subcategory in subcategories.keys():
            print(f"    📁 {subcategory}/")

if __name__ == '__main__':
    main()

