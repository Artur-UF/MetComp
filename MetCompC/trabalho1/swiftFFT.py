import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import *
import time
import copy
import os
start = time.time()
seed = 666
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


# Todos os parâmetros estão aqui:
N = 256
L = 100
dx = L/N
r = 0.4
dt = 0.0001
tf = 10
checkpoint = 500
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
x = np.arange(-L/2, L/2, dx)
y = np.arange(-L/2, L/2, dx)
size = len(x)

# Os coeficientes
kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
ky = 2 * np.pi * np.fft.fftfreq(N, d=dx)
kappax, kappay = np.meshgrid(kx, ky)

# Matriz do estado inicial
#u0 = np.random.uniform(-1, 1, (size, size))

x = size
k = -5
u0 = np.eye(x, k=k)
c = 1
for i in range(2*x-1):
    c *= -1
    k += 1
    u0 += np.eye(x, k=k)*c


# Array da evolução temporal
track = [copy.deepcopy(u0)]

# A integração ocorre aqui
c = 0
t = np.arange(0, tf, dt)
for ti in t:
    c += 1
    u0 += dt * rhs(u0, kappax, kappay, r)
    if c % checkpoint == 0:
        track.append(copy.deepcopy(u0))
    if ti % 2 == 0:
        print(f't = {ti}')

# Criação do arquivo de resultados
path = os.path.join(os.getcwd(), f'SH_r{r}_t{tf}')
try:
    os.mkdir(path)
except FileExistsError:
    pass

# Gerando o plot do último passo temporal
plt.imshow(u0, origin='lower', vmin=-1, vmax=1)
plt.colorbar()
plt.title(f'Swift-Hohenberg\nr = {r} | passos = {len(t)} | tf = {tf} | dt = {dt}')
plt.savefig(path+f'/SH-plot.png', dpi=300)

# Salvando a evolução temporal
track = np.asarray(track)
np.save(path+f'/SH-array.npy', track)

# Escrevendo o arquivo de informações
ark = open(path+f'/info-SH.txt', 'w')
ark.write(f'Integração de Swift-Hohenberg\n'
          'Para gerar a animação copie+cole os 3 primeiros parâmetros em animswift.py\n'
          f'checkpoint = {checkpoint}\n'
          f'tf = {tf}\n'
          f'r = {r}\n'
          f'dt = {dt}\n'
          f'dx = {dx}\n'
          f'passos = {len(t)}\n'
          f'numpy seed = {seed}\n')
end = time.time()
tempo = end-start
if tempo > 60:
    ark.write(f'Tempo de execução = {tempo/60:.3f}min\n')
else:
    ark.write(f'Tempo de execução = {tempo:.3f}s\n')
ark.close()
