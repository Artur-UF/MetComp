import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import *
np.random.seed(63)


def laplace(uhat, k2):
    laplaciano = - k2*uhat
    return laplaciano


def rhs2SH(u, k2, r):
    uhat = rfft2(u)
    uhat3 = rfft2(u**3)
    duhat = (r-1)*uhat - 2*laplace(uhat, k2) - laplace(laplace(uhat, k2), k2) - uhat3
    dut = irfft2(duhat).real
    return dut


def rhs(u, kappax, kappay, r):
    '''
    Calcula o lado direito da EDP
    '''
    kpx2 = np.power(kappax, 2)
    kpx4 = np.power(kappax, 4)
    kpy2 = np.power(kappay, 2)
    kpy4 = np.power(kappay, 4)
    uhat = fft2(u)
    uhat3 = fft2(u**3)
    duhatx2 = kpx2 * uhat
    duhaty2 = kpy2 * uhat
    duhatx4 = kpx4 * uhat
    duhaty4 = kpy4 * uhat
    duhatxy = kpx2 * kpy2 * uhat
    duhat = (r - 1)*uhat + 2*duhatx2 + 2*duhaty2 - duhatx4 - duhaty4 - 2*duhatxy - uhat3
    dut = ifft2(duhat)
    return dut.real


nodes = 64
x, dx = np.linspace(0, 1, nodes, retstep=True)

# Os coeficientes
kx = rfftfreq(nodes, d=dx/(2 * np.pi))
ky = fftfreq(nodes, d=dx/(2 * np.pi))
kappax, kappay = np.meshgrid(kx, ky)
k2 = kappax**2 + kappay**2

# Vetor de estado
u0 = np.random.uniform(-1, 1, (nodes, nodes))
uhat = rfft2(u0**3)

track = [u0]

dt = 1e-6
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
    #print(u0)
    if c % 15 == 0:
        track.append(u0)
        #print(u0)
        plt.imshow(track[c//15], cmap='viridis', vmin=-1, vmax=1)
        plt.title(f'Swift-Hohenberg\n r = {r} | passo = {c} | t = {ti:.3f}')
        plt.pause(0.001)
        plt.cla()

track = np.asarray(track)
np.save('testes/swiftanimgen.npy', track)
