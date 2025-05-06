#Task5:Numpy basics
import numpy as np

#Create array
arr=np.array([10,20,30,40,50])
print("Array:",arr)

#Array shape and type
print("\nShape:",arr.shape)
print("Data type:",arr.dtype)

#Basic stats
print("\nMean",np.mean(arr))
print("Sum:",np.sum(arr))
print("Standard Deviation:",np.std(arr))

#Elemet wise operations
print("\nArray+5:",arr+5)
print("\nArray Square:",arr**2)

#2D array
matrix=np.array([[1,2],[3,4]])
print("\nMatrix:\n",matrix)

# Matrix operations
print("\nTranspose:\n",matrix.T)
print("matrix multpilied by 2:\n",matrix*2)