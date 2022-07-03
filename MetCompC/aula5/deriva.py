import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


def ftcs_mtz(n, u, d):
    # Montando a matriz
    a = -u/2
    c = u/2
    m1 = np.eye(n, k=-1) * a
    m2 = np.eye(n)
    m3 = np.eye(n, k=1) * c
    mtz = m1 + m2 + m3

    # Arrumando a matriz
    mtz[0][-1] = a
    mtz[-1][0] = c

    M = np.linalg.inv(mtz)

    fxt = np.dot(M, d)
    return fxt


xf = 100
dx = 1
tf = 100
dt = .25
u = .4
x = np.arange(0, xf, dx)
n = len(x)

d = st.norm.pdf(x, loc=40, scale=5)

t = np.arange(0, tf, dt)
for ti in t:
    y = ftcs_mtz(n, u, d)
    d = y
    plt.plot(x, d)
    plt.plot(x, d)
    plt.grid()
    plt.title(f'Equação da Deriva\nt = {ti}')
    plt.ylim(0, .12)
    plt.xlim(0, 100)
    plt.pause(.01)
    plt.cla()
