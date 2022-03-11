import numpy as np
import matplotlib.pyplot as plt


def passovarRK(x0, v0, tf, dt, tol, a0, w0, w):
    fv = lambda x, t: -(w0 ** 2) * np.sin(x) + a0 * np.sin(w * t)
    pos = [x0]
    vel = [v0]
    cont = 0
    t = 0
    while t <= tf:
        if cont % 5 == 0:
            x02, x04 = x0, x0
            v02, v04 = v0, v0
            # RK2
            k1x2 = v02
            k1v2 = fv(x02, t)
            xaux2 = x02 + k1x2 * dt
            vaux2 = v02 + k1v2 * dt
            k2x2 = vaux2
            k2v2 = fv(xaux2, t + dt)
            x02 += (k1x2 + k2x2) * (dt / 2)
            v02 += (k1v2 + k2v2) * (dt / 2)

            # RK4
            k1x4 = v04
            k1v4 = fv(x04, t)
            xaux4 = x04 + k1x4 * (dt / 2)
            vaux4 = v04 + k1v4 * (dt / 2)
            k2x4 = vaux4
            k2v4 = fv(xaux4, t + (dt / 2))
            xaux4 = x0 + k2x4 * (dt / 2)
            vaux4 = v0 + k2v4 * (dt / 2)
            k3x4 = vaux4
            k3v4 = fv(xaux4, t + (dt / 2))
            xaux4 = x0 + k3x4 * dt
            vaux4 = v0 + k3v4 * dt
            k4x4 = vaux4
            k4v4 = fv(xaux4, t + dt)
            x04 += (k1x4 + 2 * k2x4 + 2 * k3x4 + k4x4) * (dt / 6)
            v04 += (k1v4 + 2 * k2v4 + 2 * k3v4 + k4v4) * (dt / 6)

            errx = ((x02 - x04)**2)**(1/2)
            errv = ((v02 - v04)**2)**(1/2)
            erro = max(errx, errv)
            dtnovo= dt * (tol/erro)**(1/3)
            if dtnovo > 2*dt:
                dt = 2 * dt
            if dtnovo < dt/2:
                dt = dt/2
        k1x = v0
        k1v = fv(x0, t)
        xaux = x0 + k1x * dt
        vaux = v0 + k1v * dt
        k2x = vaux
        k2v = fv(xaux, t+dt)
        x0 += (k1x + k2x)*(dt/2)
        v0 += (k1v + k2v)*(dt/2)
        pos.append(x0)
        vel.append(v0)
        cont += 1
        t += dt

    return pos, vel


x0 = 0.1
v0 = 0
tf = 25
dt = 0.5
tol = 1e-5
a0 = 0.1
w0 = 1
w = 0.1

plt.plot(passovarRK(x0, v0, tf, dt, tol, a0, w0, w)[0], passovarRK(x0, v0, tf, dt, tol, a0, w0, w)[1])
plt.savefig('passovar.png', dpi=300)
