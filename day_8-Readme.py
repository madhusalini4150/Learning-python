# Python Lists – Looping, List Comprehension & Nested Lists

This README explains **how to work with lists in Python**, focusing on:

* Looping through a list
* List comprehension
* Nested lists

---

## 1️⃣ Looping Through a List

Looping is used to **access each element one by one**.

### 🔹 Using `for` loop

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

**Output:**

```
apple
banana
mango
```

### 🔹 Using `while` loop

```python
numbers = [10, 20, 30]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1
```

### 🔹 Using `range()` with index

```python
colors = ["red", "blue", "green"]

for i in range(len(colors)):
    print(i, colors[i])
```

---

## 2️⃣ List Comprehension

List comprehension is a **short and clean way** to create lists using a single line.

### 🔹 Basic Syntax

```python
new_list = [expression for item in iterable]
```

### 🔹 Example: Create a new list

```python
numbers = [1, 2, 3, 4]
squares = [x*x for x in numbers]
print(squares)
```

**Output:**

```
[1, 4, 9, 16]
```

### 🔹 With condition (if)

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
```

### 🔹 Compare: Normal loop vs List comprehension

```python
# Normal loop
even = []
for x in numbers:
    if x % 2 == 0:
        even.append(x)

# List comprehension
even = [x for x in numbers if x % 2 == 0]
```

---

## 3️⃣ Nested Lists

A nested list is a **list inside another list**.

### 🔹 Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### 🔹 Access elements

```python
print(matrix[0])      # [1, 2, 3]
print(matrix[0][1])   # 2
```

### 🔹 Loop through a nested list

```python
for row in matrix:
    for item in row:
        print(item)
```

### 🔹 Nested list comprehension

```python
flat_list = [item for row in matrix for item in row]
print(flat_list)
```

**Output:**

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## ✅ Key Points

* Use **loops** to process list elements one by one
* **List comprehension** makes code short and readable
* **Nested lists** are useful for tables, matrices, and structured data

---

