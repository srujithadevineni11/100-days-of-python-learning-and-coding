#Python Program to Find the Largest Among Three Numbers
# x, y = map(int, input("enter the value: ").split())
# x, y = input("Enter a two value: ").split()
# a,b,c=int(input("enter the value of a: ")),int(input("enter the value of b: ")),int(input("enter the value of c: "))
a,b,c=map(int,input("enter three values : ").split())
if(a>b and a>c):
          print("{} is greater than {} and {}".format(a,b,c))
elif(b>c and c>a):
          print("{} is greater than {} and {}".format(b,c,a))
elif(c>a and c>b):
          print("{} is greater than {} and {}".format(c,b,a))
                    

