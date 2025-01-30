# Compiling Steps

Although it seems compilation is one step `gcc -o source source.c` there is more to it than meets the eye.

There are 3 distinct steps in the C compilation process. 

1. Preprocessing: Handles lines beginning with "#", so #includes, #defines, and
#ifdef. 

` gcc -E source.c ` To run the preprocessing step

> the output is a modified source file with all the "#" lines resolved

2. Compilation:


![Alt Text](images/3StepsCompiling.png)


