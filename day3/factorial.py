# Python Program to Find the
# Factorial of a Number

fact=1
n=int(input("enter the value of n: "))
for i in range(1,n+1):
          fact=fact*i
print("The factorial of {} is ".format(n),fact)
# output
# enter the value of n: 5
# The factorial of 5 is  120