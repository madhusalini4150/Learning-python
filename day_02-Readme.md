# Python Datatypes — int, float, complex

##  What are Datatypes?

A **datatype** tells Python what kind of value a variable holds. Based on the datatype, Python decides:

* how much memory is needed
* what operations can be performed

Python is **dynamically typed**, so you don’t need to declare the datatype explicitly.

---

##  Integer (`int`)

An **integer** is a whole number without any decimal point.

### Examples:

```python
a = 10
b = -25
c = 0
```

### Important Points:

* Can be positive, negative, or zero
* No size limit in Python
* Used for counting, indexing, calculations

---

## Floating Point (`float`)

A **float** is a number that contains a decimal point.

### Examples:

```python
x = 10.5
y = -3.14
z = 2.0
```

### Important Points:

* Used for precise values
* Suitable for measurements and averages
* Can represent very large or very small values

---

##  Complex Numbers (`complex`)

A **complex number** has two parts:

* Real part
* Imaginary part

Written in the form:

```
a + bj
```

### Examples:

```python
c1 = 3 + 4j
c2 = -2j
```

### Important Points:

* `j` represents the imaginary unit
* Mostly used in scientific and mathematical applications
* Real and imaginary parts can be accessed

```python
print(c1.real)
print(c1.imag)
```

---

##  Type Casting in Python

**Type casting** means converting one datatype into another datatype.

Python provides built‑in functions for type casting:

* `int()`
* `float()`
* `complex()`
* `str()`

---

##  Type Casting Examples

### String to Integer

```python
x = "10"
y = int(x)
```

### Integer to Float

```python
a = 5
b = float(a)
```

### Integer to Complex

```python
m = 7
n = complex(m)
```

### Float to Integer

```python
p = 9.8
q = int(p)   # decimal part is removed
```

 ###Important Notes on Type Casting

* Invalid conversions cause **errors**
* Decimal values are truncated when converting to `int`
* Complex numbers cannot be converted to `int` or `float`

```python
# This will cause an error
int(3 + 4j)
```
