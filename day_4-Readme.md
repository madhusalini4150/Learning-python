#  Python Strings

## 🔹 What is a String?
A string is a sequence of characters enclosed in:
- Single quotes (' ')
- Double quotes (" ")
- Triple quotes (''' ''')

Strings are used to store text data in Python.

Example:
name = "Python"
city = 'Hyderabad'

---

## 🔹 Uses of Strings
Strings are used for:
- Storing names and messages
- Taking user input
- Displaying output
- Text processing
- Data validation (email, password)
- Working with files

Strings make programs interactive and readable.

---

## 🔹 String Indexing
Each character in a string has a position called an index.

### Positive Indexing
- Starts from 0
- Left to right

Example:
text = "Python"
text[0] → P
text[2] → t

Index positions:
P  y  t  h  o  n
0  1  2  3  4  5

---

### Negative Indexing
- Starts from -1
- Right to left

Example:
text = "Python"
text[-1] → n
text[-3] → h

Negative index positions:
P   y   t   h   o   n
-6 -5  -4  -3  -2  -1

---

## 🔹 Accessing Characters
Characters can be accessed using index numbers.

Example:
word = "Computer"
word[1] → o
word[-2] → e

---

## 🔹 Important Points
- Strings are immutable
- Indexing helps access characters
- Invalid index causes IndexError

---
# Python String Concatenation

## 🔹 What is String Concatenation?
String concatenation means **joining two or more strings** into a single string.

In Python, string concatenation is mainly done using the **`+` operator**.

---

## 🔹 Using + Operator
The `+` operator joins strings together.

Example:
a = "Hello"
b = "World"
result = a + b
print(result)

Output:
HelloWorld

---

## 🔹 Adding Space While Concatenation
Spaces are not added automatically.  
You must add them manually.

Example:
a = "Hello"
b = "World"
result = a + " " + b
print(result)

Output:
Hello World

---

## 🔹 Concatenating Multiple Strings
You can join more than two strings.

Example:
first = "Python"
second = "is"
third = "easy"

result = first + " " + second + " " + third
print(result)

Output:
Python is easy

---

## 🔹 Concatenating String with Numbers
Strings cannot be directly concatenated with numbers.  
Numbers must be converted to strings using `str()`.

Example:
age = 20
text = "My age is " + str(age)
print(text)

Output:
My age is 20

---

## 🔹 Using += Operator
The `+=` operator is used to append a string to another string.

Example:
msg = "Hello"
msg += " Python"
print(msg)

Output:
Hello Python

---

## 🔹 Important Points
- Only strings can be concatenated with strings
- Use `str()` to convert numbers
- `+` is the most common concatenation operator
- Concatenation creates a new string

---
# Python Escape Characters

## 🔹 What are Escape Characters?
Escape characters are special characters used in strings to represent
characters that are difficult or impossible to type directly.

