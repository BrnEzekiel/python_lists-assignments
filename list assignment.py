#creating an empty list

my_list = []

#adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)          
my_list.append(40)

#inserting an element (15) at second position (index 1)
my_list.insert(1, 15)
print("List after insertion:", my_list)

#extending my_list with another elements
my_list.extend([50, 60, 70])
print("List after extension:", my_list)

#removing the last element
my_list.pop()
print("List after popping last element:", my_list)

#sorting my_list in ascending order
my_list.sort()
print("List after sorting:", my_list)

#locating and printing the index of element 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)