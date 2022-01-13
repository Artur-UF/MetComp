# Polinômios de Lagrange
import numpy as np
import matplotlib.pyplot as plt


def interpol(x, y, xx):
    px = 0
    for xi, yi in zip(x, y):
        li = 1
        for xj in x:
            if xi != xj:
                lx = (xx-xj)/(xi-xj)
                li *= lx
        px += yi*li
    return px


x = np.array([-8.8, -2.3, 2.7, 1.4, 5.1])
y = np.array([12.6, 6.2, 8.4, -14.9, 18.8])
xx = np.linspace(-10, 10, 100)
yy = interpol(x, y, xx)

plt.plot(xx, yy)
plt.ylim()
plt.show()
