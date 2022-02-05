'''
Use o método de Verlet para integrar numéricamente o problema do pêndulo simples. Use w=1, x0=3, v0=0 e dt = 0.5.

  1.  Compare as curvas no espaço de fases com o método de Euler-Cromer.
  2.  Compare a evolução da energia (Et x t) com o método de Euler-Cromer.
'''
import numpy as np
import matplotlib.pyplot as plt


def eulercr2(x0, v0, tf, dt, w):
    '''
    Método de Euler-Cromer para equações diferencais de 2 ordem.
    funcd é a função doferencial da vez
    :param x0: valor inicial
    :param v0: outro valor inicial
    :param tf: intervalo de tempo a ser calculado
    :param dt: delta t
    :param w, m: parâmetros para a funcd
    :return: retorna duas listas com os valores de y e y'
    '''
    funcd = lambda x, w: -(w**2)*np.sin(x)
    pos = []
    vel = []
    for t in np.arange(0, tf, dt):
        x0 += v0*dt
        pos.append(x0)
        v0 += funcd(x0, w)*dt
        vel.append(v0)
    return pos, vel


def metverlet(x0, v0, tf, dt, w):
    funcd = lambda x, w: -(w**2)*np.sin(x)
    pos = [x0]
    vel = [v0]
    x1 = x0 + v0*dt
    for t in np.arange(0, tf, dt):
        pos.append(x1)
        x2 = 2*x1 - x0 + funcd(x1, w)*dt**2
        v1 = (x2-x0)/(2*dt)
        vel.append(v1)
        x0 = x1
        x1 = x2
    return pos, vel


def energiaeuler(x0, v0, tf, dt, w, l, g, m):
    v = np.array(eulercr2(x0, v0, tf, dt, w)[1])
    x = np.array(eulercr2(x0, v0, tf, dt, w)[0])
    e = (m*(l**2)*(v**2)/2) + m*g*l*(1-np.cos(x))
    return e


def energiaverlet(x0, v0, tf, dt, w, l, g, m):
    v = np.array(metverlet(x0, v0, tf, dt, w)[1])
    x = np.array(metverlet(x0, v0, tf, dt, w)[0])
    e = (m*(l**2)*(v**2)/2) + m*g*l*(1-np.cos(x))
    return e


w, g, l = 1, 10, 10
x0, v0, tf, dt = 3, 0, 20, .5
t = np.arange(0, tf+dt, dt)
'''
print(len(energiaverlet(x0, v0, tf, dt, 1, l, g, 1)))
print(len(t))
'''
figura = plt.figure(figsize=(12, 5))
plt.subplot(121)
plt.plot(metverlet(x0, v0, tf, dt, 1)[0], metverlet(x0, v0, tf, dt, 1)[1], label='Verlet')
plt.plot(eulercr2(x0, v0, tf, dt, 1)[0], eulercr2(x0, v0, tf, dt, 1)[1], label='Euler-Cromer')
plt.legend()
plt.grid()
plt.ylabel('V(x)')
plt.xlabel('x')
plt.title(r'Diagrama de fases Posição $\times$ Velocidade')

plt.subplot(122)
plt.plot(t, energiaverlet(x0, v0, tf, dt, 1, l, g, 1), label='Verlet')
plt.plot(t, energiaeuler(x0, v0, tf+dt, dt, 1, l, g, 1), label='Euler-Cromer')
plt.legend()
plt.grid()
plt.ylabel('$E_{T}$(t)')
plt.xlabel('t(s)')
plt.title(r'$E_{T} \times t$')
plt.savefig('verlet.png')

