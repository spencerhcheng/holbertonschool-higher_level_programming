## 0x03. Python - Data Structures: Lists, Tuples

### Goals

Through the completion of this project, I hope to better understand how to use lists in Python, the differences and similarities between strings and lists, common methods of lists and how to use them, how to use lists as stacks and queues, list comprehension, tuples, when to use tuples vs lists, sequences, tuple packing, and sequence unpacking.

### Requirements

* [] Files will be compiled using Ubuntu 14.04 LTS using pythong3 (version 3.4.3)
* [] First line of files read #!/usr/bin/python3
* [] Code formatted using PEP 8 style

#### 0. Printing a list of integers
A function that prints all integers of a list in the format of one integer per line without importing any module. I assume that the list only contains integers.

Prototype: `def print_list_integer(my_list=[]):`

#### 1. Secure access to an element in a list
A function that retrieves an element from a list. If the idx is out of range, the function returns `None`.

Prototype: `def element_at(my_list, idx):`

#### 2. Replace element
A function that replaces an element of a list at a specific position. If the idx is out of range, the function should not modify anything, and will return the original list.

Prototype: `def replace_in_list(my_list, idx, element):`

#### 3. Print a list of integers...in reverse!
A function that prints all integers of a list, in reverse order in the format of one integer per line. I assume the list only contains integers.

Prototype: `def print_reversed_list_integer(my_lis[]):`

#### 4. Replace in a copy
A function that replaces an element in a list at a specific position without modifying the original list. If the index is out of range, the function should return a copy of the original list.

Prototype: `def new_in_list(my_list, idx, element):`

#### 5. Can you C me now?
A function that removes all characters `c` and `C` from a string. The function returns the new string.

Prototype: `def no_c(my_string);`

#### 6. List of lists = Matrix
A function that prints a matrix of integers. Assume the list contains only integers.

Prototype: `def print_matrix_integer(matrix=[[]]):`

#### 7. Tuples addition
Function that adds 2 tuples and returns a tuble with 2 integers: the first element is the first element of each argument and the second element is the addition of the second element of each argument.

#### 8. More returns!
A function that returns a tuple with the length of a string and its first character. If the sentence is empty, the first character should be equal to `None`.

Prototype: `def multiple_returns(sentence):`

#### 9. Find the max
A function that finds the biggest integer of a list. If the list is emtpy, return `None`. I assume the list only contains integers.

Prototype: `def max_integer(my_list=[]):`

#### 10. Only by 2
A function that finds all multiples of 2 in a list. The function returns a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2.

Prototype: `def divisible_by_2(my_list=[]):`

#### 11. Delete at
A function that deletes the item at a specific position in a list without using pop().

Prototype: `def delete_at(my_list=[], idx=0):`

#### 12. Switch
Function that switches the value of `a` and `b`.

### AUTHOR

Twitter: @spencerhcheng

LinkedIn: https://www.linkedin.com/in/spencer-cheng-284b4b55

Github: @spencerhcheng
