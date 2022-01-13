# Ajuste do circuito RC
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


t, v = np.loadtxt('dados-rc.txt', unpack=True)
logv = np.log(v[1:])
art = np.linspace(0, 1.9)
cof = aj_lin(t[1:], logv)
v0, c = np.exp(cof[1]), 1/(10*cof[0])

vt = lambda tt: cof[0]*tt + cof[1]

texto = f'a = {cof[0]:.3f}\nb = {cof[1]:.3f}\nV={v0:.3f}.exp(-t/R.{-c:.3f})'

plt.scatter(t[1:], logv, s=30, marker='.', c='k')
plt.plot(art, vt(art), 'magenta')
plt.text(1, 1.5, texto, bbox=dict(boxstyle='square', ec='k', color='white'))
plt.grid()
plt.title('Descarga do Capacitor')
plt.xlabel('t(s)')
plt.ylabel('ln(V)')
#plt.show()
plt.savefig('atv_rc.jpeg')
