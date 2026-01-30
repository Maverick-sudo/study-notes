# Assembly Language Notes

## About

This document contains notes on Assembly language programming, covering:
- LC-3 ISA (Instruction Set Architecture)
- x86-64 Assembly (Intel/AMD)
- Instruction formats and addressing modes
- Memory organization
- I/O mechanisms
- Interrupts and system calls

Derived from OCR-extracted handwritten and printed study notes, with focus on low-level computing concepts.

---

## Introduction to Computing Systems

### From High-Level to Machine Language

```mermaid
flowchart LR
    HL[High-Level Language] --> Assembly[Assembly Language]
    Assembly --> Machine[Machine Language]
    
    style HL fill:#e1f5ff
    style Assembly fill:#fff4e1
    style Machine fill:#ffe1e1
```

<!-- Diagram showing translation hierarchy -->

**Assembly language** instructions are translated into binary instructions (opcodes) for the machine to execute.

- **Low-level language** instructions → Assembly Translator → Machine language
- **High-level language** source code → Compiler & Interpreters → Machine language

Usually the case that each ISA has only one assembly language. Each assembly language instruction translates into one binary instruction (opcode) for the machine.

Assembly language is one step friendlier to make the programming process more friendly compared to direct machine language programming.

---

## LC-3 ISA (Little Computer 3)

<!-- OCR correction: "Regulers" → "registers", "pomber" → "pointer" -->

### Registers

**Registers** are small memory storage areas built into the CPU processor.

- **Volatile memory** (like RAM)
- LC-3 ISA has 8 general-purpose registers: **R0 → R7**
- A separate **Program Counter (PC)** which Intel rebranded in x86 ISA as Instruction Pointer (IP)
- The PC points at the next instruction to execute

**Register Width:**
- On x86-32: Registers are 32 bits wide
- On x86-64: Registers are 64 bits wide  
- On LC-3: Registers are 16 bits wide

---

### Instruction Cycle

The **Instruction Cycle** consists of 6 phases:

```mermaid
flowchart TD
    Fetch[1. FETCH] --> Decode[2. DECODE]
    Decode --> EvalAddr[3. EVALUATE ADDRESS]
    EvalAddr --> FetchOp[4. FETCH OPERANDS]
    FetchOp --> Execute[5. EXECUTE]
    Execute --> Store[6. STORE RESULT]
    Store --> |PC incremented| Fetch
```

<!-- Diagram reconstructed from OCR text showing instruction cycle -->

1. **FETCH** - Load instruction from memory: `MAR ← [PC]`, `MDR ← M[MAR]`, `IR ← MDR`, `PC ← PC + 1`
2. **DECODE** - Determine opcode from instruction bits
3. **EVALUATE ADDRESS** - Calculate address of operand (if needed)
4. **FETCH OPERANDS** - Retrieve operands from register/memory
5. **EXECUTE** - Perform operation (ADD, AND, NOT, JMP, etc.)
6. **STORE RESULT** - Write result to register or memory

**Note:** The PC is incremented in the fetch phase of each instruction, not during execute.

---

### LC-3 Instruction Format

All LC-3 instructions are **16 bits** wide:

```
┌─────┬──────────────────────────────────┐
│15-12│ 11  10  9  8  7  6  5  4  3  2  1  0│
├─────┼──────────────────────────────────┤
│OP   │      Operand Fields             │
└─────┴──────────────────────────────────┘
```

<!-- OCR correction: "Opcode" → "opcode" -->

- **Bits [15:12]:** Opcode (determines instruction type)
- **Bits [11:0]:** Operand fields (register specifiers, immediate values, offsets)

---

### LC-3 Instruction Set Table

<!-- Table reconstructed from OCR text -->

