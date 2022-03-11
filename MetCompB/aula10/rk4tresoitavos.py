import numpy as np
import matplotlib.pyplot as plt


def rk4tresoitavos(x0, v0, tf, dt, a0, w0, w):
    fv = lambda x, t: -(w0 ** 2) * np.sin(x) + a0 * np.sin(w * t)
    pos = [x0]
    vel = [v0]
    for t in np.arange(0, tf, dt):
        k1x = v0
        k1v = fv(x0, t)
        xaux = x0 + (k1x/3) * dt
        vaux = v0 + (k1v/3) * dt
        k2x = vaux
        k2v = fv(xaux, t + (dt/3))
        xaux = x0 + (-k1x/3 + k2x) * dt
        vaux = v0 + (-k1v/3 + k2v) * dt
        k3x = vaux
        k3v = fv(xaux, t + (2*dt/3))
        xaux = x0 + (k1x - k2x + k3x) * dt
        vaux = v0 + (k1v - k2v + k3v) * dt
        k4x = vaux
        k4v = fv(xaux, t + dt)
        x0 += (k1x + 3*k2x + 3*k3x + k4x)*(dt/8)
        v0 += (k1v + 3*k2v + 3*k3v + k4v)*(dt/8)
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
#plt.plot(t, rk4tresoitavos(x0, v0, tf, dt, a0, w0, w)[0], label=r'$A_{0}=$'+f'{a0}'+r' | $\omega=$'+f'{w}')
for a, w1 in zip(la, lw):
   plt.plot(t, rk4tresoitavos(x0, v0, tf, dt, a, w0, w1)[0], label=r'$A_{0}=$'+f'{a}'+r' | $\omega=$'+f'{w1}')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.title(r'Posição $\times$ Tempo')
plt.grid()

plt.subplot(122)
#plt.plot(rk4tresoitavos(x0, v0, tf, dt, a0, w0, w)[0], rk4tresoitavos(x0, v0, tf, dt, a0, w0, w)[1], label=r'$A_{0}=$'+f'{a0}'+r' | $\omega=$'+f'{w}')
for a, w1 in zip(la, lw):
    plt.plot(rk4tresoitavos(x0, v0, tf, dt, a, w0, w1)[0], rk4tresoitavos(x0, v0, tf, dt, a, w0, w1)[1], label=r'$A_{0}=$'+f'{a}'+r' | $\omega=$'+f'{w1}')
plt.xlabel('x')
plt.ylabel('v')
plt.legend()
plt.title(r'Posição $\times$ Velocidade')
plt.grid()

plt.savefig('rk4rtesoitavos-pend.png')