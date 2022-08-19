import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from scipy.stats import maxwell
import time

np.random.seed(123786789)


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
    pressao = 0

    def __init__(self, r, p, v):
        self.raio = r
        self.pos = p
        self.vel = v
        self.forc = [0, 0]
        self.pot = 0
        self.bxy = [0, 0]
        self.todas.append(self)

    @classmethod
    def tempcalc(cls):
        '''
        Algoritmo 6, pg.70, Frenkel
        '''

    @classmethod
    def velnorm(cls, temp):
        pt = Particle.todas
        n = len(pt)
        sumvx = 0
        sumvy = 0
        sumvx2 = 0
        sumvy2 = 0
        for p in pt:
            sumvx += p.vel[0]
            sumvy += p.vel[1]
            sumvx2 += p.vel[0]**2
            sumvy2 += p.vel[1]**2
        sumvx /= n
        sumvy /= n
        sumvx2 /= n
        sumvy2 /= n

        fatorx = np.sqrt(2 * temp/sumvx2)
        fatory = np.sqrt(2 * temp/sumvy2)
        for p in pt:
            p.vel[0] = (p.vel[0] - sumvx) * fatorx
            p.vel[1] = (p.vel[1] - sumvy) * fatory

    @classmethod
    def mov_pbc(cls, dt, l):
        # Atualização das posições        
        for p in Particle.todas:
            p.pos[0] += p.vel[0] * dt
            p.pos[1] += p.vel[1] * dt
            # Problema de bordas em x
            if p.pos[0] >= l:
                p.bxy[0] += 1
                p.pos[0] = p.pos[0] - l
            if p.pos[0] <= 0:
                p.bxy[0] += -1
                dx = abs(p.pos[0])
                p.pos[0] = l - dx
            # Problema de bordas em y
            if p.pos[1] >= l:
                p.bxy[1] += 1
                p.pos[1] = p.pos[1] - l
            if p.pos[1] <= 0:
                p.bxy[1] += -1
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
        aij = lambda r: 48 * (eps / (sig ** 2)) * (((sig / r) ** 14) - (0.5 * ((sig / r) ** 8)))
        uij = lambda r: 4 * eps * (((sig/r)**12) - ((sig/r)**6))
        ecut = 4 * (1/(rc**12) - 1/(rc**6))
        p = Particle.todas
        n = len(p)
        for i in p:
            i.forc = [0, 0]
            i.pot = 0

        for pi in range(n):
            for pj in range(pi + 1, n):
                dx, dy = immin(p[pi].pos[0], p[pi].pos[1], p[pj].pos[0], p[pj].pos[1], l)
                r = np.hypot(dx, dy)
                if r <= rc:
                    # Cálculo das forças
                    fxi = aij(r) * dx
                    fxj = -fxi
                    fyi = aij(r) * dy
                    fyj = -fyi

                    # Atribuição das forças
                    p[pi].forc[0] += fxi
                    p[pi].forc[1] += fyi
                    p[pj].forc[0] += fxj
                    p[pj].forc[1] += fyj

                    # Cálculo dos potenciais
                    pot = uij(r) - ecut

                    # Atribuição dos potenciais
                    p[pi].pot += pot
                    p[pj].pot += pot

                    # Cálculo da pressão
                    Particle.pressao += np.hypot(fxi, fyi) * r

    @classmethod
    def calcpressao(cls, T, num, l):
        m = 1
        kb = 1
        v = l**2
        rho = (m * len(Particle.todas))/v
        return rho * kb * T + ((Particle.pressao/num)/(2*v))

    @classmethod
    def energias(cls):
        k = 0
        pot = 0
        tot = 0
        sumvx = 0
        sumvy = 0

        n = len(Particle.todas)
        for p in Particle.todas:
            vx = p.vel[0]
            vy = p.vel[1]
            ki = (np.hypot(vx, vy) ** 2) * 0.5
            pi = p.pot
            k += ki
            pot += pi
            tot += ki + pi
            sumvx += vx
            sumvy += vy
        return k / n, pot / n, tot / n, np.hypot(sumvx, sumvy)

    @classmethod
    def rdf(cls, l, switch=0, ngr=0, g=(), size=2):
        p = Particle.todas
        n = len(p)
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
    def msd(cls, l, r0s, switch=0):
        pt = Particle.todas
        n = len(pt)
        if switch == 0:
            drs = 0
            r0s = []
            switch = 1
            for p in pt:
                r0s.append(p.pos)
            return r0s, switch, drs
        if switch == 1:
            drs = 0
            for i in range(n):
                dx = (pt[i].pos[0] + (l * pt[i].bxy[0])) - r0s[i][0]
                dy = (pt[i].pos[1] + (l * pt[i].bxy[1])) - r0s[i][1]
                drs += dx**2 + dy**2
            drs /= n
            return r0s, switch, drs

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


