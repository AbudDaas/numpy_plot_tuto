#/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

class TestNumPy:
    def __init__(self):
        pass

    def createZerosArr(self, size):
        """
        Function createZerosArr, to create zeros array.
        ---
        @param: size, tuple, the size of the array
        @return: nd-array, zeros numpy array with input size... 
        """
        return np.zeros(size)
    
    def createOnesArr(self, size):
        """
        Function createOnesArr, to create ones array.
        ---
        @param: size, tuple, the size of the array
        @return: nd-array, ones numpy array with input size... 
        """
        return np.ones(size)
    
    def createEye(self, dim):
        """
        """
        return np.eye(dim)
        
    def visualize(self, arr):
        """
        """
        plt.imshow(arr, cmap='gray')


# test_numpy_ = TestNumPy()

# siz_ =(5, 2)

# arr0 = test_numpy_.createZerosArr(siz_)
# arr1 = test_numpy_.createOnesArr(siz_)


# d = 7
# eye = test_numpy_.createEye(d)
# # print(arr0, "\n=============\n", arr1)

# test_numpy_.visualize(eye)
# plt.show()

##-------------------------------------------
# y = a * x + b ## a,b constants
# (y - y0) = m * (x - x0) ## x0, y0, m constants
"""
(y - b) = a * x

y - y0 = m * x - m * x0
y - y0 - m * x0 = m * x
y - (y0 + m * x0) = m * x

b = (y0 + m * x0)
a = m

y = m * (x - x0) + y0
"""
x_ = np.arange(0, 10)
a = 2
b = 2
y_ = a * x_ + b

##-----------------------------

m = 2
x0 = 2
y0 = 2

x1 = np.arange(0, 10)
y1 = m * (x1 - x0) + y0

plt.figure()

plt.subplot(121)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.xlim(0, 25)
plt.ylim(0, 25)

plt.plot(2.5 * x_, 2.5 * x_, color = 'r', alpha=0.1)
plt.plot(x_, y_)
# plt.show()

plt.legend(["a={}".format(a), "b={}".format(b)])
##---------
plt.subplot(122)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.xlim(0, 25)
plt.ylim(0, 25)

plt.plot(2.5 * x_, 2.5 * x_, color = 'y', alpha=0.1)
plt.plot(x1, y1, color='g')

plt.legend(["p0 = (x0 ={}, y0 = {})".format(x0, y0), "slope={}".format(m)])
##------------

plt.show()