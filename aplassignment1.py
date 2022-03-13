# SUDEM S DAIMARI(CSI21014)
# PAHAR SWRANG BARGAYARY(CSE210)
"""
#Qestion1.1 Answer:
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
#Rule 1 is Satisfied Since bothe array have the same dimension
#Rule 2 Will cause an error because their shape is not match
#A will have shape of (3, 2) and B will have shape of (3, 3)
#Since A doesnot have 1 which cannot be strechable it will raise an Error
print(A+B)


#Question1.2 Answer:
import numpy as np
A = np.arange(1, 10).reshape(3, 3)
print(A)
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
print('\n')
#Resultant of Sum A+B
#By Applying The Rule of Broadcasting(we dont actually need Brodcasting here since its Dimension and Shapes are similar)
#By Broadcasting Rule
#Rule1 is Satisfied Since both are 2D array
#Rule2 is satisfied since bothe have the shape of (3, 3)
#We can find the A+B now
result = (A+B)
print(result)
#Attributes of the The Sum
print('The Dimension of The Array A+B is:',result.ndim)
print('THE Shape of The Array A+B  is:', result.shape)
print('THE Size of The Array A+B  is:', result.size)
print('The Type of The Array A+B  is of:', result.dtype.name)
print('The ItemSize of Array A+B  is:', result.itemsize)

#Question2 Answer:
import numpy as np
arr = np.array([1, 2 , 3])
repetitions = 2
A = np.tile(arr, (repetitions, 1))
print(A)
#Attributes of the The Array A
print('The Dimension of The Array A is:', A.ndim)
print('THE Shape of The Array A is:', A.shape)
print('THE Size of The Array A is:', A.size)
print('The Type of The Array A is of:', A.dtype.name)
print('The ItemSize of Array A is:', A.itemsize)
print('\n')
B = np.array([[0, 2], [1, -1], [1, 1]])
print(B)
#Attribututes of Array B
print('The Dimension of The Array B is:', B.ndim)
print('THE Shape of The Array B is:', B.shape)
print('THE Size of The Array B is:', B.size)
print('The Type of The Array B is of:', B.dtype.name)
print('The ItemSize of Array B is:',B.itemsize)
print('\n')
result = np.dot(A, B)
print(result)
print('The Dimension of The Result is:', result.ndim)
print('The Shape of The Result is:', result.shape)
print('The Type of The Result is:', result.dtype)
print('THE Size of The Result is:', result.size)
print('The ItemSize of Result is:',B.itemsize)
print('\n')
result = np.dot(B, A)
print(result)
print('The Dimension of The Result is:', result.ndim)
print('The Shape of The Result is:', result.shape)
print('The Type of The Result is:', result.dtype)
print('THE Size of The Result is:', result.size)
print('The ItemSize of Result is:',B.itemsize)
print('\n')
#AB != BA
"""
#Question3
import numpy as np
arr = [1, 2, 1, 4, 4, 5, 6, 7, 7]
A = np.reshape(arr, (3,3))
print(A)
#Attributes of the The Array A
print('The Dimension of The Array A is:', A.ndim)
print('THE Shape of The Array A is:', A.shape)
print('THE Size of The Array A is:', A.size)
print('The Type of The Array A is of:', A.dtype.name)
print('The ItemSize of Array A is:', A.itemsize)
print('\n')
arr1 = [-7, -7, 6, 2, 1, -1, 4, 5, -4]
B = np.reshape(arr1, (3,3))
print(B)
#Attribututes of Array B
print('The Dimension of The Array B is:', B.ndim)
print('THE Shape of The Array B is:', B.shape)
print('THE Size of The Array B is:', B.size)
print('The Type of The Array B is of:', B.dtype.name)
print('The ItemSize of Array B is:',B.itemsize)
print('\n')

#Inverse
print(np.linalg.inv(A))
print(np.linalg.inv(B))
#A and B are Inverse to each Other
print('\n')

print(A*B)
print(B*A)
#for IDENTIYTY If AB= BA = I
A=np.identity(A,(3))
print(A)
print('\n')
B=np.identity(A,(3))
print(B)
