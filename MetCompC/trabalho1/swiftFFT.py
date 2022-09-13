import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import *
import time
import copy
start = time.time()
seed = 597
np.random.seed(seed)


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
L = 25
dx = L/N
dy = dx
x = np.arange(-L/2, L/2, dx)
y = np.arange(-L/2, L/2, dy)
size = len(x)

# Os coeficientes
kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(N, d=dy)
kappax, kappay = np.meshgrid(kx, ky)

# Vetor de estado
#u0 = np.random.randn(size, size)
u0 = np.random.uniform(-1, 1, (size, size))

track = [copy.deepcopy(u0)]

r = 0.4
dt = 0.0001
tf = 20
t = np.arange(0, tf, dt)
c = 0
for ti in t:
    c += 1
    u0 += dt * rhs(u0, kappax, kappay, r)
    if c % 200 == 0:
        track.append(copy.deepcopy(u0))
    if ti % 2 == 0:
        print(f't = {ti}')
end = time.time()
tempo = end-start

plt.imshow(u0, origin='lower', vmin=-1, vmax=1)
plt.colorbar()
plt.title(f'Swift-Hohenberg\nr = {r} | passos = {len(t)} | dx = {dx:.3f}')
plt.savefig(f'pltSH-r{r}-t{tf}.png', dpi=300)
track = np.asarray(track)
np.save(f'SH-r{r}-t{tf}.npy', track)
ark = open(f'infoSH-r{r}-t{tf}.txt', 'w')

ark.write(f'Integração de Swift-Hohenberg\n'
          f'Tempo total = {tf}\n'
          f'dx = {dx}\n'
          f'dt = {dt}\n'
          f'r = {r}\n'
          f'passos = {len(t)}\n'
          f'numpy seed = {seed}\n')
if tempo > 60:
    ark.write(f'Tempo de execução = {tempo/60:.3f}min\n')
else:
    ark.write(f'Tempo de execução = {tempo:.3f}s\n')
ark.close()
