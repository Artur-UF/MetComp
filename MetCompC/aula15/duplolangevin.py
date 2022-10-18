import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt
import time


class Particle:
    todas = []

    def __init__(self, p, v):
        self.pos = p
        self.vel = v
        self.todas.append(self)

    def mov_euler(self, dt, alpha, beta, dW):
        func = lambda x: (alpha*x - x**3)*dt + beta*dW
        # Posições
        self.pos[0] += func(self.pos[0])


def dinmol(x0, y0, vx0, vy0, dt, passos, alpha, beta):
    p1 = Particle([x0, y0], [vx0, vy0])
    # As raizes do potencial são x=+-sqrt(b/a)
    # A profundidade do poço é proporcional diretamente a 'b' e inversamente a 'a'
    b = alpha/2
    a = 0.25
    xlim = 2.5

    t = np.arange(passos+1)
    dW = np.random.randn(passos)*np.sqrt(dt)
    x = np.arange(-xlim, xlim, 0.01)
    y = a*x**4 - b*x**2
    fig, ax = plt.subplots()
    for ti in t:
        p1.mov_euler(dt, alpha, beta, dW[ti])
        ax.scatter(p1.pos[0], 0, c='r', s=50)
        ax.plot(x, y, 'k', label='V(x)')
        ax.set(xlim=(-xlim, xlim), title=f't = {ti}')
        plt.grid()
        plt.legend()
        plt.pause(0.001)
        plt.cla()


start = time.time()

x0 = -5
y0 = 0
vx0 = 0
vy0 = 0
dt = 0.01
passos = int(50/dt)  # tmax é o numerador
alpha = 2
beta = 1
dinmol(x0, y0, vx0, vy0, dt, passos, alpha, beta)

end = time.time()
print(f'Tempo de execução = {end-start}')

