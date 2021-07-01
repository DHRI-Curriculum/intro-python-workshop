← [Interacting with Python](01-interacting-with-python.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Variables](03-variables.md) →

---

# 2. Types

Types are classifications that let the computer know how a programmer intends to use a piece of data. You can just think of them as, well, types of data.

We've already seen one type in the last section: the integer. In this section, we'll learn four more: the floating point number, the string, the boolean, and the list.

Enter these lines as you see them below:

```pycon
>>> type(1)
<class 'int'>

>>> type(1.0)
<class 'float'>

>>> type("Hello there!")
<class 'str'>

>>> type(True)
<class 'bool'>

>>> type([1, 2, 3])
<class 'list'>
```

Each of the responses show how the different types of data registers as different "types" for Python:

**Integers** (like `1` above) are whole numbers.

**Floats** (like `1.0` above) are numbers with decimals, and are treated a little differently than integers.

**Strings** (like `"Hello there!"` above) are arbitrary sets of characters, such as letters and numbers. You can think of them as a way to store text.

**Booleans**: (like `True` above) is a fancy term for values representing "true" and "false," or "truthiness" and "falsiness." In Python they are always capitalized: `True` and `False`.

**Lists**: (like `[1, 2, 3]` above) are ordered collections of values. You can put any of the other types in a list: `["hello", "goodbye", "see ya later"]` is also a valid list.

Don't worry about trying to actively remember these types. We'll be working with each in turn in the following sections.

## What's the deal with type()?

`type()` is a function. You can think of functions in Python in a few different ways:

1. A way of doing something in Python.
2. A way of saving some code for reuse.
3. A way of taking an input, transforming that input, and returning an output. The input goes in the parentheses `()`.

These are all valid ways of thinking about functions. We'll be learning more about functions in later sections.

## Challenge

Open your web browser, and google the phrase "python function." Skim through the first few results. What words do you recognize, and which ones look unfamiliar? What do you think the unfamiliar ones mean? Try to rephrase some of this new language, and guess what they mean in your own words.

## Solution

When you google "python function," you may see some phrases that look unfamiliar, like "return value" or "pass parameters." These are advanced terms for inputting and outputting data from a function. It's important to become familiar with the Python's terminology about functions, as it will be helpful later on when you start working with these components.

## Evaluation

Select all the following that accurately describe the data type categories.
- Booleans represent only `True` or `False` values.*
- Integers can be expressed with numbers like `1` or letters `one`.
- Strings can contain numbers within quotations, like `"1"`.*
- Lists can contain strings, like `['banana, 'coffee', 'eggs']`.*

## Keywords

Do you remember the glossary terms from this section?

- [Function](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/function.md)
- [Boolean](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/boolean.md)
- [Float](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/float.md)
- [Integer](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/integer.md)
- [String](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/string.md)
- [List](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/list.md)
- [Type()](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/type.md)

---

← [Interacting with Python](01-interacting-with-python.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Variables](03-variables.md) →