| Opcode | Instruction | Format | Description |
|--------|-------------|--------|-------------|
| `0001` | **ADD** | `DR, SR1, SR2` or `DR, SR1, imm5` | Addition |
| `0101` | **AND** | `DR, SR1, SR2` or `DR, SR1, imm5` | Bitwise AND |
| `0000` | **BR** | `nzp, PCoffset9` | Conditional branch |
| `1100` | **JMP** | `BaseR` | Jump to address in register |
| `0100` | **JSR/JSRR** | `PCoffset11` or `BaseR` | Jump to subroutine |
| `0010` | **LD** | `DR, PCoffset9` | Load (PC-relative) |
| `1010` | **LDI** | `DR, PCoffset9` | Load indirect (PC-relative) |
| `0110` | **LDR** | `DR, BaseR, offset6` | Load (base+offset) |
| `1110` | **LEA** | `DR, PCoffset9` | Load effective address |
| `1001` | **NOT** | `DR, SR` | Bitwise NOT (one's complement) |
| `1000` | **RTI** | - | Return from interrupt |
| `0011` | **ST** | `SR, PCoffset9` | Store (PC-relative) |
| `1011` | **STI** | `SR, PCoffset9` | Store indirect (PC-relative) |
| `0111` | **STR** | `SR, BaseR, offset6` | Store (base+offset) |
| `1111` | **TRAP** | `trapvect8` | System call |
| `1101` | **Reserved** | - | Reserved opcode |

---

### ADD Instruction

<!-- OCR correction: "Rouler" → "register" -->

**Format 1: Register mode**
```
0001 DR SR1 0 00 SR2
```
- `DR = SR1 + SR2`

**Format 2: Immediate mode**
```
0001 DR SR1 1 imm5
```
- `DR = SR1 + SEXT(imm5)`

**Example:**
```asm
ADD R2, R0, R1    ; R2 ← R0 + R1
ADD R3, R3, #5    ; R3 ← R3 + 5
```

---

### AND Instruction

**Format 1: Register mode**
```
0101 DR SR1 0 00 SR2
```
- `DR = SR1 & SR2`

**Format 2: Immediate mode**
```
0101 DR SR1 1 imm5
```
- `DR = SR1 & SEXT(imm5)`

**Example:**
```asm
AND R5, R5, #0    ; R5 ← 0 (clear register)
AND R3, R3, R2    ; R3 ← R3 & R2
```

---

### NOT Instruction

**Format:**
```
1001 DR SR 1 1 1 1 1 1
```
- `DR = NOT(SR)` (one's complement)

**Example:**
```asm
NOT R0, R0        ; R0 ← ~R0
```

To form 2's complement negative:
```asm
NOT R0, R0        ; One's complement
ADD R0, R0, #1    ; Add 1 to get 2's complement
```

---

### BR (Branch) Instruction

<!-- OCR correction: "Condetional" → "conditional" -->

**Format:**
```
0000 n z p PCoffset9
```

- Branch based on condition codes (N, Z, P)
- `PC ← PC + SEXT(PCoffset9)` if condition is met

**Condition Codes:**
- **N (Negative):** Set if result < 0
- **Z (Zero):** Set if result == 0
- **P (Positive):** Set if result > 0

**Examples:**
```asm
BRz LABEL         ; Branch if zero (0 0 1)
BRnp LABEL        ; Branch if negative or positive (1 0 1)
BR LABEL          ; Unconditional branch (1 1 1)
```

---

### JMP Instruction

**Format:**
```
1100 0 0 0 BaseR 0 0 0 0 0 0
```

- `PC ← BaseR` (jump to address in register)

**Special Case - RET (Return):**
```
1100 0 0 0 111 0 0 0 0 0 0
```
- `JMP R7` (return from subroutine)
- R7 typically holds the return address

**Example:**
```asm
JMP R3            ; PC ← R3
RET               ; PC ← R7 (return)
```

---

### JSR/JSRR (Jump to Subroutine)

<!-- OCR correction: "SubRoudme" → "subroutine" -->

**JSR (PC-relative):**
```
0100 1 PCoffset11
```
- `R7 ← PC` (save return address)
- `PC ← PC + SEXT(PCoffset11)`

**JSRR (Base register):**
```
0100 0 0 0 BaseR 0 0 0 0 0 0
```
- `R7 ← PC` (save return address)
- `PC ← BaseR`

**Example:**
```asm
JSR SUBROUTINE    ; Call subroutine (PC-relative)
JSRR R3           ; Call subroutine (address in R3)
```

---

### Load/Store Instructions

#### LD (Load PC-relative)

**Format:**
```
0010 DR PCoffset9
```
- `DR ← M[PC + SEXT(PCoffset9)]`

#### LDI (Load Indirect)

**Format:**
```
1010 DR PCoffset9
```
- `DR ← M[M[PC + SEXT(PCoffset9)]]`
- Address of address (two memory accesses)

#### LDR (Load Base+Offset)

**Format:**
```
0110 DR BaseR offset6
```
- `DR ← M[BaseR + SEXT(offset6)]`

#### ST (Store PC-relative)

**Format:**
```
0011 SR PCoffset9
```
- `M[PC + SEXT(PCoffset9)] ← SR`

#### STI (Store Indirect)

**Format:**
```
1011 SR PCoffset9
```
- `M[M[PC + SEXT(PCoffset9)]] ← SR`

#### STR (Store Base+Offset)

**Format:**
```
0111 SR BaseR offset6
```
- `M[BaseR + SEXT(offset6)] ← SR`

---

### LEA (Load Effective Address)

**Format:**
```
1110 DR PCoffset9
```

- `DR ← PC + SEXT(PCoffset9)`
- **Does NOT access memory** - only computes address
- **Does NOT affect condition codes**

Useful for initializing a register with an address.

**Example:**
```asm
LEA R2, DATA      ; R2 ← address of DATA
```

---

### Addressing Modes Summary

<!-- OCR correction: "addresing" → "addressing" -->

LC-3 supports three main addressing modes:

| Mode | Description | Example |
|------|-------------|---------|
| **Immediate/Literal** | Operand is part of instruction | `ADD R1, R1, #5` |
| **Register** | Operand is in a register | `ADD R1, R2, R3` |
| **Memory** | Operand is in memory | |
| - PC-relative | Address = PC + offset | `LD R1, LABEL` |
| - Indirect | Address at (PC + offset) | `LDI R1, LABEL` |
| - Base+Offset | Address = BaseR + offset | `LDR R1, R2, #10` |

---

## LC-3 Memory Organization

<!-- OCR correction: "momory" → "memory" -->

```
┌──────────────────────┐ 0x0000
│   System Space       │
│   (Privileged)       │
│   - Trap vectors     │
│   - Interrupt vectors│
│   - OS code/data     │
├──────────────────────┤ 0x2FFF (Supervisor Stack)
│                      │
├──────────────────────┤ 0x3000
│   User Space         │
│   (Unprivileged)     │
│   - User code        │
│   - User data        │
│   - User stack       │
├──────────────────────┤ 0xFDFF
│                      │
├──────────────────────┤ 0xFE00
│   I/O Page           │
│   (Memory-mapped I/O)│
│   - Device registers │
└──────────────────────┘ 0xFFFF
```

<!-- Memory map diagram reconstructed from OCR text -->

- **System Space (0x0000-0x2FFF):** Privileged memory for OS
- **User Space (0x3000-0xFDFF):** Unprivileged memory for user programs
- **I/O Page (0xFE00-0xFFFF):** Memory-mapped I/O device registers

---

### Trap Vector Table

Located at **0x0000-0x00FF** (256 entries):

| Address | Trap Vector | Service Routine | Description |
|---------|-------------|-----------------|-------------|
| 0x0020 | `x20` | GETC | Read character from keyboard |
| 0x0021 | `x21` | OUT | Output character to monitor |
| 0x0022 | `x22` | PUTS | Output string to monitor |
| 0x0023 | `x23` | IN | Input character with prompt |
| 0x0025 | `x25` | HALT | Halt the program |

<!-- Table reconstructed from OCR text -->

**Example:**
```asm
TRAP x23          ; Input character (IN)
TRAP x21          ; Output character (OUT)
TRAP x25          ; Halt program (HALT)
```

---

## Sign Extension (SEXT) and Zero Extension (ZEXT)

<!-- OCR correction: "SEX7" → "SEXT", "exlord" → "extend" -->

**Sign extension** is performed to operate on representations of different lengths.

- The value of a positive number does not change if we zero-extend by filling vacated bit positions to the left with 0
- The value of a negative number does not change if we sign-extend by filling vacated bit positions to the left with the sign bit (1)

**SEXT:** Extends a smaller signed value to a larger width by copying the sign bit
- Example: `SEXT(imm5)` → 16 bits

**ZEXT:** Extends by filling with zeros
- Example: `ZEXT(trapvect8)` → 16 bits

---

## I/O and Memory-Mapped Registers

<!-- OCR correction: "Input Output" → "I/O" -->

### Keyboard Registers

**KBSR (Keyboard Status Register) - Address: 0xFE00**

```
┌──┬──┬──────────────────┐
│15│14│  13-0 (unused)   │
├──┼──┼──────────────────┤
│RD│IE│      0x00        │
└──┴──┴──────────────────┘
```

- **Bit [15] (Ready):** Set to 1 when a key is struck
- **Bit [14] (Interrupt Enable):** If set, keyboard can interrupt

**KBDR (Keyboard Data Register) - Address: 0xFE02**

```
┌──────────┬─────────────┐
│  15-8    │    7-0      │
├──────────┼─────────────┤
│  0x00    │  ASCII code │
└──────────┴─────────────┘
```

- **Bits [7:0]:** ASCII code of the character typed

---

### Display Registers

**DSR (Display Status Register) - Address: 0xFE04**

```
┌──┬──┬──────────────────┐
│15│14│  13-0 (unused)   │
├──┼──┼──────────────────┤
│RD│IE│      0x00        │
└──┴──┴──────────────────┘
```

- **Bit [15] (Ready):** Set to 1 when display is ready for next character
- **Bit [14] (Interrupt Enable):** If set, display can interrupt

**DDR (Display Data Register) - Address: 0xFE06**

```
┌──────────┬─────────────┐
│  15-8    │    7-0      │
├──────────┼─────────────┤
│  0x00    │  ASCII code │
└──────────┴─────────────┘
```

- **Bits [7:0]:** ASCII code of character to display

---

### Basic Input Routine (Polling)

```asm
START   LDI   R1, KBSR      ; Load keyboard status
        BRzp  START          ; Loop until ready bit set
        LDI   R0, KBDR       ; Load character from keyboard
        ; Process character in R0
        BRnzp NEXT_TASK

KBSR    .FILL xFE00
KBDR    .FILL xFE02
```

<!-- Code block reconstructed from OCR text -->

---

### Basic Output Routine (Polling)

```asm
START   LDI   R1, DSR       ; Load display status
        BRzp  START          ; Loop until ready bit set
        STI   R0, DDR        ; Store character to display
        BRnzp NEXT_TASK

DSR     .FILL xFE04
DDR     .FILL xFE06
```

---

### Echo Input/Output Routine

```asm
START   LDI   R1, KBSR      ; Test keyboard ready
        BRzp  START          ; Wait until ready
        LDI   R0, KBDR       ; Load character

ECHO    LDI   R1, DSR       ; Test display ready
        BRzp  ECHO           ; Wait until ready
        STI   R0, DDR        ; Output character
        
        BRnzp START          ; Repeat

KBSR    .FILL xFE00
KBDR    .FILL xFE02
DSR     .FILL xFE04
DDR     .FILL xFE06
```

---

## Interrupts

<!-- OCR correction: "Intoment" → "interrupt" -->

### Interrupt Mechanism

**Polling** requires the processor to spend time testing the ready bit repeatedly until it is set. With **interrupt-driven I/O**, the I/O device can force the running program to stop and have the processor execute a program that services the I/O device, then have the stopped program resume execution as if nothing happened.

**Requirements for Interrupt:**
1. I/O device must want service (ready bit is set)
2. I/O device must have the right to request service (interrupt enable bit [14] set)
3. I/O device must have higher urgency (priority) than what the processor is currently doing

**Interrupt Signal:**
```
INT = Ready_bit [15] AND Interrupt_Enable [14]
```

If both bits are set, the device asserts its interrupt request signal.

---

### Interrupt Vector Table

Located at **0x0100-0x01FF** (256 entries):

Each entry contains the **starting address** of an interrupt service routine.

**Process:**
1. I/O device provides 8-bit interrupt vector
2. Processor zero-extends to form 16-bit address into table
3. Table entry contains starting address of service routine
4. Processor saves PC and PSR on supervisor stack
5. Loads PC with service routine address
6. Executes service routine
7. RTI instruction restores PC and PSR
8. Execution resumes at interrupted program

---

### Interrupt Handling Sequence

```mermaid
flowchart TD
    Run[Program Running] --> |Interrupt Request| Save[Save PC & PSR to stack]
    Save --> Load[Load Service Routine PC]
    Load --> Service[Execute Service Routine]
    Service --> RTI[RTI Instruction]
    RTI --> Restore[Restore PC & PSR from stack]
    Restore --> Resume[Resume Program]
```

<!-- Diagram reconstructed from interrupt handling OCR text -->

---

### PSR (Process Status Register)

```
┌──┬──────┬──────────────┬─────┐
│15│14-11 │   10-8       │ 2-0 │
├──┼──────┼──────────────┼─────┤
│P │ 0000 │ Priority     │ NZP │
└──┴──────┴──────────────┴─────┘
```

- **Bit [15] (Privilege):** 0 = Supervisor mode, 1 = User mode
- **Bits [10:8] (Priority):** Priority level (PL0-PL7)
- **Bits [2:0] (Condition Codes):** N (negative), Z (zero), P (positive)

---

## Stack Operations

<!-- OCR correction: "LIFO" → "LIFO" (Last In First Out preserved) -->

### Stack Pointer

- **R6** is typically used as the stack pointer
- **Supervisor Stack Pointer (SSP)** - for privileged mode
- **User Stack Pointer (USP)** - for user mode
- Stack grows toward address 0x0000 (toward lower addresses)

### PUSH Operation

```asm
ADD  R6, R6, #-1     ; Decrement stack pointer
STR  R0, R6, #0      ; Store value onto stack
```

### POP Operation

```asm
LDR  R0, R6, #0      ; Load value from stack
ADD  R6, R6, #1      ; Increment stack pointer
```

---

## Subroutines and the Call/Return Mechanism

<!-- OCR correction: "SubRoutme" → "subroutine" -->

**JSR/JSRR** - Implements the call mechanism:
1. Saves return address in R7: `R7 ← PC`
2. Loads PC with subroutine address

**RET** - Implements the return mechanism:
```asm
RET               ; Same as JMP R7
```
- Loads PC with return address from R7

**Callee-Save vs Caller-Save:**
- **Caller-Save:** Calling program saves registers before call
- **Callee-Save:** Called subroutine saves registers it will modify

---

## LC-3 Assembly Directives

<!-- OCR correction: "Pseudo-OP" → "Pseudo-op" -->

**Pseudo-ops** (assembler directives) are messages to the assembler, not actual instructions.

| Directive | Purpose | Example |
|-----------|---------|---------|
| `.ORIG` | Set starting address | `.ORIG x3000` |
| `.FILL` | Initialize memory location | `.FILL x0021` |
| `.BLKW` | Reserve block of words | `.BLKW 10` |
| `.STRINGZ` | Initialize string with null terminator | `.STRINGZ "Hello"` |
| `.END` | Mark end of program | `.END` |

**Example Program:**

```asm
        .ORIG x3000
        
        LEA  R0, MSG        ; Load address of message
        TRAP x22            ; Output string (PUTS)
        TRAP x25            ; Halt
        
MSG     .STRINGZ "Hello, World!\n"
        
        .END
```

---

## x86-64 Assembly

<!-- OCR correction: "Intel AMD64" → "Intel/AMD x86-64" -->

### General-Purpose Registers (64-bit)

| 64-bit | 32-bit | 16-bit | 8-bit (high/low) | Purpose |
|--------|--------|--------|------------------|---------|
| RAX | EAX | AX | AH/AL | Accumulator (return values) |
| RBX | EBX | BX | BH/BL | Base register |
| RCX | ECX | CX | CH/CL | Counter (loop operations) |
| RDX | EDX | DX | DH/DL | Data (I/O operations) |
| RSI | ESI | SI | SIL | Source index (string ops) |
| RDI | EDI | DI | DIL | Destination index (string ops) |
| RBP | EBP | BP | BPL | Base pointer (stack frame) |
| RSP | ESP | SP | SPL | Stack pointer |
| R8-R15 | R8D-R15D | R8W-R15W | R8B-R15B | General purpose |

<!-- Table reconstructed from OCR text -->

---

### Special Registers

- **RIP (Instruction Pointer):** Points to next instruction
- **RFLAGS:** Status flags (CF, ZF, SF, OF, etc.)

**Common Flags:**
- **CF (Carry Flag):** Set on unsigned overflow
- **ZF (Zero Flag):** Set if result is zero
- **SF (Sign Flag):** Set equal to most significant bit (sign bit)
- **OF (Overflow Flag):** Set on signed overflow

---

### Calling Conventions (System V AMD64 ABI)

**Function Arguments (in order):**
1. RDI (1st argument)
2. RSI (2nd argument)
3. RDX (3rd argument)
4. RCX (4th argument)
5. R8 (5th argument)
6. R9 (6th argument)
7. Stack (additional arguments)

**Return Value:** RAX

**System Call Arguments:**
- System call number: RAX
- Arguments: RDI, RSI, RDX, RCX, R8, R9

**Caller-saved:** RAX, RDI, RSI, RDX, RCX, R8-R11
**Callee-saved:** RBX, RBP, RSP, R12-R15

---

### AT&T vs Intel Syntax

<!-- OCR correction: "Syntane" → "syntax" -->

**Intel Syntax:**
```asm
mov  rax, 2         ; destination, source
add  rax, 3         ; destination, immediate
```

**AT&T Syntax:**
```asm
mov  $2, %rax       ; source, destination
add  $3, %rax       ; immediate, destination
```

**Key Differences:**
- Intel: `destination, source`
- AT&T: `source, destination`
- AT&T uses `%` prefix for registers and `$` for immediates

---

### Common x86-64 Instructions

#### MOV - Move Data

```asm
mov  rax, rbx       ; Register to register
mov  rax, [rbx]     ; Memory to register
mov  [rbx], rax     ; Register to memory
mov  rax, 42        ; Immediate to register
```

**Note:** No memory-to-memory moves allowed.

---

#### Arithmetic Instructions

```asm
add  rax, rbx       ; rax ← rax + rbx
sub  rax, rbx       ; rax ← rax - rbx
imul rax, rbx       ; rax ← rax * rbx (signed)
mul  rbx            ; RDX:RAX ← RAX * rbx (unsigned)
```

<!-- OCR correction: "Anlhmetic" → "arithmetic" -->

---

#### Logical Instructions

```asm
and  rax, rbx       ; rax ← rax & rbx
or   rax, rbx       ; rax ← rax | rbx
xor  rax, rbx       ; rax ← rax ^ rbx
not  rax            ; rax ← ~rax
```

---

#### Shift Instructions

```asm
shl  rax, 2         ; Shift left (multiply by 4)
shr  rax, 2         ; Shift right (divide by 4, unsigned)
sal  rax, 2         ; Shift arithmetic left
sar  rax, 2         ; Shift arithmetic right (preserves sign)
```

---

#### Comparison and Conditional Jumps

```asm
cmp  rax, rbx       ; Compare (sets flags based on rax - rbx)
test rax, rax       ; Bitwise AND (sets flags, doesn't store)

je   label          ; Jump if equal (ZF=1)
jne  label          ; Jump if not equal (ZF=0)
jg   label          ; Jump if greater (signed)
jl   label          ; Jump if less (signed)
ja   label          ; Jump if above (unsigned)
jb   label          ; Jump if below (unsigned)
```

---

#### Stack Operations

```asm
push rax            ; Decrement RSP, store RAX
pop  rax            ; Load RAX, increment RSP
```

**Note:** In 64-bit mode, push/pop work with 64-bit values (8 bytes).

---

#### Subroutine Calls

```asm
call function       ; Push return address, jump to function
ret                 ; Pop return address, jump to it
```

---

### LEA (Load Effective Address)

<!-- OCR correction: "Loa" → "LEA" -->

**Special instruction** that computes an address but does NOT access memory.

```asm
lea  rax, [rbx + rcx*4 + 5]
```

This computes `rbx + rcx*4 + 5` and stores the result in RAX (not the value at that address).

**Uses:**
- Pointer arithmetic
- Fast arithmetic (e.g., `lea rax, [rax + rax*2]` computes `rax * 3`)

---

### Memory Addressing Modes

<!-- OCR correction: "Addressmy" → "addressing" -->

**Syntax:** `[base + index*scale + displacement]`

- **Base:** Any general-purpose register
- **Index:** Any general-purpose register (except RSP)
- **Scale:** 1, 2, 4, or 8
- **Displacement:** Signed 8/16/32-bit offset

**Examples:**
```asm
mov  rax, [rbx]                 ; Base only
mov  rax, [rbx + 10]            ; Base + displacement
mov  rax, [rbx + rcx*4]         ; Base + index*scale
mov  rax, [rbx + rcx*4 + 10]    ; All components
```

---

### Example: printf and scanf in x86-64

<!-- OCR correction: "prmlf" → "printf", "scomf" → "scanf" -->

**printf Example:**

```asm
section .data
    format db "Enter a number: ", 0
    output db "You entered: %d", 10, 0

section .text
    global main
    extern printf, scanf

main:
    ; Print prompt
    mov  rdi, format        ; 1st argument (format string)
    xor  eax, eax           ; No floating-point args
    call printf
    
    ; Read integer
    lea  rsi, [rsp - 4]     ; 2nd argument (address for input)
    mov  rdi, fmt_input     ; 1st argument (format string)
    xor  eax, eax
    call scanf
    
    ; Print result
    mov  esi, [rsp - 4]     ; 2nd argument (value read)
    mov  rdi, output        ; 1st argument (format string)
    xor  eax, eax
    call printf
    
    ret

section .data
    fmt_input db "%d", 0
```

<!-- Code example reconstructed from OCR text -->

---

## Run-Time Stack and Calling Conventions

<!-- OCR correction: "Qun-time" → "run-time" -->

### Stack Frame Structure

```
┌─────────────────────────┐  ← Lower addresses
│   Local Variables       │
├─────────────────────────┤
│   Saved Registers       │
├─────────────────────────┤  ← RBP (Frame Pointer)
│   Return Address        │  (pushed by call)
├─────────────────────────┤
│   Caller's RBP          │  (pushed by callee)
├─────────────────────────┤
│   Function Parameters   │  (7th onward, if needed)
├─────────────────────────┤
│   Return Value Space    │
├─────────────────────────┤  ← RSP (Stack Pointer)
│   ...                   │
└─────────────────────────┘  ← Higher addresses
```

<!-- Stack frame diagram reconstructed from OCR text -->

---

### Function Prologue and Epilogue

**Prologue:**
```asm
push rbp              ; Save caller's frame pointer
mov  rbp, rsp         ; Set up new frame pointer
sub  rsp, N           ; Allocate space for local variables
```

**Epilogue:**
```asm
mov  rsp, rbp         ; Restore stack pointer
pop  rbp              ; Restore caller's frame pointer
ret                   ; Return to caller
```

---

## System Calls in x86-64 Linux

<!-- OCR correction: "Syscoll" → "syscall" -->

**System call number in RAX:**

| RAX | System Call | Description |
|-----|-------------|-------------|
| 0 | sys_read | Read from file descriptor |
| 1 | sys_write | Write to file descriptor |
| 2 | sys_open | Open file |
| 3 | sys_close | Close file |
| 60 | sys_exit | Exit program |

**Arguments:** RDI, RSI, RDX, RCX, R8, R9

**Example: Exit program**
```asm
mov  rax, 60          ; sys_exit
mov  rdi, 0           ; exit code 0
syscall
```

**Example: Write to stdout**
```asm
mov  rax, 1           ; sys_write
mov  rdi, 1           ; stdout
mov  rsi, message     ; buffer address
mov  rdx, msg_len     ; buffer length
syscall
```

---

## Number System Conversions

<!-- OCR correction: "Bromry" → "binary" -->

| Decimal | Binary | Octal | Hexadecimal |
|---------|--------|-------|-------------|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 2 | 0010 | 2 | 2 |
| 3 | 0011 | 3 | 3 |
| 4 | 0100 | 4 | 4 |
| 5 | 0101 | 5 | 5 |
| 6 | 0110 | 6 | 6 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 10 | 8 |
| 9 | 1001 | 11 | 9 |
| 10 | 1010 | 12 | A |
| 11 | 1011 | 13 | B |
| 12 | 1100 | 14 | C |
| 13 | 1101 | 15 | D |
| 14 | 1110 | 16 | E |
| 15 | 1111 | 17 | F |

---

## Additional Topics

### Two's Complement Representation

To represent negative numbers in binary:

1. **One's complement:** Flip all bits
2. **Two's complement:** Add 1 to one's complement

**Example:** -5 in 8-bit
```
5 =      00000101
~5 =     11111010  (one's complement)
-5 =     11111011  (two's complement, add 1)
```

---

### Sign Extension vs Zero Extension

<!-- OCR correction: "exlord" → "extend" -->

**SEXT (Sign Extension):**
- Extends a signed value by copying the sign bit
- Example: `10110` (8-bit) → `11111111 10110` (16-bit)

**ZEXT (Zero Extension):**
- Extends an unsigned value by filling with zeros
- Example: `10110` (8-bit) → `00000000 10110` (16-bit)

---

### MOVSX and MOVZX (x86-64)

```asm
movsx rax, byte [rbx]   ; Sign-extend byte to 64-bit
movzx rax, byte [rbx]   ; Zero-extend byte to 64-bit
movsxd rax, dword [rbx] ; Sign-extend dword to 64-bit
```

---

## Debugging and Testing

<!-- OCR correction: "Debugging" → "debugging" -->

### Black Box vs White Box Testing

- **Black Box:** Testing without knowledge of internal implementation
- **White Box:** Testing with full knowledge of internal structure

### Types of Errors

1. **Syntactic Errors:** Caught by assembler (incorrect mnemonics, operands)
2. **Semantic Errors:** Logic errors (wrong register, incorrect offset)
3. **Algorithmic Errors:** Incorrect algorithm design
4. **Specification Errors:** Misunderstanding of requirements

---

## Compilation Pipeline

```mermaid
flowchart LR
    Source[Source Code] --> Preprocessor[Preprocessor]
    Preprocessor --> |#define, #include| Compiler[Compiler]
    Compiler --> |Analysis & Synthesis| Assembler[Assembler]
    Assembler --> |Machine code| Linker[Linker]
    Library[Libraries] --> Linker
    Linker --> Executable[Executable Image]
    Executable --> |Loaded into memory| Execute[Execute]
```

<!-- Compilation pipeline diagram -->

1. **Preprocessor:** Processes directives (#include, #define)
2. **Compiler:** Translates high-level code to assembly
3. **Assembler:** Translates assembly to machine code (object file)
4. **Linker:** Combines object files and libraries into executable
5. **Loader:** Loads executable into memory for execution

---

*End of Assembly Language Notes*
