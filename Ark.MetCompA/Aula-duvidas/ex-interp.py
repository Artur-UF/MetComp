# Exercício de interpolação
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate


def al_neville(x, p):
    '''Faz a interpolação dos pontos p em x.
    x: array com valores em x a serem calculados
    p: array bidimensional com os pontos a serem interpolados no formato [x, y]
    return: array com os valores em y calculados com a função e os pontos em x
    '''
    n = p.shape[0]
    m0 = np.zeros((n, n))
    m0[:, 0] = p[:, 1]
    y = []
    for xv in x:
        for j in range(1, n):
            for i in range(n-j):
                m0[i, j] = ((xv - p[i+j, 0])*m0[i, j-1] - (xv - p[i, 0])*m0[i+1, j-1])/(p[i, 0] - p[i+j, 0])
        y.append(m0[0, n-1])
    return y


x, y = np.loadtxt('interp.txt', unpack=True)

p = np.vstack((x, y)).T

xi = np.linspace(0, 5)
yi = al_neville(xi, p)
yii = scipy.interpolate.lagrange(x, y)

plt.scatter(x, y)
plt.plot(xi, yii(xi), 'k')
plt.plot(xi, yi)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
