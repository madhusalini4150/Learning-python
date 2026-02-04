# Python Loops in Python

## What is a Loop?

A loop in Python is used to execute a block of code repeatedly until a certain condition is met or for a fixed number of times. Loops reduce code repetition and make programs shorter, cleaner, and easier to understand.

Python mainly provides two types of loops: for loop and while loop. Python also supports nested loops and loop control statements.

## for Loop

A for loop is used when the number of iterations is known in advance. It is commonly used to iterate over sequences like lists, strings, tuples, and ranges.

```python
for i in range(5):
    print(i)
```

The loop starts from 0 and ends at 4 because the end value is excluded.

### for Loop with List

```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```

### for Loop with String

```python
name = "python"
for ch in name:
    print(ch)
```

## range() in Loops

The range() function generates a sequence of numbers and is very commonly used with for loops.

```python
for i in range(1, 6):
    print(i)
```

```python
for i in range(2, 11, 2):
    print(i)
```

## while Loop

A while loop is used when the number of iterations is not known in advance. The loop continues as long as the condition is True.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

If the condition becomes False, the loop stops automatically.

## Infinite Loop

If the condition never becomes False, the loop runs forever. This is called an infinite loop.

```python
while True:
    print("Hello")
```

Infinite loops must be stopped using break.

## Loop Control Statements

Loop control statements are used to change the normal flow of loops.

### break Statement

The break statement is used to stop the loop immediately.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

### continue Statement

The continue statement skips the current iteration and moves to the next one.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### pass Statement

The pass statement does nothing. It is used as a placeholder.

```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

## Nested Loops

A loop inside another loop is called a nested loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

## Using else with Loops

Python allows an else block with loops. The else block executes when the loop finishes normally without break.

```python
for i in range(1, 6):
    print(i)
else:
    print("Loop completed")
```

```python
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("While loop finished")
```


## Common Mistakes in Loops

Not updating the loop variable in while loop can cause infinite loops. Using wrong indentation can also lead to errors or unexpected behavior.


