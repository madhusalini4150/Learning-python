#  Python Dictionaries – 


---

##  What is a Dictionary?

A **dictionary** in Python is a collection that stores data in **key : value** pairs.

### Key Features

* Unordered (in older versions)
* Mutable (can be changed)
* Keys must be **unique**
* Keys are immutable (string, number, tuple)

### Example

```python
mydict = {
    "name": "Joy",
    "age": 22,
    "role": "Actor"
}
```

---

##  Access Dictionary Items

You can access values using **keys**.

### Using Key

```python
print(mydict["name"])
```

### Using get()

```python
print(mydict.get("age"))
```

✔ `get()` does not raise an error if the key is missing.

---

##  Change Dictionary Items

Dictionaries are mutable, so values can be updated.

```python
mydict["age"] = 25
print(mydict)
```

---

##  Add Dictionary Items

Add new key‑value pairs easily.

```python
mydict["city"] = "Hyderabad"
```

### Using update()

```python
mydict.update({"salary": 50000})
```

---

##  Remove Dictionary Items

### pop()

```python
mydict.pop("age")
```

### popitem() (removes last item)

```python
mydict.popitem()
```

### del keyword

```python
del mydict["role"]
```

### clear() (removes all items)

```python
mydict.clear()
```

---

##  Loop Through Dictionaries

### Loop through keys

```python
for key in mydict:
    print(key)
```

### Loop through values

```python
for value in mydict.values():
    print(value)
```

### Loop through key‑value pairs

```python
for key, value in mydict.items():
    print(key, value)
```

---

##  Copy Dictionaries

### Using copy()

```python
new_dict = mydict.copy()
```

### Using dict()

```python
new_dict = dict(mydict)
```

 `new_dict = mydict` creates a reference, not a copy.

---

##  Nested Dictionaries

A dictionary inside another dictionary.

```python
student = {
    "stud1": {"name": "A", "marks": 80},
    "stud2": {"name": "B", "marks": 90}
}
```

### Access nested values

```python
print(student["stud1"]["name"])
```

---

##  Dictionary Methods

| Method   | Description             |
| -------- | ----------------------- |
| keys()   | Returns all keys        |
| values() | Returns all values      |
| items()  | Returns key‑value pairs |
| get()    | Access value safely     |
| update() | Update dictionary       |
| pop()    | Remove specific key     |
| clear()  | Remove all items        |
| copy()   | Copy dictionary         |

---



---