Escape characters start with a **backslash (`\`)**.

---

## 🔹 Common Escape Characters

\n  → New line  
\t  → Tab space  
\'  → Single quote  
\"  → Double quote  
\\  → Backslash  

---

## 🔹 New Line (\n)
Moves the cursor to the next line.

Example:
print("Hello\nWorld")

Output:
Hello
World

---

## 🔹 Tab Space (\t)
Adds horizontal space like a tab.

Example:
print("Python\tProgramming")

Output:
Python    Programming

---

## 🔹 Single Quote (\')
Used to include a single quote inside a string.

Example:
print('It\'s a good day')

Output:
It's a good day

---

## 🔹 Double Quote (\")
Used to include double quotes inside a string.

Example:
print("He said \"Hello\"")

Output:
He said "Hello"

---

## 🔹 Backslash (\\)
Used to print a backslash.

Example:
print("C:\\Users\\Admin")

Output:
C:\Users\Admin

---

## 🔹 Important Points
- Escape characters begin with backslash (\)
- Used inside string literals
- Helpful for formatting output
- Avoid syntax errors in strings

---
#  Python String Formatting

## 🔹 What is String Formatting?
String formatting is used to **insert variables or values into a string**.

It helps create readable and dynamic output.

---

## 🔹 Using + Operator
Strings can be combined using the `+` operator.
Values must be converted to strings.

Example:
name = "Python"
version = 3
print("Language: " + name + " Version: " + str(version))

---

## 🔹 Using format() Method
The `format()` method replaces `{}` with values.

Example:
name = "Python"
level = "Easy"
print("Language: {} Level: {}".format(name, level))

---

## 🔹 Using Index in format()
Values can be placed using index numbers.

Example:
print("{0} is {1}".format("Python", "powerful"))

---

## 🔹 Using Named Placeholders
You can use variable names inside `{}`.

Example:
print("{lang} is {type}".format(lang="Python", type="simple"))

---

## 🔹 Using f-Strings
f-strings are the easiest and most modern way to format strings.

Example:
lang = "Python"
year = 2025
print(f"{lang} is popular in {year}")

---

## 🔹 Formatting Numbers
You can control number formatting.

Example:
pi = 3.14159
print("Value of pi: {:.2f}".format(pi))

---

## 🔹 Important Points
- String formatting improves readability
- f-strings are faster and cleaner
- `format()` works in all Python versions
- Avoid using `+` for complex formatting

---
#  Python String Methods

## 🔹 What are String Methods?
String methods are **built-in functions** used to perform operations on strings.

They help in modifying, searching, and formatting strings easily.

---

## 🔹 lower()
Converts all characters to lowercase.

Example:
text = "PYTHON"
print(text.lower())

Output:
python

---

## 🔹 upper()
Converts all characters to uppercase.

Example:
text = "python"
print(text.upper())

Output:
PYTHON

---

## 🔹 title()
Converts the first character of each word to uppercase.

Example:
text = "python is easy"
print(text.title())

Output:
Python Is Easy

---

## 🔹 capitalize()
Converts the first character of the string to uppercase.

Example:
text = "python"
print(text.capitalize())

Output:
Python

---

## 🔹 strip()
Removes spaces from both ends of the string.

Example:
text = "  hello  "
print(text.strip())

Output:
hello

---

## 🔹 lstrip()
Removes spaces from the left side.

Example:
text = "  hello"
print(text.lstrip())

---

## 🔹 rstrip()
Removes spaces from the right side.

Example:
text = "hello  "
print(text.rstrip())

---

## 🔹 replace()
Replaces one substring with another.

Example:
text = "I like Java"
print(text.replace("Java", "Python"))

Output:
I like Python

---

## 🔹 split()
Splits a string into a list.

Example:
text = "Python is easy"
print(text.split())

Output:
['Python', 'is', 'easy']

---

## 🔹 join()
Joins elements of a list into a string.

Example:
words = ["Learn", "Python", "Now"]
print(" ".join(words))

Output:
Learn Python Now

---

## 🔹 find()
Returns the index of first occurrence of a substring.

Example:
text = "Python"
print(text.find("t"))

Output:
2

---

## 🔹 count()
Counts occurrences of a substring.

Example:
text = "banana"
print(text.count("a"))

Output:
3

---

## 🔹 startswith()
Checks if string starts with a value.

Example:
text = "Python"
print(text.startswith("Py"))

Output:
True

---

## 🔹 endswith()
Checks if string ends with a value.

Example:
text = "Python"
print(text.endswith("on"))

Output:
True

---

## 🔹 Important Points
- String methods do not change the original string
- Strings are immutable
- Methods return new strings

---
# Python String Slicing

## 🔹 What is String Slicing?
String slicing is used to **extract a part of a string** using index ranges.

Syntax:
string[start : end : step]

---

## 🔹 Basic Slicing
Extracts characters from start index to end index (end not included).

Example:
text = "Python"
print(text[1:4])

Output:
yth

---

## 🔹 Slicing from Start
If start index is omitted, slicing starts from index 0.

Example:
text = "Python"
print(text[:3])

Output:
Pyt

---

## 🔹 Slicing till End
If end index is omitted, slicing goes till the last character.

Example:
text = "Python"
print(text[2:])

Output:
thon

---

## 🔹 Negative Index Slicing
Negative indexes count from the right.

Example:
text = "Python"
print(text[-5:-2])

Output:
yth

---

## 🔹 Step Value
Step defines the gap between characters.

Example:
text = "Computer"
print(text[::2])

Output:
Cmue

---

## 🔹 Reverse a String
Use step as -1 to reverse a string.

Example:
text = "Python"
print(text[::-1])

Output:
nohtyP

---

## 🔹 Slicing with Start, End and Step
All three values can be used together.

Example:
text = "Programming"
print(text[1:10:2])

Output:
rgaig

---

## 🔹 Important Points
- End index is not included
- Slicing does not modify the original string
- Works with positive and negative indexes

---








