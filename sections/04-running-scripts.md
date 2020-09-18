← [Variables](03-variables.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Errors in Python](05-errors-in-python.md) →

---

# 4. Running scripts

So far, you've interacted with Python one line at a time in the REPL. This is what we call the Interactive Mode, which is like a playground for experimenting and exploring different Python expressions, like `2 + 2` or `type("some stuff")`. The code that we write in the REPL is not saved after you exit, which means that this space is for running Python expressions and *not* for writing longer programs.

For the rest of this session, we're going to expand beyond the REPL to write and execute longer programs. To do this, we will begin to work with a text editor, where we write out Python scripts, and run those scripts from the terminal.

This is a big move, so let's take it slow. To reiterate, the major change is that we will be working across two spaces, the terminal and the text editor, rather than just the terminal alone. We will be writing our scripts into the text editor, and using the terminal to run those scripts.

## Your first script

First, let's begin with the text editor. Open your text editor of choice (such as Visual Studio Code) and create a new file with this line:

```python
print("Hello world!")
```

Save it with the name `hello.py` to a known location, such as your desktop. Open your terminal and move to the desktop directory:

```console
$ cd Desktop
```

Once you're in the folder with your `hello.py` file, move to the terminal. Do *not* enter the Python Interactive Mode (the REPL), which is unecessary to run python scripts. Instead, lookout for the `$` symbol that lets you know you're in the terminal. (If you find yourself in the Interactive mode (`>>>`), then try exiting it with <kbd>control</kbd> + <kbd>D</kbd>. You should see the `$` symbol, letting you know you're back in the terminal. If you still do not see the `$` symbol, type `exit()` followed by <kbd>enter</kbd> after the Python prompt, `>>>`.)

Now that you're in the terminal, type the following, and press enter:

```console
$ python hello.py
Hello world!
```

You should see the text `Hello world!` appear as output in the terminal window.

Congratulations! You've written your first script. That's a big deal!

There are a couple of important things to note here:
- First, it bears repeating that you are moving between two different spaces, the text editor and the terminal. You wrote your Python script in the text editor, and used the terminal to run the script.
- Second, within in the text editor, you included the `print()` function because, unlike in the REPL, things aren't automatically printed out when writing scripts. When you're in the text editor, you always need to include the `print()` function so that your output will appear in the terminal.

## A Note on Text

Fundamentally, Python programs are just text files. You can write them in any text editor, like Visual Studio Code or Notepad on Windows. When you pass the text file to Python, it runs the code in the file one line at a time. There's nothing special about `.py` files—they're just regular text files. This makes them work well with command line tools like Git. The tools you can learn through the DHRI Curriculum—the command line, Git, markdown, grep—are all designed to work well together, and the medium through which they all work is plain text.

## Challenge

1. Rewrite your program so that you assign the message to a variable, then print the variable. This will make your program two lines instead of one. There's a fancy programmer word for rewriting your code without changing it's behavior—"refactoring."

2. (optional) Are you already getting sick of typing `python hello.py` again and again? Try typing `!!` in the command line (the `$`). This will run your last line of code again. Additionally, you can press the <kbd>up arrow</kbd> at the terminal prompt, and keep pressing it to scroll through the most recent commands.

3. (even more optional) If you're on Windows and have a minute, try pressing the <kbd>Windows</kbd> button on your keyboard and searching for a program called `IDLE` that comes with Python. It's a special editor (or IDE) that lets you run Python code from inside it. You might like it more than Git Bash.

## Solution

1. You should type the following into `hello.py`:

    ```python
    greeting = "Hello World!"
    print(greeting)
    ```

    Then, making sure you're in the right directory, run `python hello.py` in the terminal `$`. You should see the following output:

    ```console
    $ python hello.py
    Hello world!
    ```

## Evaluation

What are the differences between the terminal, REPL, and text editor? Select the correct statement from the below options.
- You can run scripts from the **terminal** that were written on the text editor. *
- The **REPL** allows you to save scripts for later use.
- The **text editor** allows you to test code on the fly.

## Keywords

Do you remember the glossary terms from this section?

- [REPL](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/repl.md)
- [Scripts](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/scripts.md)
- [print()](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/print.md)

---

← [Variables](03-variables.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Errors in Python](05-errors-in-python.md) →