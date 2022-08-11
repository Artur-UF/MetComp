import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from scipy.stats import maxwell
import time

np.random.seed(123486789)


def immin(x1, y1, x2, y2, l):
    # Imagem mínima
    dx = x1 - x2
    if abs(dx) > l / 2:
        if dx < 0:
            delta = l / 2 - abs(dx)
            dx = l / 2 + delta
        else:
            delta = l / 2 - abs(dx)
            dx = -l / 2 - delta

    dy = y1 - y2
    if abs(dy) > l / 2:
        if dy < 0:
            delta = l / 2 - abs(dy)
            dy = l / 2 + delta
        else:
            delta = l / 2 - abs(dy)
            dy = -l / 2 - delta

    return dx, dy


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
        rc = 2.5
        Aij = lambda r: 48 * (eps / (sig ** 2)) * (((sig / r) ** 14) - (0.5 * ((sig / r) ** 8)))
        Uij = lambda r: 4 * eps * (((sig/r)**12) - ((sig/r)**6))
        p = Particle.todas
        n = len(p)
        for i in p:
            i.forc = [0, 0]
            i.pot = 0

        for pi in range(n):
            for pj in range(pi + 1, n):
                dx, dy = immin(p[pi].pos[0], p[pi].pos[1], p[pj].pos[0], p[pj].pos[1], l)
                if np.hypot(dx, dy) <= rc:
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

                    # Cálculo dos potenciais
                    poti = Uij(np.hypot(dx, dy))
                    potj = poti

                    # Atribuição dos potenciais
                    p[pi].pot += poti
                    p[pj].pot += potj

    @classmethod
    def energias(cls, cond='Particula'):
        k = 0
        pot = 0
        n = len(Particle.todas)
        if cond == 'Sistema':
            for p in Particle.todas:
                k += (np.hypot(p.vel[0], p.vel[1]) ** 2) / 2
                pot += p.pot
            tot = k + pot
            return k, pot, tot
        else:
            for p in Particle.todas:
                k += (np.hypot(p.vel[0], p.vel[1]) ** 2) / 2
                pot += p.pot
            tot = k + pot
            return k / n, pot / n, tot / n

    @classmethod
    def rdf(cls, l, switch=0, ngr=0, g=(), size=2):
        p = Particle.todas
        n = len(p)
        '''
        Se for só uma usa esse aqui
        # Seleção da partícula central
        pc = p[0]
        for i in range(n):
            delr = np.hypot(p[i].pos[0] - l / 2, p[i].pos[1] - l / 2)

            delrc = np.hypot(pc.pos[0] - l / 2, pc.pos[1] - l / 2)
            if delr < delrc:
                pc = p[i]
        '''
        bins = l * size
        tambin = l/(2 * bins)
        rho = n / (l ** 2)
        if switch == 0:
            g = np.zeros(bins)
            return ngr, g

        if switch == 1:
            ngr += 1
            for i in range(n):
                for j in range(i + 1, n):
                    dx, dy = immin(p[i].pos[0], p[i].pos[1], p[j].pos[0], p[j].pos[1], l)
                    r = np.hypot(dx, dy)
                    if r <= l/2:
                        ig = int(r//tambin)
                        g[ig] += 2
            return ngr, g

        if switch == 2:
            for i in range(bins):
                vb = (((i + 1)**2) - (i**2)) * (tambin**2)
                npar = np.pi * vb * rho
                g[i] /= ngr * n * npar

            return g




    @classmethod
    def plot(cls, ax):
        c = 1
        for p in Particle.todas:
            circ = plt.Circle(p.pos, p.raio, facecolor='k', edgecolor='red')
            '''cores = ['k', 'b', 'g', 'pink', 'w', 'c', 'm', 'y', 'r']
            circ = plt.Circle(p.pos, p.raio,color=cores[c-1], label=c)
            c += 1'''
            ax.add_patch(circ)

    @classmethod
    def estado(cls):
        c = 1
        print('N°|   Posição  |   Força   ')
        for p in Particle.todas:
            print(f'{c:<2}| [{p.pos[0]:<3.1f}, {p.pos[1]:<3.1f}] | {p.forc}')
            c += 1


def dinmol(l, n, r, di, eps, sig, T, tf, dt, ci='Random'):
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
    # Largura da distribuição de velocidades
    kb = 1
    m = 1
    a = np.sqrt((kb * T)/m)

    particulas = []

    # Inicializações
    if ci == 'Random':  # Sobreposição não tratada
        # Distribuição uniforme de posições e distribuição normal de velocidades
        for i in range(n ** 2):
            particulas.append([Particle(r, [uniform(r, l - r), uniform(r, l - r)],
                                        [maxwell.rvs(size=1, scale=a)[0] * (1 - (2 * np.random.randint(2))),
                                         maxwell.rvs(size=1, scale=a)[0] * (1 - (2 * np.random.randint(2)))])])

    if ci == 'Quadrado':
        aresta = (2 * r * n) + ((n - 1) * di)
        xx = np.arange((l - aresta)/2, (l + aresta)/2, 2 * r + di)
        yy = np.arange((l - aresta)/2, (l + aresta)/2, 2 * r + di)
        for y in range(n):
            for x in range(n):
                particulas.append(Particle(r, [xx[x], yy[y]],
                                           [maxwell.rvs(size=1, scale=a)[0] * (1 - (2 * np.random.randint(2))),
                                            maxwell.rvs(size=1, scale=a)[0] * (1 - (2 * np.random.randint(2)))]))

    if ci == 'Triangulo':
        ''' Como que centraliza??? '''
        i = -1
        aresta = (2 * r * n) + ((n - 1) * di)
        xx = np.arange((l - aresta)/2, (l + aresta)/2, 2 * r + di)
        yy = np.arange((l - aresta)/2, (l + aresta)/2, (2 * r + di) * (np.sqrt(3)/2))
        for y in range(n):
            for x in range(n):
                particulas.append(Particle(r, [xx[x], yy[y]],
                                           [maxwell.rvs(size=1, scale=a)[0] * (1 - (2 * np.random.randint(2))),
                                            maxwell.rvs(size=1, scale=a)[0] * (1 - (2 * np.random.randint(2)))]))
            i *= -1
            xx = np.arange((l - aresta)/2 + ((1 + i)/2) * (r + di/2), (l + aresta)/2, 2 * r + di)

    # Integração
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Inicialização das forças    
    Particle.forcas(eps, sig, l)

    # Meio passo da velocidade
    for p in particulas:
        p.vel[0] += p.forc[0] * dt/2
        p.vel[1] += p.forc[1] * dt/2

    # Resto dos passos
    c = 0
    k, u, tot, time = [], [], [], []
    ngr, g = Particle.rdf(l, switch=0, size=10)
    for t in np.arange(0, tf, dt):
        c += 1
        # Dinâmica
        Particle.mov_pbc(dt, l)
        Particle.plot(ax1)
        ax1.set_xlim(0, l)
        ax1.set_ylim(0, l)
        ax1.set_title(f'Partículas | n = {len(particulas)}')

        # RDF
        if t > tf/2:
            ngr, g = Particle.rdf(l, switch=1, ngr=ngr, g=g, size=10)

        # Energias
        if c % 10 == 0:
            cin, pot, to = Particle.energias(cond='Particulas')
            k.append(cin)
            u.append(pot)
            tot.append(to)
            time.append(t)
            # Cinetica
            ax2.plot(time, k,  marker='+', color='r', linewidth=.1)
            ax2.set_title('Energias')
            ax2.set(xlabel='t', ylabel='E/n')

            # Potencial
            ax2.plot(time, u,  marker='^', color='b', linewidth=.1)

            # Total
            ax2.plot(time, tot, marker='*', color='k', linewidth=.1)

        fig.suptitle(f'Potencial Lennard-Jones\nPassos = {c:>5} | dt = {dt} | t = {t:>3.1f}')
        if t == tf-dt:
            fig.savefig(f'MD_lj_'+str(dt)[2:]+'.png')
        plt.pause(0.0001)
        ax1.cla()

    g = Particle.rdf(l, switch=2, ngr=ngr, g=g, size=10)
    rs = np.linspace(0, l/2, len(g))
    plt.figure(4)
    plt.plot(rs, g)
    plt.title(f'Função de Distribuição Radial\nn = {n**2} | Ti = {T}')
    plt.xlabel('r')
    plt.ylabel('g(r)')
    plt.grid()
    plt.savefig('RDF.png')


l = 10
n = 9
r = .3
di = .4
eps = 1
sig = 1
T = .5
tf = 5
dt = .005
ci = 'Triangulo'
start = time.time()
dinmol(l, n, r, di, eps, sig, T, tf, dt, ci)
end = time.time()
print(f'Tempo de execução: {end - start}s')

'''
Essa energia total tá certa?
'''