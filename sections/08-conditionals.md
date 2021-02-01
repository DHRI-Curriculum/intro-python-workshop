← [Loops](07-loops.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Input](09-input.md) →

---

# 8. Conditionals

Conditionals allow programs to change their behavior based on whether some statement is true or false. Let's try this out by writing a script that will give different outputs (consisting of book titles) based on the specified field of study:

```python
field = "Media Studies"

if field == "Media Studies":
    print("Grammophone, Film, Typewriter")
else:
    print("I don't know what field you're talking about! I'm just a little program...")
```

In our first line, we set a variable `field` to the string `"Media Studies"`, representing our chosen field of study. The `if` statement checks whether the field is set to the string "Media Studies". If it is, the code in the block beneath is executed, so the string `"Grammophone, Film, Typewriter"` will be printed.

It's important to note at this point the use of the double equals sign `==` in `if` statements. The double equals is an _equality_ operator, and it checks to see if the two values on either side are equivalent. Contrast this with the single equals that you've already seen, `=`, which is an _assignment_ operator, that assigns a value to a variable. In the line `field = "Media Studies"`, you are using the assignment operator `=` to set the variable's value to "Media Studies", (a string) while in the `if` statement, you're using the equality operator `==` to check if the field is equivalent to "Media Studies".

You'll also notice the inclusion of a new line, the `else` statement. The `else` statement handles any inputs that aren't "Media Studies", and the program merely prints out that it doesn't know what you should bring.

Try this script out both with the variable set to "Media studies" and the variable set to some other value, representing another field of study.

What if we want our program to handle more fields of study, giving different messages for each one? Other cases after the first `if` statement are handled with `elif`, which is a shortened version of `else if`:

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

You can add as many `elif` statements as you need, meaning that conditionals in Python have one `if` statement, any number of `elif` statements, and one `else` statement that catches any input not covered by `if` or `elif`. Over the next sections, we'll work on improving this little application, making it able to handle user input directly.

## Challenge

Add two more `elif` statements to this program to make it better able to handle different potential fields of study. Change the field of study a couple of times, making sure to save after each change, to test out your code.

## Solution

```python
field = "Media Studies"

if field == "Media Studies":
    print("Grammophone, Film, Typewriter")
elif field == "Critical University Studies":
    print("The Undercommons")
elif field == "Textual Scholarship":
    print("Radiant Textuality")
elif field == "Critical Race Studies"
    print("The New Jim Crow")
elif field == "DH Methodologies"
    print("Algorithmic Criticism")
else:
    print("I don't know what field you're talking about! I'm just a little program...")
```

## Evaluation

What is the difference between the double equals (`==`) and single equals (`=`)?
- The double equals checks to see if one value is equivalent to the other, as in `2 == 2`.*
- The double equals assigns the value on the right to the variable on the left, as in `x == 2`.
- The single equals checks to see if one value is equivalent to the other, as in `2 = 2`.
- The single equals assigns the value on the right to the variable on the left, as in `x = 2`.*

## Keywords

Do you remember the glossary terms from this section?

- [if-Statement](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/if_statement.md)

---

← [Loops](07-loops.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Input](09-input.md) →