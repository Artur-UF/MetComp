import numpy as np
import matplotlib.pyplot as plt
from random import uniform


class Particle:
    todas = []

    def __init__(self, r, p, v):
        self.raio = r
        self.pos = p
        self.vel = v
        self.forc = [0, 0]
        self.pot = 0
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
    def forcas(cls, eps, sig, l):
        Aij = lambda r: 48 * (eps / sig ** 2) * (((sig / r) ** 14) - (0.5 * (sig / r) ** 8))
        p = Particle.todas
        n = len(p)
        c = 1
        for pi in range(n):
            for pj in range(c, n):
                # PBC
                dx = p[pi].pos[0] - p[pj].pos[0]
                if abs(dx) > l/2:
                    if abs(p[pj].pos[0] - p[pi].pos[0]) < l/2:
                        dx = -(l/2 - np.fmod(abs(p[pj].pos[0] - p[pi].pos[0]), l/2))
                    else:
                        dx = l/2 - np.fmod(abs(p[pj].pos[0] - p[pi].pos[0]), l/2)
                dy = p[pi].pos[1] - p[pj].pos[1]
                if abs(dy) > l/2:
                    if p[pj].pos[1] - p[pi].pos[1] < 0:
                        dy = -(l/2 - np.fmod(abs(p[pj].pos[1] - p[pi].pos[1]), l/2))
                    else:
                        dy = l/2 - np.fmod(abs(p[pj].pos[1] - p[pi].pos[1]), l/2)

                # Cálculo das forças
                fxi = Aij(np.hypot(dx, dy)) * dx
                fxj = -fxi
                fyi = Aij(np.hypot(dx, dy)) * dy
                fyj = -fyi

                # Atribuição das forças
                p[pi].forc[0] += fxi
                p[pi].forc[1] += fyi
                p[pj].forc[0] += fxj
                p[pj].forc[1] += fyj

                c += 1

    @classmethod
    def potencial(cls, eps, sig, l):
        Uij = lambda r: 4 * eps * (((sig/r)**12) - ((sig/r)**6))
        p = Particle.todas
        n = len(p)
        c = 1
        for pi in range(n):
            for pj in range(c, n):
                # PBC
                dx = p[pi].pos[0] - p[pj].pos[0]
                if abs(dx) > l / 2:
                    if abs(p[pj].pos[0] - p[pi].pos[0]) < l / 2:
                        dx = -(l / 2 - np.fmod(abs(p[pj].pos[0] - p[pi].pos[0]), l / 2))
                    else:
                        dx = l / 2 - np.fmod(abs(p[pj].pos[0] - p[pi].pos[0]), l / 2)
                dy = p[pi].pos[1] - p[pj].pos[1]
                if abs(dy) > l / 2:
                    if p[pj].pos[1] - p[pi].pos[1] < 0:
                        dy = -(l / 2 - np.fmod(abs(p[pj].pos[1] - p[pi].pos[1]), l / 2))
                    else:
                        dy = l / 2 - np.fmod(abs(p[pj].pos[1] - p[pi].pos[1]), l / 2)

                ''' Essa parte tá certa??? '''
                # Cálculo dos potenciais
                poti = Uij(np.hypot(dx, dy))
                potj = poti

                # Atribuição dos potenciais
                p[pi].pot += poti
                p[pj].pot += potj

                c += 1

    @classmethod
    def plot(cls, ax):
        for p in Particle.todas:
            circ = plt.Circle(p.pos, p.raio, edgecolor='red')
            ax.add_patch(circ)


def dinmol(l, n, r, di, eps, sig, tf, dt, ci='Random'):
    ''''
    l: tamanho da aresta da caixa
    r: raio das partículas
    tf: tempo final
    dt: delta tempo
    ci: condições de inicialização ; Triangulo, Quadrado, Random
    n: quantidade de partículas na 1ª linha da inicialização
    '''
    npa = l // (2 * r)
    # Largura da distribuição de velocidades
    dsv = 1

    particulas = []
    if n == 0:
        if ci == 'Random':
            # Distribuição uniforme de posições e distribuição normal de velocidades
            particulas = [Particle(r, [uniform(r, l - r), uniform(r, l - r)],
                                   [np.random.normal(0, dsv), np.random.normal(0, dsv)]) for i in range(npa ** 2)]

        if ci == 'Quadrado':
            xx = np.arange(r, l, 3 * r)
            yy = np.arange(r, l, 3 * r)
            for x in xx:
                for y in yy:
                    particulas.append(Particle(r, [x, y], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))

        if ci == 'Triangulo':
            i = 1
            x = np.arange(r, l, 3 * r)
            y = np.arange(r, l, r * np.sqrt(3) * (3/2))
            for yi in y:
                for xi in x:
                    particulas.append(Particle(r, [xi, yi], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))
                i += 1
                x = np.arange(i * r * (3/2), l - (i - 1) * r * (3/2), 3 * r)
    else:
        if ci == 'Random':
            # Distribuição uniforme de posições e distribuição normal de velocidades
            particulas = [Particle(r, [uniform(r, l - r), uniform(r, l - r)],
                                   [np.random.normal(0, dsv), np.random.normal(0, dsv)]) for i in range(n ** 2)]

        if ci == 'Quadrado':
            aresta = 2 * n * r + (n + 1) * di
            xx = np.arange((l - aresta)//2, (l + aresta)/2, 2 * r + di)
            yy = np.arange((l - aresta)//2, (l + aresta)/2, 2 * r + di)
            for x in range(n):
                for y in range(n):
                    particulas.append(Particle(r, [xx[x], yy[y]], 0))

        if ci == 'Triangulo': # Não ta atualizada
            i = 1
            x = np.arange(r, l, 2 * r)
            y = np.arange(r, l, r * np.sqrt(3))
            for yi in y:
                for xi in x:
                    particulas.append(Particle(r, [xi, yi], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))
                i += 1
                x = np.arange(i * r, l - (i - 1) * r, 2 * r)

    fig, ax = plt.subplots()

    Particle.forcas(eps, sig, l)
    for p in Particle.todas:
        print(f'Força total [Fx, Fy] na partícula {Particle.todas.index(p):>2} = {p.forc}')
    Particle.plot(ax)
    ax.grid()
    ax.set_xlim(0, l)
    ax.set_ylim(0, l)
    plt.show()


l = 10
n = 5
r = .2
di = .2
eps = 1
sig = .2
tf = 20
dt = .1
ci = 'Quadrado'

dinmol(l, n, r, di, eps, sig, tf, dt, ci)
