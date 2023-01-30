#Python Program to Print the Fibonacci sequence
n=int(input("enter the value of n: "))
a=0
b=1
sum=0
if(n<0):
          print("please enter a positive number")
else:
          for i in range(0,n):
                    print(sum)
                    a=b
                    b=sum
                    sum=a+b