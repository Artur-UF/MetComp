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
axs[0, 0].plot(x, u2[0], label=f'r = {r2}\nt = {dt*0}')
axs[0, 0].set(ylim=(-1.5, 1.5), xlabel='x', ylabel='y')
axs[0, 0].legend()
axs[0, 0].grid()

axs[0, 1].plot(x, u2[1000], label=f'r = {r2}\nt = {dt*1000}')
axs[0, 1].set(ylim=(-1.5, 1.5), xlabel='x', ylabel='y')
axs[0, 1].legend()
axs[0, 1].grid()

axs[0, 2].plot(x, u2[-1], label=f'r = {r2}\nt = {tf}')
axs[0, 2].set(ylim=(-1.5, 1.5), xlabel='x', ylabel='y')
axs[0, 2].legend()
axs[0, 2].grid()

# Segunda simulação
axs[1, 0].plot(x, u1[0], 'r', label=f'r = {r1}\nt = {dt*0}')
axs[1, 0].set(ylim=(-1.5, 1.5), xlabel='x', ylabel='y')
axs[1, 0].legend()
axs[1, 0].grid()

axs[1, 1].plot(x, u1[1000], 'r', label=f'r = {r1}\nt = {dt*1000}')
axs[1, 1].set(ylim=(-1.5, 1.5), xlabel='x', ylabel='y')
axs[1, 1].legend()
axs[1, 1].grid()

axs[1, 2].plot(x, u1[-1], 'r', label=f'r = {r1}\nt = {tf}')
axs[1, 2].set(ylim=(-1.5, 1.5), xlabel='x', ylabel='y')
axs[1, 2].legend()
axs[1, 2].grid()

fig.suptitle(f'Swift-Hohenberg: 1-D')
plt.savefig('plot-1D-SH.png')
