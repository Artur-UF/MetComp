import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.fft import *
from scipy.integrate import odeint


def rhs(u0, t, kappa, c):
    uhat = fft(u0)
    duhatx = 1.0j * kappa * uhat
    dux = ifft(duhatx).real
    dut = -c * dux
    return dut


N = 128
L = 50
dx = L/N
x = np.arange(-L/2, L/2, dx)
c = 100
size = len(x)

# Os coeficientes
kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)


# Vetor de estado
y0 = norm.pdf(x, loc=0, scale=5)


dt = .01
tf = 10
t = np.arange(0, tf, dt)

u = odeint(rhs, y0, t, args=(kx, c))

for i in range(len(t)):
    plt.plot(x, u[i])
    plt.title(f'passo = {i}')
    plt.grid()
    plt.pause(0.001)
    plt.cla()


'''
for ti in t:
    y0 += dt*rhs(y0, kx, c)
    plt.plot(x, y0)
    plt.title(f't = {ti:.3f}')
    plt.grid()
    plt.pause(0.001)
    plt.cla()
'''