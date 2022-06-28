import copy
import numpy as np
import matplotlib.pyplot as plt


def thomasexp(k, s, dd):
    # Criação dos arrays
    aa = np.ones(s) * k
    cc = np.ones(s) * k
    bb = np.ones(s) * (2 - (2 * k))

    # Corte dos arrays
    a = copy.deepcopy(aa[1:-1])
    b = copy.deepcopy(bb[1:-1])
    c = copy.deepcopy(cc[1:-1])
    d = copy.deepcopy(dd[1:-1])
    a[0] = 0
    c[-1] = 0

    n = len(d)
    # Trata os casos das primeiras linhas
    c[0] /= b[0]
    d[0] /= b[0]

    # Fazendo a substituição no resto das linhas
    for i in range(1, n):
        ptemp = b[i] - (a[i] * c[i - 1])
        c[i] /= ptemp
        d[i] = (d[i] - (a[i] * d[i - 1])) / ptemp

    # Atribuindo valor aos x em ordem inversa
    x = np.zeros(n)
    x[-1] = d[-1]
    for i in range(-2, -n - 1, -1):
        x[i] = d[i] - (c[i] * x[i + 1])

    x = np.append(x, dd[-1])
    x = np.append(dd[0], x)
    return x


def cranknic(k, s, dd):
    # Realiza o processo explícito
    d2 = thomasexp(k, s, dd)

    # Criação dos arrays
    aa = np.ones(s) * (-k)
    cc = np.ones(s) * (-k)
    bb = np.ones(s) * (2 + (2 * k))

    a = copy.deepcopy(aa[1:-1])
    b = copy.deepcopy(bb[1:-1])
    c = copy.deepcopy(cc[1:-1])
    d = copy.deepcopy(d2[1:-1])
    a[0] = 0
    c[-1] = 0

    n = len(d)
    # Trata os casos das primeiras linhas
    c[0] /= b[0]
    d[0] /= b[0]

    # Fazendo a substituição no resto das linhas
    for i in range(1, n):
        ptemp = b[i] - (a[i] * c[i - 1])
        c[i] /= ptemp
        d[i] = (d[i] - (a[i] * d[i - 1])) / ptemp

    # Atribuindo valor aos x em ordem inversa
    x = np.zeros(n)
    x[-1] = d[-1]
    for i in range(-2, -n - 1, -1):
        x[i] = d[i] - (c[i] * x[i + 1])

    x = np.append(x, dd[-1])
    x = np.append(dd[0], x)
    return x


dx = 1
dt = .25
xf = 10
tf = .5 # [0, 50, 500, 1000, 2000]
k = .4
x = np.arange(0, xf, dx)

d = np.zeros(len(x))
# Condição inicial
d[int(len(d) / 4):int((3 * len(d)) / 4)] = 1.

#for time in tf:
t = np.arange(0, tf, dt)
for ti in t:
    y = cranknic(k, len(x), d)
    d = y
plt.plot(x, d, label=f't = {tf}')
plt.grid()
plt.legend()
plt.title(f'Crank-Nicolson\nk = {k}')
plt.ylim(-0.1, 1.1)
plt.show()
