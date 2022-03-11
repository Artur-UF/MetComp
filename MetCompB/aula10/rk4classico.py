import numpy as np
import matplotlib.pyplot as plt


def rk4classico(x0, v0, tf, dt, a0, w0, w):
    fv = lambda x, t: -(w0 ** 2) * np.sin(x) + a0 * np.sin(w * t)
    pos = [x0]
    vel = [v0]
    for t in np.arange(0, tf, dt):
        k1x = v0
        k1v = fv(x0, t)
        xaux = x0 + k1x * (dt/2)
        vaux = v0 + k1v * (dt/2)
        k2x = vaux
        k2v = fv(xaux, t + (dt/2))
        xaux = x0 + k2x * (dt/2)
        vaux = v0 + k2v * (dt/2)
        k3x = vaux
        k3v = fv(xaux, t + (dt/2))
        xaux = x0 + k3x * dt
        vaux = v0 + k3v * dt
        k4x = vaux
        k4v = fv(xaux, t + dt)
        x0 += (k1x + 2*k2x + 2*k3x + k4x)*(dt/6)
        v0 += (k1v + 2*k2v + 2*k3v + k4v)*(dt/6)
        pos.append(x0)
        vel.append(v0)
    return pos, vel


x0 = 0.1
v0 = 0
tf = 25
dt = 0.1
a0 = 0.1
w0 = 1
w = 0.1

la = [0.1, 0.1, 1]
lw = [0.1, 0.5, 0.5]

t = np.arange(0, tf+dt, dt)

figura = plt.figure(figsize=(13, 5))
plt.subplot(121)
#plt.plot(t, rk4classico(x0, v0, tf, dt, a0, w0, w)[0], label=r'$A_{0}=$'+f'{a0}'+r' | $\omega=$'+f'{w}')
for a, w1 in zip(la, lw):
    plt.plot(t, rk4classico(x0, v0, tf, dt, a, w0, w1)[0], label=r'$A_{0}=$'+f'{a}'+r' | $\omega=$'+f'{w1}')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.title(r'Posição $\times$ Tempo')
plt.grid()

plt.subplot(122)
#plt.plot(rk4classico(x0, v0, tf, dt, a0, w0, w)[0], rk4classico(x0, v0, tf, dt, a0, w0, w)[1], label=r'$A_{0}=$'+f'{a0}'+r' | $\omega=$'+f'{w}')
for a, w1 in zip(la, lw):
    plt.plot(rk4classico(x0, v0, tf, dt, a, w0, w1)[0], rk4classico(x0, v0, tf, dt, a, w0, w1)[1], label=r'$A_{0}=$'+f'{a}'+r' | $\omega=$'+f'{w1}')
plt.xlabel('x')
plt.ylabel('v')
plt.legend()
plt.title(r'Posição $\times$ Velocidade')
plt.grid()

plt.savefig('rk4clasico-pend.png')
