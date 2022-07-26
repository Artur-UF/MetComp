import numpy as np
import matplotlib.pyplot as plt
from random import uniform


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


def simula(xa, xb, va, vb, r, tf, dt):
    ma, mb = 1, 2
    r0 = xa + ((xb - xa)*mb)/(ma + mb)
    k = 10

    fig, ax = plt.subplots()

    f1p = lambda x1, x2: -k * (x1 - r0)
    fa = lambda x1, x2: k * ((x2 - x1) - r0)
    fb = lambda x1, x2: -k * ((x2 - x1) - r0)
    f2p = lambda x1, x2: -k * (x2 - 2 * r0)

    pa = Particle(r, [xa, 0], va, fa(xa, xb) + f1p(xa, xb), ma, 'blue')
    pb = Particle(r, [xb, 0], vb, fb(xa, xb) + f2p(xa, xb), mb, 'red')
    parts = [pa, pb]
    fs = [f1p, fa, fb, f2p]
    for i in range(0, 2, 2):
        parts[i].vel += ((fs[i](pa.pos[0], pb.pos[0]) + fs[i+1](pa.pos[0], pb.pos[0])) * dt) / 2
    t = np.arange(0, tf, dt)
    for ti in t:
        for p in parts:
            p.pos[0] = p.pos[0] + p.vel*dt
        for i in range(0, 2, 2):
            parts[i].forc = fs[i](pa.pos[0], pb.pos[0]) + fs[i+1](pa.pos[0], pb.pos[0])
        for p in parts:
            p.vel += (p.forc*dt)/2
        Particle.plot(ax)
        plt.grid()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlim(-.5, 8)
        plt.ylim(-1, 1)
        plt.vlines(r0, -.5, .5)
        plt.vlines(0, -.5, .5)
        plt.vlines(3 * r0, -.5, .5)
        plt.pause(0.001)
        plt.cla()


xa = 1
xb = 3
va = .1
vb = -.1
r = .3
tf = 10
dt = .1
simula(xa, xb, va, vb, r, tf, dt)

