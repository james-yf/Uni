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

- `hello` is the target executable.

- `main.o` and `hello.o` are dependencies for the `hello` target.

- `gcc -o hello main.o hello.o` is the command to link the object files into the final executable.

- The `clean` target is a convenience target to remove generated files.

## Useful features

### 1. Automatic Variables: 

Make provides several automatic variables that make it easier to write rules.

- `$@`: The target name.

- `$<`: The first dependency.

- `$^`: All dependencies.

- `$?`: Dependencies that are newer than the target.


### Difference between `$^` and `$?`:

`$^` (Caret): This variable holds the list of all prerequisites, regardless of whether they are newer than the target. This is useful when you need to process all dependencies together, irrespective of their modification time.



`$?` (Question Mark): This variable holds the list of prerequisites that are newer than the target. Essentially, it gives you the files that have changed and need to be recompiled or processed. This is useful when you only want to process updated files.

```
# Define source files and the target
SOURCES = foo.c bar.c
TARGET = myprogram

# Rule to compile the target
$(TARGET): $(SOURCES)
    gcc -o $(TARGET) $^  # Use all dependencies to compile

# Rule to recompile only updated source files
recompile: $(SOURCES)
    gcc -o $(TARGET) $?  # Use only the updated dependencies to recompile
```

In this example:

The `gcc -o $(TARGET) $^` command will compile `foo.c` and `bar.c`, regardless of which one has been modified.

The `gcc -o $(TARGET) $?` command will only recompile the modified source files (i.e., if only `foo.c` was modified, it will only recompile `foo.c`).


### 2. Pattern Rules: 

These allow you to define generic rules that apply to multiple targets. For example, you can specify how to build any `.o` file from a `.c` file using a single rule.

```
%.o: %.c
    gcc -c $< -o $@
```

In this rule:

- `%` is a wildcard that matches any filename.

- `$<` is an automatic variable representing the first dependency (the `.c` file).

- `$@` is an automatic variable representing the target (the `.o` file).

### 3. Variables: 

You can define variables to simplify and customize your Makefile. This is useful for setting compiler options, defining lists of files, etc.

```
CC = gcc
CFLAGS = -Wall -g
OBJS = main.o hello.o

hello: $(OBJS)
    $(CC) -o hello $(OBJS)

%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

### There are more, but they aren't necessary for this course
