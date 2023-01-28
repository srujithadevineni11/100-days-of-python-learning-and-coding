# reate a program using maths and
# f-Strings that tells us how many days,
# weeks, months we have left if we live
# until 90 years old.

# It will take your current age as the input
# and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual 
# calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remaining_age=90-age
x=365*remaining_age
y=52*remaining_age
z=12*remaining_age
print(f"You have {x} days, {y} weeks,and {z} months left.")

