# Instructions
# You are going to write a program that tests 
# the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for
# the number of times the letters in
# the word TRUE occurs. 

# Then check for the number of times the 
# letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, 
# the message should be:

# "Your score is **x**, you go together
# like coke and mentos."
# For Love Scores between 40 and 50,
# the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. 
# e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name=name1+name2
lower=name.lower()
t=lower.count("t")
r=lower.count("r")
u=lower.count("u")
e=lower.count("e")
true=t+r+u+e
l=lower.count("l")
o=lower.count("o")
v=lower.count("v")
e=lower.count("e")
love=l+o+v+e

love_score = int(str(true)+str(love))
if (love_score<10) or (love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score>=40) and (love_score<=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")