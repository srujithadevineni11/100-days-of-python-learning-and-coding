# Iterating over a String
# print("String Iteration")
# s = "srujitha"
# for i in s:
# 	print(i)

# output
# String Iteration
# s
# r
# u
# j
# i
# t
# h
# a

# l = ["srujitha", "devineni", "india"]
# for i in l:
#     print(i)
    
# output
# srujitha
# devineni
# india

# break
for i in range(10):
	print(i)
	if i == 2:
                    break
# output
# 0
# 1
# 2  
       
#continue

for i in range(10):
	if i == 6:
		continue
	else:
		print(i, end=" ")
# output

# 0 1 2 3 4 5 7 8 9    

# for i in range(10):
# 	print(i)
# 	if i == 2:
#                     continue
# output        
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9