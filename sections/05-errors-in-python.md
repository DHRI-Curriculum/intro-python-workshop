← [Running Scripts](04-running-scripts.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Lists](06-lists.md) →

---

# 5. Errors in Python

Our usual response when seeing an error on a computer screen is a stress response. Our heart rate elevates and, if we cannot do what we were asking the computer to do, our frustration mounts. This is because many errors when interacting with programs are not useful or informative, and because we often have no capability to fix the program in front of us.

In Python, errors are our friends. This might be hard to accept initially, but the errors you see when running Python scripts generally do a good job of pointing you to what's going wrong in your program. When you see an error in Python, therefore, try not to fall into the stress response you may be used to when interacting with your computer normally.

## Two Kinds of Errors

In Python, there are two kinds of errors you will encounter frequently. One appears before the program runs, and the other appears during the execution of a program.

**Syntax errors**: When you ask Python to run a program or execute a line in the REPL, it will first check to see if the program is valid Python code—that is, that it follows the grammatical or syntactical rules of Python. If it doesn't, before the program even runs, you'll see a syntax error printed out to the screen.

In this below example, the syntax error is a common one—mismatched single and double quotes, which is not allowed in Python. You can replicate the below error by opening the REPL (type `python` in the command line) and entering the line after the `>>>` prompt.

```pycon
>>> print('This string has mismatched quotes. But Python will help us figure out this bug.")
  File "<stdin>", line 1
    print('This string has mismatched quotes. But Python will help us figure out this bug.")
                                                                                           ^
SyntaxError: EOL while scanning string literal
```

Note the caret (`^`) underneath the mismatched quote, helpfully pointing out where the error lies. Similarly, if this error happened when running a script, Python would tell us the filename and the line number for the line on which the error occurs.

**Traceback errors**: These errors occur during the execution of a Python program when the program finds itself in an untenable state and must stop. Traceback errors are often logical inconsistencies in a program that is valid Python code. A common traceback error is referring to a variable that hasn't been defined, as below.

```pycon
>>> print(not_a_variable)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'not_a_variable' is not defined
```

Traceback errors try to tell you a little about what happened in the program that caused the problem, including the category of error, such as `NameError` or `TypeError`.

## Debugging

Debugging is a fancy word for fixing problems with a program. Here are some common strategies for debugging a program when first learning Python:

- If the error is a syntax error:
    - Look at where the caret is pointing.
    - Pay attention to grammatical features such as quotes, parentheses, and indentation.
    - Consider reading the program, or the offending line, backward. It's surprising, but this often helps to detect the issue.
- If the error is a traceback error:
    - First look at the line where the error occured, then consider the general category of error. What could have gone wrong?
    - If the error is a name error (NameError), check your spelling.
    - Try copying the last line of the error and pasting it into Google. You'll often find a quick solution this way.
- If you changed the program and expect a different output, but are getting old output, you may not have saved the file. Go back and make sure the file has been correctly saved.

## Challenge

Try to create as many errors as you can in the next few minutes. After getting your first two syntax errors, try instead to get traceback errors. Some areas to try include mathematical impossibilities and using math operations on types that do not support them.

## Solution

Some examples of **syntax errors** include...

- Starting the variable name with a special character.

    ```pycon
    >>> %greeting = "Hello World"
      File "<stdin>", line 1
        %greeting = "Hello World"
        ^
    SyntaxError: invalid syntax
    ```

- Starting a variable by writing the data values before the variable.

    ```pycon
    >>> "hey there!" = greeting
      File "<stdin>", line 1
    SyntaxError: can't assign to literal
    ```

- Including spaces in a variable.

    ```pycon
    >>> pleasant greeting = "Hello!"
      File "<stdin>", line 1
        pleasant greeting = "Hello!"
                        ^
    SyntaxError: invalid syntax
    ```

Some examples of **traceback errors** include...

- Concatenating data types, like strings and integers.

    ```pycon
    >>> greeting = "hello" + 1
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate str (not "int") to str
    ```

- Using Booleans (`True` or `False`) without capitalizing them.

    ```pycon
    >>> greeting = false
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'false' is not defined

    >>> greeting = False

    >>> greeting
    False
    ```

## Evaluation

If you get an error, what can you do to debug it? Select all that apply:
- If it's a _syntax error_, look for the caret as a starting point.*
- If it's a _traceback error_, make sure all your variables are defined.*
- Copy the error message into a Google search.*
- Run spell check on your code.

## Keywords

Do you remember the glossary terms from this section?

- [Syntax Errors](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/syntax_error.md)
- [Traceback Errors](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/traceback_error.md)

---

← [Running Scripts](04-running-scripts.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Lists](06-lists.md) →