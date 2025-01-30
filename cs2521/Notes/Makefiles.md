# GCC Compiler Steps

Although COMP1511 has made it seem compilation is as simple as `gcc -o executable_name source.c` which produces an executable in a one liner, there is more to it than meets the eye.

There are 4 distinct steps in the C compilation process. Since this topic isn't directly assessed in the COMP2521 course, each step is covered briefly. 

## 1. Preprocessing:

   **Handles lines beginning with `#`**, so #includes, #defines, and #ifdef. 

` gcc -E source.c ` To run the preprocessing step

> the output is a modified source file with all the `#` lines resolved

## 2. Compilation:

   The compiler **translates the preprocessed code into assembly**. The compiler also checks for syntax errors
   and translates high-level language constructs into low-level assembly instructions.

` gcc -c source.c ` To run the compilation step 

` gcc -S source.c ` Outputs an assembly language file with the translated instructions 

> produces an assembly language file, such as `.s`

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

