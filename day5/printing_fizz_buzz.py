# Instructions
# You are going to write a program that 
# automatically prints the solution to the FizzBuzz game.

# Your program should print each number
# from 1 to 100 in turn.

# When the number is divisible by 3 then
# instead of printing the number it should print "Fizz".

# When the number is divisible by 5, 
# then instead of printing the number it should print "Buzz".`

#   And if the number is divisible by both 3 and 5 e.g. 
#   15 then instead of the number it should print "FizzBuzz"

# e.g. it might start off like this:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
#Write your code below this row 👇

for i in range(1,101):
    if(i%5==0 and i%3==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)

# output
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz
# 31
# 32
# Fizz
# 34
# Buzz
# Fizz
# 37
# 38
# Fizz
# Buzz
# 41
# Fizz
# 43
# 44
# FizzBuzz
# 46
# 47
# Fizz
# 49
# Buzz
# Fizz
# 52
# 53
# Fizz
# Buzz
# 56
# Fizz
# 58
# 59
# FizzBuzz
# 61
# 62
# Fizz
# 64
# Buzz
# Fizz
# 67
# 68
# Fizz
# Buzz
# 71
# Fizz
# 73
# 74
# FizzBuzz
# 76
# 77
# Fizz
# 79
# Buzz
# Fizz
# 82
# 83
# Fizz
# Buzz
# 86
# Fizz
# 88
# 89
# FizzBuzz
# 91
# 92
# Fizz
# 94
# Buzz
# Fizz
# 97
# 98
# Fizz
# Buzz
