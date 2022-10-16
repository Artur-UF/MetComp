import matplotlib.pyplot as plt
import numpy as np
import os

#*-*-*-**-Definições-*-*-*-*
dt = 0.01
tf = 10000
g = 0.5
a = 0.25
b = 1
T = 1
POT = 'Livre'
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*

if POT == 'Livre':
    path = os.path.join(os.getcwd(), 'BAOAB_livre')
else:
    path = os.path.join(os.getcwd(), 'BAOAB_duplo')
#track = np.load(path+f'/langevin_g{g}T{T}tf{tf}.npy')
msd = np.load(path+f'/msd_g{g}T{T}tf{tf}.npy')
msd = msd[:-1]

t = np.arange(0, int(tf/10), dt)
plt.plot(t, msd)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('log(t)')
plt.ylabel('log(r²)')
plt.grid()
plt.title(f'MSD de uma partícula livre: Equação de Langevin\n'+r'$\gamma$ = '+
          f'{g} | T = {T} | '+r'$\Delta t$ = '+f'{dt} | tf = {tf}')
plt.savefig(path+f'/PLOTmsd_g{g}T{T}tf{tf}.png', dpi=300)
