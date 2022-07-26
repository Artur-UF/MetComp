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

    def mov_elast(self, dt, lim):
        self.pos[0] += dt * self.vel[0]
        self.pos[1] += dt * self.vel[1]
        # Problema de bordas em x
        if self.pos[0] >= lim:
            dx = self.pos[0] - lim
            self.pos[0] -= 2 * dx
            self.vel[0] *= -1
        if self.pos[0] <= 0:
            dx = abs(self.pos[0])
            self.pos[0] += 2 * dx
            self.vel[0] *= -1
        # Problema de bordas em y
        if self.pos[1] >= lim:
            dy = self.pos[1] - lim
            self.pos[1] -= 2 * dy
            self.vel[1] *= -1
        if self.pos[1] <= 0:
            dy = abs(self.pos[1])
            self.pos[1] += 2 * dy
            self.vel[1] *= -1

    def mov_pbc(self, dt, lim):
        self.pos[0] += dt * self.vel[0]
        self.pos[1] += dt * self.vel[1]
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


def dinmol(l, r, tf, dt, ci='Random', cc='pbc', n=0):
    ''''
    l: tamanho da aresta da caixa
    r: raio das partículas
    tf: tempo final
    dt: delta tempo
    ci: condições de inicialização ; Triangulo, Quadrado, Random
    cc: condições de contorno ; pbc e Fechada
    n: quantidade de partículas na 1 linha da inicialização
    '''
    npa = l // (2 * r)
    # Largura da distribuição de velocidades
    dsv = 1

    if n == 0:
        if ci == 'Random':
            # Distribuição uniforme de posições e distribuição normal de velocidades
            particulas = [Particle(r, [uniform(r, l - r), uniform(r, l - r)],
                                   [np.random.normal(0, dsv), np.random.normal(0, dsv)]) for i in range(npa ** 2)]

        if ci == 'Quadrado':
            xx = np.arange(r, l, 3 * r)
            yy = np.arange(r, l, 3 * r)
            particulas = []
            for x in xx:
                for y in yy:
                    particulas.append(Particle(r, [x, y], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))

        if ci == 'Triangulo':
            i = 1
            x = np.arange(r, l, 3 * r)
            y = np.arange(r, l, r * np.sqrt(3) * (3/2))
            particulas = []
            for yi in y:
                for xi in x:
                    particulas.append(Particle(r, [xi, yi], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))
                i += 1
                x = np.arange(i * r * (3/2), l - (i - 1) * r * (3/2), 3 * r)
    if n > 0:
        if ci == 'Random':
            # Distribuição uniforme de posições e distribuição normal de velocidades
            particulas = [Particle(r, [uniform(r, l - r), uniform(r, l - r)],
                                   [np.random.normal(0, dsv), np.random.normal(0, dsv)]) for i in range(n ** 2)]

        if ci == 'Quadrado':
            xx = np.arange((l - n) // 2, r * 3 * n, 3 * r)
            yy = np.arange((l - n) // 2, r * 3 * n, 3 * r)
            particulas = []
            for x in xx:
                for y in yy:
                    particulas.append(Particle(r, [x, y], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))

        if ci == 'Triangulo':
            i = 1
            x = np.arange(r, l, 2 * r)
            y = np.arange(r, l, r * np.sqrt(3))
            particulas = []
            for yi in y:
                for xi in x:
                    particulas.append(Particle(r, [xi, yi], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))
                i += 1
                x = np.arange(i * r, l - (i - 1) * r, 2 * r)

    ec = []
    # Assumindo que m = 1
    for i in particulas:
        vx = i.vel[0]
        vy = i.vel[1]
        vq = (vx ** 2) + (vy ** 2)
        ec.append(vq / 2)
    ecmed = sum(ec) / len(ec)

    fig, ax = plt.subplots()

    t = np.arange(0, tf, dt)
    for ti in t:
        Particle.plot(ax)
        if cc == 'pbc':
            Particle.run_pbc(dt, l)
        else:
            Particle.run_elast(dt, l)
        ax.set_xlim(0, l)
        ax.set_ylim(0, l)
        ax.set_title(f'Dinâmica Molecular\n t = {ti:>4.1f}')
        plt.pause(.01)
        plt.cla()


l = 20
r = 1
tf = 20
dt = 0.1
ci = 'Triangulo'
cc = 'gsg'
n = 0

dinmol(l, r, tf, dt, ci, cc, n)



