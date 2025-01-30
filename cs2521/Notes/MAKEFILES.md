# Makefiles

## What is a Makefile
It is a special file, typically named "Makefile" or "makefile", used by the make build automation tool to compile and build programs.

> typicially named (M/m)akefile
 
## How to use Makefiles

There are three critical components that make up makefiles,

1. Targets: 
These are typically the output files you want to generate (e.g., executable files). A target can also be a label for a group of commands.

2. Dependencies: 
These are the files or targets that the current target depends on. If any of the dependencies have changed, the commands associated with the target are executed.

3. Commands: 
These are the shell commands to execute in order to build the target. They must be preceded by a tab character.
