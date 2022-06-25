import copy
import numpy as np
import matplotlib.pyplot as plt


def thomas(aa, bb, cc, dd):
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


k = .4
dx = 1
dt = .25
xf = 100
tf = [5, 50, 500, 1000, 2000]
x = np.arange(0, xf, dx)


a = np.ones(len(x)) * (-k)
c = np.ones(len(x)) * (-k)
b = np.ones(len(x)) * (1 + (2 * k))
d = np.zeros(len(x))
d[int(len(d) / 4):int((3 * len(d)) / 4)] = 1.

for time in tf:
    t = np.arange(0, time, dt)
    for ti in t:
        y = thomas(a, b, c, d)
        d = y
    plt.plot(x, d, label=f't = {time}')

plt.grid()
plt.legend()
plt.title('Algoritmo de Thomas')
plt.ylabel('f(x, t)')
plt.xlabel('x')
plt.savefig('thomas.png')



