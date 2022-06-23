'''
Suponhamos que há uma quantidade finita de material que se difunde
em 1D. No instante t = 0, ele se encontra todo entre x = L/4 e
x = 3 L/4, isto é, f(x = L/4..3 L/4, 0) = 1. Primeiramente, considere
que há sumidouros em x = 0 e x = L. Em seguida, considere a
situação onde os pontos x = 0 e x = L estão conectados, formando
um anel. As condições de contorno desta segunda forma são
chamadas de condições de contorno periódicas.
'''
import numpy as np
import matplotlib.pyplot as plt


def ftcs_ex2(x0, xf, D, dx, dt, tf, k):
    k1 = (D * dt)/(dx**2)
    x = list(np.arange(x0, xf, dx))
    ftemp = np.zeros(len(x))
    ftemp[int(len(x)/4):int((3*len(x))/4)] = 1.
    fxt = np.zeros(len(x))
    fxt[int(len(x)/4):int((3*len(x))/4)] = 1.
    for t in np.arange(dt, tf, dt):
        for i in range(1, len(x)-1):
            ftemp[i] = fxt[i] + k * (fxt[i-1] - 2 * fxt[i] + fxt[i+1])
        for j in range(1, len(x)-1):
            fxt[j] = ftemp[j]
    return x, fxt


def ftcs_pbc(x0, xf, D, dx, dt, tf, k):
    k1 = (D * dt)/(dx**2)
    x = list(np.arange(x0, xf, dx))
    ftemp = np.zeros(len(x))
    ftemp[int(len(x)/4):int((3*len(x))/4)] = 1.
    fxt = np.zeros(len(x))
    fxt[int(len(x)/4):int((3*len(x))/4)] = 1.
    for t in np.arange(dt, tf, dt):
        for i in range(0, len(x)):
            if i < len(x)-1:
                ftemp[i] = fxt[i] + k * (fxt[i-1] - 2 * fxt[i] + fxt[i+1])
            else:
                ftemp[i] = fxt[i] + k * (fxt[i - 1] - 2 * fxt[i] + fxt[0])
        for j in range(0, len(x)):
            fxt[j] = ftemp[j]
    return x, fxt


x0 = 0
xf = 100
k = .4
D = 2
tf = [0, 50, 400, 2000]
dx = 1
dt = .25

plt.figure(1)
for t in tf:
    x, y = ftcs_ex2(x0, xf, D, dx, dt, t, k)
    plt.plot(x, y, marker='+', mec='k', ms=1.3, label=f't = {t}')
plt.grid()
plt.legend()
plt.title(f'Equação da difusão por FTCS\nk = {k}')
plt.xlabel('x')
plt.ylabel('f(x, t)')
plt.savefig('ftcs-ex2.png')

plt.figure(2)
for t in tf:
    x, y = ftcs_pbc(x0, xf, D, dx, dt, t, k)
    plt.plot(x, y, marker='+', mec='k', ms=1.3, label=f't = {t}')
plt.grid()
plt.legend()
plt.title(f'Equação da difusão por FTCS (PBC)\nk = {k}')
plt.xlabel('x')
plt.ylabel('f(x, t)')
plt.savefig('ftcs-ex2-pbc.png')



