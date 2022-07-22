import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from random import uniform


def swifthoh(r, tf, dt, dx, l, fxt):
    x = np.arange(0, l, dx)

    for t in np.arange(0, tf, dt):
        for j in range(len(x)):
            i = j - 2
            fxt[i] = (-(dt) / (dx ** 4)) * fxt[i - 2] + ((-2 * dt) / (dx ** 2) + (4 * dt) / (dx ** 4)) * fxt[i - 1] + (
                        dt * (r - 1) + (4 * dt) / (dx ** 2) - (6 * dt) / (dx ** 4) + 1) * fxt[i] + (
                                 (-2 * dt) / (dx ** 2) + (4 * dt) / (dx ** 4)) * fxt[i + 1] + ((-dt) / (dx ** 4)) * fxt[
                         i + 2] - (dt * fxt[i] ** 3)
        plt.plot(x, fxt)
        plt.grid()
        plt.xlim(0, l)
        plt.ylim(-.2, .2)
        plt.title(f'Swift-Hohenbreg\nr = {r} | t = {t:>5.1f}')
        plt.pause(.01)
        plt.cla()


r = 0.01
tf = 30
dt = .1
dx = 1
l = 100

x = np.arange(l)
# fxt = st.norm.pdf(x, loc=50, scale=5)

fxt = list(uniform(-.1, .1) for xi in x)

swifthoh(r, tf, dt, dx, l, fxt)
