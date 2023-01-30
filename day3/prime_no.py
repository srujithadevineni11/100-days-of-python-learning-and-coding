#Python Program to Check Prime Number
count=0
n=int(input("enter the value of n: "))
for i in range(1,n+1):
          if(n%i)==0:
                    count=count+1
if(count==2):
          print("{} is a prime number".format(n))
else:
          print("{} is not a prime number".format(n))
          
                    