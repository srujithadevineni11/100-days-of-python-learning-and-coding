
Day-3

* Conditionals

There comes situations in real life when we need to make some decisions and based on these decisions, we decide what should we do next. Similar situations arise in programming also where we need to make some decisions and based on these decisions we will execute the next block of code. Decision-making statements in programming languages decide the direction of the flow of program execution. 

1) In Python, if-else elif statement is used for decision making.
2) if statement
if statement is the most simple decision-making statement. It is used to decide whether a certain statement or block of statements will be executed or not i.e if a certain condition is true then a block of statement is executed otherwise not.
Syntax: 
if condition1:
statements-to-execute when condition1 is satisfied
As we know, python uses indentation to identify a block. So the block under an if statement will be identified as shown in the below example:  
if condition:
   statement1
statement2

# Here if the condition is true, if block 
# will consider only statement1 to be inside 
# its block.

Coding:

# x=int(input("enter a number: "))
# if x<=10:
#           print("inside if block ")
# print("outside if block ") 
   
# output
# enter a number: 9
# inside if block 
# outside if block 


i = 10

if (i > 15):
          print("10 is less than 15")
print("I am Not in if")
#output
# I am Not in if
# As the condition present in the
# if statement is false. So, 
# the block below the if statement is executed.

3.)if-else
The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. But what if we want to do something else if the condition is false. Here comes the else statement. We can use the else statement with if statement to execute a block of code when the condition is false. 

Syntax: 
if (condition):
             statements-to-execute when condition is satisfied
else:
             statements-to-execute when condition is not satisfied

Coding:

x=int(input("enter a number: "))
if x<=10:
          print("inside if block ") 
else:
          print("inside else block")
   
# output
# enter a number: 1
# inside if block 

# enter a number: 11
# inside else block

4.)nested-if
A nested if is an if statement that is the target of another if statement. Nested if statements mean an if statement inside another if statement. Yes, Python allows us to nest if statements within if statements. i.e, we can place an if statement inside another if statement.
if (condition1):
     Executes when condition is true
   if (condition2): 
    Executes when condition is true
   # if Block is end here
# if Block is end here

Coding:
x=int(input("enter a number: "))
if x==10:
          print("inside if block ") 
          if x>=10:
                    print("inside nested if block")
# output         
# enter a number: 10
# inside if block 
# inside nested if block

5.)if-elif-else ladder

Here, a user can decide among multiple options. The if statements are executed from the top down. As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final else statement will be executed.
Syntax: 
if (condition):
    statements-to-execute when condition is satisfied
elif (condition):
    statements-to-execute when condition1 is not satisfied & condition2 is satisfied
.
.
else:
    statements-to-execute when none of the conditions are satisfied
i = 20
if (i == 10):
          print("i is 10")
elif (i == 15):
          print("i is 15")
elif (i == 20):
          print("i is 20")
else:
          print("i is not present")

# output
# i is 20

￼

* Use the correct short hand syntax to write the following conditional expression in one line:
*  if 5 > 2 
*      print("Yes")
* else 
*      print("No")

print("Yes") if 5 > 2 else print("No")

Checking more than two conditions is very common in Programming Languages. Let’s say we want to check the below condition:
a < b < c
The most common syntax to do it is as follows:

if a < b and b < c :
   {...}
In Python, there is a better way to write this using the Comparison operator Chaining. The chaining of operators can be written as follows:
if a < b < c :
    {.....}

Coding:

# Python code to illustrate
# chaining comparison operators
x = 5
print(1 < x < 10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)

Output

True
False
True
True
True

* Loops


1) These are used when you need to do something repeatedly.
2) It is really important to make sure that the repetition is not infinite. We can ensure this by -
a) Using a condition, until it is true, the loop will continue.
b) Making sure that condition is not true forever.
3) while, for keywords are used to implement the loops in python.
4.)for
Python For loop is used for sequential traversal i.e. it is used for iterating over an iterable like String, Tuple, List, Set or Dictionary.
In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). There is “for” loop which is similar to each loop in other languages.
For Loops Syntax

for var in iterable:
    # statements

Coding:

# Iterating over a String
# print("String Iteration")
# s = "srujitha"
# for i in s:
#         print(i)

# output
# String Iteration
# s
# r
# u
# j
# i
# t
# h
# a

l = ["srujitha", "devineni", "india"]
for i in l:
    print(i)
    
# output
# srujitha
# devineni
# india

5)while

Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.

Syntax: 

while expression:
       statements-to-execute until condition is satisfied

count = 0
while (count < 3):
          count = count + 1
          print("srujitha")

# output
# srujitha
# srujitha
# srujitha

# checks if list still
# contains any element
a = [1, 2, 3, 4]
while a:
          print(a.pop())
# output
# 4
# 3
# 2
# 1


5) The range() Function
If we  need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

 for i in range(5):
              print(i)

0
1
2
3
4

6.)To iterate over the indices of a sequence, you can combine range() and len() as follows:

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
          print(i, a[i])

0 Mary
1 had
2 a
3 little
4 lamb

We can range() to generate a collection on the go in the following way-

a) range(end)
b) range(start, end)
c) range(start, end, step_size)
Please note: end is not included in the collection.

7) After every : we are giving space, this is called indentation. Indentation is used to make sure that all required statements that are to be
executed under a loop are grouped.


￼


* break & continue

1) These are keywords.
2) These are generally used in loops.
3) break - makes the execution complete exit the loop
break statement in python is used to bring the control out of the loop when some external condition is triggered. break statement is put inside the loop body (generally after if condition).  It terminates the current loop, i.e., the loop in which it appears, and resumes execution at the next statement immediately after the end of that loop. If the break statement is inside a nested loop, the break will terminate the innermost loop.
Loop{
    Condition:
        break
    }
Coding:

for i in range(10):
          print(i)
          if i == 2:
                    break
# output
# 0
# 1
# 2 

4) continue - makes the execution skip the current iteration/repetition only.
Python Continue statement is a loop control statement that forces to execute the next iteration of the loop while skipping the rest of the code inside the loop for the current iteration only, i.e. when the continue statement is executed in the loop, the code inside the loop following the continue statement will be skipped for the current iteration and the next iteration of the loop will begin.
Coding:


for i in range(10):
          if i == 6:
                    continue
          else:
                    print(i, end=" ")
# output

# 0 1 2 3 4 5 7 8 9  

for i in range(10):
          print(i)
          if i == 2:
                    continue
# output        
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

￼



￼

The pass statement is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored. 

Python pass Statement Syntax:

pass

Python pass Statement Example

When the user does not know what code to write, So user simply places pass at that line. Sometimes, pass is used when the user doesn’t want any code to execute. So user can simply place pass where empty code is not allowed, like in loops, function definitions, class definitions, or in if statements. So using pass statement user avoids this error.

Example 1: Pass statement can be used in empty functions
def function:
pass

Example 2: pass statement can also be used in empty class
class geekClass:
pass


Example 3: pass statement can be used in for loop when user doesn’t know what to code inside the loop
n = 10
for i in range(n):
	
# pass can be used as placeholder
# when code is to added later
pass

Example 4: pass statement can be used with conditional statements 
a = 10
b = 20

if(a<b):
pass
else:
print("b<a")

Example 5: lets take another example in which the pass statement get executed when the condition is true 
li =['a', 'b', 'c', 'd']

for i in li:
	if(i =='a'):
		pass
	else:
		print(i)

Output:
b
c
d
