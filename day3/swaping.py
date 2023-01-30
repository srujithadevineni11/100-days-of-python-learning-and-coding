#Python Program to Swap Two Variables
a=int(input("enter any value: "))
b=int(input("enter any value: "))
print("Before swapping the numbers are :",a,b)
(a,b)=(b,a)
#above and below both codes gives same answer
# t=a
# a=b
# b=t
print("After swapping the numbers are :",a,b)

# output
# enter any value: 12
# enter any value: 14
# Before swapping the numbers are : 12 14
# After swapping the numbers are : 14 12