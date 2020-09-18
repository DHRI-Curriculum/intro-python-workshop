← [Conditionals](08-conditionals.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Doing Things to Lists](10-doing-things-to-lists.md) →

---

# 9. Input

**Note:** If you're using Python 2.7, replace all `input()` functions in the code below with `raw_input()`. You can check your version by running `python --version` in the command line.

Python allows you to take input directly from the user using the `input()` function.

Let's try it out by setting the function to a variable, which we will call `greeting`. Open the Python REPL and type:

```pycon
>>> greeting = input()
```

When you press <kbd>enter</kbd>, you should see a blank line. Type in your favorite greeting. I'm going to type `hey you!`. Then, press <kbd>enter</kbd>.

```pycon
>>> greeting = input()
hey you!
```

Python has saved your input text to the variable `greeting`. When you type in `greeting` one more time, it will print out that input text. Pretty nifty, right?

```pycon
>>> greeting = input()
hey you!

>>> greeting
'hey you!'
```

You can play around with `input()` by adding some prompt text within the parenthesis. Whatever you put inside the parenthesis, enclosed by quotes, will prompt the user to type in their text, which is then assigned to the variable set to `input()`. Sounds complicated, so give it some practice:

```pycon
>>> feelings = input('How are you feeling today? ')
How are you feeling today?
```

Note that there's a little space after the question mark and before the closing quotation mark, which is to improve readability.

We can answer with `like a rollercoaster of emotions`. Then, when we type in our variable `feelings` and press enter, we'll get our input printed back at us.

```pycon
>>> feelings = input('How are you feeling today? ')
How are you feeling today? like a rollercoaster of emotions

>>> feelings
'like a rollercoaster of emotions'
```

## Challenge

Remember this loop?

```python
field = "Media Studies"

if field == "Media Studies":
    print("Grammophone, Film, Typewriter")
elif field == "Critical University Studies":
    print("The Undercommons")
elif field == "Textual Scholarship":
    print("Radiant Textuality")
else:
    print("I don't know what field you're talking about! I'm just a little program...")
```

Now, that we understand a bit about how `input()` works, let's use it to improve our book application. We are going to use `input()` to ask for the field before displaying the output. To do this, add one more line of code that sets the `field` variable to an `input()`. Make sure you include a little prompt that asks the user what book they want to select or read that day.

## Solution

```python
field = input("Which field of study do you want to read about today? ")

if field == "Media Studies":
    print("Grammophone, Film, Typewriter")
elif field == "Critical University Studies":
    print("The Undercommons")
elif field == "Textual Scholarship":
    print("Radiant Textuality")
else:
    print("I don't know what field you're talking about! I'm just a little program...")
```

## Evaluation

If we wanted to calculate the length of an input using `len()`, how would we write that expression?
- `input() = len()`
- `response = len().input()`
- `len(input()) = length_of_response`
- `length_of_response = len(input())`*

## Keywords

Do you remember the glossary terms from this section?

- [input()](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/input.md)

---

← [Conditionals](08-conditionals.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Doing Things to Lists](10-doing-things-to-lists.md) →