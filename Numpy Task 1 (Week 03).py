import numpy as np

array = np.array([0,1,2,3,4,5,6,7,8,9])

print(array)

array_2 = np.array([1,1,1,1,1,1,1,1,1])
three_three_Array = array_2.reshape(3,3)
print(three_three_Array)

array_3 = np.arange(1,11,2)

print(array_3)

array_4 = np.arange(1, 11, 1)  
 
array_4[array_4%2==1] = -1    

print(array_4)

array_5 = np.reshape(array,(2,5))
print(array_5)

a = np.arange(1,6,1)
b = np.arange(6,11,1)
c = np.dot(a,b)
d = np.sum(c,axis = 0 )
print(d)