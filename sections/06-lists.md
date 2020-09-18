← [Errors in Python](05-errors-in-python.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Loops](07-loops.md) →

---

# 6. Lists

Remember lists? They look like this:

```python
books = ['Gender Trouble', 'Cruising Utopia', 'Living a Feminist Life']
```

For now, let's just create a list and print it out. In a text editor, our script will look like this:

```python
books = ['Gender Trouble', 'Cruising Utopia', 'Living a Feminist Life']
print(books)
```

Save this to a new file called `loop.py` and run it with `python loop.py`. You should see the list printed out in the terminal.

So far, we've only learned one function: `type()`. Let's try out another, called `len()`, which returns the number of items in a list or the number of characters in a string. Type out the following lines in your loop.py file:

```python
books = ['Gender Trouble', 'Cruising Utopia', 'Living a Feminist Life']
# print(books)

list_length = len(book)

print(list_length)
```

Let's take apart this unfamiliar line of code: `list_length = len(book)`
- First, look to the end of this statement. `list_length = len(book)` takes the `book ` variable as an argument for the `len()` function. That's why `book` is within the parenthesis. This format basically means that it will run the `len()` function on the items in `book`.
- Then, it sets the result of that process to a new variable, called `list_length`.

This might appear a bit complex at first, but if you read the line slowly you should be able to connect the dots.

Notice that when you run the code above, you don't see the `books` list printed out. That's because that line has become a comment. If you put a `#` (hash or pound) at the beginning of a line, that line will be ignored.

## List Indexing

A useful property of a list is the list index. This allows you to pick out an item from within the list by a number starting from zero:

```python
print(books[0]) # Gender Trouble
print(books[1]) # Cruising Utopia
```

Note that the first item in the list is `item[0]`. The second item is `item[1]`. That's because counting in Python, and in almost all programming languages, starts from `0`.

Additionally, you can print out the last item in a list using negative numbers, where `-1` denotes the last item in the list:

```python
print(books[-1]) # Living a Feminist Life
```

## Slicing Lists

There are many things you can do with list indexing, like slicing. Slicing consists of taking a section of a list, using the list index to pick out a range of list items. For example, you could take out the first _two_ items of a list with a slice that begins with `0` and ends with `2`.

The slice syntax consists of square brackets, start point and end point, and a colon to indicate the gap in between. This should print out the first two items of your list.

```python
print(books[0:2])
```

Note a couple of things. First, the start point is *inclusive*, meaning that Python will include the `[0]` item in your range, and the end point is _exclusive_, so Python won't print the `[2]` item. Instead, it will print everything up until that `[2]` item.

For ultimate brevity, you can also write this expression as:

```python
print(books[:2])
```

The empty value before the colon allows Python to assume the range starts at the first list item, at `[0]`. You can also end the slice with `:`, if you want the list range to include all subsequent items until the end of the list. The example below will print everything from the second item to the end of the list.

```python
print(books[1:])
```

With a list that contains three items total, list slicing might not seem very impressive right now. However, this will become a powerful tool once we get to more sophisticated text analysis and start to encounter lists that contain hundreds (or thousands!) of items.

## Challenge

Create a new list of books in the REPL, with at least 5 books in your list. Make sure the total number of books in the list is an **odd** number. How do you get python to print out the book in the middle of the list? What about the three books in the middle? Remember that the first value in a slice is _inclusive_, and the final value is _exclusive_.

## Solution

```pycon
>>> books = ['Gender Trouble', 'Cruising Utopia', 'Living a Feminist Life', 'Radiant Textuality', 'The Undercommons']

>>> books[2] # ['Living a Feminist Life']

>>> books[1:4] # ['Cruising Utopia', 'Living a Feminist Life', 'Radiant Textuality']
```

## Evaluation

How would you get Python to print the length of the last book in the list? Hint: this number reflects the length of the _string_ which is the last item in the list. Choose the correct expression from the options below.
- `len(books)`
- `print(books[-1])`
- `print(len[-1])`
- `print(len(books[-1]))`*

## Keywords

Do you remember the glossary terms from this section?

- [list](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/list.md)
- [list indexing](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/list_indexing.md)
- [len()](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/len.md)

---

← [Errors in Python](05-errors-in-python.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Loops](07-loops.md) →