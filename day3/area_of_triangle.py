#s=a+b+c/2
#area=rootof(s*s-a*s-b*s-c)
a=int(input("enter the first side of triangle: "))
b=int(input("enter the second side of triangle: "))
c=int(input("enter the third side of triangle: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of tringle = %0.2f "%area)

# output
# enter the first side of triangle: 5
# enter the second side of triangle: 6
# enter the third side of triangle: 7
# Area of tringle = 14.70 