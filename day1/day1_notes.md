
Day-1

* Created by Guido Van Rossum in 1981 
1991 1st version

Python is a simple, general purpose, high level, and object-oriented programming language.
It is a interpreted programming language

Python supports multiple programming pattern, including object-oriented, imperative, and functional or procedural programming styles.
 
Used for web development ,software devploment in complex mathematics and system scripting it can be used with web, enterprise, 3D CAD, etc.
It is used to deal with big data 
cIt willl allow oop
Easy to code beacuse the syntax is simple 
Easy to read it is like normal english 
It is interpreted
It is portable 
We don't need to use data types to declare variable because it is dynamically typed so we can write a=10 to assign an integer value in an integer variable.

Why should we learn a programming language

* Lets take computer the main thing in the computer is the processor 
- Programming means talking to the processor 
- To talk with the processor we should know some lang because processor can only understand 0s and 1s
- So we should learn some programming language 
- So programming language is the meduim to talk to the processor 
- So a program is a set of instructions given to the proccessor to perform our required task 
- If there are 5 or 20 instructions it will be a program if there are 1000 of lines of codes then  we call it a software 

* To run a program we should have space in computer we have  secondary memory(tbs) and main memory(gbs) and cache(mbs) register(kbs),Register is the fastet of all the memorys .
The program or anything we write will be stored the secondary memory but if we want to run it it can be only done by register beacause processor can only run register data
 
* Mips:- Million instructions per sec 
 Registers are to costly so we dont use only register we use diffferent memorys .

* How to comment a line
* 
We can use # for single line comments 
And we can use “”” …….. “”” for multiple lines of code

1) Comments are used mainly in two cases -
a) To avoid a line of code from running/executing
b) To avoid description of a code from being treated as code and executed.
2) There are two types of comments -
a) Single line comments ( # )
i) Eg: #a = 3
b) Multi line comments ( “”” “”” )
i) Eg: “”” a = 3 b = 6 “””
In jupyter

If we want it as a sentence we use -
f we want it as a italic we use  *
If we want it as a bold type we use **
If we want it as a bold italic we use ***

* Variables 

To store data we use variables 
Python is case sensitive

- Rules for variable name in python

It should start with letter (a-z or A-Z) or underscore
It shouldnt start witrh a number or special char @ or number

Camel Case

Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case

Each word starts with a capital letter:
MyVariableName = "John"

Snake Case

Each word is separated by an underscore character:
my_variable_name = "John"

The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:\

Coding:

x = 5
y = "John"
print(x, y)

Output

5,john

* Global Variables

Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

Example
Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

* Input function

1) To get some data from the user.
2) input() functionality is used
3) By default, data received using input() is of string data type. It can be converted into the required data type by typecasting.

* Typecasting

1) Type casting means type conversion
2) There are two types of type casting -
a) Implicit type casting - happens directly without our intervention
i) Eg: a = 3 Here, a is automatically made into an int by assigning 3 into it.

b) Explicit type casting - requires our intervention
i) Eg: b = 3.14
ii) c = int(b) Here, c is made into int forcefully and 0.14 data is discarded which makes c = 3

4) To convey the purpose of this data input to the user, we can pass string to the input()
5.)Eg:-input(‘write a number : ’) this whole line will be replaced by the input we give 

We can input like this too
input(“hello”+input(“what is ur name ? : ”)+”!”)
output: Hello srujitha!

Coding: 

input("enter a number: ")
input("hello "+input("enter you name: ")+" !.")

Output

enter a number: 12
enter you name: srujitha
hello srujitha !.

￼
￼

- We cant convert a character string into an integer 
- We can convert number string into an integer or float 

* What is concatenation in programming?

Concatenation, in the context of programming, is the operation of joining two strings together. The term"concatenation" literally means to merge two things together. Also known as string concatenation.
- We can’t concat a string and a integer, so to concat integer and string we use the map function

* Taking multiple inputs from user using  split and map 

Using split() method : 
 This function helps in getting multiple inputs from users. It breaks the given input by the specified separator. If a separator is not provided then any white space is a separator. Generally, users use a split() method to split a Python string but one can use it in taking multiple inputs.

Syntax : 
input().split(separator, maxsplit)

Coding: 

x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

Output

Enter two values: 1 2
Number of boys:  1
Number of girls:  2


a,b=input("enter your two name: ").split()
print("hi "+a+" !.")
print("hi "+b+" !.")

Output

enter your two name:  srujitha sanjana
hi srujitha !.
hi sanjana !.

a,b,c=input("enter your three name: ").split()
print("hi "+a+" !.")
print("hi "+b+" !.")
print("hi "+c+" !.")

Output

enter your three name: srujitha sanjana meghana
hi srujitha !.
hi sanjana !.
hi meghana !.

If we want to input for 100 variables then we cant take 100 variable names and then input so in one variable name using list and map function we take multiple inputs .

Syntax

map(function, iterables)
Eg:-
x, y = map(int, input().split())
It works as follows:
1. input() will query the user for input, and read one line of user input;
2. .split() will split that input into a list of “words”;
3. map(int, ...) will call int on each word, it will to that lazily (although that is not important here); and
4. x, y = ... will unpack the expression into two elements, and assign the first one to n and the second one to S.

Coding:

x, y = map(int, input("Enter 2 number with space: ").split())
print("First Number: ", x)
print("Second Number: ", y)

x,y,z=map(int,input().split())
print(x,y,z,sep="\n")

Output:-
1 2 3
1
2
3

x=list(map(int,input("enter numbers: ").split()))
print(x,sep=",")

Output
enter numbers: 1 2 3 4 5 6 7  88 9
[1, 2, 3, 4, 5, 6, 7, 88, 9]


* Output

1) To display data to the user.
2) print() functionality is used.
3) We can pass any type of data to the print() function.
4) We can even pass multiple data elements at once.
a) Eg: print(a,b)
5) Parameter ‘end’ can be used to specify how the output should end.
a) Eg: print(‘Hello’,end=’ ’)
6) Parameter ‘sep’ can be used to specify how the multiple data elements
passed have to be separated.
a) Eg: print(a,b,sep=’\n’)

￼
