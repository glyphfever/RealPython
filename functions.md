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

```python
# 5 inner function
def outer_func(a, b):
    def inner_func():
        val = a + b + 5
        return val
    
    res = inner_func()
    return res

print(outer_func(5,10))

```

```python
# 6 recursive function
def addition(num):
    if num > 0:
        return num + addition(num - 1)
    else:
        return 0
res = addition(10)
print(res)
```

```python
def display_student(name, age):
    print(name, age)

show_student = display_student
show_student("Emma" , 25)
```
```python
#8
def EvenNumberGenerator():
    list = range(4, 30)
    evenList = []
    for i in list:
        if i  % 2 == 0:
            evenList.append(i)
    return evenList           
            
print(EvenNumberGenerator())
```
```python
#9
def LargestItem():
    list = [4, 6, 8, 24, 12, 2]
    theOne = 0
    for i in list:
        if i > theOne:
            theOne = i
    return theOne           
            
print(LargestItem())
```

```python
# 10
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
            
# Call 1 (Positional): "hamster", "Harry"
describe_pet("hamster", "Harry")

# Call 2 (Keyword): animal_type="dog", pet_name="Willie"
describe_pet(animal_type="dog", pet_name="Willie")
```





