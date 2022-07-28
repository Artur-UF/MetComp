import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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


def molas_acop():
    n = 10
    r0 = 1
    xa = 1.3
    xb = 2
    va = 0
    vb = 0
    r = .2
    tf = 40
    dt = .1
    ma, mb = 1, 1
    k = 10

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

        yield parts, ti, r0, n


fig, ax = plt.subplots()


def init():
    '''
    É o inicio de todo frame após o 'run'
    '''
    ax.clear()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()


def run(i):
    parts, ti, r0, n = i

    Particle.plot(ax)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-.5, (n + 2) * r0)
    ax.set_ylim(-1, 1)
    for i in range(len(parts) + 2):
        ax.vlines(i * r0, -.5, .5, colors='k', linewidth=.1)
    ax.set_title(f'Molas acopladas\nt = {ti:>5.1f}')


ani = animation.FuncAnimation(fig, run, molas_acop, interval=1500, init_func=init, save_count=1500)
#plt.show()
writergif = animation.PillowWriter(fps=30)
ani.save(r'D:\Aplicações\GItHub D\MetCompA\MetCompC\aula7\molas_acop.gif', writer=writergif)
plt.close()
