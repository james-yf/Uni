# Compiling Steps

Although it seems compilation is one step `gcc -o source source.c` there is more to it than meets the eye.

There are 3 distinct steps in the C compilation process. 

1. Preprocessing: **Handles lines beginning with `#`**, so #includes, #defines, and
#ifdef. 

` gcc -E source.c ` To run the preprocessing step

> the output is a modified source file with all the `#` lines resolved

2. Compilation: The compiler **translates the preprocessed code into assembly**. The compiler also checks for syntax errors
   and translates high-level language constructs into low-level assembly instructions.

` gcc -c source.c ` To run the compilation step 

` gcc -S source.c ` Outputs an assembly language file with the translated instructions 

> produces a `.o` file

3. Assembly: The assembler **converts the assembly language file into machine code**.

   Although compilation and assembly are considered as separate steps, the `-c` flag tells the compiler to compile the source code and      assemble it into an object file `.o`. 

3. Linking: 
   

![Alt Text](images/3StepsCompiling.png)


