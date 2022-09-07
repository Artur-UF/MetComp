import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import *


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


N = 64
L = 50
dx = L/N
dy = dx
r = -0.1
x = np.arange(-L/2, L/2, dx)
y = np.arange(-L/2, L/2, dy)
size = len(x)

# Os coeficientes
kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(N, d=dy)
kappax, kappay = np.meshgrid(kx, ky)
'''print(kappax)
plt.scatter(range(len(kappax[0])), kappax[0])
plt.scatter(range(len(kappay[0])), kappay[0])
plt.grid()
plt.show()
'''
# Vetor de estado
u0 = np.random.randn(size, size)

allstates = [u0]

dt = 0.0001
tf = 1
t = np.arange(0, tf, dt)
figure = plt.figure(1)
plt.imshow(u0, cmap='viridis', vmin=0, vmax=.8)
plt.colorbar()
for ti in t:
    passo = np.where(t == ti)[0][0]
    u0 += dt * rhs(u0, kappax, kappay, r)
    if passo % 15 == 0:
        allstates.append(u0)
        plt.imshow(u0, cmap='viridis', vmin=-1, vmax=1)
        plt.title(f'Swift-Hohenberg\n r = {r} | passo = {passo} | t = {ti:.3f}')
        plt.pause(0.001)
        plt.cla()
allstates = np.asarray(allstates)
np.save('swiftanimgen.npy', allstates)
