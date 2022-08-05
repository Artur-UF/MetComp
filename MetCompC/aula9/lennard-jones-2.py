import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from scipy.stats import maxwell


class Particle:
    todas = []

    def __init__(self, r, p, v):
        self.raio = r
        self.pos = p
        self.vel = v
        self.forc = [0, 0]
        self.pot = 0
        self.todas.append(self)
    
    @classmethod
    def mov_pbc(cls, dt, l):
        # Atualização das posições        
        for p in Particle.todas:
            p.pos[0] += p.vel[0] * dt
            p.pos[1] += p.vel[1] * dt
            # Problema de bordas em x
            if p.pos[0] >= l:
                p.pos[0] = p.pos[0] - l
            if p.pos[0] <= 0:
                dx = abs(p.pos[0])
                p.pos[0] = l - dx
            # Problema de bordas em y
            if p.pos[1] >= l:
                p.pos[1] = p.pos[1] - l
            if p.pos[1] <= 0:
                dy = abs(p.pos[1])
                p.pos[1] = l - dy
        
        # Atualização das forças        
        Particle.forcas(eps, sig, l)
    
        # Atualização das velocidades        
        for p in Particle.todas:
            p.vel[0] += p.forc[0] * (dt/2)
            p.vel[1] += p.forc[1] * (dt/2)

    @classmethod
    def forcas(cls, eps, sig, l):
        Aij = lambda r: 48 * (eps / (sig ** 2)) * (((sig / r) ** 14) - (0.5 * ((sig / r) ** 8)))
        p = Particle.todas
        n = len(p)
        for i in p:
            i.forc = [0, 0]
        for pi in range(n):
            for pj in range(0, n):
                if pi != pj:
                    # Imagem mínima
                    dx = p[pi].pos[0] - p[pj].pos[0]
                    if abs(dx) > l/2:
                        if dx < 0:
                            delta = l/2 - abs(dx)
                            dx = l/2 + delta
                        else:
                            delta = l/2 - abs(dx)
                            dx = -l/2 - delta

                    dy = p[pi].pos[1] - p[pj].pos[1]
                    if abs(dy) > l/2:
                        if dx < 0:
                            delta = l/2 - abs(dy)
                            dy = l/2 + delta
                        else:
                            delta = l/2 - abs(dy)
                            dy = -l/2 - delta

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

    @classmethod
    def potencial(cls, eps, sig, l):
        Uij = lambda r: 4 * eps * (((sig/r)**12) - ((sig/r)**6))
        p = Particle.todas
        n = len(p)
        c = 1
        for pi in range(n):
            for pj in range(c, n):
                # Imagem mínima
                dx = p[pi].pos[0] - p[pj].pos[0]
                if abs(dx) > l / 2:
                    if dx < 0:
                        delta = l / 2 - abs(dx)
                        dx = l / 2 + delta
                    else:
                        delta = l / 2 - abs(dx)
                        dx = -l / 2 - delta

                dy = p[pi].pos[1] - p[pj].pos[1]
                if abs(dy) > l / 2:
                    if dx < 0:
                        delta = l / 2 - abs(dy)
                        dy = l / 2 + delta
                    else:
                        delta = l / 2 - abs(dy)
                        dy = -l / 2 - delta

                # Cálculo dos potenciais
                poti = Uij(np.hypot(dx, dy))
                potj = poti

                # Atribuição dos potenciais
                p[pi].pot += poti
                p[pj].pot += potj

                c += 1

    @classmethod
    def plot(cls, ax):
        c = 1
        #cores = ['k', 'b', 'g', 'pink', 'w', 'c', 'm', 'y', 'r']
        for p in Particle.todas:
            circ = plt.Circle(p.pos, p.raio, facecolor='k', edgecolor='red')
            #circ = plt.Circle(p.pos, p.raio,color=cores[c-1], label=c)
            #c += 1
            ax.add_patch(circ)

    @classmethod
    def estado(cls):
        c = 1
        print('N°|   Posição  |   Força   ')
        for p in Particle.todas:
            print(f'{c:<2}| [{p.pos[0]:<3.1f}, {p.pos[1]:<3.1f}] | {p.forc}')
            c += 1


def dinmol(l, n, r, di, eps, sig, tf, dt, ci='Random'):
    ''''
    l: tamanho da aresta da caixa
    n: quantidade de partículas na 1ª linha da inicialização
    r: raio das partículas
    di: distância entre partículas
    eps: epsilon
    sig: sigma
    tf: tempo final
    dt: delta tempo
    ci: condições de inicialização ; Triangulo, Quadrado, Random
    '''
    npa = l // (2 * r)
    # Largura da distribuição de velocidades
    dsv = 2

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
            for y in range(n):
                for x in range(n):
                    particulas.append(Particle(r, [xx[x], yy[y]], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))

        if ci == 'Triangulo':
            i = -1
            aresta = 2 * n * r + (n + 1) * di
            xx = np.arange((l - aresta)//2, (l + aresta)/2, 2 * r + di)
            yy = np.arange((l - aresta)//2, (l + aresta)/2, (2 * r + di) * (np.sqrt(3)/2))
            for y in range(n):
                for x in range(n):
                    particulas.append(Particle(r, [xx[x], yy[y]], [np.random.normal(0, dsv), np.random.normal(0, dsv)]))
                i *= -1
                xx = np.arange((l - aresta)//2 + ((1 + i)/2) * (r + di/2), (l + aresta)/2, 2 * r + di)

    
    # Integração
    fig, ax = plt.subplots()
    
    # Inicialização das forças    
    Particle.forcas(eps, sig, l)
    '''
    Particle.estado()
    Particle.plot(ax)
    ax.grid()
    ax.set_xlim(0, l)
    ax.set_ylim(0, l)
    plt.legend()
    plt.show()
    '''
    # Meio passo da velocidade
    for p in particulas:
        p.vel[0] += p.forc[0] * dt/2
        p.vel[1] += p.forc[1] * dt/2
    
    # Resto dos passos
    for t in np.arange(0, tf, dt):
        Particle.mov_pbc(dt, l)   
        Particle.plot(ax)
        #ax.grid()
        ax.set_xlim(0, l)
        ax.set_ylim(0, l)
        ax.set_title(f'Potencial Lennard-Jones\nt = {t:>3.1f}')
        plt.pause(0.001)
        plt.cla()


l = 10
n = 3
r = .5
di = .5
eps = 1
sig = 1
tf = 10
dt = .01
ci = 'Triangulo'

dinmol(l, n, r, di, eps, sig, tf, dt, ci)
