import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import os

#*-*-*-**-Definições-*-*-*-*
dt = 0.01
tf = 100000
g = 0.5
a = 0.25
b = 1
T = 1
cic = 100
POT = 'Livre'
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*

if POT == 'Livre':
    path = os.path.join(os.getcwd(), f'BAOAB_livre_g{g}T{T}tf{tf}')
else:
    path = os.path.join(os.getcwd(), f'BAOAB_duplo_g{g}T{T}tf{tf}')
#track = np.load(path+f'/langevin_g{g}T{T}tf{tf}.npy')
msd = np.load(path+f'/msd_g{g}T{T}tf{tf}.npy')
msd = msd[1:-1]

t = np.arange(dt, int(tf/cic), dt)

D_num = sum(msd[300:]/(4*t[300:]))/len(t)

msd = np.log10(msd)
t = np.log10(t)
results1 = sp.linregress(t[:300], msd[:300])
a1 = results1.slope
b1 = results1.intercept

y1 = a1*t + b1

results2 = sp.linregress(t[500:], msd[500:])
a2 = results2.slope
b2 = results2.intercept

y2 = a2*t + b2

texto = f'D analítico = {T/g}\n' \
        f'D numérico = {D_num:.4f}'

change = -np.log10(g) + 0.5

plt.scatter(t, msd, marker='.', s=10, c='k')
plt.plot(t, y1, 'r', label=f'y1 = {a1:.3f}t + {b1:.3f}')
plt.plot(t, y2, 'g', label=f'y2 = {a2:.3f}t + {b2:.3f}')
plt.text(-1.9, 1.5, texto, bbox=dict(boxstyle='square', ec='k', color='white'))
plt.vlines(change, -4, 4, label=f'Equilíbrio: x = {change:.3f}')
plt.xlabel(r'$log_{10}(t)$')
plt.ylabel(r'$log_{10}(r^{2})$')
plt.xlim(-2, 3)
plt.ylim(-4, 4)
plt.grid()
plt.legend(loc=2)
plt.title(f'MSD de uma partícula livre: Equação de Langevin\n'+r'$\gamma$ = '+
          f'{g} | T = {T} | '+r'$\Delta t$ = '+f'{dt} | tf = {tf}')
plt.savefig(path+f'/PLOTmsd_g{g}T{T}tf{tf}.png', dpi=300)
