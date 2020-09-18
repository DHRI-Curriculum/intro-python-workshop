← [Types](02-types.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Running Scripts](04-running-scripts.md) →

---

# 3. Variables

A variable is **a symbol that refers to an object**, such as a string, integer, or list. If you're not already at the Python prompt, open your terminal and type `python` at the `$`. You're in the right place when you see `>>>`.

Try these commands in order:

```pycon
>>> x = 5

>>> x
5

>>> x + 10
15

>>> y = "hello"

>>> y
'hello'

>>> y + " and goodbye"
'hello and goodbye'
```

As you can see from the examples above, the `=` sign lets you assign symbols like `x` and `y` to data.

Variables can be longer words as well, and they can be set to lists:

```pycon
>>> books = ['Gender Trouble', 'Cruising Utopia','Living a
>Feminist Life']

>>> books
['Gender Trouble', 'Cruising Utopia', 'Living a Feminist Life']

>>> type(books)
<class 'list'>
```

Variables can have letters, numbers, and underscores, **but should start with a letter**.

If you are curious about learning more about naming conventions for variables, you can check out the PEP8 style guide's section on [Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions). PEP8 is the widely accepted guide for Python programmers everywhere.

## Challenge

So I just told you that variables shouldn't start with a number or an underscore. What does that even mean? Will your computer explode if you write `1_book = "Gender Trouble"`?

Only one way to find out. Try giving weird names to variables and see if you can learn a bit about the rules.

## Solution

There are a few rules regarding the way that you write the variable statement. This is because Python reads everything left to right, and needs things to be in a certain order.

First, you cannot use any numbers or special characters to start a variable name. So `1_book`, `1book`, or any variable that contains special characters `@`, `#`, `$`, `$`, etc, wouldn't be acceptable in Python. You must start the variable with a letter and avoid using special characters.

You can incorporate numbers after you've started with a letter. So `book_1` or `b1` is acceptable, though you cannot use special characters at any point in the variable name.

Second, you might also notice that variable syntax requires you to write the variable name first, followed by an equal sign `=`, and then the value, or data. You cannot start the variable statement with the data value, because python always recognizes the first thing written as the thing to be assigned. The thing that comes after the `=` is the data that becomes attached to the preceding variable.

## Evaluation

Select all the variable expressions that are allowed in Python.
- `1 = one`
- `one = 1`*
- `$$$ = "dollar_signs"`
- `first_book = "Orlando"`*

## Keywords

Do you remember the glossary terms from this section?

- [Variables](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/variables.md)

---

← [Types](02-types.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Running Scripts](04-running-scripts.md) →