def dinmol(l, n, r, di, eps, sig, T, tf, dt, s, ci='Random'):
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
    start = time.time()
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
        Particle.velnorm(T)

    if ci == 'Triangulo':
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
        Particle.velnorm(T)

    # Integração
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Inicialização das forças    
    Particle.forcas(eps, sig, l)

    # Meio passo da velocidade
    for p in particulas:
        p.vel[0] += p.forc[0] * dt/2
        p.vel[1] += p.forc[1] * dt/2

    # Resto dos passos
    # Inicialização de variáveis de medida e auxiliares
    ngr, g = Particle.rdf(l, switch=0, size=10)
    k, u, tot, tempo, c = [], [], [], [], 0
    # MSD
    cmsd = 0
    teq = 0.75
    r0s, switch, tmax = [], 0, tf/s
    drs = list([] for i in range(s))
    for t in np.arange(0, tf+dt, dt):
        c += 1
        # Dinâmica
        Particle.mov_pbc(dt, l)
        Particle.plot(ax1)
        ax1.set_xlim(0, l)
        ax1.set_ylim(0, l)
        ax1.set_title(f'Partículas | n = {len(particulas)}')

        # MSD
        if (cmsd * tmax) + (tmax * teq) <= t <= (cmsd * tmax) + tmax:
            r0s, switch, drsi = Particle.msd(l, r0s, switch=switch)
            drs[cmsd].append(drsi)
            ''' Faz um contador pra limitar o número de valores em cada espaço de tempo '''
        if t > (cmsd * tmax) + tmax:
            switch = 0
            cmsd += 1

        # RDF
        if t > tf/2:
            ngr, g = Particle.rdf(l, switch=1, ngr=ngr, g=g, size=10)

        # Energias
        if c % 10 == 0:
            cin, pot, to, vcm = Particle.energias()
            k.append(cin)
            u.append(pot)
            tot.append(to)
            tempo.append(t)
            # Cinetica
            ax2.plot(tempo, k,  marker='+', color='r', linewidth=.1)
            ax2.set_title(f'Energias\n vcm = {vcm}')
            ax2.set(xlabel='t', ylabel='E/n')

            # Potencial
            ax2.plot(tempo, u,  marker='^', color='b', linewidth=.1)

            # Total
            ax2.plot(tempo, tot, marker='*', color='k', linewidth=.1)

        fig.suptitle(f'Potencial Lennard-Jones\nPassos = {c:>5} | dt = {dt} | t = {t:>3.1f}')
        if t == tf-dt:
            fig.savefig(f'MD_lj_'+str(dt)[2:]+'.png')
        plt.pause(0.0001)
        ax1.cla()

    # Plot da RDF
    g = Particle.rdf(l, switch=2, ngr=ngr, g=g, size=10)
    rs = np.linspace(0, l/2, len(g))
    plt.figure(4, figsize=(15, 5))
    plt.subplot(121)
    plt.plot(rs, g)
    plt.title(f'Função de Distribuição Radial\nn = {n**2} | Ti = {T}')
    plt.xlabel('r')
    plt.ylabel('g(r)')
    plt.grid()

    # Plot do MSD
    #igualar os tamanhos
    sizes = []
    for j in range(s):
        sizes.append(len(drs[j]))
    sz = min(sizes)
    for j in range(s):
        if len(drs[j]) > sz:
            drs[j].pop()

    msd = np.asarray(drs[0])
    for i in range(1, s):
        msd += np.asarray(drs[i])
    msd = msd/s
    tm = np.linspace(teq * tmax, tmax+dt, len(msd))
    plt.subplot(122)
    plt.plot(tm, msd)
    plt.xlabel('t (s)')
    plt.ylabel('MSD (m^2)')
    plt.xscale('log')
    plt.yscale('log')
    plt.title(f'Desvio quadrático médio\n tf = {tf} | dt = {dt}')
    plt.grid('log')
    plt.savefig('RDF_MSD.png')

    pressao = Particle.calcpressao(T, c, l)
    end = time.time()
    exec = end - start
    ark = open('MD_info.txt', 'w', encoding='utf-8')
    ark.write(f'-*- Dinâmica Molecular -*-\n'
              f'l = {l}\nn = {n}\nr = {r}\ndi = {di}\neps = {eps}\nsig = {sig}\nT = {T}\ntf = {tf}\ndt = {dt}\n'f'ci = {ci}\n'
              f'Pressão = {pressao:.2f}\nDensidade = {len(particulas)/(l**2):.2f}m^-2\nTempo de execução = {exec:.2f}s')
    ark.close()


l = 10
n = 10
r = .3
di = .4
eps = 1
sig = 1
T = .5
tf = 6.45
dt = .01
s = 3
ci = 'Triangulo'
dinmol(l, n, r, di, eps, sig, T, tf, dt, s, ci)

'''
Essa energia total tá certa?
Talvez o msd esteja certo agora
'''
