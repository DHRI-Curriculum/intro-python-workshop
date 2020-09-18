← [A Little Motivation](12-a-little-motivation.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Start](../README.md) ↺

---

# 13. Objects in Python

Objects in Python (and other programming languages) are basically containers that can hold data and/or functions inside them. When a function is inside an object, we usually call the function a "method." When data is inside an object, we usually call it an "attribute." The terminology isn't that important, though. What we do need to know is that you can access these "methods" and "attributes" with a `.` (a dot or period).

When we added `sort()`, `append()`, `pop()`, and `lower()` to our library app, we briefly saw how some methods contained inside certain objects in Python, like Lists (for sort, append, and pop), and String objects, like lower.

```pycon
>>> loud_greeting = "HELLO!"

>>> loud_greeting.lower()
'hello!'
```

Many, or most, objects in Python have methods that allow you to use them in different ways. As you move into using more advanced Python, you'll find that understanding what methods are available becomes more important.

## Examining Objects

When you encounter an object, how can you learn its methods and atributes so you can use them? There are two main ways. The first, and likely the most practical, is to read the documentation of the library you're using.

However, you can also use the `dir()` function, which will tell you which methods and attributes are available in an object.

Let's use the REPL for a moment—open it by typing `python` at the command line.

```pycon
>>> s = 'Hello, world!'

>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
...
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

The above output shows some of the methods and attributes for Python strings that can be accessed using the dot (`.`) syntax. Also, be aware that Python doesn't print all the possible methods and attributes, just what it considers to be most important. Also, when using `dir()`, you'll mostly want to ignore the methods and attributes that have underscores around them. They mainly have to do with the internals of the Python language. For now, ignore the information within underscores (like `__add__`) and focus on the stuff surrouned by single quotes (like `startswith`).

You can also use `dir()` to see what functions are available from Python libraries that you import. Try importing the `random` library again and see what you get when you enter `dir(random)`.

```pycon
>>> import random

>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```

Try entering other objects based on Python types we've already learned to the `dir()` function. For example, you might try `dir([1, 2, 3])` to see what methods are available when using lists.

## Challenge

*Advanced Final Challenge*:

Let's try out a library for web scraping, called `requests`. It allows you to send queries over web browsers (which we call HTTP requests) in order to grab data from websites. It is a foundational module for web scraping tasks. While `requests` is relatively easy to grasp at first, it has a bit of a learning curve. With some practice, though, it can yield sophisticated web scraping results.

For this challenge, let's get some hands-on practice using `requests`, to scrape the surface of what it can do. Feel free to attempt as much of this challenge as you are comfortable with.

First, import requests into your REPL:

```pycon
>>> import requests
```

Then, let's set up a request _object_. Basically, we will declare a variable `r` to represent the content from a website that we want to scrape. After the equal sign `=`, we call the `requests` module, and within that module, a method called `get`, which includes the parameter of the website URL, enclosed in single quotes. Like so:

```pycon
>>> import requests

>>> r = requests.get('https://www.nytimes.com')
```

Now, let's examine that request object. Use the `dir` function to see what methods and attributes are available to `r`. Focus on the items within single quotes, rather than the underscores. Look up any of the items that seem interesting but unclear to you. Try to find out what at least one of these methods does, such as `encoding`. Can you try out some of these methods in the REPL? This would involve adding the dot operator `.` to your variable `r`, followed by the method.

Even if you don't understand the results—that's okay! This is an advanced challenge, meant to expose you to the beginning of your exploration with this module. This is only the first step to running more robust web scraping experiments.

## Solution

First, checking out what methods are available to the `r` object:

```pycon
>>> dir(r)
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
```

Then, trying out some of the methods:

```pycon
>>> r.status_code
200

>>> r.encoding
'utf-8'

>>> r.cookies
<RequestsCookieJar[Cookie(version=0, name='nyt-a', value='04u7q0SFZ2OpnpLqevHY65', port=None, port_specified=False, domain='.nytimes.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=1627494229, discard=False, comment=None, comment_url=None, rest={'SameSite': 'none'}, rfc2109=False), Cookie(version=0, name='nyt-gdpr', value='1', port=None, port_specified=False, domain='.nytimes.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1595979829, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='nyt-geo', value='PT', port=None, port_specified=False, domain='.nytimes.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1595979829, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='nyt-purr', value='cfhspnahhu', port=None, port_specified=False, domain='.nytimes.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=1627494229, discard=False, comment=None, comment_url=None, rest={'SameSite: Lax': None}, rfc2109=False)]>

```

What do these methods do? For the `r.status_code`, the `200` return value means that the request was successful, because 200 is the HTTP code for a successful request. This is opposed to 400 codes, like 404 error, which indicates a failure to reach the website.

The most useful method, however, is likely `text`:

```pycon
>>> r.text
...
```

`text` allows you to access the text content of the site you have requested, which is extremely useful when you want to scrape websites for information, for instance.

This is just the tip of the iceberg for using `requests`. In order to get more information, you'll have to read up on the module. Here is [an excellent tutorial](https://scotch.io/tutorials/getting-started-with-python-requests-get-requests) to get started.

## Evaluation

Why would someone use `dir()`? Select all that apply:
- to examine a function like `print()`.*
- to see what can be done with an object, like a string or a list.*
- to see what can be done with a variable that's been assigned to a value.*
- to examine a particular method, like `sort()`.

## Keywords

Do you remember the glossary terms from this section?

- [Modules](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/module.md)
- [requests](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/requests.md)
- [Objects](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/object.md)
- [dir()](https://github.com/DHRI-Curriculum/glossary/blob/v2.0/terms/dir.md)

---

← [A Little Motivation](12-a-little-motivation.md)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Start](../README.md) ↺