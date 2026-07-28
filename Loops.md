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

