← [Lists](6-lists.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Conditionals](8-conditionals.md) →

---

# 7. Loops

What if we want to print out each item in the list separately? For that, we'll need something called a loop:

```python
books = ['Gender Trouble', 'Cruising Utopia', 'Living a Feminist Life']
# print(books)

for book in books:
    print("My favorite book is " + book)
```

What's happening here? This kind of loop is called a "for loop", and tells Python: "for each item in the list, do something." Let's break it down:

```python
for <variable name> in <list name>:
    <do something>
```

Indented code like this is known as a "code block." Python will run the `<do something>` code in the code block once for each item in the list. You can also refer to `<variable name>` in the `<do something>` block.

You can also loop through items within a string. For example, type the following into your `loop.py` file:

```python
for letter in "hello":
    print(letter)
```

The result should print out each letter of the string `hello`, one by one.

## A Note on Variable Names

In this section, we've discussed books in the context of a list. Why do we use the variable name `books` in this section for our list of book names? Why not just use the variable name `x`, or perhaps `f`?

While the computer might not care if our list of books is called `x`, giving variables meaningful names makes a program considerably easier to read than it would be otherwise. Consider this for loop:

```python
y = ['Gender Trouble', 'Cruising Utopia', 'Living a Feminist Life']

for x in y:
    print(x)
```

Which is easier to read, this for loop or the one used in the example?

When variable names accurately reflect what they represent, and are therefore meaningful, we call them "semantic." Always try to create semantic variable names whenever possible.

## Challenge

1. Here's a list of numbers:

    ```python
    prime_numbers = [2, 3, 5, 7, 11]
    ```

    Write some code to print out the square of each of these numbers. Remember that the square of a number is that number times itself. The solution is below, but you're not allowed to look at it until you've tried to solve it yourself for 3.5 minutes. (Seriously! That's 210 seconds.)

2. First, ignore this challenge because it's too hard. Next, look up a new concept—"f-string" (a formatting technique for strings)—on Google and use it to write a loop that gives the following output:

    ```
    The square of 2 is 4.
    The square of 3 is 9.
    The square of 5 is 25.
    The square of 7 is 49.
    The square of 11 is 121.
    ```

    Note: the "f-string" is a new string formatting method for Python 3. You can [read more about this new string formatting method](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python).

## Solution

1. To get the square of the elements in the list `prime_numbers`, you can:

    ```python
    prime_numbers = [2, 3, 5, 7, 11]

    for num in prime_numbers:
        print(num * num)
    ```

2. Using "f-strings" to output the list of results in the challenge would look something like this:

    ```python
    prime_numbers= [2,3,5,7,11]
    for num in prime_numbers:
        print(f"The square of {num} is {num * num}")
    ```

## Evaluation

What are different ways for describing what a "for loop" can do?
- for each item in a list, multiply it against itself.*
- print the contents of a list.*
- add a new item to a list.
- loop through characters in a string.

## Keywords

Do you remember the glossary terms from this section?

- [for-loop](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/for_loop.md)
- [f-string](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/f-string.md)

---

← [Lists](6-lists.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Conditionals](8-conditionals.md) →