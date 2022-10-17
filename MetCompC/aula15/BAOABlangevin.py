import numpy as np
from time import time
import os
seed = 420
np.random.seed(seed)


class Particle:
    todas = []

    def __init__(self, p, v):
        self.pos = p
        self.vel = v
        self.todas.append(self)

    def baoab_livre(self, dt, exp, sqexp, sqt, G):
        # 1/2 passo da distância
        self.pos[0] += self.vel[0]*(dt/2)
        self.pos[1] += self.vel[1]*(dt/2)
        # Passo estocástico
        self.vel[0] = exp*self.vel[0] + sqexp*sqt*G[0]
        self.vel[1] = exp*self.vel[1] + sqexp*sqt*G[1]
        # Atualização final da posição
        self.pos[0] += self.vel[0]*(dt/2)
        self.pos[1] += self.vel[1]*(dt/2)

    def baoab_duplo(self, dt, exp, sqexp, sqt, G, g, a, b):
        fr = lambda x, y, vx, vy: - a*np.hypot(x, y)**3 + b*np.hypot(x, y)
        fx = lambda x, y, vx, vy: fr(x, y, vx, vy)*(x/np.hypot(x, y))
        fy = lambda x, y, vx, vy: fr(x, y, vx, vy)*(y/np.hypot(x, y))

        # Primeiro cálculo de forças
        fxx = fx(self.pos[0], self.pos[1], self.vel[0], self.vel[1])
        fyy = fy(self.pos[0], self.pos[1], self.vel[0], self.vel[1])
        # 1/2 passo das velocidades
        self.vel[0] += fxx*(dt/2)
        self.vel[1] += fyy*(dt/2)
        # 1/2 passo da distância
        self.pos[0] += self.vel[0] * (dt / 2)
        self.pos[1] += self.vel[1] * (dt / 2)
        # Passo estocástico
        self.vel[0] = exp * self.vel[0] + sqexp * sqt * G[0]
        self.vel[1] = exp * self.vel[1] + sqexp * sqt * G[1]
        # Atualização final da posição
        self.pos[0] += self.vel[0] * (dt / 2)
        self.pos[1] += self.vel[1] * (dt / 2)
        # Atualização das forças
        fxx = fx(self.pos[0], self.pos[1], self.vel[0], self.vel[1])
        fyy = fy(self.pos[0], self.pos[1], self.vel[0], self.vel[1])
        # Atualização das velocidades
        self.vel[0] += fxx*(dt/2)
        self.vel[1] += fyy*(dt/2)

    def msd(self, r0, dr, switch):  # Essa é uma medição para n partículas né?
        if switch == 0:
            r0 = [self.pos[0], self.pos[1]]   # Posição de referência nesse ciclo
            dr = 0                            # Desvio no tempo de referência 0
            switch = 1
            return r0, dr, switch
        if switch == 1:
            dx = self.pos[0] - r0[0]        # Desvio em x
            dy = self.pos[1] - r0[1]    # Desvio em y
            dr = dx**2 + dy**2          # Desvio quadrático
            return r0, dr, switch


def dinmol(x0, y0, vx0, vy0, passos, dt, g, a, b, T, cic, POT='Livre'):
    start = time()
    p1 = Particle([x0, y0], [vx0, vy0])

    t = np.arange(passos)

    G = np.random.randn(passos, 2)
    exp = np.exp(-g*dt)
    sqexp = np.sqrt(1-np.exp(-2*g*dt))
    sqt = np.sqrt(T)
    track = [[], [], [], []]

    # MSD
    ciclos = cic
    cat = 1
    tmax = int(passos/ciclos)
    cont = 0
    r0 = 0
    dr = 0
    switch = 0
    arrmsd = np.zeros(tmax+1)
    if POT == 'Livre':
        pasta = 'BAOAB_livre'
        for ti in t:
            p1.baoab_livre(dt, exp, sqexp, sqt, G[ti])

            track[0].append(p1.pos[0])
            track[1].append(p1.pos[1])
            track[2].append(p1.vel[0])
            track[3].append(p1.vel[1])

            # MSD
            if cont < tmax:
                r0, dr, switch = p1.msd(r0, dr, switch)
                arrmsd[cont] += dr
            cont += 1
            if cont >= tmax:
                cat += 1
                switch = 0
                cont = 0

    else:
        pasta = 'BAOAB_duplo'
        for ti in t:
            p1.baoab_duplo(dt, exp, sqexp, sqt, G[ti], g, a, b)
            track[0].append(p1.pos[0])
            track[1].append(p1.pos[1])
            track[2].append(p1.vel[0])
            track[3].append(p1.vel[1])
    track = np.asarray(track)
    arrmsd /= ciclos

    # Criação do arquivo de resultados
    path = os.path.join(os.getcwd(), pasta+f'_g{g}T{T}tf{tf}')
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    np.save(path+f'/langevin_g{g}T{T}tf{tf}.npy', track)
    np.save(path+f'/msd_g{g}T{T}tf{tf}.npy', arrmsd)

    ark = open(path+f'/info_g{g}T{T}tf{tf}.txt', 'w')
    ark.write(f'dt = {dt}\n'
              f'tf = {tf}\n'
              f'g = {g}\n'
              f'a = {a}\n'
              f'b = {b}\n'
              f'T = {T}\n'
              f'cic = {cic}\n'
              f'POT = \'{POT}\'\n'
              f'Seed = {seed}\n'
              f'Passos = {passos}\n'
              f'Tempo de execução = {time() - start:.3f}s')


x0 = 1
y0 = 0
vx0 = 0
vy0 = 0
dt = 0.01
tf = 10
passos = int(tf/dt)
g = 10
a = 0.25
b = 1
T = 1
cic = 100
POT = 'Livre' #'Duplo'

dinmol(x0, y0, vx0, vy0, passos, dt, g, a, b, T, cic, POT=POT)



