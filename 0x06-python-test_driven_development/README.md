## 0x06. Python - Test-driven development

### GOALS
Learn how to run interactive tests, understand the importance of testing, how to write docstrings to create tests, how to write documentation for each module and function, what are the basic option flags to create tests and how to find edge cases.

### REQUIREMENTS
Files are interpreted and compiled with `Ubuntu 14.04 LTS` using `Python 3.4.3`

Code follows `PEP 8` style protocols

#### 0. Integers addition
A function that adds 2 integers together. a and b must be either integers or floats. Otherwise, a TypeError exception with the message `a must be an integer` or `b must be an integer` will print out to standard output. `a` and `b` must first be casted to integers if they are a float. The function will return an integer (the sum of `a` and `b`)

Prototype: `def add_integer(a, b):`

#### 1. Divide a matrix
A function that divides all elements of a matrix. The matrix is a list of `ints` or `floats`; otherwise a `TypeError` exception is raised with the message `matrix must be a matrix (list of lists) of integers/floats`. Each row of the `matrix` must be the same size, otherwise a `TypeError` is raised with the message: `Each row of the matrix must have the same size`. `div` must be a number (integer or float), otherwise a `TypeError` exception is raised with the message `div must be a number`. `div` can't be equal to `0`, otherwise an exception error `ZeroDivisionError` is raised with the message `division by zero`. All elements of the matrix should be divided by `div` rounded to 2 decimal places. The function resturns a new matrix.

Prototype: `def matrix_divided(matrix, div):`

#### 2. Say my name
A function that prints `"My name is "`. `first_name` and `last_name` must be strings, otherwise a `TypeError` is raised with the message `first_name must be a string` or `last_name must be a string`.

Prototype: `def say_my_name(first_name, last_name=""):`

#### 3. Print square
A function that prints a square with the character `#`. `size` is the size length of the square. `size` must be an integer, otherwise a `TypeError` is raised with the message `size must be an integer`. If `size` is less than `0`, a `ValueError`exception with the message `size must be >= 0` is preinted to output. If `size` is a float and is less than `0`, a `TypeError` is raised with the message `size must be an integer`.

Prototype: `def print_square(size):`

#### 4. Text indentation
A function that prints text with 2 new lines after the following characters: `.`, `?` and `:`. `text` must be a string, otherwise a `TypeError` exception is raised with the message `text must be a string`. There are no spaces at the beginning or end of each printed line.

Prototype: `def text_indentation(text):`

#### 5. Max integer - Unittest
Unittests for the function prototype: `def max_integer(list=[]):`. Test file should be inside a folder `tests`. This test uses the `unnittest module` and is executed by the command: `python3 - m unittest tests.6-max_integer-test`


