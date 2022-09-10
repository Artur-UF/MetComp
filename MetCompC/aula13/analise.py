import numpy as np
import matplotlib.pyplot as plt

t01, x01, y01, vx01, vy01 = np.loadtxt('langevin_tau0.1Dt0.5.txt', unpack=True, delimiter=',')
t1, x1, y1, vx1, vy1 = np.loadtxt('langevin_tau1Dt0.5.txt', unpack=True, delimiter=',')
t10, x10, y10, vx10, vy10 = np.loadtxt('langevin_tau10Dt0.5.txt', unpack=True, delimiter=',')
t100, x100, y100, vx100, vy100 = np.loadtxt('langevin_tau100Dt0.5.txt', unpack=True, delimiter=',')

ts = [t01, t1, t10, t100]
xs = [x01, x1, x10, x100]
ys = [y01, y1, y10, y100]
tau = [0.1, 1, 10, 100]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

for t, x, taup in zip(ts, xs, tau):
    ax1.plot(t, x, label=f'{taup}')
ax1.set(xlabel='t', ylabel='x')
ax1.grid()
ax1.legend()

for t, y, taup in zip(ts, ys, tau):
    ax2.plot(t, y, label=f'{taup}')
ax2.set(xlabel='t', ylabel='y')
ax2.grid()
ax2.legend()

for t, x, y, taup in zip(ts, xs, ys, tau):
    ax3.plot(t, (x**2 + y**2), label=f'{taup}')
ax3.set(xlabel='t', ylabel=r'$r^{2}$')
ax3.grid()
ax3.legend()

plt.savefig('tracklangevin.png')

