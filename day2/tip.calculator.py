#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("WELCOME TO THE TIP CALCULATOR !")
bill=float(input("What was your total bill? $"))
tip=int(input("How much tip would you like to give ?10,12 or 15 "))
people=int(input("How many people would split the bill ?"))
tip_per=tip/100
tip=bill*tip_per
total=bill+tip
bill_per_person=total/people
final_bill="{:.2f}".format(bill_per_person)
print(f"each person should pay : ${final_bill}")
