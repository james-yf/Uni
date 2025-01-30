# Makefiles

## What is a Makefile?
It is a special file, typically named "Makefile" or "makefile", used by the `make` build automation tool to compile and build programs.

> typicially named (M/m)akefile
 
There are three critical components that make up makefiles,

### 1. Targets:
   
These are typically the output files you want to generate (e.g., executable files). A target can also be a label for a group of commands.

### 2. Dependencies:
   
These are the files or targets that the current target depends on. If any of the dependencies have changed, the commands associated with the target are executed.

### 3. Commands:
   
These are the shell commands to execute in order to build the target. They must be preceded by a tab character.

## How to use Makefiles

To understand the syntax we'll look at an example program,

```
# This is a comment
# Target: Dependencies
#   Command

hello: main.o hello.o
    gcc -o hello main.o hello.o

main.o: main.c
    gcc -c main.c

hello.o: hello.c
    gcc -c hello.c

clean:
    rm -f hello main.o hello.o
```

- hello is the target executable.

- main.o and hello.o are dependencies for the hello target.

- gcc -o hello main.o hello.o is the command to link the object files into the final executable.

- The clean target is a convenience target to remove generated files.
