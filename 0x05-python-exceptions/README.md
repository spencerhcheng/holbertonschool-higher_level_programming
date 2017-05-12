# 0x05. Python - Exceptions

### GOALS
Learn about error handling and exceptions; including understanding the difference between them, how to use exceptions, when we need to use them, what is the purpose of catching exceptions, how to raise a builtin exception and when we need to implement a clean-up action after an exception.

#### 0. Safe list printing
A function that prints x elements of a list. my_list can contain any type (integer, string, etc.) All elements are printed ont eh same line followe by a new line. x represents the number of elements to print and can be larger than the length of my_list. Returns the number of elements printed

Prototype: `def safe_print_list(my_list=[], x=0):`

#### 1. Safe printing of an integer list
A function that prints an integer with `"{:d}".format()`. Value can be of any type (integer, string, etc.) The function returns `True` if `value` is correctly printed (`value` is of type `int`).

Prototype: `def safe_print_integer(value):`

#### 2. Print and count integers
A function that prints the first `x` elements of a list and only integers. `my_list` can contain any type (integer, string, etc.). `x` represents the number of elements to access in `my_list` and can be larger than the length of `my_list`. Function returns the number of integers printed.

Prototype: `def safe_print_list_integers(my_list=[], x=0):`

#### 3. Integers division with debuf
A function that divides 2 integers and prints the result. We assume that `a` and `b` are integers. The result of the divisiion is printed in the `finally:` section preceded by `Inside result:`. Function returns the value of the vidision, or `None` otherwise.

Prototype: `def safe_print_division(a, b):`

#### 4. Divide a list
A function that divides element by 2 element lists. Both `my_list_1` and `my_list_2` can contain any type (integer, string, etc.). `list_length can be bigger than the length of both lists. If the two elements cannot be divided, the division result should equate to `0`. Returns a new list with all division values.

Prototype: `def list_division(my_list_1, my_list_2, list_length):`

#### 5. Raise exception
A function that raises a type exception.

Prototype: `def raise_exception():`

#### 6. Raise a message
A functiont hat raises a name exception with a message.

Prototype: `def raise_exception_msg(message=""):`
