import numpy as np
import matplotlib.pyplot as plt
from random import uniform


class Particle:
    todas = []

    def __init__(self, r, p, v):
        self.raio = r
        self.pos = p
        self.vel = v
        self.todas.append(self)

    def mov(self, dt, lim):
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

    @classmethod
    def run(cls, dt, lim):
        for i in Particle.todas:
            i.mov(dt, lim)

    @classmethod
    def plot(cls, ax):
        for p in Particle.todas:
            circ = plt.Circle(p.pos, p.raio)
            ax.add_patch(circ)


def dinmol(l, r, tf, dt, ci='Random'):
    n = l//(2*r)
    # Largura da distribuição de velocidades
    dsv = 1

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

    ec = []
    # Assumindo que m = 1
    for i in particulas:
        vx = i.vel[0]
        vy = i.vel[1]
        vq = (vx**2) + (vy**2)
        ec.append(vq/2)
    ecmed = sum(ec)/len(ec)

    fig, ax = plt.subplots()

    t = np.arange(0, tf, dt)
    for ti in t:
        Particle.plot(ax)
        Particle.run(dt, l)
        ax.set_xlim(-r, l+r)
        ax.set_ylim(-r, l+r)
        ax.set_title(f'Dinâmica Molecular\n t = {ti:>4.1f}')
        plt.pause(.1)
        plt.cla()


dinmol(10, 1, 10, .1, ci='Triangulo')




