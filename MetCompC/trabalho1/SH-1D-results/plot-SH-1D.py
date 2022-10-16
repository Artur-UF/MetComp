import numpy as np
import matplotlib.pyplot as plt
# Todos os parâmetros estão aqui:
N = 128
L = 150
dx = L/N
x = np.arange(-L/2, L/2, dx)
#*-*-*-*-*--*-*-*-*-

#-*-*-*-*-*-*-*-*
dt = 0.01
tf = 100
r1 = 0.1
r2 = -0.1
#-*-*-*-*-*-*-*-*

u1 = np.load(f'SH-1D-array-r{r1}.npy')

u2 = np.load(f'SH-1D-array-r{r2}.npy')


fig, axs = plt.subplots(2, 3, figsize=(15, 8))

# Primeira simulação
axs[0, 0].plot(x, u2[0])
axs[0, 0].set(ylim=(-1.5, 1.5), xlabel='x', ylabel='y', title=f'r = {r2} | t = {dt*0}')
axs[0, 0].grid()

axs[0, 1].plot(x, u2[1000])
axs[0, 1].set(ylim=(-0.1, 0.1), xlabel='x', ylabel='y', title=f'r = {r2} | t = {dt*1000}')
axs[0, 1].grid()

axs[0, 2].plot(x, u2[-1])
axs[0, 2].set(ylim=(-5e-6, 5e-6), xlabel='x', ylabel='y', title=f'r = {r2} | t = {tf}')
axs[0, 2].grid()

# Segunda simulação
axs[1, 0].plot(x, u1[0], 'r')
axs[1, 0].set(ylim=(-1.5, 1.5), xlabel='x', ylabel='y', title=f'r = {r1} | t = {dt*0}')
axs[1, 0].grid()

axs[1, 1].plot(x, u1[1000], 'r')
axs[1, 1].set(ylim=(-0.5, 0.5), xlabel='x', ylabel='y', title=f'r = {r1} | t = {dt*1000}')
axs[1, 1].grid()

axs[1, 2].plot(x, u1[-1], 'r')
axs[1, 2].set(ylim=(-0.5, 0.5), xlabel='x', ylabel='y', title=f'r = {r1} | t = {tf}')
axs[1, 2].grid()

fig.suptitle(f'Swift-Hohenberg: 1-D', size='xx-large')
fig.tight_layout()
plt.savefig('newplot-1D-SH.png')
