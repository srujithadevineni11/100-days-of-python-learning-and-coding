# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column=int(position[0])
row=int(position[1])
# row_hold=map[row-1]
# row_hold[column-1]="X"
map[row-1][column-1]="X"
# place="x"

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
# output
# ['⬜️', '️⬜️', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', '⬜️️', '⬜️']
# Where do you want to put the treasure? 23
# ['⬜️', '️⬜️', '️⬜️']
# ['⬜️', '⬜️', '️⬜️']
# ['⬜️️', 'X', '⬜️']
