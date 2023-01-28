# Comparison of Relational operators compares the values. 
# It either returns True or False according to the condition.
# Operator	Description	                                                            Syntax
# >	Greater than: True if the left operand is greater than the right	                    x > y
# <	Less than: True if the left operand is less than the right                      	x < y
# ==	Equal to: True if both operands are equal	                                        x == y
# !=	Not equal to – True if operands are not equal	                                        x != y
# >=	Greater than or equal to True if the left operand is greater than or equal to the right	x >= y
# <=	Less than or equal to True if the left operand is less than or equal to the right	x <= y
# is 	x is the same as y	                                                                      x is y
# is not	x is not the same as y	                                                            x is not y

n1=int(input("enter a number: "))
n2=int(input("enter a number: "))
# output will be in boolean form it is either true or false

print(n1>n2)
print(n1<n2)
print(n1==n2)
print(n1!=n2)
print(n1>=n2)
print(n2>=n1)
print(n1<=n2)
print(n2<=n1)
# output
# enter a number: 12
# enter a number: 14
# False
# True
# False
# True
# False
# True
# True
# False