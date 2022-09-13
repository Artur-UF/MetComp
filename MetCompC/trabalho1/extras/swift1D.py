import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as sp
from scipy.integrate import odeint


def rhs(u0, t, kappa, r):
    uhat = sp.fft(u0)
    uhat3 = sp.fft(u0**3)
    duhat2 = (kappa**2) * uhat
    duhat4 = (kappa**4) * uhat
    duhat = (r - 1)*uhat + 2*duhat2 - duhat4 - uhat3
    dut = sp.ifft(duhat).real
    return dut


N = 128
L = 150
dx = L/N
r = -0.1
x = np.arange(-L/2, L/2, dx)
size = len(x)

# Os coeficientes
kappa = 2 * np.pi * sp.fftfreq(N, d=dx)

u0 = np.random.randn(size)

dt = 0.01
tf = 50
t = np.arange(0, tf, dt)

u = odeint(rhs, u0, t, args=(kappa, r))

for i in range(len(t)):
    plt.plot(x, u[i])
    plt.title(f'Swift-Hohenberg 1-D\n r = {r} | passo = {i} | t = {t[i]:.2f}')
    plt.grid()
    plt.ylim(-1, 1)
    plt.pause(0.001)
    plt.cla()

'''
for ti in t:
    passo = np.where(ti == t)[0]
    if passo % 15 == 0:
        plt.plot(x, u0)
        plt.title(f'Swift-Hohenberg 1-D\n r = {r} | t = {ti:.4f}')
        plt.ylim(0, 1)
        plt.grid()

        plt.pause(0.001)
        plt.cla()
    u0 += dt*rhs(u0, kappa, r)
'''


