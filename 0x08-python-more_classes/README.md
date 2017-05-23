## 0x08. PYTHON - More Classes and Objects

### GOALS FOR THIS PROJECT
What is OOP, what is a class, what is an object and an instance, what is the difference between a class and an object or instance, what is an attribute, what are and how to use public, protected and private attributes, what is self, what is a method, what is the special __init__ method and how to use it, what is data abstraction, data encapsulation, and information handling, what is a protperty, what's the difference between an attribute and property, what is the Pythonic way to write getters and setters in Python, what are the special __str__ and __repr__ methods?

### SPECIFICATIONS AND USAGE
This code was written using Vim. Files were interpreted and compiled on Ubuntu 14.04 LTS using python3 and follows the PEP 8 style guidelines.

#### 0. Simple rectangle
An empty class `Rectangle` that defines a rectangle.

#### 1. Real definition of a rectangle.
A class `Rectangle` that defines a rectangle

* [] - Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):

#### 2. Area and Perimeter
A class `Rectangle` that defines a triangle:

* [] - Private instance attribute: width:
* [] - property def width(self): to retrieve it
* [] - property setter def width(self, value): to set it:
* [] - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* [] - Private instance attribute: height:
* [] - property def height(self): to retrieve it
* [] - property setter def height(self, value): to set it:
* [] - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):
* [] - Public instance method: def area(self): that returns the rectangle area
* [] - Public instance method: def perimeter(self): that returns the rectangle perimeter:
* [] - if width or height is equal to 0, perimeter is equal to 0

#### 3. String representation
A class `Rectangle` that defines a rectangle:

* [] - Private instance attribute: width:
* [] - property def width(self): to retrieve it
* [] - property setter def width(self, value): to set it:
* [] - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* [] - Private instance attribute: height:
* [] - property def height(self): to retrieve it
* [] - property setter def height(self, value): to set it:
* [] - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):
* [] - Public instance method: def area(self): that returns the rectangle area
* [] - Public instance method: def perimeter(self): that returns the rectangle perimeter:
* [] - if width or height is equal to 0, perimeter is equal to 0
* [] - if width or height is equal to 0, return an empty string

#### 4. Eval is magic
A class `Rectangle` that defines a rectangle:

* [] - Private instance attribute: width:
* [] - property def width(self): to retrieve it
* [] - property setter def width(self, value): to set it:
* [] - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* [] - Private instance attribute: height:
* [] - property def height(self): to retrieve it
* [] - property setter def height(self, value): to set it:
* [] - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):
* [] - Public instance method: def area(self): that returns the rectangle area
* [] - Public instance method: def perimeter(self): that returns the rectangle perimeter:
* [] - if width or height is equal to 0, perimeter is equal to 0
* [] - if width or height is equal to 0, return an empty string
* [] - repr() returns a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)

#### 5. Detect instance deletion
A class `Rectangle` that defines a rectangle:

* [] - Private instance attribute: width:
* [] - property def width(self): to retrieve it
* [] - property setter def width(self, value): to set it:
* [] - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* [] - Private instance attribute: height:
* [] - property def height(self): to retrieve it
* [] - property setter def height(self, value): to set it:
* [] - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):
* [] - Public instance method: def area(self): that returns the rectangle area
* [] - Public instance method: def perimeter(self): that returns the rectangle perimeter:
* [] - if width or height is equal to 0, perimeter is equal to 0
* [] - if width or height is equal to 0, return an empty string
* [] - repr() returns a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
* [] -  "Bye rectangle..." is printed when an instance of Rectangle is deleted

#### 6. How many instances
A class `Rectangle` that defines a rectangle:

* [] - Private instance attribute: width:
* [] - property def width(self): to retrieve it
* [] - property setter def width(self, value): to set it:
* [] - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* [] - Private instance attribute: height:
* [] - property def height(self): to retrieve it
* [] - property setter def height(self, value): to set it:
* [] - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):
* [] - Public instance method: def area(self): that returns the rectangle area
* [] - Public instance method: def perimeter(self): that returns the rectangle perimeter:
* [] - if width or height is equal to 0, perimeter is equal to 0
* [] - if width or height is equal to 0, return an empty string
* [] - repr() returns a string representation of the rectangle to be able to recreate a new instance by using eval()
* [] -  "Bye rectangle..." is printed when an instance of Rectangle is deleted
* [] - Public class attribute number_of_instances:
* [] - Initialized to 0
* [] - Incremented during each new instance instantiation
* [] - Decremented during each instance deletion

