# Bitwise operators act on bits
# and perform the bit-by-bit 
# operations. 
# These are used to operate on 
# binary numbers.

# Operator	Description	Syntax
# &	Bitwise AND	x & y
# |	Bitwise OR	x | y
# ~	Bitwise NOT	~x
# ^	Bitwise XOR	x ^ y
# >>	Bitwise right shift	x>>
# <<	Bitwise left shift	x<<


a=int(input("enter a number: "))
b=int(input("enter a number: "))

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
# output
# enter a number: 5
# enter a number: 11
# 1
# 15
# -6
# 14
# 1
# 20