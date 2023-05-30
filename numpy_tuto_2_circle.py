#/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

"""
# Circle
p0(x0, y0); r ==> 
p(x, y): distance(p, p0) = r

r**2 = (y-y0)**2+(x-x0)**2
"""

x = np.arange(-10, 11, 0.1)

x0 = 0
y0 = 0
# p0 = (x0, y0)

r = 5

y_pos = np.sqrt(r**2 - (x-x0)**2) + y0 
y_neg = - y_pos

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.xlim(-6, 6)
plt.ylim(-6, 6)

plt.plot(x, y_pos, color='g')
plt.plot(x, y_neg, color='g')

plt.scatter(x0, y0)

plt.legend(["p0 = (x0 ={}, y0 = {})".format(x0, y0), "radius={}".format(r)], loc="lower right")

plt.grid()
plt.show()