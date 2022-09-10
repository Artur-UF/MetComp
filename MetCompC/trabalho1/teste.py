import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sp


arr = np.arange(0, 10, 0.1)
print(len(arr))




'''
u = np.load('swiftanimgen.npy')
print(len(u))
for i in u:
    plt.imshow(i, vmin=-1, vmax=1)
    plt.title(f'{np.where(i == u)[0]}')
    plt.pause(0.001)


N = 64
L = 50
dx = L/N
dy = dx
r = 0
x = np.arange(-L/2, L/2, dx)
y = np.arange(-L/2, L/2, dy)
size = len(x)

# Os coeficientes
kx = 2 * np.pi * sp.fftfreq(N, d=dx)
ky = 2 * np.pi * sp.fftfreq(N, d=dy)
kappax, kappay = np.meshgrid(kx, ky)
plt.figure(1)
plt.scatter(range(len(kappax[0])), kappax[0], label='kappax')
plt.scatter(range(len(kappay[0])), kappay[0], label='kappay')
plt.grid()
plt.legend()
plt.savefig('coeficientesFFT.png')
'''


