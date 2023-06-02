#/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

"""
r**2 = (y-y0)**2+(x-x0)**2

1 = (y-y0)**2/r**2 + (x-x0)**2/r**2
1 = ((y-y0)/r)**2  + ((x-x0)/r)**2

1 = ((y-y0)/a)**2  + ((x-x0)/b)**2
y = a(x-h)**2 + k 
"""

x = np.arange(-10, 11, 0.1)

x0 = 0
y0 = 0
# p0 = (x0, y0)

a = 1
b = 3

# a*x**2+b*x*y+c*y**2+d*x+e*y+f=0
y_pos = y0 + np.sqrt(4*a*(x-x0))
y_neg = - y_pos

x_pos = x0 + np.sqrt(-4*a*(x-x0))
x_neg = -x_pos

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.xlim(-20, 20)
plt.ylim(-20, 20)

plt.plot(x, y_pos, color='g')
plt.plot(x, y_neg, color='g')
plt.plot(x, x_pos, color='g')
plt.plot(x, x_neg, color='g')

plt.scatter(x0, y0)

plt.legend(["p0 = (x0 ={}, y0 = {})".format(x0, y0), "radius={}".format(a, b)], loc="lower right")

plt.grid()
plt.show()