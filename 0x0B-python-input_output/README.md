# 0x0B. Python - Input/Output

### OBJECTIVE
To understand the following:
* [] - How to open a file
* [] - How to write text in a file
* [] - How to read the full content of a file
* [] - How to read a file line by line
* [] - How to move the cursor in a file
* [] - How to make sure a file is closed after using it
* [] - What is and how to use the `with` statement
* [] - What is `JSON`
* [] - What is serialization and deserialization
* [] - How to convert a Python data structure to a `JSON` string
* [] - How to convert a `JSON` string to a Python data structure

##### GitHub repository: `holbertonschool-higher_level_programming`
##### Directory: `0x0B-python-input_output`

### FILE SETUP
All files are interpreted and compiled on Ubuntu 14.04 LTS using Python3 (version 3.4.3). Files are written in accordance to the PEP 8 style guidelines and include #!/usr/bin/python3 scripting line.

#### 0. Read file
Function that reads a text file (`UTF-8`) and prints it to stdout. The `with` statement is used. 

File name: `0-read_file.py`
Main file: `0-main.py`
Prototype: `def read_file(filename=""):`

#### 1. Number of lines
Function that returns the number of of a text file.

File name: `1-number_of_lines.py`
Main file: `1-main.py`
Prototype: `def number_of_lines(filename=""):`

#### 2. Read `n` lines
Function that reads `n` lines of a text (`UTF-8`) file and prints it to std out. It reads the entire file if `nb_lines` is lower or equal to `0` -or- greater or equal to the number of total number of lines of the file.

File name: `2-read_lines.py`
Main file: `2-main.py`
Prototype: `def read_lines(filename="", nb_lines=0):`

#### 3. Write to a file
Function that writes a string to a text file (`UTF-8`) and returns the number of characters written.

File name: `3-write-file.py`.
Main file: `3-main.py`
Prototype: `def write_file(filename="", text=""):`

#### 4. Append to a file
Function that appends a string at the end of a text file (`UTF-8`) and returns the number of characters added.

File name: `4-append_write.py`
Main file: `4-main.py`
Prototype: `def append_write(filename="", text=""):`

#### 5. To `JSON` string
Function that returns the `JSON` representation of an object(string).

File name: `5-to_json_string.py`
Main file: `5-main.py`
Prototype: `def to_json_string(my_obj):`

#### 6. From `JSON` string to Object
Function that returns an object(Python data structure) represented by a `JSON` string.

File name: `6-from_json_string.py`
Main file: `6-main.py`
Prototype: `def from_json_string(my_str):`

#### 7. Save Object to a file
Function that writes an Object to a text file, using a `JSON` representation.

File name: 7-save_to_json_file.py
Main file: 7-main.py
Prototype: `def save_to_json_file(my_obj, filename):`

#### 8. Create object from a `JSON` file
Function that creates an Object from `JSON` file.

File name: 8-load_from_json file.py`
Main file: 8-main.py
Prototype: `def load_from_json_file(filename):`

#### 9. Load, add, save
Function that adds all arguments to a Python list, and then saves them to a file. Uses function `save_to_json_file` from `7-save_to_json_file.py`. Loads function `load_from_json_file` from `8-load_from_json_file.py`. Files saved in `add_item.json`.

File name: `9-add_item.py`
Main file: 9-main.py

#### 10. Class to `JSON`
Function that returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object.

File name: `10-class_to_json.py`
Main file: 10-main.py
Prototype: `def class_to_json(obj):`

#### 11. Student to JSON
A class `Student` that defines a student by:
* [] - `first_name`
* [] - `last_name`
* [] - `age`

Instantiation with `first_name`, `last_name` and `age: def __init__(self, first_name, last_name, age):`. The public method `def to_json(self):` retrieves a dictionary representation of a `Student` instance.

File name: `11-student.py`
Main file: 11-main.py

#### 12. Student to JSON with filter
A class `Student` that defines a student by:
* [] - `first_name`
* [] - `last_name`
* [] - `age`

Instantiation with `first_name`, `last_name` and `age: def __init__(self, first_name, last_name, age):`. The public method `def to_json(self):` retrieves a dictionary representation of a `Student` instance.

Public method `def to__json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance.
* [] - If `attrs` is a list of strings, only the attributes name contained in the list must be retrieved. Otherwise, all attributes must be retrieved.

File name: `12-student.py`
Main file: 12-main.py

#### 13. Student to disk and reload
A class `Student` that defines a student by:
* [] - `first_name`
* [] - `last_name`
* [] - `age`

Instantiation with `first_name`, `last_name` and `age: def __init__(self, first_name, last_name, age):`. The public method `def to_json(self):` retrieves a dictionary representation of a `Student` instance.

Public method `def to__json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance.
* [] - If `attrs` is a list of strings, only the attributes name contained in the list must be retrieved. Otherwise, all attributes must be retrieved.

Public method `def reload_from_json(self, json):` that replaces all attributs of the `Student` instance.
* [] - It is assumed that `json` will always be a dictionary
* [] - A dictionary key will be a public attribute name
* [] - A dictionary value will be the value of the public attribute

File name: `13-student.py`
Main file: 13-main.py
