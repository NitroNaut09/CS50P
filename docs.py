# Hello! This is start of a new journey of me learning Python. I will be using this file to practice Python.
'''This can also act as my own reference guide for Python. A shortened version of Python documentation.'''

# The first thing I will be looking at is the print() function.
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)


print("hello, \"world\"")  # This will tell the interpreter to skip the characters *after* the backslash.
print(f"Hello! {world}")  # This is an f-string. It allows you to embed expressions inside string literals, using curly braces {}.

# String Methods are functions that are called on a string object. They are used to manipulate strings.
# Common string methods in Python 3.11 with examples


# capitalize() - Capitalizes the first character of the string
example = "hello world"
print(example.capitalize())  # Output: "Hello world"

# upper() - Converts all characters in the string to uppercase
example = "hello world"
print(example.upper())  # Output: "HELLO WORLD"

# lower() - Converts all characters in the string to lowercase
example = "HELLO WORLD"
print(example.lower())  # Output: "hello world"

# strip() - Removes leading and trailing whitespace
example = "   hello world   "
print(example.strip())  # Output: "hello world"

# replace() - Replaces a substring with another substring
example = "hello world"
print(example.replace("world", "Python"))  # Output: "hello Python"

# split() - Splits the string into a list of substrings based on a delimiter
example = "hello world"
print(example.split())  # Output: ["hello", "world"]

# join() - Joins a list of strings into a single string with a specified delimiter
example = ["hello", "world"]
print(" ".join(example))  # Output: "hello world"

# find() - Returns the index of the first occurrence of a substring, or -1 if not found
example = "hello world"
print(example.find("world"))  # Output: 6

# count() - Returns the number of occurrences of a substring
example = "hello world"
print(example.count("o"))  # Output: 2

# startswith() - Checks if the string starts with a specified substring
example = "hello world"
print(example.startswith("hello"))  # Output: True

# endswith() - Checks if the string ends with a specified substring
example = "hello world"
print(example.endswith("world"))  # Output: True

#title() - Converts the first character of each word to uppercase
example = "hello world"
print(example.title())  # Output: "Hello World"

# isalpha() - Checks if all characters in the string are alphabetic
example = "hello"
print(example.isalpha())  # Output: True

# isdigit() - Checks if all characters in the string are digits
example = "123"
print(example.isdigit())  # Output: True

# isalnum() - Checks if all characters in the string are alphanumeric
example = "hello123"
print(example.isalnum())  # Output: True

# isspace() - Checks if all characters in the string are whitespace
example = "   "
print(example.isspace())  # Output: True

# format() - Formats the string using placeholders
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Output: "My name
# is Alice and I am 30 years old."

# f-string - Formats the string using f-strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: "My name is
# Alice and I am 30 years old."

# l strip() - Removes leading whitespace
example = "   hello world   "
print(example.lstrip())  # Output: "hello world   "

# rstrip() - Removes trailing whitespace
example = "   hello world   "
print(example.rstrip())  # Output: "   hello world"

# center() - Centers the string within a specified width
example = "hello"
print(example.center(10))  # Output: "  hello   "

# zfill() - Pads the string with zeros to a specified width
example = "42"
print(example.zfill(5))  # Output: "00042"

# encode() - Encodes the string using the specified encoding
example = "hello"
print(example.encode("utf-8"))  # Output: b'hello'

