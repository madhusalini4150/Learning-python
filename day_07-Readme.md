#  Python List Methods

Python lists are used to store multiple items in a single variable.  
Python provides built-in **list methods** to add, remove, search, and modify list elements.

---

## append()

Adds an element at the end of the list.

Syntax:
list.append(item)

Example:
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)

Output:
['apple', 'banana', 'mango']

---

## clear()

Removes all the elements from the list.

Syntax:
list.clear()

Example:
numbers = [1, 2, 3]
numbers.clear()
print(numbers)

Output:
[]

---

## copy()

Returns a copy of the list.

Syntax:
new_list = list.copy()

Example:
a = [1, 2, 3]
b = a.copy()
print(b)

Output:
[1, 2, 3]

---

## count()

Returns the number of elements with the specified value.

Syntax:
list.count(value)

Example:
nums = [1, 2, 2, 3, 2]
print(nums.count(2))

Output:
3

---

## extend()

Adds the elements of another list (or iterable) to the end of the current list.

Syntax:
list.extend(iterable)

Example:
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1)

Output:
[1, 2, 3, 4]

---

## index()

Returns the index of the first element with the specified value.

Syntax:
list.index(value)

Example:
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana"))

Output:
1

---

## insert()

Adds an element at the specified position.

Syntax:
list.insert(index, item)

Example:
numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)

Output:
[1, 2, 3, 4]

---

## pop()

Removes the element at the specified position and returns it.  
If no index is specified, it removes the last element.

Syntax:
list.pop(index)

Example:
nums = [1, 2, 3]
nums.pop()
print(nums)

Output:
[1, 2]

---

## remove()

Removes the item with the specified value.

Syntax:
list.remove(value)

Example:
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)

Output:
[1, 3, 2]

---

## reverse()

Reverses the order of the list.

Syntax:
list.reverse()

Example:
nums = [1, 2, 3]
nums.reverse()
print(nums)

Output:
[3, 2, 1]

---

## sort()

Sorts the list in ascending order by default.

Syntax:
list.sort()

Example:
nums = [3, 1, 2]
nums.sort()
print(nums)

Output:
[1, 2, 3]

---

## Note

• All list methods modify the original list (except copy())  
• `del` is a keyword, not a list method  

---

