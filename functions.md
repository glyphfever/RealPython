```python
def func1(*args):
    print("Printing values:")
    for i in args:
        print(i)

# Calling with 3 arguments
func1(20, 40, 60)

# Calling with 2 arguments
func1(80, 100)
```

```python
def calculation(a, b):
    
    add = a + b
    sub = a - b
    
    return add, sub
res = calculation(40,10)
print(res)
```

```python
def show_employee(emp_name, salary=9000):
    
    label = "Name="+ emp_name + " salary=" + str(salary)
    
    return label
print(show_employee("Ben",12000) )
print(show_employee("Jessa"))
```
