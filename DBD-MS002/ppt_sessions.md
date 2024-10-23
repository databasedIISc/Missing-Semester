---
title: Missing Semester DBD002
author: Anirudh Gupta
sub_title: Debuggers and Testing
theme:
  name: catppuccin-mocha
  override:
  footer:
    style: template
    left: "Anirudh Gupta"
    middle: "Introduction to Debuggers and Testing"
    right: "{current_slide} / {total_slides}"
---

# Introduction

<!-- pause-->

## What is a Debugging?

<!-- pause-->

When your code does not behave as you would expect, means it has some errors AKA `BUGS`. Debugging is `De-bug-ing`.

<!-- pause-->

## So what are Debuggers?

Debuggers are tools that help you find and fix bugs in your code.

## Why Debuggers?

<!-- pause-->

Debuggers are not just for finding bugs, they are also useful for understanding how a piece of code works.

<!-- pause-->

It's like `PythonTutor` but more complicated and more powerful!

<!-- pause-->

## Languages and Debuggers

Different languages have different debuggers. For example-

- `gdb` for C/C++
- `pdb` for Python

<!-- end_slide -->

# Let's Debug!

## Methods of Debugging

<!-- pause-->

To Debug, we have various methods, some of them are:

<!-- pause-->

- `print` statements
- `assert` statements
- `logging`
- Using Debuggers like `gdb`, `pdb`, etc.
<!-- pause-->

Error Handling is REALLY important!

<!-- pause-->

## Print statement Debugging

- You insert `print` statements in your code to see which line messes up.
<!-- pause-->

## Assert statement Debugging

- You add `assert` statements to check if a condition is true. This is REALLY POWERFUL since you can make sure what is allowed to go ahead in the code!

```python
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a/b
```

<!-- end_slide -->

# Logging

<!-- pause-->

- Logging is a way to track events that happen when some software runs.
<!-- pause-->

Let's look at the example present in the `logging_example.py` file, in repostory: https://github.com/databasedIISc/Missing-Semester

```bash
python3 logging_example.py
# Raw output as with just prints

python3 logging_example.py log
# Log formatted output

python3 logging_example.py log ERROR
# Print only ERROR levels and above

python3 logging_example.py color
# Color formatted output
```

> Note: Leaning how to use colors makes visuals better! :)

<!-- end_slide -->

# How Linux and other OS's use logging?

<!-- pause-->

- Every software, website, databases, etc. use logging to track events.
- and in future, you will too!

## Linux

<!-- pause-->

- Most Linux applications uses `/var/log` directory to store logs.
- Linux has `system log` which stores logs of all system events.
- `systemd` AKA `System Daemon` is a system and service manager for Linux like which services are enabled and running.
- `systemd` places the logs under `/var/log/journal` in a specialized format and you can use the `journalctl` command to display the messages.
- For MacOS, you have `/var/log/system.log` as the system log location.
- On most UNIX systems you can also use the `dmesg` command to access the kernel log.
<!-- pause-->

## logger

- For logging under the system logs you can use the `logger` shell program.

```bash
logger "I like cats! Meow"
# For MacOS
log show --last 1m | grep Meow
# For Linux
journalctl --since "1m ago" | grep Meow
```

<!-- pause-->

There exists more tools which are easier to use and more powerful than `logger`.

<!-- end_slide -->

# Debuggers

<!-- pause-->

## Let's use Debuggers!

We will see how to use debuggers, mainly use `Python` debugger.

<!-- pause-->

## Some Concepts

<!-- pause-->

Debuggers are programs that let you interact with the execution of a program, allowing the following:

- Halt execution of the program when it reaches a certain line.
- Step through the program one instruction at a time.
- Inspect values of variables after the program crashed.
- Conditionally halt the execution when a given condition is met.
- And many more advanced features.

<!-- pause-->

## PDB

<!-- pause-->

It has the following common commands and let's look into that!

- l(ist) - Displays 11 lines around the current line or continue the previous listing.
- s(tep) - Execute the current line, stop at the first possible occasion.
- n(ext) - Continue execution until the next line in the current function is reached or it returns.
- b(reak) - Set a breakpoint (depending on the argument provided).
- p(rint) - Evaluate the expression in the current context and print its value. There’s also pp to display using pprint instead.
- r(eturn) - Continue execution until the current function returns.
- q(uit) - Quit the debugger.

<!-- end_slide -->

# VS Code Debugging

As you saw Command line visualisation of PDB, we will use VS code, since it provides an easier UI for us.

<!-- pause-->

```
Why make Debugging harder when it's already hard!
```

<!-- pause-->

See the `debugging_example.py` file in the repository for the code.

## What's the issue?

<!-- pause-->

```
n - i - 2 -> n - i - 1
```

