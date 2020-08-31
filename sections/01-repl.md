# Interacting with Python

Let's begin by starting an "interactive session" session with Python. This means we will be using Python in the terminal, which is a special space that allows us to run little bits of Python, experimenting and exploring what it can do, without having to save it. Think of this interactive space as a playground. Later on, we will be working with Python in a more robust way, doing what we call saving and executing Python scripts.

For now, though, let's start an interactive session with Python, which is accessed through the terminal. 

Open your terminal and type:

```console
$ python
```

at the prompt. You should see something like this

```pycon
Python 3.6.3 |Anaconda, Inc.| (default, Oct 13 2017, 12:02:49)
[GCC 7.2.0] on Linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Unlike the normal `$` terminal prompt, the Python prompt looks like this:

```pycon
>>>
```

These carrots are how you know that you have entered an interactive session with Python. Now you are interacting directly with Python, rather than in the regular terminal. Keep an eye on these carrots, as a common early source of confusion is entering terminal commands into the Python prompt or entering Python commands into the terminal.

## A Little Math

Let's try a little math at the Python prompt. In the example below, type the text that appears after the Python prompt (the `>>>`). The line below is the output that is returned. This will be a standard convention when giving examples using the Python prompt.

<!--

Rafa: add print to the expressions; can point out that it's not necessary in the REPL, but it is with scripts.
Filipa: isn't this too much information, though? We don't want to confuse them at this point by introductin functions. 

-->
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

Note the way you interact with Python at the prompt. After entering an expression such as `2 + 3`, Python "evaluates" it to a simpler form, `5`, and then prints out the answer for you. **This process is called the Read Eval Print Loop, or REPL**. Reading takes commands from you, the input is evaluated or run, the result is printed out, and the prompt is shown again to wait for more input. The normal terminal (the one with the `$`) is another example of a REPL. The REPL is the same thing as the Interactive mode, what we described earlier as the playground for running Python. REPL and Interactive mode describe this specific context for using Python, by running it within the terminal.

The REPL is useful for quick tests and, later, can be used for exploring and debugging your programs interactively.

## Challenges

1. For a few minutes, practice moving in and out of Python's interactive mode (also known as the REPL). You can get out of Python by hitting `Control-d` (or `Control-z` if you're using Git Bash) or by typing `exit()`, and you can get back in by typing `python` at the `$` prompt. Remember that you're in the REPL when you see `>>>`, and you're in bash when you see the `$`.

2. One "operator" (math symbol) we didn't learn is the exponent—you know, "x raised to the power of..."  If you were Guido van Rossum, the creator of Python, how would you define this operator? Look up the exponent operator in Python on Google and see how close you were.
