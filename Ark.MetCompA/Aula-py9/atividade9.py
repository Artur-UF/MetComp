import numpy as np
import matplotlib.pyplot as plt


def fac(N):
    fact = 1
    for i in range(1, N+1):
        fact *= i
    return fact


def binomial(n, k):
    try:
        int(n)
        int(k)
        if k == 0:
            return 1
        elif k < 0:
            return print('ERRO: k deve ser > 0')
        else:
            bin = fac(n)/(fac(k)*fac(n-k))
            return bin
    except TypeError:
        return print('Os valores devem ser inteiros')


y = np.array([binomial(100, k) for k in range(20, 80)])
x = np.arange(60)
plt.plot(x, y, 'k')
plt.fill_between(x, y)
plt.show()

