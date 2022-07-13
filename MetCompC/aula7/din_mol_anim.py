import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import uniform


class Particle:
    todas = []

    def __init__(self, r, p, v):
        self.raio = r
        self.pos = p
        self.vel = v
        self.todas.append(self)

    def mov_elast(self, dt, lim):
        self.pos[0] += dt*self.vel[0]
        self.pos[1] += dt*self.vel[1]
        # Problema de bordas em x
        if self.pos[0] >= lim:
            dx = self.pos[0] - lim
            self.pos[0] -= 2*dx
            self.vel[0] *= -1
        if self.pos[0] <= 0:
            dx = abs(self.pos[0])
            self.pos[0] += 2*dx
            self.vel[0] *= -1
        # Problema de bordas em y
        if self.pos[1] >= lim:
            dy = self.pos[1] - lim
            self.pos[1] -= 2*dy
            self.vel[1] *= -1
        if self.pos[1] <= 0:
            dy = abs(self.pos[1])
            self.pos[1] += 2*dy
            self.vel[1] *= -1

    def mov_pbc(self, dt, lim):
        self.pos[0] += dt*self.vel[0]
        self.pos[1] += dt*self.vel[1]
        # Problema de bordas em x
        if self.pos[0] >= lim:
            self.pos[0] = self.pos[0] - lim
        if self.pos[0] <= 0:
            dx = abs(self.pos[0])
            self.pos[0] = lim - dx
        # Problema de bordas em y
        if self.pos[1] >= lim:
            self.pos[1] = self.pos[1] - lim
        if self.pos[1] <= 0:
            dy = abs(self.pos[1])
            self.pos[1] = lim - dy

    @classmethod
    def run_elast(cls, dt, lim):
        for i in Particle.todas:
            i.mov_elast(dt, lim)

    @classmethod
    def run_pbc(cls, dt, lim):
        for i in Particle.todas:
            i.mov_pbc(dt, lim)

    @classmethod
    def plot(cls, ax):
        for p in Particle.todas:
            circ = plt.Circle(p.pos, p.raio, edgecolor='red')
            ax.add_patch(circ)


def dinmol(l, r, ci='Random'):
    n = l//(2*r)
    # Largura da distribuição de velocidades
    dsv = .7

    if ci == 'Random':
        # Distribuição uniforme de posições e distribuição normal de velocidades
        particulas = [Particle(r, [uniform(r, l-r), uniform(r, l-r)], [np.random.normal(0, dsv), np.random.normal(0, dsv)]) for i in range(n**2)]

    if ci == 'Quadrado':
        xx = np.arange(r, l, 2*r)
        yy = np.arange(r, l, 2*r)
        particulas = []
        for x in xx:
            for y in yy:
                particulas.append(Particle(r, [x, y], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))

    if ci == 'Triangulo':
        i = 1
        x = np.arange(r, l, 2*r)
        y = np.arange(r, l, r * np.sqrt(3))
        particulas = []
        for yi in y:
            for xi in x:
                particulas.append(Particle(r, [xi, yi], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))
            i += 1
            x = np.arange(i*r, l-(i-1)*r, 2*r)

    return particulas


def gen():
    l = 10
    r = 1
    ci = 'Random'
    tf = 20
    dt = 0.1
    dinmol(l, r, ci)
    t = np.arange(0, tf, dt)
    for ti in t:
        yield Particle.todas, ti, l, r
        Particle.run_pbc(dt, l)


fig, ax = plt.subplots()


def init():
    '''
    É o inicio de todo frame após o 'run'
    '''
    ax.clear()
    ax.set_xlabel('x')
    ax.set_ylabel('y')


def run(i):
    partics, t, l, r = i
    ax.set_xlim(-r, l + r)
    ax.set_ylim(-r, l + r)
    Particle.plot(ax)
    ax.set_title(f'Dinâmica Molecular\nt = {t:>4.1f}')


ani = animation.FuncAnimation(fig, run, gen, interval=200, init_func=init, save_count=1500)
#plt.show()
writergif = animation.PillowWriter(fps=30)
ani.save(r'D:\Aplicações\GItHub D\MetCompA\MetCompC\aula7\moleculas_pbc.gif', writer=writergif)
plt.close()
