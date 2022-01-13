# Ajuste de funções
import numpy as np
import matplotlib.pyplot as plt


def aj_lin(xi, yi):
    '''
    Realiza o ajuste linear de pontos em uma reta de ajuste no formato "y = ax + b"
    :param xi: coordenadas x dos pontos
    :param yi: coordenadas y dos pontos
    :return: coeficiente angular "a" e coeficiente linear "b" da reta de ajuste
    '''
    n = len(xi)
    mxy = sum(xi*yi)/n
    mx = sum(xi)/n
    my = sum(yi)/n
    mqx = sum(xi**2)/n
    a = (mxy - (mx*my))/(mqx - (mx**2))
    b = ((mqx*my) - (mx*mxy))/(mqx - (mx**2))
    return a, b


x, y = np.loadtxt('dados.dat', unpack=True)

xi = np.linspace(0, 9.50)
pars = aj_lin(x, y)
yi = lambda p: pars[0]*p + pars[1]

plt.scatter(x, y, s=30, c='k', marker='.', label='Pontos')
plt.plot(xi, yi(xi), 'g', label='Reta de ajuste')
plt.xlim(0, 9.5)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

