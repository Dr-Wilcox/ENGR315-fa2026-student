import numpy as np

# generate a random array. Max value is 10, length is 5
a = np.random.randint(10, size=5)

# generate a random array. Max value is 10, length is 5
b = np.random.randint(10, size=5)

# add the two arrays, piece-wise
c = a + b

# square each element of the array
squares = a ** 2

# square each element and then add piece-wise
added_squares = a ** 2 + b ** 2

# sum the resulting array to a single value
num = sum(added_squares)

########################################################
# generate a random array. Max value is 10, length is 3
c = np.random.randint(10, size=3)
print('First vector is:',c)

# generate a random array. Max value is 10, length is 3
d = np.random.randint(10, size=3)
print('Second vector is:',d)

# take the cross product of the two arrays as if they are vectors
cross_product = np.cross(c,d)
print('Cross product is: ', cross_product)

# take the dot product of the two arrays as if they are vectors
dot_product = np.dot(c,d)
print('Dot product is: ', dot_product)

########################################################
# matrix multiplication
new_array1 = np.array([[1,2],[3,4]])
new_array2 = np.array([[0,1],[2,2]])

matrix_multiplication = np.matmul(new_array1,new_array2)

print('First matrix is:')
print(new_array1)
print('Second matrix is:')
print(new_array2)
print('These two matrices multiplied equal:')
print(matrix_multiplication)

