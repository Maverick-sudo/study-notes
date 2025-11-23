#!/usr/bin/env python3
import os
import shutil
from pathlib import Path
import glob

base = Path('.')

# Find files by pattern matching
files_to_move = {
    "PHP*DOCUMENTATION.md": "web-development/backend/php/",
    "*JavaScript*Introduction.md": "web-development/frontend/javascript/",
    "*HyperText*Markup*Language*.md": "web-development/frontend/html/"
}

moved = 0
for pattern, target_dir in files_to_move.items():
    matches = glob.glob(pattern)
    if not matches:
        # Try with non-breaking spaces
        pattern_alt = pattern.replace(' ', '\xa0')
        matches = glob.glob(pattern_alt)
    
    for filename in matches:
        if filename.endswith('.md') and not filename.startswith('README'):
            source = base / filename
            target_path = base / target_dir
            target_path.mkdir(parents=True, exist_ok=True)
            target = target_path / filename
            
            if source.exists():
                shutil.move(str(source), str(target))
                print(f"✓ Moved: {filename} → {target_dir}")
                moved += 1

print(f"\n✅ Done! Moved {moved} files.")

