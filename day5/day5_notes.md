DAY-5

For loop for lists

l = ["srujitha", "devineni", "india"]
for i in l:
    print(i)
    
# output
# srujitha
# devineni
# india

range() function

The Python range() function returns a sequence of numbers, in a given range. The most common use of it is to iterate sequence on a sequence of numbers using Python loops.
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

Syntax of Python range() function
Syntax: range(start, stop, step)

Parameter:
* start: [ optional ] start value of the sequence
* stop: next value after the end value of the sequence
* step: [ optional ] 
* The step value must not be zero. If a step is zero, python raises a ValueError exception.

What is the use of the range function in Python

In simple terms, range() allows the user to generate a series of numbers within a given range. Depending on how many arguments the user is passing to the function, the user can decide where that series of numbers will begin and end, as well as how big the difference will be between one number and the next. Python range() function takes can be initialized in 3 ways.
* range (stop) takes one argument.
* range (start, stop) takes two arguments.
* range (start, stop, step) takes three arguments.

Python range (start, stop)

When the user call range() with two arguments, the user gets to decide not only where the series of numbers stops but also where it starts, so the user don’t have to start at 0 all the time. Users can use range() to generate a series of numbers from X to Y using range(X, Y).
￼

Coding:

# print first 5 integers
# using python range() function
for i in range(5):
	print(i, end=" ")
print()

Output:
0 1 2 3 4 

Python range (start, stop, step)
When the user call range() with three arguments, the user can choose not only where the series of numbers will start and stop, but also how big the difference will be between one number and the next. If the user doesn’t provide a step, then range() will automatically behave as if the step is 1. In this example, we are printing even numbers between 0 and 10, so we choose our starting point from 0(start = 0) and stop the series at 10(stop = 10). For printing an even number the difference between one number and the next must be 2 (step = 2) after providing a step we get the following output (0, 2, 4, 8). 
￼

Coding:

for i in range(0, 10, 2):
	print(i, end=" ")
print()

Output
0 2 4 6 8 

# incremented by -2
for i in range(25, 2, -2):
	print(i, end=" ")
print()

Output

25 23 21 19 17 15 13 11 9 7 5 3 

* Python range() with float does not work
* Python range() function doesn’t support the float numbers. i.e. user cannot use floating-point or non-integer numbers in any of its argument. Users can use only integer numbers.

Concatenation of two range() functions using itertools chain() method

The result from two range() functions can be concatenated by using the chain() method of itertools module. The chain() method is used to print all the values in iterable targets one after another mentioned in its arguments.
from itertools import chain

# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))

for i in res:
	print(i, end=" ")

Output: ‘

0 1 2 3 4 10 12 14 16 18 

range() to a list in Python

* 		Difficulty Level : Medium
* 		Last Updated : 30 Jan, 2019
Read

Discuss

Courses

Practice

Video



Often times we want to create a list containing a continuous value like, in a range of 100-200. Let’s discuss how to create a list using the range() function.
Will this work ?




# Create a list in a range of 10-20
My_list = [range(10, 20, 1)]
  
# Print the list
print(My_list)
Output : 
￼
 As we can see in the output, the result is not exactly what we were expecting because Python does not unpack the result of the range() function.
Code #1: We can use argument-unpacking operator i.e. *.

# Create a list in a range of 10-20
My_list = [*range(10, 21, 1)]
  
# Print the list
print(My_list)
Output :
￼
 As we can see in the output, the argument-unpacking operator has successfully unpacked the result of the range function.   Code #2 : We can use the extend() function to unpack the result of range function.


# Create an empty list
My_list = []
  
# Value to begin and end with
start, end = 10, 20
  
# Check if start value is smaller than end value
if start < end:
    # unpack the result
    My_list.extend(range(start, end))
    # Append the last value
    My_list.append(end)
  
# Print the list
print(My_list)
Output : 
￼
