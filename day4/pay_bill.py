# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
length=len(names)
bill=random.randint(0,length-1)
bill_pay=names[bill]
print(f"{bill_pay} is going to buy the meal today!")
