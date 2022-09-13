import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import *
np.random.seed(63)


def laplace(uhat, k2):
    laplaciano = - k2*uhat
    return laplaciano


def rhs2SH(u, k2, r):
    uhat = rfft2(u)
    duhatp1 = (r-1)*uhat - 2*laplace(uhat, k2) - laplace(laplace(uhat, k2), k2)
    dut = irfft2(duhatp1).real - u**3
    return dut


nodes = 64
x, dx = np.linspace(0, 1, nodes, retstep=True)

# Os coeficientes
kx = 2 * np.pi * rfftfreq(nodes, d=dx)
ky = 2 * np.pi * fftfreq(nodes, d=dx)
kappax, kappay = np.meshgrid(kx, ky)
k2 = kappax**2 + kappay**2

# Vetor de estado
u0 = np.random.uniform(-1, 1, (nodes, nodes))
uhat = rfft2(u0**3)

track = [u0]

dt = 1e-5
tf = .5
t = np.arange(0, tf, dt)
r = -0.01

figure = plt.figure(1)
plt.imshow(track[0], cmap='viridis', vmin=-1, vmax=1)
plt.colorbar()
c = 0

for ti in t:
    c += 1
    u0 += dt * rhs2SH(u0, k2, r)
    if c % 100 == 0:
        track.append(u0)
        plt.imshow(track[c//100], cmap='viridis', vmin=-1, vmax=1)
        plt.title(f'Swift-Hohenberg\n r = {r} | passo = {c} | t = {ti:.3f}')
        plt.pause(0.0001)
        plt.cla()

track = np.asarray(track)
np.save('../testes/swiftanimgen.npy', track)
