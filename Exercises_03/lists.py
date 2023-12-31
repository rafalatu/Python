"""
By: Rafal
Initial: 19OCT23
Purpose: demonstrate lists
"""

#Test slicing
my_list = [1,2,3,4,5,6,7,8,"A","B","C"]
slice1 = my_list[::-1]
print(slice1)

#Concatenate lists
my_list2 = [11,12,13,14,5,6,7,8,"A","B","C"]
print(my_list + my_list2)

# Nested lists
my_list3 = [[1,2,3], [4,5,6]]
#print(my_list3[0])

#Append lists
my_list.append("D")
print(my_list)
