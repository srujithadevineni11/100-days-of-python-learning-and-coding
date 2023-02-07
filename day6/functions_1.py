#function without parameters
# def function():
#           print("Hello ,this is a function")
          
# function()         
   
   
#function with parameters       
# def even_odd(x):
# 	if (x%2==0):
# 		print("even")
# 	else:
# 		print("odd")
         
# even_odd(1)
# even_odd(2)    


# function with default arguments
# def myfun(x, y=50):
# 	print("x: ", x)
# 	print("y: ", y)
# myfun(10)
# output
# x:  10
# y:  50


# def myfun(x=20, y=50):
# 	print("x: ", x)
# 	print("y: ", y)
# myfun(10)
# output
# x:  10
# y:  50


# def myfun(x=20, y=50):
# 	print("x: ", x)
# 	print("y: ", y)
# myfun(10,90)
# output
# x:  10
# y:  90


# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# Output
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil


#keyword arguments
# def student(firstname, lastname):
# 	print(firstname, lastname)
# # Keyword arguments
# student(firstname='Geeks', lastname='Practice')
# student(lastname='Practice', firstname='Geeks')

# def student(firstname,lastname):
#           print(firstname, lastname)
# student(lastname="devineni",firstname="srujitha")
# student(firstname="srujitha",lastname="devineni")
# output
# srujitha devineni


#return statement in function
# def square(num):
# 	"""This function returns the square
# 	value of the entered number"""
# 	return num**2


# print(square(2))
# output
# 4


#pass function in python
# def myrules():
#           pass

# Arbitrary Arguments, *args

# def my_function(*kids):
#           print("The youngest child is ", kids)
# my_function("Emil","Tobias","Linus")
# output
# The youngest child is  ('Emil', 'Tobias', 'Linus')

# def my_function(*kids):
#           print("The youngest child is "+ kids[2])
# my_function("Emil","Tobias","Linus")
# Output
# The youngest child is Linus

# Arbitrary Keyword Arguments, **kwargs
# def my_function(**kid):
#           print("His last name is ", kid)
# my_function(fname ="Tobias",lname ="Refsnes")
# Output
# His last name is  {'fname': 'Tobias', 'lname': 'Refsnes'}

#lambda function

# x=lambda a:a+10
# print(x(5))
# output 15

# x=lambda a,b:a+10
# print(x(5,10))
# output 15

# x=lambda a,b:a+b+10
# print(x(5,10))
# output 25

# x=lambda a,b:a+10,b+10
# print(x(5,10))
# output gives an error as only one expression should be used

# calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
# print(calc(20))
# Output Even number

