import numpy as np
import scipy.stats as sp
import time


class Particle:
    todas = []

    def __init__(self, p, v):
        self.pos = p
        self.vel = v
        self.todas.append(self)

    def mov_pbc(self, dt, taup, Dt, escala):
        # Forças aleatórias
        fx, fy = sp.norm.rvs(loc=0, scale=escala, size=2)
        # Velocidades
        self.vel[0] += -(1/taup)*self.vel[0]*dt + np.sqrt(dt*2*Dt)*fx
        self.vel[1] += -(1/taup)*self.vel[1]*dt + np.sqrt(dt*2*Dt)*fy
        # Posições
        self.pos[0] += dt*self.vel[0]
        self.pos[1] += dt*self.vel[1]


def dinmol(x0, y0, vx0, vy0, escala, passos, dt, taup, Dt):
    p1 = Particle([x0, y0], [vx0, vy0])

    t = np.arange(passos+1)
    ark = open(f'langevin_tau{taup}Dt{Dt}.txt', 'w')
    for ti in t:
        p1.mov_pbc(dt, taup, Dt, escala)
        if ti % 100 == 0:
            ark.write(f'{ti*dt},{p1.pos[0]},{p1.pos[1]},{p1.vel[0]},{p1.vel[1]}\n')
    ark.close()


start = time.time()

x0 = 0
y0 = 0
vx0 = 0
vy0 = 0
escala = 1
passos = 1e6
dt = 0.01
taup = [0.1, 1, 10, 100]
Dt = 0.5
for tau in taup:
    dinmol(x0, y0, vx0, vy0, escala, passos, dt, tau, Dt)

end = time.time()
print(f'Tempo de execução = {end-start}')

