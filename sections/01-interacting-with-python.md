↻ [Start](../README.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Types](02-types.md) →

---

# 1. Interacting with Python

Let's begin by starting an "interactive session" session with Python. This means we will be using Python in the terminal, which is a special space that allows us to run little bits of Python, experimenting and exploring what it can do, without having to save it. Think of this interactive space as a playground. Later on, we will be working with Python in a more robust way, doing what we call saving and executing Python scripts.

For now, though, let's start an interactive session with Python, which is accessed through the terminal.

Open your terminal and type:

```console
$ python
```

at the prompt. You should see something like this

```pycon
Python 3.7.6 (default, Jan  8 2020, 13:42:34)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Unlike the normal `$` terminal prompt, the Python prompt looks like this:

```pycon
>>>
```

These greater-than symbols `>` are how you know that you have entered an interactive session with Python. Now you are interacting directly with Python, rather than in the regular terminal. Keep an eye on these greater-than symbols, as a common early source of confusion is entering terminal commands into the Python prompt or entering Python commands into the terminal.

## A Little Math

Let's try a little math at the Python prompt. In the example below, type the text that appears after the Python prompt (the `>>>`). The line below is the output that is returned. This will be a standard convention when giving examples using the Python prompt.

```pycon
>>> 2 + 3
5

>>> 14 - 10
4

>>> 10 * 10
100

>>> 6 / 3
2

>>> 21 % 4
1
```

The first four operations above are addition, subtraction, multiplication, and division, respectively. The last operation is modulo, or mod, which returns the remainder after division.

Note the way you interact with Python at the prompt. After entering an expression such as `2 + 3`, Python "evaluates" it to a simpler form, `5`, and then prints out the answer for you. **This process is called the Read Eval Print Loop, or REPL**. Reading takes commands from you, the input is evaluated or run, the result is printed out, and the prompt is shown again to wait for more input. The normal terminal (the one with the `$`) is another example of a REPL.

The REPL is useful for quick tests and, later, can be used for exploring and debugging your programs interactively. You might consider it a kind of playground for testing and experimenting with python expressions.

## Challenge

1. For a few minutes, practice moving in and out of Python's interactive mode (aka the REPL). You can get out of Python by hitting <kbd>control</kbd> + <kbd>d</kbd> (or <kbd>control</kbd> + <kbd>z</kbd> or <kbd>control</kbd> + <kbd>z</kbd> + <kbd>enter</kbd> if you're on a computer running Windows) or by typing `exit()`. You can get back in the REPL by typing `python` at the `$` prompt. Remember that you're in the REPL when you see `>>>`, and you're in bash or your terminal when you see the `$`.

2. One "operator" (math symbol) we didn't learn is the exponent—you know, "x raised to the power of..." If you were Guido van Rossum, the creator of Python, how would you define this operator?

## Solution

2. The exponent operator is two asterisks (`**`). For example, the number `3` to the power of `2` would be expressed as `3**2`.

## Evaluation

What are the characteristics of the REPL? Select all that apply.
- The REPL has a prompt that begins with `$`.
- The REPL has a prompt that begins with `>>>`.*
- The REPL and the terminal are the same thing.
- The REPL can be used to evaluate mathematical expressions like `2 + 2`.*

## Keywords

Do you remember the glossary terms from this section?

- [REPL](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/repl.md)

---

↻ [Start](../README.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Types](02-types.md) →