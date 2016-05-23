[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Python

Hey, Polyglots! Ready for another programming language?

## Prerequisites

-   [Ruby-vs-JS](https://github.com/ga-wdi-boston/ruby-vs-js)
-   [Ruby-vs-JS-Arrays](https://github.com/ga-wdi-boston/ruby-vs-js-arrays)
-   [Ruby-vs-JS-Hash-Dictionary](https://github.com/ga-wdi-boston/ruby-vs-js-hash-dictionary)

## Objectives

By the end of this, students should be able to:

-   Contrast Python REPL with Ruby REPL.
-   Contrast basic language features and types from Python with basic language
    features and types from Ruby.
-   Write a simple script in Python.

## Preparation

1.  [Fork and clone](https://github.com/ga-wdi-boston/meta/wiki/ForkAndClone)
    this repository.

## Installation

### OS X

1.  `brew install pyenv`
1.  Open `~/.bashrc` and add the following between Rbenv and Git configs:

  ```bash
  # Pyenv
  export PYENV_ROOT=/usr/local/var/pyenv
  eval "$(pyenv init -)"
  ```

1.  `pyenv install 3.5.1`
1.  `pyenv global 3.5.1`
1.  Python doesn't ship with the most up to date version of package manager
pip, so upgrade pip : `pip install -upgrade pip`
1.  `brew install pyenv-virtualenv`
1.  Add the following to `~/.bashrc` under your additions from step 2:

    ```bash
    eval "$(pyenv virtualenv-init -)"
    ```

### Linux

1.  `curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash`
1.  Python doesn't ship with the most up to date version of package manager
pip, so upgrade pip : `pip install -upgrade pip`
1.  Open `~/.bashrc` and add the following between Rbenv and Git configs:

  ```bash
  # Pyenv
  export PATH="/root/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  ```

### Atom Linter

We'll be using [linter-pylint](https://atom.io/packages/linter-pylint).

`apm install linter-pylint`

## Python REPL

We'll be using Python's built-in REPL to practice what we learn today.

Typing `python` onto the command line will bring you into this REPL, similar to
using `pry` or `node`.

To run Python scripts, simply run
`python <filename.rb>` from the command line.

_Hint: to print to the console in Python, we use `print <string to print>`_

Let's practice this. Take a minute to look at [lib/fizzbuzz.rb](lib/fizzbuzz.rb),
then run the `fizzbuzz` script from the command line using
`python lib/fizzbuzz.rb`.

## Core Syntax, Variables, and Operators

### Syntax

Snake case lives on! Aka, `keep_your_variables_defined_this_way`.

**Parens** `()` in Python are required around parameters as opposed to optional
 in Ruby.

Similar to Ruby, there is a lack of semicolons in Python. Line breaks in your
code are enough to denote the end of an expression.

However, as you may have noticed from our `fizzbuzz` script, we are introduced
to **colons** `:` throughout our code. Colons always come directly after the
first line of the block statement. Colons are also immediately followed by a
new, indented line (this indentation is purposeful **whitespace**).

Python's colons/whitespace combo act similarly to Ruby's `end` for method
declarations and loops.

While whitespace in Ruby is essentially ignored, in Python, it is critical to
ensuring working code. Otherwise, you'll run into an `IndentationError`.

### Variable Declaration

Variable declaration in Python is extremely similar to Ruby's. Variables can be
 defined without being previously declared. Variable reassignment is also as
 flexible as Ruby's.

```python
>>> x = 2 # assigns x to numerical value 2
>>> x = "WDI is top tier" # reassigns x to string value
```

Also similar to Ruby, variables in Python _cannot_ be called or stated without
being defined.

```python
>>> z
NameError: name 'z' is not defined
```

### True and False

In Python, true and false are represented by `True` and `False` (yes, case
matters).

The falsy values of Python are:

`False` `None` `0` `0.0` `''` `[]` `{}`

`None` is equivalent to Ruby's `nil`.

### Operators

|                      |        Ruby                          |        Python               |
|:---------------------|:------------------------------------:|:---------------------------:|
| logical operators    | `&&`, <code>&#124;&#124;</code>, `!` | `and`, `or`, `not`          |
| relational operators | `==` `!=` `>` `<` `>=` `<=`          | `==` `!=` `>` `<` `>=` `<=` |
| arithmetic operators | `+`, `-`, `*`, `/` `//`, `%`         | `+`, `-`, `*`, `/`, `%`     |

#### Brief Aside: Double Slash (`//`) Operator

If you remember from Ruby, integer division will always return a whole integer.
For best results, division with Floats returns most accurate results.

In Python, this whole integer division behavior can be mirrored with the `//`
operator.

```python
>>> 14.5 / 3    # => 4.833333
>>> 14.5 // 3   # => 4.0
```

Note that operations on floats will still return floats no matter the operator.

To convert between floats and integers, use:

```python
>>> int(14.5)    # => 14
>>> float(14)    # => 14.0
```

## Lab: Practice Using Operators

Let's get used to these operators.

In your Python REPL from the command line, take some time to practice each
logical, relational and artithmetic operator listed for you above.

## Strings

In Python, there is no difference between using `" "` or `' '`.
[Escape Characters](http://python-reference.readthedocs.io/en/latest/docs/str/escapes.html)
are evaluated in both.

```python
>>> print "This is a \n new line."
# => This is a
# => new line.

>>> print 'This is a \n new line.'
# => This is a
# => new line.
```

### String Interpolation

Like Ruby, there are many options for string interpolation in Python. For our
purposes, we'll be using `.format()`, as it is preferred for Python 3.5.

`.format()` is appended to a string and takes a parameters the strings to be
concatenated. If the string contains empty `{}`s, the parameters fill the `{}`s
in the order passed in. If they contain a number (beginning with 0), they will
be mapped to the parameter passed to `.format()` at said index.

```python

>>> awkward_nerd = "Lauren"
>>> awesome_nerd = "Jason"
>>> occupation = "consultant"

>>> "{} is a pretty cool {}.".format(awkward_nerd, occupation)
# => "Lauren is a pretty cool consultant."

>>> "{0} is a {1}. {2} is a {1} as well.".format(awkward_nerd, occupation, awesome_nerd)
# => "Lauren is a consultant. Jason is a consultant as well."
```

## Flow Control

### Conditionals

Again, colons and whitespace are critical to working Python code. Aside from
that and the use of `elif` vs. `elsif`, these should feel very similar to Ruby
conditional statements.

```python
if x < 0:
  print 'Negative'
elif x == 0:
  print 'Zero'
else:
  print 'Positive'
```

### Loops

Also like Ruby, Python employs `while` and `for` loops.

Python also allows for an optional `else` statement with each of these. With
`while` loops, the `else` statement is executed once the `while` condition is
no longer true. With `for` loops, `else` is executed upon the loop's
completion.

```python
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
```

```python
count = 15
for i in range(1,count):
  print i
else:
  print "done"
```

Again, this `else` is optional and different in nature from a conditional else.
It functions more as a completion handler.

## Functions

Functions in Python are similar to Ruby methods (Python also has methods, but
we only refer to them as such when they are functions of a Class).

Aside from syntactical differences, the main difference to note is the need for
an **explicit return**. Think JavaScript!

Basic function structure:

```python
def function_example(param_one, param_two):
  """Example function returning string interpolation of parameters."""
  concat = "What a splendid function! I've got my {0} and {1}.".format(param_one, param_two)
  return concat
```

#### Brief Aside: Docstrings

You may have noticed something like

`"""This function..."""`

within each of our example functions. These are called `docstrings` and are
conventionally used in Python to provide documentation throughout a codebase.
Code will run fine without them, but that would stray from Python's conventions
as well as throw you into linter message hell. Try them out!

## Lab: Build a Calculator

In [lib/calculator.py](lib/calculator.py), create a calculator function that
takes two parameters. The first should be the operation to be completed
(`addition`, `subtraction`, `multiplication`, `division`). The second should be
a list with the appropriate number of numbers to operate on. The function
mapped to the appropriate operation should take the expected numbers by index
from the list passed in and return back to you the result of the operation.

We haven't discussed lists yet, but they are very similar to Ruby arrays. The
syntax required for this is very similar to how you would approach this in
Ruby. Lean on the knowledge you gained from the [Python vs Ruby study](https://github.com/ga-wdi-boston/python-vs-ruby-study/)!

Remember, to run a Python script from the command line:

`python <filename.py>`

## Collections

### Lists

Python lists are comparable to Ruby arrays. They store comma separated values
of varying data types between square brackets `[]`.

Lists are ordered, thus, indices can be leveraged to get or set their elements.

```python
wdi_base_langs = ["JavaScript", "Ruby", "SQL"]
wdi_base_langs[2] # => "SQL"
wdi_base_langs[0] = "JS" # => ["JS", "Ruby", "SQL"]
```

`len()` is used to get the length of a list in Python.

```python
len(wdi_base_langs) # => 3
```

We can merge lists together using the `+` operator:

```python
wdi_new_langs = ["Python"]
all_wdi_langs = wdi_new_langs + wdi_base_langs # => ["JS", "Ruby", "SQL", "Python"]
```

#### List Methods

We could have gone about adding "Python" to the end of the `wdi_base_langs`
list by using `.append()`.

```python
wdi_base_langs.append("Python") # => ["JS", "Ruby", "SQL", "Python"]
```

Like Ruby, `.pop()` removes the last element from a Python list. `.append()`
will add to the end of a list.

We do not have built-in operators for removing or adding to the beginning of a
list. As hackers, we've got some hacks, though.

`.remove()` allows us to remove an element at any index. Thus, `list.remove(0)`
would remove the first element from a list.

We could implement our array merging to add to the beginning of a list. Look at
the following:

```python
a = "first"
b = ["second", "third"]
[a] + b # => ["first", "second", "third"]
```

#### Looping Through Lists

`for` loops with lists don't stray far from the loops we saw earlier.

```python
all_wdi_langs = ["JS", "Ruby", "SQL", "Python"]

for lang in all_wdi_langs:
  print lang
```

### Dictionaries

Python dictionaries are very similar to other key-value objects we've seen.

Dictionary keys **must** be unique. Creating a key-value pair for a key that
already exists will simply reassign the value of the existing key.

Keys can be either strings or numbers.

There are two ways of instantiating a Python dictionary:

```python
new_dict = dict()   # => {}
# or
new_dict = {}       # => {}

example_dict = {
  "key_one": "val one",
  "key_two": "val two",
  "key_three": "val three"
}
```

To add or retrieve a key-value pair, we implement square bracket notation:

```python
new_dict["fun_key"] = "fresh"
new_dict["fun_key"]    # => "fresh"
```

`.get()` is another option for retrieving a key's value.

```python
new_dict.get("fun_key") # => "fresh"
```

Dictionary defaults are a little different from Ruby. If it is unknown that a
key you are retrieving exists, you can call `.get()` with a default value
should it not exist.

```python
new_dict.get("no_key", "not there") # => "not there"
```

## Lab: Revamp FizzBuzz

In [lib/list_and_dict_buzz.rb](lib/list_and_dict_buzz.rb), build a more robust
FizzBuzz from scratch. Create a dictionary containing keys `fizz`, `buzz`,
`fizzbuzz`, and `other`, each with lists as values. As you iterate through all
the numbers from 1 to max_num, add each number to one of the lists mentioned
above; numbers divisible by 3 only should go into the `fizz` list, numbers
divisible by 5 only should go into the `buzz` list, numbers divisible by both
should go into the `fizzbuzz` list, and numbers divisible by neither should go
into the "other" list. Finally, once you're done, print the resulting
dictionary to check that your code works properly.

## Additional Resources

-   [Python's Documentation](https://docs.python.org/3/)

## [License](LICENSE)

Source code distributed under the MIT license. Text and other assets copyright
General Assembly, Inc., all rights reserved.
