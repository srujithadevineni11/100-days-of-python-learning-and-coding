# Logical Operators
# Logical operators perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.

# Operator	Description	                                Syntax
# and	Logical AND: True if both the operands are true	  x and y
# or	Logical OR: True if either of the operands is true  x or y
# not	Logical NOT: True if the operand is false 	  not x


n1=int(input("enter a number: "))
n2=int(input("enter a number: "))
print(n1 and n2)
print(n1 or n2)
print(not n2)
# output
# enter a number: 12
# enter a number: 13
# 13
# 12
# False