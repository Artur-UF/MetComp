import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as sp

#u = np.load('swiftanimgen.npy')

N = 64
L = 50
dx = L/N
dy = dx
r = 0
x = np.arange(-L/2, L/2, dx)
y = np.arange(-L/2, L/2, dy)
size = len(x)

# Os coeficientes
kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(N, d=dy)
kappax, kappay = np.meshgrid(kx, ky)
kx2 = 2 * np.pi * sp.fftfreq(N, d=dx)
ky2 = 2 * np.pi * sp.fftfreq(N, d=dy)
kappax2, kappay2 = np.meshgrid(kx2, ky2)
#print(kappax)
#figure = plt.figure(figsize=(10, 5))
#plt.subplots(121)
'''
plt.scatter(range(len(kappax[0])), kappax[0])
plt.scatter(range(len(kappay[0])), kappay[0])
plt.grid()
'''
#plt.subplots(122)
plt.scatter(range(len(kappax2[0])), kappax2[0])
plt.scatter(range(len(kappay2[0])), kappay2[0])
plt.grid()

plt.show()