<!-- end_slide-->

# Linters and Statics Analysis

<!-- pause-->

## Linters? Never heard?

Linters are tools that analyze your code to find potential errors, style issues, and other problems.

- But they do it within the code itself, not by running it.
- Advance linters point it out within the editor itself.
- Examples for python - `pylint`, `flake8`, `black`, etc.
<!-- pause-->

Let's see an example -

<!-- pause-->

- `static_analysis.py` file in the repository.

Clealy we see the issues in the code, but we need not notice, if we have linters!

<!-- pause-->

## Linters for other languages

- `clang-tidy` for C/C++
- `shellcheck` for shell scripts
- `eslint` for JavaScript
- `golint` for Go
- `rust-analyzer` for Rust

and more....

<!-- end_slide -->

# More into (only) Python Formatters, Linters and LSP!

<!-- pause-->

```
LSP - Language Server Protocol
```

Every language has its own formatters, linters and LSPs. These tools let you -

<!-- pause-->

- Format your code automatically
- Find errors in your code(like linters)
- Provide autocompletion and other IDE features
- Let you rename imports, variables, etc. easily
- AND MUCH MORE.... For real! It's GODLY!
<!-- pause-->

## Python

- `black` for formatting
- `pylint` for linting
- `mypy` for static type checking
- `pep8` for style checking
- `rope` for refactoring
- `jedi` for autocompletion

and more ...

<!-- pause-->

## LSP in Text Editors

<!-- pause-->

Most text editors support LSPs, and sometimes have them inbuilt, like VS Code or JetBrains, after simple installation of Extensions.

<!-- end_slide -->

# Testing

<!-- pause-->

Now before we end up debugging, we should also know what the error is? Sometimes we don't even know where the code failed?

For algorithm, Moodle says - "WRONG!" and you are like - "Where?"

<!-- pause-->

## Writing Tests

```
You write tests before you write your code,
otherwise it will test your patience!
```

<!-- pause-->

- Testing is a way to ensure that your code works as expected for your made test cases.
- It's like minimum requirement for your code to work. It may still not work always for all inputs after passing your made test cases.
<!-- pause-->

## Python Testing

<!-- pause-->

- `unittest` - Python's built-in testing framework.
- `pytest` - A third-party testing framework that is easier to use and more powerful than `unittest`.
<!-- pause-->

Let's do some "Pytesting" right now!

<!-- end_slide -->

# Pytest

```bash
pip install pytest
```

<!-- pause-->

- Now check out the `test_example.py` file in the repository.
<!-- pause-->

You run the tests by running `pytest` by-

```bash
pytest test_example.py -v
```

- `-v` is for verbose output.
- `-h` for more options.

<!-- pause-->

## SUS

We noticed the test failed for `-10, -4` case. So we need to fix it.

<!-- pause-->

### TO KNOW MORE INTO PYTEST, Check out their official documentation!

<!-- end_slide -->

# Let's Get more into Testing!

<!-- pause-->

## Profiling

- Profiling is a way to measure the performance of your code.
- It helps you identify bottlenecks in your code. The slowest part of your code.
<!-- pause-->

## Timing

- You can use the `time` module to measure the time taken by your code.
- better way it to use python's `cProfile` module or `line-profiler` module.
<!-- pause-->

```bash
pip install line_profiler
```

- Check out the `profiling_example.py` file in the repository.
<!-- pause-->

```bash
# For cProfile
python -m cProfile profiling_example.py

# For line-profiler
kernprof -l -v profiling_example.py
```

<!-- pause-->

You can see the clear difference in the output!

<!-- end_slide -->

# Timings for general processes

- There exists a command line tool called `time`, in Unix which tells you the real, sys, user, etc time taken by ANY PROCESS to run in the shell.

```bash
time python3 profiling_example.py
```

This gives you at the bottom, the time taken by `time` command.

<!-- end_slide-->

## Profiling

- Profiling is a way to measure the performance of your code.
- It helps you identify bottlenecks in your code. The slowest part of your code.
<!-- pause-->

## Memory Profiling

- You can use the `memory_profiler` module to measure the memory usage of your code.

```bash
pip install memory_profiler
```

<!-- pause-->

Now run on the same code -

```bash
python -m memory_profiler profiling_example.py
```

<!-- pause-->

You can see the memory usage of your code!

<!-- end_slide -->

# Conclusion

There are more tools and techniques to debug and test your code, but these are the basics.

<!-- pause-->

## More Exploration

- Check out `perf` command in linux for Flame graphs.
- `valgrind` for memory profiling.
- `gdb` for C/C++ debugging. (We can have a session after you guys learn C/C++)

<!-- pause-->

```
Hope you liked the session!
```

### ANY QUESTIONS?
