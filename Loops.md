```python
string1 = "Python"
string2 = string1[::-1]
print(string2)
```

```python
string1 = "Loops are Fun!"
string1 = string1.lower()

v = "aeiou"
vcount = 0
ccount = 0

for i in range(0, len(string1), 1):
    if string1[i].isalpha():
        if string1[i] in v:
            vcount += 1
        else:
            ccount += 1
    
print (f"v count: {vcount}")
print (f"c count: {ccount}")
```

```python
num = 75869
count = 0
# // 10 chops off the last digit. It tells you "how many tens fit into this number."
# % 10 extracts only the last digit. It tells you "what is left over."
while num != 0:
    num = num // 10
    count += 1
print(f"Total digits are: {count}")
```

```python
num = 76542
final = 0

while num != 0:
    digit = num % 10
    final = (final * 10) + digit
    num = num // 10
    
print(final)
```

```python
num = 75869
min = 9
max = 0

while num != 0:
    digit = num % 10
    if digit < min:
        min = digit
    if digit > max:
        max = digit
    num = num // 10
print(min)
print(max)
```

```python
#16
num: int = 121
original_num = 121
final: int = 0

while num != 0:
    digit = num % 10
    final = (final * 10) + digit
    num = num // 10

if original_num == final:
    print("Yes")
else:
    print("No")
    print(final)
```

```python
#17
num = 5
factorial = 1
for i in range(1, num + 1, 1):
    factorial = factorial * i
print(factorial)
```

```python
# 18, Collatz conjecture
n = 6
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(f", {n}", end=""
```

```python
"""
#19, Practice Problem: Write a program to check if a number is an Armstrong number. An Armstrong number (for a 3-digit number) is an integer such that the sum of the cubes of its digits is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).
"""
#Enter Python code here and hit the Run button 
n=153
n_str = str(n)
total = 0
for i in n_str:
    total = total + int(i) ** 3

if total == n:
    print("Yes")
else:
    print("No")

```

```python
#20
i=1
j=1
while i <= 5:
    j = 1
    while j <= i:
        print(f"{j}", end="")
        j += 1
    print()
    i+= 1
```

```python
#21
n=5
for i in range(5, 0, -1):
    j=i
    for j in range(j, 0, -1):
        print(f"{j}", end ="")
    print()
```

```python
for i in range(1,21,2):
    print(f"{i} ", end="")
```

```python
import string
rows = 5
values = string.ascii_uppercase[:rows]

for idx, letter in enumerate(values):
    repeat_count = idx + 1
    print(letter * repeat_count)
```

```python
size = 5
for i in range(1, size+1, 1):
    if i == 1 or i == size:
        print("* " * size)
    else:
        print("* " + "  " * (size - 2) + "* ")

```

