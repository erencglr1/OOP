# Python Cheatsheet

## Variables
```python
# Creating variables
x = 5
name = "Eren"
pi = 3.14
is_active = True
```

## Data Types
```python
# int
age = 21

# float
height = 5.9

# str
city = "New York"

# bool
is_student = False
```

## Conditional Statements
```python
# if, elif, else
age = 18

if age >= 18:
    print("You are an adult.")
elif age > 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```

## Loops

### While Loop
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### For Loop
```python
for i in range(5):
    print(i)
```

## Data Structures

### List
```python
fruits = ["apple", "banana", "cherry"]
```

### Dictionary
```python
person = {"name": "Eren", "age": 21}
```

### Tuple
```python
coordinates = (10, 20)
```

### Set
```python
unique_numbers = {1, 2, 3}
```

## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Eren"))
```
