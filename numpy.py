import numpy as np
import time
import sys

a= np.array([1,2,3])
print(a)
print(a[0])
print(a[1])


#less memory, fast, convinient

l=range(1000)
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size * array.itemsize)


l
