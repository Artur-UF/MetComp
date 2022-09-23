import numpy as np
from numba import njit
from time import time
import os
start = time()


@njit
def ising(n, nup, j, beta, rep):
    M = lambda up: 2 * up - n
    delE = lambda M: ((2 * j)/n) * (M - 1)
    h = -(j * (M(nup)**2)) / n
    for r in range(rep):
        # Proposta
        nupaux = nup
        prob = np.random.randint(1, n+1)
        if prob <= nupaux:
            nupaux -= 1
            delta = delE(-M(nupaux))
        if prob > nupaux:
            nupaux += 1
            delta = delE(M(nupaux))

        # Decidir se aceito ou não        
        if delta <= 0:
            h += delta
            nup = nupaux
        if delta > 0:
            odd = np.random.random(1)
            flip = np.exp(-beta * delta)
            if odd < flip:
                h += delta
                nup = nupaux
    return h, M(nup), nup

n = 1000
nup = 0
j = 1
beta = .5
rep = 10000
h, M, up = ising(n, nup, j, beta, rep)
print(f'Energia = {h}')
print(f'Magnetização = {M}')
print(f'Nups = {up}')
print(time() - start)

ark = open(path+f'/ising_nup{nup}.txt', 'w')
ark.write(f'Energia = {h}\nMagnetização = {M}')
ark.close()

