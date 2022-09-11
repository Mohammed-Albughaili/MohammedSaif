import numpy as np

array1 = np.zeros(25)
array2 = np.ones(8)
array3 = np.arange(25)
array4 = np.array([1,2,3,4,5,6,7,8,9])
array5 = np.random.rand(6,5)


print(array1)
print(array2)
print(array3)
print(array4)
print(array5)


print(array5.transpose())
print(array5.shape)

print(array4.sum())
print(array4.min())
print(array4.max())

array6 = array3 - 2
print(array6)
print(array6.shape)
array7 = array5 * 3
print(array7)
print(array7.shape)
