<!--

revision notes from rafa: 
More emphasis on the major shift from REPL to text editor, to reinforce the different spaces. 

-->

[<<< Previous](03-variables.md) | [Next >>>](05-errors.md)

# Running scripts

So far, you've interacted with Python one line at a time in the REPL. This is what we call the Interactive Mode, which is like a playground for experimenting and exploring different Python expressions,  like `2 + 2` or `type("some stuff")`. The code that we write in the REPL is not saved after you exit, which means that this space is for running Python expressions and *not* for writing longer programs. 

For the rest of this session, we're going to expand beyond the REPL to write and execute longer programs. To do this, we will begin to work with text editor, where we write out longer Python scripts, and run those scripts from the terminal. 

This is a big move, so let's take it slow. The major change is that we will be working across two spaces, the terminal and the text editor, rather than just the terminal alone. We will be writing our scripts into the text editor, and using the terminal to run those scripts. 

## Your first script

First, let's begin with the text editor. Open your text editor of choice (such as VS Code) and create a new file with this line:

```python
print("Hello world!")
```

Save it with the name `hello.py` to a known location, such as your desktop. Open your terminal and move to the desktop directory:

```console
$ cd Desktop
```

Once you're in the folder with your `hello.py` file, move to the terminal. Do *not* enter the Python Interactive Mode (the REPL), which is unecessary to run python scripts. Instead, lookout for the `$` symbol that lets you know you're in the terminal. If you find yourself in the Interactive mode (`>>>`), then exit it with `control-D`. You should see the `$` symbol, letting you know you're back in the terminal.  

Now that you're in the terminal, type the following, and press enter:

```console
$ python hello.py
Hello world!
```

You should see the text `Hello world!` appear as output in the terminal window. 

There are a couple of important things to note here. First, it bears repeating that you are moving between two different spaces, the text editor and the terminal. You wrote your Python script in the text editor, and used the terminal to run the script. Second, within in the text editor, you included the `print()` function  because, unlike in the REPL, things aren't automatically printed out when writing scripts. When you're in the text editor, you always need to include the `print()` function so that your output will appear in the terminal. 

Congratulations! You've written your first script. That's kind of a big deal.

## Challenges

1. Rewrite your program so that you assign the message to a variable, then print the variable. This will make your program two lines instead of one. There's a fancy programmer word for rewriting your code without changing it's behavior—"refactoring."

2. (optional) Are you already getting sick of typing `python hello.py` again and again? Try typing `!!` in the command line (the `$`). This will run your last line of code again.

3. (even more optional) If you're on Windows and have a minute, try pressing the Windows button on your keyboard and searching for a program called `IDLE` that comes with Python. It's a special editor (or IDE) that lets you run Python code from inside it. You might like it more than git bash.

## A Note on Text

Fundamentally, Python programs are just text files. You can write them in any text editor, like VS Code or Notepad on Windows. When you pass the text file to Python, it runs the code in the file one line at a time. There's nothing special about `.py` files—they're just regular text files. This makes them work well with command line tools like Git. The tools you've learned so far—the command line, Git, markdown, grep—are all designed to work well together, and the medium through which they all work is plain text.

[<<< Previous](03-variables.md) | [Next >>>](05-errors.md)
