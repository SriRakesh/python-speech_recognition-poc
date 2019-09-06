import matplotlib.pyplot as plt
import numpy as np
import sys
import time

#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
#plt.plot(x, np.sin(x))       # Plot the sine of each x point
#plt.show()

#list = [1,2,3,4,5]
#np_arr = np.array([(1,2,3),(4,5,6)])
#type(np_arr)
#print(np_arr)

#diff between size taken by list and numpy array.
# s = range(1000)
# print(sys.getsizeof(5)*len(s))
# d = np.arange(1000)
# print(d.size*d.itemsize)

# SIZE = 100000
# l1 = range(SIZE)
# l2 = range(SIZE)
# try:
#     n1 = np.arange(SIZE)
#     n2 = np.arange(SIZE)
#     start = time.time()
#     r1 = [(x,y) for x,y in zip(l1,l2)]
#     print(time.time()-start)
#     start = time.time()
#     r2 = n1+n2
#     print(time.time()-start)
# except MemoryError as e:
#     print("Memory is too big")

list = np.array([(1,2,3),(4,5,6)])
print(list.reshape(3,2).shape)