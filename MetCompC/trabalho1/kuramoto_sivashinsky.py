import numpy as np
import matplotlib.pyplot as plt
from random import uniform


def KS_eq(l, dx, tf, dt, fxt):
    x = np.arange(0, l, dx)
    d2 = dt/(dx**2)
    d4 = dt/(dx**4)
    c = 0
    for t in np.arange(0, tf, dt):
        c += 1
        for i in range(len(x)):
            j = i - 2
            fxt[j] = (d4 * fxt[j - 2]) + ((-d2 + 4 * d4) * fxt[j-1]) + ((1 + 2 * d2 - 6 * d4) * fxt[j]) + \
                     ((-d2 + 4 * d4) * fxt[j+1]) + (-d4 * fxt[j+2]) - ((fxt[j+1] - fxt[j-1])**2)/(8 * dx**4)

        plt.plot(x, fxt)
        plt.grid()
        plt.xlim(0, l)
        #plt.ylim(-.2, .2)
        plt.title(f'Kuramoto-Sivashinsky\ncont = {c:>3} | t = {t:>5.1f}')
        plt.pause(.01)
        plt.cla()


l = 50
dx = 1
tf = 20
dt = 0.01

x = np.arange(0, l, dx)

#fxt = list(uniform(-.001, .001) for xi in x)
#fxt = np.zeros(len(x))
fxt = np.sin(x) * 0.01

KS_eq(l, dx, tf, dt, fxt)
