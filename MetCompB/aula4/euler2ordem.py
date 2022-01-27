# Aplicar o método para a integração de EDOs de 2 ordem
'''
Integre o sistema massa-mola usando os métodos de Euler explícito e Euler-Cromer.

Use w=1, x0=2 e v0=0.

   1. Faça gráficos de X x t para os dois métodos no mesmo gráfico.
   2. Faça gráficos de V x t para os dois métodos em um mesmo gráfico.
   3. Faça gráficos de energia x tempo.

'''
import numpy as np
import matplotlib.pyplot as plt


def eulerex2(x0, v0, tf, dt, w, m):
    funcd = lambda x, w, m: -((w**2)*x)/m
    pos = []
    vel = []
    for t in np.arange(0, tf, dt):
        xaux = x0
        x0 += v0*dt
        pos.append(x0)
        v0 += funcd(xaux, w, m)*dt
        vel.append(v0)
    return pos, vel


def eulercr2(x0, v0, tf, dt, w, m):
    funcd = lambda x, w, m: -((w**2)*x/m)
    pos = []
    vel = []
    x = x0
    v = v0
    for t in np.arange(0, tf, dt):
        x += v*dt
        pos.append(x)
        v += funcd(x, w, m)*dt
        vel.append(v)
    return pos, vel


def energia(x0, v0, tf, dt, w, m):
    xex = np.array(eulerex2(x0, v0, tf, dt, w, m)[0])
    vex = np.array(eulerex2(x0, v0, tf, dt, w, m)[1])
    eex = (m*(vex**2))/2 + (m*(w**2)*(xex**2))
    xec = np.array(eulercr2(x0, v0, tf, dt, w, m)[0])
    vec = np.array(eulercr2(x0, v0, tf, dt, w, m)[1])
    eec = (m * (vec ** 2)) / 2 + (m * (w ** 2) * (xec ** 2))
    return eex, eec


tf = 30

figura = plt.figure(figsize=(25, 5))
plt.subplot(131)
plt.plot(np.arange(0, tf, .1), eulerex2(2, 0, tf, .1, 1, 1)[0], label='Euler Ex.')
plt.plot(np.arange(0, tf, .1), eulercr2(2, 0, tf, .1, 1, 1)[0], label='Euler-Cromer')
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Posição X Tempo')
plt.legend()
plt.subplot(132)
plt.plot(np.arange(0, tf, .1), eulerex2(2, 0, tf, .1, 1, 1)[1], label='Euler Ex.')
plt.plot(np.arange(0, tf, .1), eulercr2(2, 0, tf, .1, 1, 1)[1], label='Euler-Cromer')
plt.grid()
plt.xlabel('t')
plt.ylabel('v(t)')
plt.title('Velocidade X Tempo')
plt.legend()
plt.subplot(133)
plt.plot(np.arange(0, tf, .1), energia(2, 0, tf, .1, 1, 1)[0], label='Euler Ex.')
plt.plot(np.arange(0, tf, .1), energia(2, 0, tf, .1, 1, 1)[1], label='Euler-Cromer')
plt.grid()
plt.xlabel('t')
plt.ylabel('E(t)')
plt.title('Energia X Tempo')
plt.legend()
plt.show()
