import matplotlib.pyplot as plt
import numpy as np


x0 = 0
xf = 100
D = 2.2
dx = 1
dt = .25
tf = 1000
k = 0.4
x = list(np.arange(x0, xf+dx, dx))
ftemp = np.zeros(len(x))
ftemp[0] = 1.
fxt = np.zeros(len(x))
fxt[0] = 1.
for t in np.arange(dt, tf, dt):
    for i in range(1, len(x)-1):
        ftemp[i] = fxt[i] + k * (fxt[i-1] - 2 * fxt[i] + fxt[i+1])
    for j in range(1, len(x)-1):
        fxt[j] = ftemp[j]
    plt.scatter(x, fxt, marker='.', color='k')
    plt.title(f'Tempo: {t}')
    plt.pause(.001)
    plt.clf()
