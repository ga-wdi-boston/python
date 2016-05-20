[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Python

Hey, Polyglots! Ready for another programming language?

## Prerequisites

-   [ga-wdi-boston/js-basics](https://github.com/ga-wdi-boston/js-basics)
-   [ga-wdi-boston/js-reference-types](https://github.com/ga-wdi-boston/js-reference-types)

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
1.  Open `~/.bashrc` and add the following between Rbenv and Git configs:

  ```bash
  # Pyenv
  export PATH="/root/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  ```

## Outline



## Foreword

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

**Parens** `()` in Python blocks are required as opposed to optional in Ruby.

Similar to Ruby, there is a lack of semicolons in Python. Line breaks in your
code are enough to denote the end of an expression.

However, as you may have noticed from our `fizzbuzz` script, we are introduced
to **colons** `:` throughout our code. Colons always come directly after the parens
in function or loop blocks. Colons are also immediately followed by a new,
indented line (this indentation is purposeful **whitespace**).

Python's parens/colons/whitespace act similarly to Ruby's `end` for method
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

Also similar to Ruby, variables in Python *cannot* be called or stated without
being defined.

```python
>>> z
NameError: name 'z' is not defined
```

### Operators

## Strings

### String interpolation

## Flow Control

### Conditionals

### Loops

## Functions

## Ruby vs JS :: Collections

### Arrays

### Hashes

## Common Gotchas

## Additional Resources

## [License](LICENSE)

Source code distributed under the MIT license. Text and other assets copyright
General Assembly, Inc., all rights reserved.
