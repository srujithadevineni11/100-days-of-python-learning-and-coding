# Identity Operators
# is and is not are the identity operators 
# both are used to check if two values are
# located on the same part of the memory.
# Two variables that are equal do not imply 
# that they are identical. 

# is          True if the operands are identical 
# is not      True if the operands are not identical 


n1=int(input("enter a number: "))
n2=int(input("enter a number: "))
print(n1 is n2)
print(n1 is not n2)
# output
# enter a number: 12
# enter a number: 12
# True
# False