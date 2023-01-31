# import random

# list1=[1,2,3,4,5]
# print(random.choice(list1))

# output
# 5

# import random
# value=random.randint(1,10)
# print(value)

# Output:-
# 1

# import random

# import random
# value=random.random()
# print(value)

# Output:-
# 1.4668973



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