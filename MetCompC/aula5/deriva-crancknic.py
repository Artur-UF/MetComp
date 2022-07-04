import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


def crancknic_deriva(n, k, d):
    # Montando a matriz M
    a = k
    c = -k
    m1 = np.eye(n, k=-1) * a
    m2 = np.eye(n)
    m3 = np.eye(n, k=1) * c
    Mmtz = m1 + m2 + m3

    Mmtz[0][-1] = a
    Mmtz[-1][0] = c

    # Montando a matriz E
    e1 = np.eye(n, k=-1) * c
    e3 = np.eye(n, k=1) * a
    Emtz = e1 + m2 + e3

    Emtz[0][-1] = c
    Emtz[-1][0] = a

    Einv = np.linalg.inv(Emtz)

    fxt = np.dot(Einv, np.dot(Mmtz, d))
    return fxt


xf = 200
dx = 1
tf = 100
dt = .25
k = .4
x = np.arange(0, xf, dx)
n = len(x)

d = st.norm.pdf(x, loc=40, scale=10)

t = np.arange(0, tf, dt)
for ti in t:
    y = crancknic_deriva(n, k, d)
    d = y
    plt.plot(x, d)
    plt.plot(x, d)
    plt.grid()
    plt.title(f'Equação da Deriva\nk = {k} | t = {ti}')
    plt.ylim(-0.02, .05)
    plt.xlim(0, 200)
    plt.pause(.01)
    plt.cla()
