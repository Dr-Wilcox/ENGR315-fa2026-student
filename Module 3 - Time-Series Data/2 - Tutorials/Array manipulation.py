import numpy

# Fill in the brackets to make a 2x2 identity matrix
iden_array = numpy.array([[None,None],[None,None]])

# This checks to see if it is correct
if iden_array[0,0] == iden_array[1,1] == 1 and iden_array[1,0] == iden_array[0,1] == 0:
    print('Correct! The 2x2 identity matrix in array form is:')
    print(iden_array)
else:
    print('Something is wrong, array is:')
    print(iden_array)


# Now, create an array for the following matrix:
"""
[11 12 13]
[21 22 23]
[31 32 33]
"""

new_array = None
print('The new array is:')
print(new_array)

# Now, access or slice this array to create the following:
"""
#1: 22 (middle element of array)      #2:  [13 23 33]       #3: [11  12]       

#4:[[21 22]
    [31 32]]

"""

slice_1 = None
print(slice_1)

slice_2 = None
print(slice_2)

slice_3 = None
print(slice_3)

slice_4 = None
print(slice_4)

# Check the terminal output to verify your work