#### 7. Change representation
A class `Rectangle` that defines a rectangle:

* [] - Private instance attribute: width:
* [] - property def width(self): to retrieve it
* [] - property setter def width(self, value): to set it:
* [] - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* [] - Private instance attribute: height:
* [] - property def height(self): to retrieve it
* [] - property setter def height(self, value): to set it:
* [] - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):
* [] - Public instance method: def area(self): that returns the rectangle area
* [] - Public instance method: def perimeter(self): that returns the rectangle perimeter:
* [] - if width or height is equal to 0, perimeter is equal to 0
* [] - if width or height is equal to 0, return an empty string
* [] - repr() returns a string representation of the rectangle to be able to recreate a new instance by using eval() 
* [] -  "Bye rectangle..." is printed when an instance of Rectangle is deleted
* [] - Public class attribute number_of_instances:
* [] - Initialized to 0
* [] - Incremented during each new instance instantiation
* [] - Decremented during each instance deletion
* [] - Public class attribute print_symbol:
	* [] - Initialized to #
	* [] - Used as symbol for string representation
	* [] - Can be any type

#### 8. Compare rectangles
A class `Rectangle` that defines a rectangle:

* [] - Private instance attribute: width:
* [] - property def width(self): to retrieve it
* [] - property setter def width(self, value): to set it:
* [] - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* [] - Private instance attribute: height:
* [] - property def height(self): to retrieve it
* [] - property setter def height(self, value): to set it:
* [] - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):
* [] - Public instance method: def area(self): that returns the rectangle area
* [] - Public instance method: def perimeter(self): that returns the rectangle perimeter:
* [] - if width or height is equal to 0, perimeter is equal to 0
* [] - if width or height is equal to 0, return an empty string
* [] - repr() returns a string representation of the rectangle to be able to recreate a new instance by using eval()
* [] -  "Bye rectangle..." is printed when an instance of Rectangle is deleted
* [] - Public class attribute number_of_instances:
* [] - Initialized to 0
* [] - Incremented during each new instance instantiation
* [] - Decremented during each instance deletion
* [] - Public class attribute print_symbol:
	* [] - Initialized to #
	* [] - Used as symbol for string representation
	* [] - Can be any type
* [] - Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
	* [] - rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
	* [] - rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
	* [] - Returns rect_1 if both have the same area value

#### 9. A square is a rectangle
A class `Rectangle` that defines a rectangle:

* [] - Private instance attribute: width:
* [] - property def width(self): to retrieve it
* [] - property setter def width(self, value): to set it:
* [] - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
* [] - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* [] - Private instance attribute: height:
* [] - property def height(self): to retrieve it
* [] - property setter def height(self, value): to set it:
* [] - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* [] - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* [] - Instantiation with optional width and height: def __init__(self, width=0, height=0):
* [] - Public instance method: def area(self): that returns the rectangle area
* [] - Public instance method: def perimeter(self): that returns the rectangle perimeter:
* [] - if width or height is equal to 0, perimeter is equal to 0
* [] - if width or height is equal to 0, return an empty string
* [] - repr() returns a string representation of the rectangle to be able to recreate a new instance by using eval()
* [] -  "Bye rectangle..." is printed when an instance of Rectangle is deleted
* [] - Public class attribute number_of_instances:
* [] - Initialized to 0
* [] - Incremented during each new instance instantiation
* [] - Decremented during each instance deletion
* [] - Public class attribute print_symbol:
        * [] - Initialized to #
        * [] - Used as symbol for string representation
        * [] - Can be any type
* [] - Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
        * [] - rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
        * [] - rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
        * [] - Returns rect_1 if both have the same area value
* [] - Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size

