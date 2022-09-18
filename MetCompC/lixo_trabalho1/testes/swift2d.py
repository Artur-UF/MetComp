import matplotlib.pyplot as plt
import numpy as np


def swift2d(dx, dy, dt, r, fxy):
    n = len(fxy[0])
    dx4 = dt/dx**4
    dy4 = dt/dy**4
    dxy = dt/((dx**2) * (dy**2))
    dx2 = dt/dx**2
    dy2 = dt/dy**2

    for y in range(n):
        for x in range(n):
            i = x - 2
            j = y - 2
            fxy[j][i] = fxy[j][i] - dx4*(fxy[j][i-2] - 4*fxy[j][i-1] + 6*fxy[j][i] - 4*fxy[j][i+1] + fxy[j][i+2])
            - dy4*(fxy[j-2][i] - 4*fxy[j-1][i] + 6*fxy[j][i] - 4*fxy[j+1][i] + fxy[j+2][i])
            + 2*dxy*(fxy[j-1][i-1] - 2*fxy[j-1][i] + fxy[j-1][i+1]) - 4*dxy*(fxy[j][i+1] - 2*fxy[j][i] + fxy[j][i+1])
            + 2*dxy*(fxy[j+1][i-1] - 2*fxy[j+1][i] + fxy[j+1][i+1]) - 2*dx2*(fxy[j][i-1] - 2*fxy[j][i] + fxy[j][i+1])
            - 2*dy2*(fxy[j-1][i] - 2*fxy[j][i] + fxy[j+1][i]) - dt*(fxy[j][i]**3) + dt*(r - 1)*fxy[j][i]
    return fxy


dx = 1
dy = 1
dt = .1
r = 0.1
tf = 30
l = 50

fxy = np.random.uniform(-1, 1, size=(l, l))

fig, ax = plt.subplots()

t = np.arange(0, tf, dt)
for ti in t:
    z = swift2d(dx, dy, dt, r, fxy)
    plt.imshow(z, cmap='viridis', vmin=-.5, vmax=.5)
    plt.title(f'Swift-Hohenberg\nr = {r} | t = {ti:<4.2f}')
    plt.xlabel('x')
    plt.ylabel('y')
    fxy = z
    plt.pause(0.01)
    plt.cla()
