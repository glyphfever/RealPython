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

