← [Input](9-input.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Finding Answers with Google](11-finding-answers-with-google.md) →

---

# 10. Doing Things to Lists

Okay. Let's make our little book application a little more robust. We are going to create a list of books (remember lists?) that we can then manipulate in all sorts of ways.

First, go back to your terminal and enter the REPL, or Python's interactive mode. When you see the `>>>`, create a list with at least three books that are important to your research right now. Shorten the titles to one or two words if need be. Let's call this list our `library`. Remember the proper syntax for creating a list includes square brackets with commas separating the list items. Because the items are strings, they should also be inside quotes.

```pycon
library = ["Orlando", "Confessions of the Fox", "These Waves of Girls"]
```

Next, let's sort our `library` in alphabetical order. There's a handy method called `sort()` for doing just this kind of thing. What's a _method_, you might ask? Well, _methods_ are very similar to _functions_, and you'll remember that functions are ways of doing things, like `print()` and `type()`. Methods are also ways of doing things, but these things are attached to what we call _objects_ in Python. Objects are part of object-oriented-programming, and that's definitely not necessary to learn right now. Suffice it to say that methods are just like functions, that is, they are ways of doing things to your data.

To sort the list, use the `sort()` method on your list. It should look like this:

```pycon
library = ["Orlando", "Confessions of the Fox", "These Waves of Girls"]
library.sort()
print(library)
```

What happened here? Let's take it line by line. First, we created a list `library` with three items attached to it. Then, we applied the `sort()` method to the library list. Finally, we printed the `library`, which is now sorted in alphabetical order.

You'll see that we have a couple of new things happening with symbols.
- First, the period `.` which is an _operator_ in Python. The period operator is another part of object-oriented-programming, and it basically means that we are applying a task to whatever precedes the period. In this case, we are applying the `sort()` method to our `library` list. It's kind of like attaching a function to our `library`.
- Second, we have the parenthesis `()` after `sort`. When you get more comfortable with programming, you'll often use the parentheses to include what we call _arguments_ that allows us to do more complex things to data. Let's see how an argument works with the `append()` method.

What if we want to add items to the list? We can use the `append()` method for that. Try:

```pycon
library = ["Orlando", "Confessions of the Fox", "These Waves of Girls"]
library.append("La Frontera")
print(library)
```

Here, we added `"La Frontera"` as an argument to the `append()` method, but putting it between the parenthesis. It basically means that we will be appending this specific title to the library list.

When you print `library`, you should see your new book appear at the end of the list. Pretty cool, right? Go ahead and add a couple more books to your list.

What if you wanted to take out some of the books? We can use `pop()` to remove the last item, or "pop" it off, from our list.

```pycon
library = ["Orlando", "Confessions of the Fox", "These Waves of Girls", "La Frontera", "Dawn"]
library.pop()
print(library)
```

The last item that you added to your list should be missing from the `library` when you print the list.

## Challenge

Remember the `input()` function from the last lesson? This challenge uses that function in combination with what you know about list methods to create a little library app. You will play around with the input button, asking the user what kinds of things they want to do with their library, and writing some code that does those things and prints out the results.

First, create a new file called `library.py`. Save it to your current working folder.

Second, create a list of `library` books, with at least three books (you can use the same ones as before).

```python
library = ["Orlando", "Confessions of the Fox", "These Waves of Girls"]
```

Then, add an input statement that will save the user's response to a variable, like `response`.

```python
response = input("What do you want to do with your books today? ")
```

Now, create a conditional statement that matches the user's response to series of options for doing things to the `library` list. You can include `sort()`, `append()`, and `pop()`. I'll do the first one, `sort()`, for you:

```python
library = ["Orlando", "Confessions of the Fox", "These Waves of Girls"]
response = input("What do you want to do with your books today? ")
if response == "sort":
    library.sort()
    print(library)
else:
    print("I don't know what you want me to do!")
```

See how the order of statements build on each other toward the final product? First, we create a library of books. Then, we set the user's response about what to do with those books. Then, we create a conditional statement that matches the response to specific tasks. The first condition checks to see if the user wants to "sort" the books, then sorts them, then prints the final result.

After adding a few more conditions, test out your code! You should have a little library app that sorts, adds, and removes books from your list.

## Solution

```python
library = ["Orlando", "Confessions of the Fox", "These Waves of Girls"]
response = input("What do you want to do with your books today? ")
if response == "sort":
    library.sort()
    print(library)
elif response == "add":
    library.append("La Frontera")
    print(library)
elif response == "remove":
    library.pop()
    print(library)
else:
    print("I don't know what you want me to do!")
```
## Evaluation

Select the following statements that truly describe `sort()`, `append()`, and `pop()`.
- methods are like functions which are attached to objects.*
- `sort()`, `append()`, and `pop()` are functions.
- `append()` always takes an argument.*
- `pop()` can be applied to a string.

Advanced question: If you `sort()` the library in between adding and popping a book, you'll end up with a different list than if you didn't run sort() in between `append()` and `pop()`. Can you guess why?

## Keywords

Do you remember the glossary terms from this section?

- [append](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/append.md)
- [sort()](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/sort.md)
- [pop()](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/pop.md)

---

← [Input](9-input.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Finding Answers with Google](11-finding-answers-with-google.md) →