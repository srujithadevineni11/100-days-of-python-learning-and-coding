# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# output
# ['apple', 'banana', 'cherry']

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(list1,list2,list3,sep="\n")
# output
# ['apple', 'banana', 'cherry']
# [1, 5, 7, 9, 3]
# [True, False, False]

# list1 = ["abc", 34, True, 40, "male"]
# print(list1)
# output
# ['abc', 34, True, 40, 'male']

# list1 = [["abc", 4, True],[40, "male"]]
# # accessing an element from the
# # Multi-Dimensional List using
# # index number
# print("Accessing a element from a Multi-Dimensional list")
# print(list1[0][1])
# print(list1[1][0])

"""
list1=[1,"sruji",3.8,"adi"]
print(list1[2])#output 3.8 #acsessing the list
print(list1[:2])#output[1, 'sruji'] #slicing the list from end 
print(list1[2:])#output [3.8, 'adi'] slicing the list from start 
print(list1[-2])#output 3.8 #negative index
print(list1[:-1])#output [1, 'sruji', 3.8] #slicing negative index
#Check if Item Exists
if "sruji" in list1:
    print("yes")
if "ai" not in list1:
    print("yes")
#output yes yes

list1[1]="srujitha"#output [1, 'srujitha', 3.8, 'adi'] Change Item Value in list
print(list1)
list1.insert(1,"chandrika")#output [1, 'chandrika', 'srujitha', 3.8, 'adi'] inserting a element in the list in a specified place
print(list1)
list1.append("sada")#output [1, 'chandrika', 'srujitha', 3.8, 'adi', 'sada'] with append we can add a item to the end
print(list1)

list2=[2,"tanya",5.22,"sanj",8] #combing two lists
print(list2)#output [2, 'tanya', 5.22, 'sanj', 8]
list2.extend(list1)
print(list2)#output [2, 'tanya', 5.22, 'sanj', 8, 1, 'chandrika', 'srujitha', 3.8, 'adi', 'sada']

list1.remove("srujitha")#to remove an item from list
print(list1)#output [1, 'chandrika', 3.8, 'adi', 'sada']
del list2 # to delete a list completly
print("length of list")    
print(len(list1))#output 5
for x in list1:#looping in list 
    print(x)
#ouput
# 1
# chandrika
# 3.8
# adi
# sada
list1.clear()
print(list1)#output [] #to clear a lsit
"""