# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
print("Welcome To My Password Generator")
lower_case=int(input("How many Lower Case Letters you want: \n"))
upper_case=int(input("How many upper Case Letters you want: \n"))
symbols= int(input("How many symbols would you like?\n"))
numbers= int(input("How many numbers would you like?\n"))
if_upper_case=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if_lower_case=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if_symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
if_numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password=" "
for i in range(1,lower_case+1):
    #if we just write 1 to lowercase then if we want 4 lowercase letters we will get only 3 letters because the range function does not include the last value into the result so we should add 1 to get appropriate result 
    password+=random.choice(if_lower_case)
for i in range(1,upper_case+1):
    password+=random.choice(if_upper_case)
for i in range(1,symbols+1):
    password+=random.choice(if_symbols)
for i in range(1,numbers+1):
    password+=random.choice(if_numbers)
print("Here Is Your Password: ",password)


# output

# Welcome To My Password Generator
# How many Lower Case Letters you want: 
# 7
# How many upper Case Letters you want: 
# 7
# How many symbols would you like?
# 4
# How many numbers would you like?
# 3
# Here Is Your Password:   mcacanwSKFZTEF!()$836
