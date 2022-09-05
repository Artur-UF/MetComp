import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import *

N = 128
L = 50
dx = L/N
dy = dx
r = -0.1
x = np.arange(-L/2, L/2, dx)
y = np.arange(-L/2, L/2, dy)

# Os coeficientes
kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(N, d=dy)
kappax, kappay = np.meshgrid(kx, ky)

# Vetor de estado
u0 = np.random.rand(len(x), len(x))

dt = .01
tf = 10
t = np.arange(0, tf, dt)

# Ir para o espaço K
def rhs(u, kappax, kappay, r):
    kpx2 = np.power(kappax, 2)
    kpx4 = np.power(kappax, 4)
    kpy2 = np.power(kappay, 2)
    kpy4 = np.power(kappay, 4)
    uhat = fft2(u)
    duhatx2 = kpx2 * uhat
    duhaty2 = kpy2 * uhat
    duhatx4 = kpx4 * uhat
    duhaty4 = kpy4 * uhat
    duhatxy = kpx2 * kpy2 * uhat
    dux2 = ifft2(duhatx2)
    duy2 = ifft2(duhaty2)
    dux4 = ifft2(duhatx4)
    duy4 = ifft2(duhaty4)
    duxy = ifft2(duhatxy)
    dut = (r - 1)*u - 2*dux2 - 2*duy2 - dux4 - duy4 - 2*duxy - u**3
    return dut.real


for ti in t:
    plt.imshow(u0)
    plt.pause(0.001)
    plt.cla()
    u0 += dt*rhs(u0, kappax, kappay, r)
