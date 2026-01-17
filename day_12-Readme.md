# Python Tuples – 


* Python Tuples
* Access Tuples
* Update Tuples
* Unpack Tuples
* Loop Tuples
* Join Tuples
* Tuple Methods

---

##  1. Python Tuples

### What is a Tuple?

A **tuple** is a collection data type in Python used to store **multiple values in a single variable**.

### Key Characteristics

* Ordered (elements have index positions)
* **Immutable** (cannot be changed after creation)
* Allows duplicate values
* Faster than lists

### Creating a Tuple

```python
fruits = ("apple", "banana", "cherry")
print(fruits)
```

### Single‑Item Tuple (Important!)

```python
single = (10,)   # comma is mandatory
```

Without the comma, Python treats it as an integer.

---

##  2. Access Tuples

### Access Using Index

```python
colors = ("red", "green", "blue")
print(colors[0])    # red
print(colors[-1])   # blue
```

### Access Using Slicing

```python
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
```

### Check if Item Exists

```python
if "apple" in fruits:
    print("Apple is present")
```

---

##  3. Update Tuples

### ❌ Tuples Cannot Be Changed Directly

```python
# This will cause an error
fruits[0] = "mango"
```

### ✅ Correct Way to Update a Tuple

Convert tuple → list → modify → convert back

```python
fruits = ("apple", "banana", "cherry")
fruits_list = list(fruits)
fruits_list[0] = "mango"
fruits = tuple(fruits_list)
print(fruits)
```

---

##  4. Unpack Tuples

### Basic Unpacking

```python
student = ("Madhu", 20, "CSE")
name, age, branch = student
print(name, age, branch)
```

### Using Asterisk (*) for Multiple Values

```python
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)
print(middle)
print(last)
```

---

##  5. Loop Tuples

### Loop Using for Loop

```python
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
```

### Loop Using Index

```python
for i in range(len(fruits)):
    print(fruits[i])
```

### While Loop

```python
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

## 6. Join Tuples

### Join Using + Operator

```python
t1 = (1, 2, 3)
t2 = (4, 5)
result = t1 + t2
print(result)
```

### Repeat Tuple

```python
nums = (1, 2)
print(nums * 3)
```

---

##  7. Tuple Methods

Tuples have **only two built‑in methods** because they are immutable.

### count()

Returns how many times a value appears.

```python
nums = (1, 2, 2, 3, 2)
print(nums.count(2))
```

### index()

Returns index of first occurrence.

```python
print(nums.index(3))
```

---



##  When to Use Tuples

* When data should **not change**
* To improve performance
* For fixed data (days, coordinates, settings)

---


