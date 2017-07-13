## 0x0A. Python - Inheritance

### OBJECTIVE
The goal of this project is to understand and obtain experience with inheritance in Python. Topics explored include:
* [] - What are superclasses, baseclasses or parentclasses
* [] - What is a subclass
* [] - How to list all attributes and methods of a class or instance
* [] - When can an instance have new attributes
* [] - How to inherit class from another
* [] - How to defind a class with multiple base classes
* [] - What is the default class every class inherits from
* [] - How to override a method or attribute inherited from the base class
* [] - What is the purpose of inheritance
* [] - What are, when and how to use: `isinstance`, `issubclass`, `type` and `super` built-in functions.

##### GitHub repository: `holbertonschool-higher_level_programming`
##### Directory: `0x0A-python-inheritance`

### REQUIREMENTS
All files are interpreted and compiled on Ubuntu 14.04 LTS using Python3 (version 3.4.3). Files are written in accordance to the PEP 8 style guideline.

####. 0. Lookup
A function that returns the list of available attributes and methods of an object. Returns a `list` object.

Prototype: `def lookup(obj):`

#### 1. My list
A class `MyList` that inherits from `list`. All elements of the list are of type `int`.

Prototype: `def print_sorted(self):`

#### 2. Exact same object
A function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

Prototype: `def is_same_class(obj, a_class):`

#### 3. Same class or inherit from
A function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class, otherwise `False`.

Prototype: `def is_kind_of_class(obj, a_class):`

#### 4. Only sub class of
A function that returns `True` if the object is an instance of a class that inherited (either directly or indirectly) from the specified class, otherwise `False`.

Prototype: `def inherits_from(obj, a_class):`

#### 5. Geometry module
An empty class `BaseGeometry`.

#### 6. Improve Geometry
A class `BaseGeometry`. Raises an `Exception` with the message `area() is not implemented`.

Prototype: `def area(self):`

#### 7. Integer validator
A class `BaseGeometry`. Raises an `Exception` with the message `area() is not implemented`. 

Prototype: `def area(self):

The following prototype validates `value`:
* [] - assume `name` is always a string
* [] - if `value` is not an integer: raise a `TypeError` exception with the message `<name> must be an integer`
* [] - if `value` is less than or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`.

Prototype: `def integer_validator(self, name, value):`

#### 8. Rectangle
A class `Rectangle` that inherits from `BaseGeometry (7 - base_geometry.py)`. Instantiationw ith `width` and `height: def __init__(self, width, height):`
* [] - `width` and `height` are private with no getter or setter.
* [] - `width` and `height` are positive integers, validated by `integer_validator`.

#### 9. Full rectangle
A class `Rectangle` that inherits from `BaseGeometry (7 - base_geometry.py)`. Instantiationw ith `width` and `height: def __init__(self, width, height):`
* [] - `width` and `height` are private with no getter or setter.
* [] - `width` and `height` are positive integers, validated by `integer_validator`.
The `area()` method is implemented and `print()` prints and `str()` returns the following rectangle description:
* [] - `[Rectangle] <width>/<height>`

#### 10. Square #1
A class `Square` that inherits from `Rectangle (9-rectangle.py). Instantiationw ith `size: def __init__(self, size):`
* [] - `size` is private. No getter or setter.
* [] - `size` is a positive integer, validated by `integer_validator`.
The `area()` method is implemented in this program.

#### 11. Square #2
A class `Square` that inherits from `Rectangle (9-rectangle.py). Instantiationw ith `size: def __init__(self, size):`
* [] - `size` is private. No getter or setter.
* [] - `size` is a positive integer, validated by `integer_validator`.
The `area()` method is implemented in this program.
`print()` prints, `str()` returns the square description: `[Square]<width>/<height>`
