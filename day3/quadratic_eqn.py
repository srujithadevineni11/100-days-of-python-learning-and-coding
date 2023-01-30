#Python Program to Solve Quadratic Equation
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
print("The quadratic equation is {}x^2+{}x+{}=0".format(a,b,c))
discriminent=(b*b)-(4*a*c)
print(discriminent)
if discriminent>0:
    root1=((-b)+(discriminent)**0.5)/(2*a)
    root2=((-b)-(discriminent)**0.5)/(2*a)
    print("There are 2 distinct real roots ",(root1,root2))
elif discriminent==0:
    root=-b/(2*a)
    print("There is exactly 1 root",root)
else:
     print("Complex Roots") 
     real=-b/(2*a)
     imaginary=((discriminent)**0.5)
     print(real ,"+ i",imaginary)
     print(real ,"- i",imaginary)