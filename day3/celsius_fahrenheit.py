#Python Program to Convert Celsius To Fahrenheit
#(f-32)*5/9=c
c=float(input("enter the value in celsius :"))
f=(c*1.8)+32
print('%0.1f degrees celsius is equal to %0.1f degrees fahrenheit'%(c,f))
c=(f-32)/1.8
print(f,"degrees faherenheit is equal to ",c,"degrees celsius")