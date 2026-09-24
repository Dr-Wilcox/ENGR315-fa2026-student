# create a new list of integers
new_list = [2, 3, 4, 5, 6]
print('Length of List is: '+str(len(new_list)))

# create a list of integers, floats, and strings
mixed_list = [2, 3.14159, 'Cats', 'Rain', -1]

# print out all the element types in this list
for element in mixed_list:
    print(type(element))

# create an empty list. Two methods,
empty_list = list()

# append several elements
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
empty_list.append(4)

# print out contents
print(empty_list)

# Add the elements of another list to my list?
list_A = [1, 2, 3, 4]
list_B = [5, 6, 7, 8, 9]
list_A.append(list_B)

# print list contents and length
print(list_A)
print('Length of List is: '+str(len(list_A)))

