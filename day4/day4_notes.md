Day-4

https://www.geeksforgeeks.org/random-seed-in-python/

* Random function in python

Python Random module is an in-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these are not truly random. This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc.


Creating Random Integers

random.randint() method is used to generate random integers between the given range.
Syntax :
randint(start, end)
Example: Creating random integers


import random
 value=random.randint(1,10)
print(value)
Output:-
1

import random
random_integer=random.randint(1,10)
print(random_integer)

The above code gives the output as a  number btw 1 to 10 only 


Creating Random Floats

random.random() method is used to generate random floats between 0.0 to 1.

# import random

import random
 value=random.random()
print(value)
Output:-
1.4668973

The above code gives the output as a number btw 0 to 1 only it does not incude 0 and 1

Creating Random Floats but both numbers inclusive

random.uniform() Return random floating number between two numbers both inclusive

import random
 value=random.uniform(1,10)
print(value)
Output:-
9.4668973211
The above code gives the output as a floating number btw 1 to 10 only it includes 0 and 1

Selecting Random Elements

random.choice() function is used to return a random item from a list, tuple, or string.

import random
greetings=[‘hello’,’hi’,’hey’,’howdy’,’hola’]
 value=random.choice(greetings)
print(value+’, srujitha!’)
Output:-
Hello, srujitha!
This choice method pics up a string in the list randomly and gives the output

# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))


Shuffling List
random.shuffle() method is used to shuffle a sequence (list). Shuffling means changing the position of the elements of the sequence. Here, the shuffling operation is inplace.


import random
sample_list = [1, 2, 3, 4, 5]
print("Original list : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)

# output
# Original list : 
# [1, 2, 3, 4, 5]

# After the first shuffle : 
# [3, 5, 1, 2, 4]

# After the second shuffle : 
# [1, 2, 5, 3, 4]


- This random is just a module that is created by different python makers we can also create our own python module and we can import that into our code also
Eg:-in a few file named my_module write pi=3.14
Now in your new file import my_module and we get that my_module data everything into this code 
Code in my_module 
pi=3.14
Code in my_generator
import my_module
print(my_module.pi,end="\n")
Output
3.14

- A module allows you to logically organize your Python code. 
- Grouping related code into a module makes the code easier to understand and use. 
- A module is a Python object with arbitrarily named attributes that you can bind and reference. 
- Simply, a module is a file consisting of Python code.


- To use the below methods first we have to import the random module into the code 
- Eg:- import random
The random module has a set of methods:
Method	Description
seed()	Initialize the random number generator
getstate()	Returns the current internal state of the random number generator
setstate()	Restores the internal state of the random number generator
getrandbits()	Returns a number representing the random bits
randrange()	Returns a random number between the given range
randint()	Returns a random number between the given range
choice()	Returns a random element from the given sequence
choices()	Returns a list with a random selection from the given sequence
shuffle()	Takes a sequence and returns the sequence in a random order
sample()	Returns a given sample of a sequence
random()	Returns a random float number between 0 and 1
uniform()	Returns a random float number between two given parameters
triangular()	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()	Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate()	Returns a random float number based on the Gamma distribution (used in statistics)
gauss()	Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate()	Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate()	Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate()	Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate()	Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate()	Returns a random float number based on the Weibull distribution (used in statistics)


- Sequence(strings,list,tulpe)

* List and tuple
￼
note* mutable is also know as changable
These are collection based datat types .

Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

- List[]

Lists are used to store multiple items in a single variable.
Lists are created using square brackets:
A single list may contain DataTypes like Integers, Strings, as well as Objects.
List items are ordered, changeable, and allow duplicate values.


Note: The first item of the list has index 0.

Negative Indexing
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.


Example


thislist = ["apple", "banana", "cherry"]
print(thislist)

# output
# ['apple', 'banana', 'cherry']

Example

String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1,list2,list3,sep="\n")
# output
# ['apple', 'banana', 'cherry']
# [1, 5, 7, 9, 3]
# [True, False, False]

Example

A list can contain different data types:
A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

Example 

accessing an element from the Multi-Dimensional List using index number

list1 = [["abc", 4, True],[40, "male"]]
 print("Accessing a element from a Multi-Dimensional list")
 print(list1[0][1])
 print(list1[1][0])


Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
- Coding:

list1=[1,"sruji",3.8,"adi"]
print(list1[2])#output 3.8 #acsessing the list
print(list1[:2])#output[1, 'sruji'] #slicing the list from end 
print(list1[2:])#output [3.8, 'adi'] slicing the list from start 
print(list1[-2])#output 3.8 #negative index
print(list1[:-1])#output [1, 'sruji', 3.8] #slicing negative index
#Check if Item Exists
if "sruji" in list1:
    print("yes")
if "ai" not in list1:
    print("yes")
#output yes yes

list1[1]="srujitha"#output [1, 'srujitha', 3.8, 'adi'] Change Item Value in list
print(list1)
list1.insert(1,"chandrika")#output [1, 'chandrika', 'srujitha', 3.8, 'adi'] inserting a element in the list in a specified place
print(list1)
list1.append("sada")#output [1, 'chandrika', 'srujitha', 3.8, 'adi', 'sada'] with append we can add a item to the end
print(list1)

list2=[2,"tanya",5.22,"sanj",8] #combing two lists
print(list2)#output [2, 'tanya', 5.22, 'sanj', 8]
list2.extend(list1)
print(list2)#output [2, 'tanya', 5.22, 'sanj', 8, 1, 'chandrika', 'srujitha', 3.8, 'adi', 'sada']

list1.remove("srujitha")#to remove an item from list
print(list1)#output [1, 'chandrika', 3.8, 'adi', 'sada']
del list2 # to delete a list completly
print("length of list")    
print(len(list1))#output 5
for x in list1:#looping in list 
    print(x)
#ouput
# 1
# chandrika
# 3.8
# adi
# sada
list1.clear()
print(list1)#output [] #to clear a lsit

Output

[1, 'sruji', 3.8, 'adi']
3.8
[1, 'sruji', 3.8]
['sruji', 3.8, 'adi']
3.8
[1, 'sruji', 3.8]
yes
yes
[1, 'srujitha', 3.8, 'adi']
[1, 'chandrika', 'srujitha', 3.8, 'adi', 'sada']
[1, 'chandrika', 'srujitha', 3.8, 'adi', 'sada']
[2, 'tanya', 5.22, 'sanj', 8]
[2, 'tanya', 5.22, 'sanj', 8, 1, 'chandrika', 'srujitha', 3.8, 'adi', 'sada']
[1, 'chandrika', 3.8, 'adi', 'sada']
1
chandrika
3.8
adi
sada
lenth of list
5
[]
￼
￼
- Nested lists[]

list1=["sruji","adi","jai"]
list2=["sanju","joy"]
newlist=[list1,list2]
print(newlist)

Output
[['sruji', 'adi', 'jai'], ['sanju', 'joy']]

Question 1:

Given the following list:
* 		fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
Which line of code will give you "Apples"?
 fruits[3]
		 fruits[4]
		 fruits.Apples()
		 fruits[-5] correct answer
		 fruits[-4]


  Using a negative index offsets from the end of the list. To offset from the start of the list the code would be: fruits[2] 

		fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
		vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
		 
		dirty_dozen = [fruits, vegetables]
		 
		print(dirty_dozen[1][1])

What will be printed?
 "Spinach"
		 "Strawberries"
		 "Kale" correct answer
		 ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
	 "Nectarines"

