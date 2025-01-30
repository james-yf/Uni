# GCC Compiler Steps

Although COMP1511 has made it seem compilation is as simple as `gcc -o executable_name source.c` which produces an executable in a one liner, there is more to it than meets the eye.

There are 4 distinct steps in the C compilation process. Since this topic isn't directly assessed in the COMP2521 course, each step is covered briefly. 

## 1. Preprocessing:

   **Handles lines beginning with `#`**, so #includes, #defines, and #ifdef. 

` gcc -E source.c ` To run the preprocessing step

> the output is a modified source file with all the `#` lines resolved

Example source.c
```
  #include <stdio.h>
  #define SIZE 10

  int main(void) {
      int numbers[SIZE];
  	  return 0;
  }
```

Output after preprocessing
```

  int main(void) {
      int numbers[10];
      return 0;
  }

```
> There are hundreds of lines more in output than shown above, since `stdio.h` is replaced with its function declarations, macros and constants, and type definitions, so I have chosen to omit them. The chosen snippet highlights modifications to `main`.

## 2. Compilation:

   The compiler **translates the preprocessed code into assembly**. The compiler also checks for syntax errors
   and translates high-level language constructs into low-level assembly instructions.

` gcc -c source.c ` To run the compilation step 

` gcc -S source.c ` Outputs an assembly language file with the translated instructions 

```
	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 13, 0	sdk_version 13, 3
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #80
	.cfi_def_cfa_offset 80
	stp	x29, x30, [sp, #64]             ; 16-byte Folded Spill
	add	x29, sp, #64
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	stur	x8, [x29, #-8]
	str	wzr, [sp, #12]
	ldur	x9, [x29, #-8]
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	subs	x8, x8, x9
	cset	w8, eq
	tbnz	w8, #0, LBB0_2
	b	LBB0_1
LBB0_1:
	bl	___stack_chk_fail
LBB0_2:
	mov	w0, #0
	ldp	x29, x30, [sp, #64]             ; 16-byte Folded Reload
	add	sp, sp, #80
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols

```
source.c translated into an assembly language `.s` file 

> produces an assembly language file, such as a `.s`, as shown above

## 3. Assembly: 

  The assembler **converts the assembly language file into machine code**.

> produces an object file `.o`

- Although compilation and assembly are considered distinct steps, the `-c` flag tells the compiler to compile the source code and      
  assemble it into an object file `.o`, we don't have to handle the two steps separately.

- This is why an assembly language file is not produced during compilation.

- As a result, some descriptions/diagrams of the process exclude assembly, since compilation encompasses it. 

## 4. Linking:

The linker's primary job is to combine multiple object files (and possibly libraries) into a single executable.

` gcc -o source.o [any other object files] executable_name` To run the linking step 

> produces an executable file

## Diagram
![Alt Text](images/3StepsCompiling.png)
The 3 GCC Compiler Steps (excludes assembly)

