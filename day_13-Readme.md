#  Python Sets 


---

## What is a Set in Python?

A **set** is a built-in Python data type used to store **multiple items** in a single variable.

### Key Characteristics:

* Unordered collection
* Unindexed (no index positions)
* Mutable (can add or remove items)
* Does **not allow duplicate values**

### Example:

```python
my_set = {1, 2, 3, 4}
print(my_set)
```

---

##  Access Set Items

Sets are **unordered**, so you cannot access items using index numbers like lists or tuples.

### How to access elements?

You can:

* Use a **for loop**
* Use the **in** keyword

### Example:

```python
colors = {"red", "green", "blue"}

for color in colors:
    print(color)

print("red" in colors)  # True
```

---

## ➕ Add Set Items

You can add elements to a set using:

### 1️⃣ add() – Add a single item

```python
fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)
```

### 2️⃣ update() – Add multiple items

```python
fruits.update(["mango", "grapes"])
print(fruits)
```

>  Duplicate values are ignored automatically.

---

## ➖ Remove Set Items

Python provides multiple methods to remove elements from a set.

### 1️⃣ remove() – Removes specified element

* Raises an error if element not found

```python
fruits.remove("apple")
```

### 2️⃣ discard() – Removes element safely

* No error if element does not exist

```python
fruits.discard("apple")
```

### 3️⃣ pop() – Removes a random item

```python
item = fruits.pop()
print(item)
```

### 4️⃣ clear() – Removes all elements

```python
fruits.clear()
```

---

##  Loop Through Sets

You can loop through a set using a **for loop**.

### Example:

```python
numbers = {1, 2, 3, 4}

for num in numbers:
    print(num)
```

---

##  Join Sets

Python provides multiple ways to join sets.

### 1️⃣ union() or | (OR operator)

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A | B)
```

### 2️⃣ intersection() – Common elements

```python
print(A.intersection(B))
```

### 3️⃣ difference() – Elements in A but not in B

```python
print(A.difference(B))
```

### 4️⃣ symmetric_difference() – Elements not common

```python
print(A.symmetric_difference(B))
```

---

##  Frozenset

A **frozenset** is an immutable version of a set.

### Key Features:

* Cannot add or remove elements
* Useful as dictionary keys or set elements

### Example:

```python
fs = frozenset([1, 2, 3])
print(fs)
```

❌ Not allowed:

```python
fs.add(4)  # Error
```

---

##  Set Methods

| Method                 | Description                          |
| ---------------------- | ------------------------------------ |
| add()                  | Adds an element                      |
| update()               | Adds multiple elements               |
| remove()               | Removes element (error if not found) |
| discard()              | Removes element safely               |
| pop()                  | Removes random element               |
| clear()                | Clears the set                       |
| union()                | Combines sets                        |
| intersection()         | Common elements                      |
| difference()           | Difference of sets                   |
| symmetric_difference() | Non-common elements                  |
| copy()                 | Copies a set                         |
| isdisjoint()           | Checks no common elements            |
| issubset()             | Checks subset                        |
| issuperset()           | Checks superset                      |

---

## When to Use Sets?

* Removing duplicate values
* Membership testing (fast lookup)
* Mathematical set operations
* Comparing collections

---


---


