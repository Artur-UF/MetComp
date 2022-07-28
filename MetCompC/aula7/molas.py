'''
Simulação de n molas acopladas
'''

import numpy as np
import matplotlib.pyplot as plt


class Particle:
    todas = []

    def __init__(self, r, p, v, f, m, cor):
        self.raio = r
        self.pos = p
        self.vel = v
        self.mass = m
        self.forc = f
        self.c = cor
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
            circ = plt.Circle(p.pos, p.raio, color=p.c)
            ax.add_patch(circ)


def molas_acop(n, r0, xa, xb, va, vb, r, tf, dt):
    ma, mb = 1, 1
    k = 10

    fig, ax = plt.subplots()

    f1p = lambda x1, x2: -k * (x1 - r0)
    f12 = lambda x1, x2: k * ((x2 - x1) - r0)
    f21 = lambda x1, x2: -k * ((x2 - x1) - r0)
    f2p = lambda x1, x2: -k * (x2 - n * r0)

    # Criação das partículas
    parts = [Particle(r, [xa, 0], va, 0, ma, 'red')]
    for i in range(1, n):
        parts.append(Particle(r, [(i + 1) * r0, 0], vb, 0, mb, 'red'))

    # -*- Forças iniciais -*-

    # Paredes
    parts[0].forc = f1p(parts[0].pos[0], parts[1].pos[0]) + f12(parts[0].pos[0], parts[1].pos[0])
    parts[-1].forc = f2p(parts[-2].pos[0], parts[-1].pos[0]) + f21(parts[-2].pos[0], parts[-1].pos[0])

    # Meio do sistema
    for i in range(1, n - 1):
        parts[i].forc = f21(parts[i-1].pos[0], parts[i].pos[0]) + f12(parts[i].pos[0], parts[i+1].pos[0])

    # -*- Meio passo para a velocidade -*-

    # Paredes
    parts[0].vel += ((f1p(parts[0].pos[0], parts[1].pos[0]) + f12(parts[0].pos[0], parts[1].pos[0])) * dt) / 2
    parts[-1].vel += ((f2p(parts[-2].pos[0], parts[-1].pos[0]) + f21(parts[-2].pos[0], parts[-1].pos[0])) * dt) / 2

    # Meio do sistema
    for i in range(1, n - 1):
        parts[i].vel += (f21(parts[i-1].pos[0], parts[i].pos[0]) + f12(parts[i].pos[0], parts[i+1].pos[0])) * (dt/2)
    t = np.arange(0, tf, dt)

    # O resto do método
    for ti in t:
        for p in parts:
            p.pos[0] = p.pos[0] + p.vel*dt

        # -*-Atualizão da força -*-

        # Paredes
        del parts[0].forc
        del parts[-1].forc
        parts[0].forc = (f1p(parts[0].pos[0], parts[1].pos[0]) + f12(parts[0].pos[0], parts[1].pos[0]))
        parts[-1].forc = (f2p(parts[-2].pos[0], parts[-1].pos[0]) + f21(parts[-2].pos[0], parts[-1].pos[0]))

        # Meio do sistema
        for i in range(1, n - 1):
            del parts[i].forc
            parts[i].forc = f21(parts[i - 1].pos[0], parts[i].pos[0]) + f12(parts[i].pos[0], parts[i + 1].pos[0])

        for p in parts:
            p.vel += (p.forc*dt)/2
        Particle.plot(ax)
        plt.grid()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlim(-.5, (n+2) * r0)
        plt.ylim(-1, 1)

        for i in range(len(parts) + 2):
            plt.vlines(i * r0, -.5, .5)

        plt.title(f'Molas acopladas\nt = {ti:>5.1f}')
        plt.pause(0.001)
        plt.cla()


n = 10
r0 = 1
xa = 1.3
xb = 2
va = 0
vb = 0
r = .2
tf = 20
dt = .1

molas_acop(n, r0, xa, xb, va, vb, r, tf, dt)
