import random

#randint(to print integer values)
# value=random.randint(1,10)
# print(value)
# Output:-
# 1

#random(to print floating point values btw 0 and 1)
# value=random.random()
# print(value)
# Output:-
# 0.3632932841059614

#uniform(to print floating point values btw to given numbers)
# value=random.uniform(1,10)
# print(value)#5.870309908469984
# print("%.2f"%value)#5.87

#choice(selecting random elements from a list or a string)
# greetings=['hello','hi','hey','howdy','hola']
# value=random.choice(greetings)
# print(value + ', srujitha!')
# Output:-
# Hello, srujitha!

# string="srujitha"
# value=random.choice(string)
# print(value)
# output
# r

import random
sample_list = [1, 2, 3, 4, 5]
print("Original list : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)

# output
# Original list : 
# [1, 2, 3, 4, 5]

# After the first shuffle : 
# [3, 5, 1, 2, 4]

# After the second shuffle : 
# [1, 2, 5, 3, 4]
