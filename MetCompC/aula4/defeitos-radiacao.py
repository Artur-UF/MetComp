import copy

import numpy as np
import matplotlib.pyplot as plt


def ftcs(x, dt, tf, S, s):
    ftemp = np.zeros(len(x))
    fxt = np.zeros(len(x))

    for t in np.arange(dt, tf, dt):
        for i in range(1, len(x)-1):
            ftemp[i] = fxt[i] + dt * ((fxt[i+1] + fxt[i-1] - 2 * fxt[i]) - S * fxt[i] + s[i])
        for j in range(1, len(x)-1):
            fxt[j] = ftemp[j]
    return x, fxt


def ftcs_mtz(n, k, S, s, d):
    # Montando a matriz
    a = k
    b = 1 - (k * (2 + S))
    c = k
    m1 = np.eye(n, k=-1) * a
    m2 = np.eye(n) * b
    m3 = np.eye(n, k=1) * c
    mtz = m1 + m2 + m3

    # Arrumando a matriz
    mtz[0][1], mtz[-1][-2], mtz[0][0], mtz[-1][-1] = 0., 0., 1., 1.

    fxt = np.dot(mtz, d) + (k * s)
    return fxt


x0 = 100
xf = 400
dx = 1
dt = .25
S = .002
tempos = [5, 50, 500, 5000]
sigma = 10.
s0 = 10.
k = .4

x = np.arange(0, xf+dx, dx)

s = s0 * np.exp(-((x - x0)**2)/(sigma**2))

fi = np.zeros(len(x))
for tf in tempos:
    t = np.arange(0, tf, dt)
    for ti in t:
        y = ftcs_mtz(len(x), k, S, s, fi)
        fi = copy.deepcopy(y)
    plt.plot(x, fi, linewidth=1, label=f't = {tf}')
plt.plot(x, s, 'orange', label='Fonte')
plt.grid()
plt.legend()
plt.savefig('radiacao.png')
#plt.show()

