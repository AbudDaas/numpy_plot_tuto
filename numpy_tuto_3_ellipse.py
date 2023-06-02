#/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

"""
r**2 = (y-y0)**2+(x-x0)**2

1 = (y-y0)**2/r**2 + (x-x0)**2/r**2
1 = ((y-y0)/r)**2  + ((x-x0)/r)**2

1 = ((y-y0)/a)**2  + ((x-x0)/b)**2
"""

x = np.arange(-10, 11, 0.1)

x0 = 0
y0 = 0
# p0 = (x0, y0)

a = 7
b = 2

# y = y0 + ((a*b)**2 - a**2 * (x-x0))/b**2 
y_pos = y0 + np.sqrt(b**2 * (1 - ((x - x0)**2 / a**2)))
y_neg = -y_pos


plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.xlim(-10, 10)
plt.ylim(-10, 10)

# plt.plot(x, y_neg, color='g')
plt.plot(x, y_pos, color='g')
plt.plot(x, y_neg, color='g')


plt.scatter(x0, y0)

plt.legend(["p0 = (x0 ={}, y0 = {})".format(x0, y0), "radius={}".format(a, b)], loc="lower right")

plt.grid()
plt.show()