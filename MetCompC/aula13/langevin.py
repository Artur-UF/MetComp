import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import matplotlib.patches as pt


class Particle:
    todas = []

    def __init__(self, r, p, v):
        self.raio = r
        self.pos = p
        self.vel = v
        self.todas.append(self)

    def mov_pbc(self, dt, lim, g, G, escala):
        # Forças aleatórias
        fx, fy = sp.norm.rvs(loc=0, scale=escala, size=2)
        # Velocidades
        self.vel[0] += -g*self.vel[0]*dt + np.sqrt(dt*G)*fx
        self.vel[1] += -g*self.vel[1]*dt + np.sqrt(dt*G)*fy
        # Posições
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
    def run_pbc(cls, dt, lim):
        for i in Particle.todas:
            i.mov_pbc(dt, lim)

    @classmethod
    def plot(cls, ax):
        for p in Particle.todas:
            circ = plt.Circle(p.pos, p.raio, edgecolor='k')
            arrow = pt.FancyArrow(p.pos[0], p.pos[1], p.vel[0], p.vel[1], head_width=0.05, head_length=0.1)
            ax.add_patch(circ)
            ax.add_patch(arrow)


def dinmol(x0, y0, vx0, vy0, l, r, tf, dt, gamma, Gamma):
    n = l//(2*r)
    # Largura da distribuição de velocidades
    escala = 1

    p1 = Particle(r, [x0, y0], [vx0, vy0])

    # TU PAROU AQUI
    fig, ax1 = plt.subplots(figsize=(10, 10))

    track = [[], [], [], []]
    t = np.arange(0, tf, dt)
    for ti in t:
        Particle.plot(ax1)
        p1.mov_pbc(dt, l, gamma, Gamma, escala)
        track[0].append(p1.pos[0])
        track[1].append(p1.pos[1])
        track[2].append(p1.vel[0])
        track[3].append(p1.vel[1])
        ax1.set_xlim(0, l)
        ax1.set_ylim(0, l)
        ax1.grid()
        ax1.set_title(f'Equação de Langevin\n'+r'$\gamma$ = '+f'{gamma}'
                      +r' | $\Gamma$ = '+f'{Gamma}'+f' | t = {ti:<4.1f}')
        ax1.plot(track[0], track[1], 'r', linewidth=1)
        plt.pause(.01)
        plt.cla()
    ax1.plot(track[0], track[1], 'r', linewidth=1)
    plt.grid()
    ax1.set_title(f'Equação de Langevin\n' + r'$\gamma$ = ' + f'{gamma}'
                  + r' | $\Gamma$ = ' + f'{Gamma}' + f' | t = {tf}')
    plt.savefig('langavin.png')
    track = np.asarray(track)
    np.save('tracker_langavin.npy', track)


l = 10
x0 = l/2
y0 = l/2
vx0 = 0
vy0 = 0
r = .3
dt = 0.05
tf = 20
gamma = 1
Gamma = .5


dinmol(x0, y0, vx0, vy0, l, r, tf, dt, gamma, Gamma)




