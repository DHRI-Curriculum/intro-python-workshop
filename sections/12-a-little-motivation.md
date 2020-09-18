← [Finding Answers with Google](11-finding-answers-with-google.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Objects in Python](13-objects-in-python.md) →

---

# 12. A Little Motivation

Early on, we learned a bit about lists, which look like this:

```python
["Gender Trouble", "Cruising Utopia", "Living a Feminist Life"]
```

We're going to create a small application that will print a random motivational saying every time a user presses <kbd>enter</kbd>. Our first step will be to create a list of positive sayings:

```python
motivational_phrases = [
        "Importing modules is easy!",
        "Programming! Yay!",
        "You write lists like a pro!",
    ]
```

You're still using the same list format. Remember lists open with a square bracket `[`, have items seperated with commas, and end with a square bracket `]`, like this:

```python
[1, 2, 3, 4, 5]
```

However, our positivity list above spreads the list out over multiple lines for greater readability, which is allowed in Python. Remember that you can change the strings in the list to whatever phrases you choose.

## Importing a module

Now that we have our sayings, let's use it in conjunction with some functionality from a module that's built into Python: the `random` module.

```python
import random

motivational_phrases = [
        "Importing modules is easy!",
        "Programming! Yay!",
        "You write lists like a pro!",
    ]

print(random.choice(motivational_phrases))
```

The `random.choice` function chooses a random item from a list and returns it. The `.` syntax indicates that the function is coming from the `random` library.

## Challenge

1. As with our library app, this positive saying generator could be improved by making it so the program doesn't have to run again every time to get new output. Add a while loop for the final version. Remember to include a `break` statement or use <kbd>control</kbd> + <kbd>c</kbd> to get out of the loop! Read more [about while loops here](https://www.w3schools.com/python/python_while_loops.asp).

2. The real point of this section is to learn `import`, which is where Python really starts to get interesting. Python comes with many libraries (importable collections of code), written by others that can be pulled into your program, allowing you to use that functionality. In this challenge, do a little research on Python libraries that might solve a problem for you or address a domain that you're interested in.

Think of something you're interested in doing (statistics, text analysis, web scraping, quantitative analysis, processing Excel/PDF/image files) and search google "<_thing you are interested in_> python library". You're almost certain to find some useful results. For example, if you wanted to find Python libraries for dealing with cleaning up HTML files, you might search one of these:

> working with html python library

> html parser python library

In your research, you may also want to look at the libraries that come with Python. You can find a list of libraries in these libraries [here](https://docs.python.org/3/py-modindex.html).

## Solution

1. Here's how you could add a `while` loop to our positive saying generator:

    ```python
    import random

    while True:
        motivational_phrases = [
            "Importing modules is easy!",
            "Programming! Yay!",
            "You write lists like a pro!",
            ]

        # Because this is input, the user will need to hit enter to see a new phrase
        input(random.choice(motivational_phrases))
    ```

## Evaluation

What is a module? Select all that apply:
- A module is a file of code.*
- Applications can incorporate many different modules.*
- A module needs to be downloaded and installed.
- A module needs to be imported with an `import` statement.*

## Keywords

Do you remember the glossary terms from this section?

- [Modules](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/module.md)
- [Random](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/random.md)
- [while loops](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/while_loop.md)

---

← [Finding Answers with Google](11-finding-answers-with-google.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Objects in Python](13-objects-in-python.md) →