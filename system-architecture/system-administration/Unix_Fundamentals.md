# Unix Fundamentals

## Command Line Interface (CLI)

A command line interface (CLI) is a command screen or text interface called a shell that allows users to interact with a program. A useful tool for understanding commands is [explainshell.com](https://explainshell.com/).

On BSD-based Unix systems, you may encounter different types of terminals:

-   **Real TTY (`/dev/ttyX`)**: An actual virtual keyboard/screen pair.
-   **PTY (`/dev/pts/X`)**: A software-made fake TTY that pretends to be a keyboard/screen.
-   **tmux**: Multiplexes shells inside your session without creating new keyboards, running within a TTY or PTY.

## Fixing GPG Key Errors

If you encounter an error indicating that a GPG key has expired or is invalid, you may need to update the key for the repository.

1.  **Download the updated key**:
    ```bash
    wget -q -O - https://archive.kali.org/archive-key.asc | sudo apt-key add -
    ```

2.  **Update and upgrade again**:
    ```bash
    sudo apt update
    sudo apt full-upgrade -y
    ```

## Executable Python Scripts

Python scripts can be made directly executable, similar to shell scripts.

To do this, add a "shebang" line at the very beginning of the script and give the file executable permissions. The `#!` must be the first two characters of the file.

```bash
#!/usr/bin/env python3
```

This line tells the system to use the `python3` interpreter, assuming it is in the user's `PATH`. On some platforms, this first line must end with a Unix-style line ending (`\n`), not a Windows (`\r\n`) line ending. The hash character (`#`) is used to start a comment in Python.

Give the script executable permissions using the `chmod` command:

```bash
chmod +x myscript.py
```

On Windows, there is no "executable mode." The Python installer automatically associates `.py` files with `python.exe`, so double-clicking a file will run it as a script. If the extension is `.pyw`, the console window that normally appears is suppressed.

## Listing Sudo Permissions

You can list the allowed (and forbidden) commands for a user.

```bash
sudo -l
```

If no command is specified, the `-l` (list) option will list the allowed commands for the invoking user on the current host. If a command is specified and permitted, the fully-qualified path to the command is displayed along with any command line arguments. If a command is specified but not allowed, `sudo` will exit with a status value of 1. If the `-l` option is specified with an `l` argument (`-ll`), or if `-l` is specified multiple times, a longer list format is used.

## Shebang

A shebang (`#!`) is a character sequence at the beginning of a script that specifies the path to the interpreter for executing it. It does not signify a binary file. For example: `#!/bin/sh`, `#!/bin/zsh`, or `#!/bin/bash`.

## Bash Scripting

Bash is a scripting language that runs within the terminal on most Linux distros, as well as macOS. Shell scripts are a sequence of Bash commands within a file, combined to achieve more complex tasks than simple one-liners. They are especially useful for automating system administration tasks such as backups.

### Bash Variables

> Please note that for variables to work, you cannot leave a space between the variable name, the `=` sign, and the value. Variable names also cannot have spaces. You must add a `$` to the front of a variable name to use it, similar to JavaScript template literals `${variableName}` but without the curly braces.

### Debugging Bash Scripts

Debugging is an important part of programming. Bash has built-in features to simplify this process. To debug the syntax of a script, you can run it with `bash -x`:

```bash
bash -x ./fileName.sh
```

This command outputs each command before it is executed, prefixed with a `+` sign, followed by the command's output. This makes it easy to spot where you have gone wrong. You can also debug a specific section of a script by inserting `set -x` before the section and `set +x` after it.

---

## Interacting with Amazon S3

The following is a process for interacting with an Amazon S3 bucket using the AWS CLI, uploading a PHP shell to execute remote commands, and setting up a reverse shell. The files stored in an S3 bucket are called S3 objects.

You can interact with an S3 bucket using the `awscli` utility. It can be installed and configured on Linux using the following command:

```bash
apt install awscli && aws configure
```

### S3 Commands

-   **Listing S3 Buckets:**
    ```bash
    aws --endpoint=http://s3.Server.AWS s3 ls
    ```
    This lists all S3 buckets available at the specified endpoint.

-   **Listing Objects in a Bucket:**
    ```bash
    aws --endpoint=http://s3.Server.AWS s3 ls s3://Server.AWS
    ```

## Security Concepts

### Unrestricted File Upload Vulnerabilities

Unrestricted file upload vulnerabilities occur when a web server allows users to upload files without sufficient validation. If an attacker can upload an executable script (like a `.php` file) and then browse to it, the server may execute that script.

-   **Risk**: Remote Code Execution (RCE).
-   **Mitigation**:
    -   Validate file types and extensions (allowlisting).
    -   Store uploaded files outside the web root.
    -   Rename uploaded files to randomized identifiers.
    -   Disable script execution in upload directories.

### Reverse vs. Bind Shells

-   **Bind Shell**: The attacker connects *to* the target (Target listens on a port). This is often blocked by firewalls (ingress filtering).
-   **Reverse Shell**: The target connects *back* to the attacker (Attacker listens). This often bypasses firewalls because outbound traffic (egress) is frequently less restricted than inbound.

### Defensive Monitoring

System administrators should monitor for:

-   Unusual outbound connections (e.g., servers connecting to external IPs on arbitrary ports).
-   Processes spawned by web server users (e.g., `www-data` spawning `bash` or `sh`).
-   Unexpected open ports or listening services (checking with `netstat` or `ss`).

## Common Commands

### Netcat (nc)

Netcat is a networking utility for reading from and writing to network connections using TCP or UDP. It is often used for debugging network issues.

-   **Listen Mode**: `nc -lvnp [port]`
    -   `-l`: Listen
    -   `-v`: Verbose
    -   `-n`: No DNS lookup (IPs only)
    -   `-p`: Port

### grep

The `grep` command searches for patterns in text.

#### Recursive Search

This command searches for the pattern "passw" in all files and directories recursively, starting from the current directory.

```bash
grep -ri 'passw' *
```

-   `-r`: Recursively searches subdirectories.
-   `-i`: Ignores case (case-insensitive search).

#### Piped Search

This command concatenates all files in the current directory into a single stream and then searches that stream for the pattern "passw".

```bash
cat * | grep -i passw*
```

The `grep -ri 'passw' *` command is generally more efficient and reliable for searching through files and directories, as it inherently handles directories and binary files without issue. In contrast, `cat * | grep ...` can generate errors if `cat` tries to read directories or non-text files.

### find

The `find` command is useful for searching the target system for important information.

#### Basic Usage

-   `find . -name flag1.txt`: Find the file named `flag1.txt` in the current directory.
-   `find /home -name flag1.txt`: Find the file named `flag1.txt` in the `/home` directory.
-   `find / -type d -name config`: Find the directory named `config` under `/`.
-   `find /home -user frank`: Find all files for user `frank` under `/home`.

#### Searching by Permissions

-   `find / -type f -perm 0777`: Find files with `777` permissions.
-   `find / -perm a=x`: Find executable files.

#### Searching by Time

-   `find / -mtime 10`: Find files that were modified in the last 10 days.
-   `find / -atime 10`: Find files that were accessed in the last 10 days.
-   `find / -cmin -60`: Find files changed within the last hour (60 minutes).
-   `find / -amin -60`: Find files accessed within the last hour (60 minutes).

#### Searching by Size

-   `find / -size 50M`: Find files with a 50MB size. This can also be used with `+` (larger than) and `-` (smaller than).

#### Suppressing Errors

The `find` command can generate errors that make the output hard to read. You can redirect errors to `/dev/null` for a cleaner output.

-   For files: `find . -type f -name "search" 2>/dev/null`
-   For directories: `find . -type d -name "search" 2>/dev/null`

#### Finding Writable/Executable Locations

-   `find / -writable -type d 2>/dev/null`: Find world-writable folders.
-   `find / -perm -222 -type d 2>/dev/null`: Find world-writable folders.
-   `find / -perm -o w -type d 2>/dev/null`: Find world-writable folders.
-   `find / -perm -o x -type d 2>/dev/null`: Find world-executable folders.
-   `find / -perm -o r -type d 2>/dev/null`: Find world-readable folders.

#### SUID Files

Commonly noted as SUID (Set owner User ID), this special permission allows a file to execute as the user who owns it, regardless of the user running the command. This can be used to escalate privileges.

-   `find / -perm -u=s -type f 2>/dev/null`: Find files with the SUID bit set.

#### File Types

The `-type` flag filters by file type:

-   `b`: block special
-   `c`: character special
-   `d`: directory
-   `f`: regular file
-   `l`: symbolic link
-   `p`: FIFO
-   `s`: socket

### strings

The `strings` command makes it possible to view the human-readable characters within any file. Its main purpose is to help determine the file type, but it can also be used to extract text.

### chmod

The `chmod` (change file mode) utility modifies the file mode bits (permissions) of files and directories. It can also be used to modify Access Control Lists (ACLs).

Permissions are grouped into user, group, and other.

-   `r`: readable
-   `w`: writable
-   `x`: executable
-   `-`: empty permission
-   `d`: directory

Permissions can also be represented numerically:

-   `4`: read
-   `2`: write
-   `1`: execute

### chown

The `chown` (change owner) utility modifies the user and/or group ownership of a file.

### whatis

Displays one-line manual page descriptions.

### apropos

Searches the manual page names and descriptions.

### man

Formats and displays the on-line reference manual pages.

### which

Locates a command.

### pushd / popd

Puts the current working directory onto a stack and allows you to return to it later.

### updatedb

Updates the database used by the `locate` command.

### nano

A command-line text editor that can interpret and compile many programming languages. It takes an optional filename argument.

### file

A standard program for recognizing the type of data contained in a computer file.

### readlink

Displays the value of a symbolic link.

### stat

Displays information about a file, such as size, permissions, and modification times. Read, write, or execute permissions are not required, but all directories in the path must be searchable.

### wget

Allows you to download files from the web via HTTP. You provide the address of the resource you wish to download.

### ps

The `ps` utility displays information about running processes.

```bash
ps -ax | grep <application_name>
```

This command reveals the processes associated with a running application.

### ping

The `ping` command is used to test whether a connection to a remote resource is possible by sending ICMP ECHO_REQUEST packets. It can also be used to determine the IP address of a server. Packets are transmitted via ICMP (type 8 for request, type 0 for response). Pinging `localhost` or `127.0.0.1` can help diagnose network card failures, while pinging a domain name can help resolve DNS issues.

### netstat

Resolves and displays network statistics such as current network connections and port activities.

-   `netstat -a`: Shows all listening ports and established connections.
-   `netstat -at` or `netstat -au`: Lists TCP or UDP protocols respectively.
-   `netstat -l`: Lists ports in "listening" mode.
-   `netstat -s`: Lists network usage statistics by protocol.
-   `netstat -tp`: Lists connections with the service name and PID information.
-   `netstat -i`: Shows interface statistics.
-   `netstat -ano`: A common usage that displays all sockets, does not resolve names, and displays timers.

## Networking

### Network Configuration

Commands used to view and manage network interface information.

-   `ipconfig` (Windows)
-   `ifconfig` (older Linux/macOS)
-   `ip a` / `ip addr` (modern Linux)
-   `arp -a` (displays the ARP table)

### Time-to-Live (TTL)

Time-to-live (TTL) is a value for the period of time that a packet should exist on a network before being discarded. It is a counter or timestamp embedded in each packet. When the predefined timespan or event count expires, the packet is either discarded or revalidated. In networking, TTL prevents data packets from circulating indefinitely and helps determine how long a packet has been in circulation.

### tcpdump

You can start a `tcpdump` listener to capture packets. The following command listens for ICMP traffic, which is used by `ping`.

```bash
sudo tcpdump ip proto \\icmp -i <interfaceName>
```

### traceroute

The `traceroute` command resolves the route that data packets take from a local network to an internet destination, providing more information than `ping`. It works by sending packets with a low TTL to elicit ICMP `Time Exceeded` messages from intermediate hops.

-   **Linux**: `traceroute <destination>` (operates over UDP by default)
-   **Windows**: `tracert <destination>` (operates over ICMP by default)

### whois

The `whois` utility looks up registration records for domain names and IP addresses from databases maintained by Network Information Centers (NICs).

> **Note**: You may need to install `whois` before using it. On Debian-based systems, this can be done with `sudo apt update && sudo apt-get install whois`.

### nslookup

`nslookup` (Name Server Look Up) finds the IP address of a domain name.

The syntax is `nslookup [-type=RECORD] [DOMAIN_NAME] [SERVER]`.

-   `type`: The record type to query (e.g., `A` for IPv4, `AAAA` for IPv6).
-   `DOMAIN_NAME`: The domain to look up.
-   `SERVER`: The DNS server to query (e.g., Cloudflare `1.1.1.1`, Google `8.8.8.8`, Quad9 `9.9.9.9`).

### dig

`dig` (Domain Information Groper) is a flexible tool for interrogating DNS name servers. It's useful for viewing the TTL (Time To Live) of a DNS record, which indicates how long the record should be cached.

The syntax is `dig @server name type`.

-   `@server`: The name or IP address of the name server to query.
-   `name`: The name of the resource record to look up.
-   `type`: The type of query (e.g., `ANY`, `A`, `MX`, `SIG`). If omitted, `dig` performs a lookup for an `A` record.

### host

The `host` utility is a simple tool for performing DNS lookups, converting names to IP addresses and vice versa.

The syntax is `host {name} [server]`.

-   `name`: The domain name or IP address to look up.
-   `server`: (Optional) The name or IP address of a specific name server to query instead of the system default.

## File Permissions

The process of converting source code into an executable involves compilers (like GNU) turning text-based scripts into binary scripts.

### chmod

The `chmod` command changes file modes or permissions.

-   **Syntax**: `chmod +perm fileName` or `chmod -perm fileName`
-   `+` adds a permission, `-` removes it.
-   Permissions can be `r` (read), `w` (write), and `x` (execute).

### chown

The `chown` command changes the user and/or group ownership of a file.

## Process Management

### Daemons and Namespaces

A system daemon like `systemd` (or `launchd` on macOS) is one of the first processes started at boot. Other programs are started as child processes of the daemon. The OS uses namespaces to isolate processes from each other, splitting up system resources like CPU and RAM for security.

### systemctl

The `systemctl` command allows you to interact with the `systemd` process. The equivalent on macOS is `launchctl`.

-   **Syntax**: `systemctl [option] [service]`
-   **Options**: `start`, `stop`, `enable` (start at boot), `disable`.

### ps

The `ps` utility displays information about your active processes. Processes are the programs running on your machine, managed by the kernel. Each process has a Process ID (PID).

### top

The `top` command provides a real-time, sorted list of system processes and their statistics, which refreshes automatically.

## Privilege Escalation

### LXD

LXD is a management API for LXC containers. A user in the local `lxd` group can instantly escalate their privileges to root on the host OS, regardless of `sudo` rights. This vulnerability can be exploited by using a custom image to mount the host's root filesystem. The exploit involves building a custom Alpine image, transferring it to the target, and using it to spawn a privileged container.

For more details, see:

-   [HackTricks: LXD Privilege Escalation](https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/interesting-groups-linux-pe/lxd-privilege-escalation.html#lxdlxc-group---privilege-escalation)
-   [Hacking-Articles: LXD Privilege Escalation](https://www.hackingarticles.in/lxd-privilege-escalation/)

The simplified steps are:

1.  **On the attacker machine:**
    -   Download a pre-built Alpine image from the official LXC repository.
2.  **On the host machine:**
    -   Import the downloaded image for LXD.
    -   Initialize the image inside a new container.
    -   Mount the host filesystem inside the container (e.g., at `/mnt/root`).

## Shell Operators and Redirection

### Job Control

-   **`&`**: The ampersand operator allows you to run a command in the background of your terminal. You can also use `Ctrl + Z` to send a running process to the background.
-   **`fg`**: The foreground command brings a backgrounded process back to the foreground.

### Shell Operators

-   **`&&`**: Combines multiple commands, executing the next command only if the previous one succeeds.
-   **`>`**: Redirects the output of a command to a file, overwriting the file's contents.
-   **`>>`**: Appends the output of a command to a file.
-   **`;`**: Separates commands to be run in sequence, regardless of whether the previous command succeeds or fails.
-   **`|` (pipe)**: Allows separate processes to communicate. The output of the command on the left is used as the input for the command on the right.
    -   An **unnamed pipe** exists only within the kernel and cannot be accessed by the processes that created it.
    -   A **named pipe** (FIFO) is a file on the filesystem that allows processes to communicate. FIFO stands for "First In, First Out," meaning the order of bytes is preserved.

### I/O Redirection

Redirection operators are used to control where a command's output is sent (stdout and stderr) and where it gets its input from (stdin).

#### Standard File Descriptors

-   **`0`**: `stdin` (standard input)
-   **`1`**: `stdout` (standard output)
-   **`2`**: `stderr` (standard error)

#### Redirection Operators

The `n>&m` syntax redirects file descriptor `n` to the same location as file descriptor `m`. If `n` is omitted, it defaults to `1` (stdout).

-   `>&`: Redirects both `stdout` and `stderr` to a file.
-   `>&2`: Redirects `stdout` to `stderr`.
-   `2>&1`: Redirects `stderr` to wherever `stdout` is currently going.
-   `2>`: Redirects `stderr` to a file.
-   `&>`: Redirects both `stdout` and `stderr` to a file (a common shorthand).
-   `0>&1`: Redirects `stdin` to wherever `stdout` is currently directed.
-   `<>`: Opens a file for both reading and writing on `stdin`.

## System Administration

### Automated Job Execution (Cron)

`crontab` is used to schedule and manage cron jobs (automated tasks). A crontab is a special file with formatting that the `cron` process recognizes to execute each line.

| Value | Description           |
| :---- | :-------------------- |
| MIN   | Minute (0-59)         |
| HOUR  | Hour (0-23)           |
| DOM   | Day of the month (1-31) |
| MON   | Month (1-12)          |
| DOW   | Day of the week (0-6) |
| CMD   | Command to be executed|

The crontab file is structured as follows:

```bash
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of the month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
# │ │ │ │ │
# * * * * * <command to execute>

# Use @reboot to run a command once at boot.
@reboot /path/to/script.sh
```

You can edit the crontab file with `crontab -e`.

#### Cron Permissions

-   `/etc/cron.allow`: If this file exists, a user must be listed in it to use cron jobs.
-   `/etc/cron.deny`: If `cron.allow` does not exist, a user must *not* be listed in this file to use cron jobs.

### Linux Filesystem Hierarchy

-   `/`: The root directory of the entire file system hierarchy.
-   `/bin`: Essential command binaries for all users.
-   `/sbin`: System binaries, typically used by the system administrator.
-   `/boot`: Contains all files needed for the OS to boot.
-   `/dev`: Device files, including terminals and hardware.
-   `/etc`: Host-specific, system-wide configuration files. The `/etc/hosts` file is used to resolve a hostname to an IP address before querying DNS. You can add an entry like this:
    ```bash
    sudo echo "IP_ADDRESS FQDN" | sudo tee -a /etc/hosts
    ```
-   `/home`: Users' home directories.
-   `/lib`: System libraries required by binaries in `/bin` and `/sbin`.
-   `/media` & `/mnt`: Mount points for removable media and temporary filesystems.
-   `/opt`: Optional application software packages.
-   `/proc`: A virtual filesystem providing process and kernel information as files.
-   `/root`: The home directory for the root user.
-   `/run`: A temporary filesystem that stores volatile runtime data.
-   `/srv`: Site-specific data served by the system (e.g., for web or FTP servers).
-   `/sys`: A virtual filesystem for interacting with the kernel.
-   `/tmp`: Temporary files that are often not preserved between reboots.
-   `/usr`: User utilities and applications.
-   `/var`: Variable data, such as logs (`/var/log`), that changes as the system runs.
-   `.conf` or `.config`: Files that often contain application configurations and sensitive information.

### User and Password Files

#### /etc/passwd

The `/etc/passwd` file stores essential user account information required during login. It is a plain text file that contains a list of the system’s accounts. It should have general read permission, but write access must be limited to the root account.

#### /etc/passwd format

The file contains one entry per line for each user, with seven fields separated by a colon (`:`):
`TestUser:x:0:0:root:/root:/bin/bash`

-   **Username**: The login name (1-32 characters).
-   **Password**: `x` indicates the encrypted password is stored in `/etc/shadow`.
-   **User ID (UID)**: A unique ID for each user. UID `0` is for root.
-   **Group ID (GID)**: The primary group ID for the user.
-   **User ID Info**: A comment field for extra information (e.g., full name).
-   **Home directory**: The absolute path to the user's home directory upon login.
-   **Command/shell**: The absolute path to the user's default shell (e.g., `/bin/bash`).

### PATH Environment Variable

`PATH` is an environmental variable that specifies the directories containing executable programs. When a user runs a command, the shell searches these directories to find the corresponding executable.

To view the current `PATH`:

```bash
echo $PATH
```

To add a directory (like `/bin` or the current directory `.`) to the `PATH`:

```bash
export PATH=/bin:$PATH
export PATH=.:$PATH
```

### GTFOBins

GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems. The project collects legitimate functions of Unix binaries that can be abused for tasks like breaking out of restricted shells, escalating privileges, transferring files, and spawning shells.

### Landscape Server

A Landscape Server is a systems management tool by Canonical for managing fleets of Ubuntu computers from a centralized web interface or API.

-   **Core Functionality**: Centralized management, inventory tracking, software and patch management, monitoring, automation, user management, compliance, and reporting.
-   **Key Features**: Web UI, REST API, scalability, custom dashboards, alerting, and Role-Based Access Control (RBAC).
-   **Deployment**: Can be self-hosted or managed by Canonical.

### Kali Undercover Mode

To prevent unnecessary attention in public, Kali Undercover mode changes the look and feel of your Kali desktop to resemble Windows 10.

```bash
kali-undercover
```

## Package Management

The `apt` command is part of the APT suite of tools for managing software packages and sources.

-   `apt update`: Fetches the latest information about available packages.
-   `apt-get upgrade`: Upgrades installed packages.
-   `apt-get dist-upgrade` or `apt full-upgrade`: Upgrades the core operating system as well as packages.
-   `apt-get clean`: Cleans the local repository of retrieved package files.
-   `apt-get install -f`: Fixes broken dependencies.
-   `dpkg --configure -a`: Configures all unpackaged packages.
-   `dpkg -i <software.deb>`: Installs a Debian package.
-   `git clone <url>`: Clones a repository from a version control system like GitHub.

## Python Tools

### bpython

A fancy interface for the Python interpreter with features like in-line syntax highlighting, autocomplete, and auto-indentation.

### Simple HTTP Server

Python provides a simple `http.server` module that turns your computer into a web server to serve files from the directory you run it in.

```bash
python3 -m http.server
```

## Security and Encryption

### OpenSSL

OpenSSL is a cryptography toolkit for SSL/TLS. It can be used for creating keys, certificates, digests, and for encryption/decryption.

### scp

`scp` (secure copy) allows you to securely transfer files between two computers using the SSH protocol for authentication and encryption.

### sftp

`sftp` is a file transfer client with an FTP-like command interface that also uses SSH.

### sshd

`sshd` is the SSH daemon that runs on the server, listening for client connections.

-   **Linux**: `service ssh start`, `service ssh stop`, `service ssh restart`
-   **macOS**: `sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist`
-   **Windows**: `Start-Service sshd`

## Firmware

### Legacy BIOS vs. UEFI

-   **Legacy BIOS**: A 16-bit firmware that uses a Master Boot Record (MBR), limiting disk sizes to 2TB. It has a text-only interface.
-   **UEFI**: A modern 32-bit or 64-bit firmware that uses a GUID Partition Table (GPT), supporting much larger disks. It features a graphical interface and security features like Secure Boot.

### Redirection Output Table

| Syntax      | Visible in Terminal (stdout/stderr) | Visible in File (stdout/stderr) | Existing File |
| :---------- | :---------------------------------- | :------------------------------ | :------------ |
| `>`         | no / yes                            | yes / no                        | overwrite     |
| `>>`        | no / yes                            | yes / no                        | append        |
| `2>`        | yes / no                            | no / yes                        | overwrite     |
| `2>>`       | yes / no                            | no / yes                        | append        |
| `&>`        | no / no                             | yes / yes                       | overwrite     |
| `&>>`       | no / no                             | yes / yes                       | append        |
| `| tee`     | yes / yes                           | yes / no                        | overwrite     |
| `| tee -a`  | yes / yes                           | yes / no                        | append        |
| `|& tee`    | yes / yes                           | yes / yes                       | overwrite     |
| `|& tee -a` | yes / yes                           | yes / yes                       | append        |

## Other Topics

### QEMU

QEMU is an emulator and virtualizer. For example, it can be used to virtualize Windows on an M1 Mac. See [this MacRumors thread](https://forums.macrumors.com/threads/success-virtualize-windows-10-for-arm-on-m1-with-alexander-grafs-qemu-hypervisor-patch.2272354/) for details.

### Network Controllers

Network Controllers provide a centralized GUI to monitor and configure multiple network devices. However, they can be vulnerable to attacks like MAC address spoofing, which can poison switch forwarding tables or ARP tables.

### Scapy for ARP Poisoning

Scapy is a powerful packet manipulation tool. In the context of ARP poisoning:

-   `hwsrc`: Sender hardware address (SHA)
-   `psrc`: Sender protocol address (SPA)
-   `hwdst`: Target hardware address (THA)
-   `pdst`: Target protocol address (TPA)

Broadcasting to `FF:FF:FF:FF:FF:FF` delivers a packet to all stations on the local network.

### Scapy Commands

```
sr               : Send and receive packets at layer 3
sr1              : Send packets at layer 3 and return only the first answer
srp              : Send and receive packets at layer 2
srp1             : Send and receive packets at layer 2 and return only the first answer
arpcachepoison   : Poison target's cache with (your MAC,victim's IP) couple
```

### NetfilterQueue

To use `netfilterqueue` with Python, you need to install it:

```bash
apt-get install build-essential python-dev libnetfilter-queue-dev
pip3 install -U git+https://github.com/kti/python-netfilterqueue
```

To send packets to the queue, use `iptables`:

```bash
iptables -I INPUT -d 192.168.0.0/24 -j NFQUEUE --queue-num 1
```

### Chisel

Chisel is a fast TCP/UDP tunnel, transported over HTTP, secured via SSH.

-   **Server**:
    ```bash
    chisel server -p 8000 --reverse
    ```
-   **Client**:
    ```bash
    ./chisel client 10.10.14.55:8000 R:8001:127.0.0.1:8000
    ```

## Mobile Security Tools

1.  **Needle**
    -   **Use**: iOS app security testing on jailbroken devices.
    -   **Features**: Checks for insecure data storage, weak encryption, and reverse engineering risks.
2.  **APKX**
    -   **Use**: Android APK decompilation.
    -   **Features**: Decompiles APKs into readable source code (Java or Smali) for analysis.
3.  **Drozer**
    -   **Use**: Android app vulnerability assessment.
    -   **Features**: Interacts with app internals to find and exploit exposed components.