#Qestion1 Answer:
import numpy as np
A = np.array([range(i, i+2) for i in [1, 4, 7]])
print(A)
print('\n')
B = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
print(B)
print('\n')
#Attributes of the The Array A
print('The Dimension of The Array A is:', A.ndim)
print('THE Shape of The Array A is:', A.shape)
print('THE Size of The Array A is:', A.size)
print('The Type of The Array A is of:', A.dtype.name)
print('The ItemSize of Array A is:', A.itemsize)
print('\n')
#Attribututes of Array B
print('The Dimension of The Array B is:', B.ndim)
print('THE Shape of The Array B is:', B.shape)
print('THE Size of The Array B is:', B.size)
print('The Type of The Array B is of:', B.dtype.name)
print('The ItemSize of Array B is:',B.itemsize)
#Resultant of Sum A+B
#By Applying The Rule of Broadcasting
#By Broadcasting Rule
#Rule 1 is Satisfied
#Rule 2 Will cause an error because their shape is not match
#A will have shape of (3, 2) and B will have shape of (3, 3)
#Since A doesnot have 1 which cannot be strechable it will raise an Error
print(A+B)