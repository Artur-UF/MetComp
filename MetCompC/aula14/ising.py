import numpy as np
from numba import njit
from time import time
start = time()


@njit
def ising(n, nup, j, beta, rep):
    M = lambda up: 2 * up - n
    delE = lambda M: ((2 * j)/n) * (M - 1)
    h = -(j * (M(nup)**2)) / n
    for r in range(rep):
        #print(nup)
        nupaux = nup
        prob = np.random.randint(1, n+1)
        if prob <= nupaux:
            nupaux -= 1
            delta = delE(-M(nupaux))
        if prob > nupaux:
            nupaux += 1
            delta = delE(M(nupaux))
        if delta <= 0:
            h += delta
            nup = nupaux
        if delta > 0:
            odd = np.random.random(1)
            flip = np.exp(-beta * delta)
            if odd > flip:
                nup = nupaux
    return h, M(nup), nup


n = 1000
nup = 1000
j = 1
beta = .5
rep = 10**6
h, M, up = ising(n, nup, j, beta, rep)
print(h)
print(M)
print(up)
print(time() - start)
