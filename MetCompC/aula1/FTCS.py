'''
Suponhamos que em x = 0 há uma fonte inesgotável de material que
se difunde para x > 0 a partir do instante t = 0, isto é, f(x = 0, t) = 1.
Suponhamos ainda que em x = L há um sumidouro que absorve todo
o material que lá chega, ou seja, f(L, t) = 0. Como condição inicial
supomos que f(x > 0, t = 0) = 0.
No enunciado não é especificado o valor de L. Pode-se usar L = 100,
como na resolução no livro. Além disso, é necessário que se escolha
uma valor para tmax: usaremos tmax = 400 como no livro. Explore os
valores de k. Ex: 0,1 , 0,2 , ... Para quais valores de k o sistema é
estável?
'''
import numpy as np
import matplotlib.pyplot as plt


def ftcs(x0, xf, D, dx, dt, tf):
    k = (D * dt)/(dx**2)
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
    return x, fxt


x0 = 0
xf = 100
D = 1.6  # np.arange(1, 6)
dx = 1
dt = 0.25
tf = 400

x, y = ftcs(x0, xf, D, dx, dt, tf)

plt.figure(1)
plt.scatter(x, y, marker='.', c='k')
plt.grid()
plt.title(f'Equação da difusão por FTCS\nk = {(D * dt)/(dx**2)} | t = {tf}')
plt.xlabel('x')
plt.ylabel('f(x, t)')
plt.savefig('ftcs.png')


