# Boolean Values and Operators in Python



###======================== Boolean Values (bool)===========================

In Python, a **Boolean** represents a logical value. It can have only **two possible values**:

* `True`
* `False`

These values are used when we want to make **decisions** in a program.

### Example:

```python
is_raining = True
is_sunny = False
```

Here, the variables don’t store numbers or text, they store **conditions**.

### Boolean from comparisons

Most of the time, Boolean values come from **comparisons**:

```python
print(10 > 5)     # True
print(3 == 4)     # False
print(7 <= 7)     # True
```

### Truthy and Falsy values

Python also treats some values as **True** or **False** automatically:

Falsy values (treated as `False`):

* `0`
* `0.0`
* `""` (empty string)
* `[]`, `{}`, `()` (empty collections)
* `None`

Everything else is considered **True**.

```python
print(bool(0))      # False
print(bool("Hi"))   # True
```

---

## ==============Operators in Python==============

Operators are symbols that tell Python **what operation to perform**.

---

## 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning             |
| -------- | ------------------- |
| `+`      | Addition            |
| `-`      | Subtraction         |
| `*`      | Multiplication      |
| `/`      | Division            |
| `%`      | Modulus (remainder) |
| `//`     | Floor division      |
| `**`     | Power               |

```python
print(10 + 3)
print(10 % 3)
print(2 ** 3)
```

---

## 2. Comparison (Relational) Operators

Used to compare two values. The result is always **True or False**.

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal to              |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

```python
print(5 == 5)
print(10 < 3)
```

---

## 3. Logical Operators

Used to combine conditions.

| Operator | Meaning                      |
| -------- | ---------------------------- |
| `and`    | True if both are True        |
| `or`     | True if at least one is True |
| `not`    | Reverses the result          |

```python
print(10 > 5 and 3 < 2)   # False
print(10 > 5 or 3 < 2)    # True
print(not True)           # False
```

---

## 4. Assignment Operators

Used to assign and update values.

| Operator | Example  |
| -------- | -------- |
| `=`      | `x = 5`  |
| `+=`     | `x += 2` |
| `-=`     | `x -= 2` |
| `*=`     | `x *= 2` |
| `/=`     | `x /= 2` |

```python
x = 10
x += 5
print(x)
```

---

## 5. Bitwise Operators

Work at the **binary (bit) level**.

| Operator | Name        |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

```python
print(5 & 3)
print(5 | 3)
```

---

## 6. Membership Operators

Used to check if a value exists in a sequence.

| Operator | Meaning     |
| -------- | ----------- |
| `in`     | Present     |
| `not in` | Not present |

```python
print('a' in 'apple')
print(5 not in [1, 2, 3])
```

---

## 7. Identity Operators

Used to compare **memory location**, not values.

| Operator | Meaning          |
| -------- | ---------------- |
| `is`     | Same object      |
| `is not` | Different object |

```python
a = 10
b = 10
print(a is b)
```

---


