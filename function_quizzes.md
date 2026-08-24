1. What is a Python decorator primarily used for?

 To create new functions from existing ones.
 To modify or extend the behavior of functions or methods without directly changing their source code.
 To define private functions within a class.
 To handle exceptions within a function.
 
2. What is the output of the following function call

def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)
 Emma 25
 Emma 20
 Error
 
3. Which function from the random module would you use to get a random integer between 1 and 10 (including 1 and 10)?

 random.number(1, 10)
 random.choice(1, 10)
 random.randint(1, 10)
 random.integer(1, 10)
 
4. What is a “default argument” in a Python function?

 An argument that must always be provided
 An argument that has a predefined value if not supplied by the caller.
 An argument that can only be passed by keyword.
 An argument that is always a string.

5. Select which is True for Python function

 A function only executes when it is called and we can reuse it in a program
 A function can take an unlimited number of arguments.
 A Python function can return multiple values.
 All of the above

6. What is the output of the following display() function call

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)
 Error
 Kelly
9000
 (’emp’, ‘Kelly’)
(‘salary’, 9000)
 emp
salary

7. What is the output of the following function call

def add(a, b):
  return a + b
  a = 20
  b = 30
  return a + b

result = add(5, 10)
print(result)
 (15, 50)
 15
 50
 Error

8. Select all correct function calls

Given the following function fun1() Please select all the correct function calls.

def fun1(name, age):
    print(name, age)
 
fun1("Emma", age=23)
fun1(age =23, name="Emma")
 fun1(name="Emma", 23)
 fun1(age =23, "Emma")

9. What is the output of the following display() function call

def display(**kwargs):
    for i in kwargs.values():
        print(i)

display(emp="Kelly", salary=9000)
 Error
 Kelly
9000
 emp: Kelly
salary: 9000
 emp
salary

10. What will be the output of the following Python code?

def multiply(a, b):
    return a * b

def apply_operation(func, x, y):
    return func(x, y)

result = apply_operation(multiply, 5, 3)
print(result)
 8
 15
 Error
 multiply

11. Which of the following best describes a Python lambda function?

 A named function defined using the def keyword.
 An anonymous, small, single-expression function.
 A function that can only accept one argument.
 A function used exclusively for mathematical operations.

12. Select Correct Function

Which random module function would you use to get a random integer within a specific range (inclusive of both ends)?

 random.random()
 random.uniform()
 random.randint(a, b)
 random.choice(sequence)

13. What is a key characteristic of a Python generator function?

 It uses the return keyword multiple times.
 It stores all its results in memory before returning them.
 It uses the yield keyword to produce a sequence of values lazily.
 It can only be called once.
14. Choose the correct declaration for fun1().

To enable the successful execution of the below two fun1() function call, choose the correct declaration for fun1().

fun1(25, 75, 55)
fun1(10, 20)
 def fun1(**kwargs)
 No, it is not possible in Python
 def fun1(args*)
 def fun1(*args)
15. What is the primary purpose of *args and **kwargs in Python function definitions?

 To define optional parameters
 To accept a variable number of positional and keyword arguments, respectively
 To enforce type hinting for arguments
 To create decorators
16. What is the primary purpose of the if __name__ == "__main__": block in a Python script?

 To define global variables
 To prevent the code from running when imported as a module
 To mark the start of the script’s execution when run directly
 To indicate that the script is a library
17. How would you get the current date and time using the datetime module?

 datetime.current_time()
 datetime.datetime.now()
 datetime.get_time()
18. What will be the output of the following Python code?

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x*x, numbers))
print(squared_numbers)
 [1, 4, 9, 16, 25]
 [1, 2, 3, 4, 5]
 Error
19. What will be the output of the following Python code?

def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(calculate_sum(1, 2, 3, 4))
print(calculate_sum())
 10
0
 10
None
 Error
 10
Error
20. One of the main benefits of using modules in Python is:

 They make your code run faster.
 They allow you to reuse code across different programs.
 They automatically fix errors in your code.
 They reduce the amount of memory your program uses.
21. Which of the following is the correct way to import only the pi constant from the math module?

 import math.pi
 from math import pi
 import pi from math
 All of the above
22. What will be the output of the following Python code?

def do_nothing():
    pass

result = do_nothing()
print(result)
 do_nothing()
 pass
 None
 Error
23. You want to import the numpy module but refer to it as np in your code. Which syntax is correct?

 import numpy as np
 from numpy as np
 import np = numpy
 numpy.import(np)
 
24. The os.path module in Python is primarily used for:

 Interacting with the operating system’s environment variables.
 Performing mathematical operations on file paths.
 Pathname manipulation (e.g., joining paths, checking existence, getting file extensions).
 Managing processes and threads.
 
25. What is the output of the following display_person() function call

def display_person(*args):
    for i in args:
        print(i)

display_person(name="Emma", age="25")
 Error
 Emma
25
 name
age
