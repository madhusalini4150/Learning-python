Python Lists
In Python, a list is a built-in data structure that can hold an ordered collection of items. Unlike arrays in some languages, Python lists are very flexible:
>Can contain duplicate items
>Mutable: items can be modified, replaced, or removed
>Ordered: maintains the order in which items are added
>Index-based: items are accessed using their position (starting from 0)
>Can store mixed data types (integers, strings, booleans, even other lists)
 List--
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)
Creating a List--
Lists can be created in several ways, such as using square brackets, the list() constructor or by repeating elements. Let's look at each method one by one with example:
1. Using Square Brackets-
We use square brackets [] to create a list directly.
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types
print(a)
print(b)
print(c)
 
2. Using list() Constructor-
We can also create a list by passing an iterable (like a tuple, string or another list) to the list() function.
a = list((1, 2, 3, 'apple', 4.5))  
print(a)
b = list("GFG")
print(b)

3. Creating List with Repeated Elements--
We can use the multiplication operator * to create a list with repeated items.
a = [2] * 5
b = [0] * 7
print(a)
print(b)

Allow Duplicates--
Since lists are indexed, lists can have items with the same value:

Example
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
List Length--
To determine how many items a list has, use the len() function:

Example
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
Python Collections (Arrays)--
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

Unpacking List Items--
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
 
Slicing Items from a List
Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] 
all_fruits = fruits[0:] 
orange_and_mango = fruits[1:3] 
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] 
 
Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] 
orange_and_mango = fruits[-3:-1] 
orange_mango_lemon = fruits[-3:]]
reverse_fruits = fruits[::-1] 


Modifying Lists--
List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

Check if Item Exists--
To determine if a specified item is present in a list use the in keyword:

Example
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


