'''
Integre numericamente a equação associada à dinâmica de um cometa na vizinhança do Sol. Use método de passo variável
com RK2 corrigido por RK4. Use GM=1.

Condições iniciais:

   1. x=0; y=4; vx=-1/2; vy=0 (órbita circular)
   2. x=0; y=4; vx=-1/4; vy=0 (órbita elíptica 1)
   3. x=0; y=4; vx=-0.65; vy=0 (órbita elíptica 2)
   4. x=0; y=4; vx=-sqrt(2)/2; vy=0 (órbita parabólica)
   5. x=0; y=4; vx= -1; vy=0 (órbita hiperbólica)

'''
import numpy as np
import matplotlib.pyplot as plt


def rk2heun(x0, y0, vx0, vy0, tf, dt, gm):
    fvx = lambda x, y: -(gm * x) / (((x ** 2) + (y ** 2)) ** (3 / 2))
    fvy = lambda x, y: -(gm * y) / (((x ** 2) + (y ** 2)) ** (3 / 2))
    posx = [x0]
    posy = [y0]
    velx = [vx0]
    vely = [vy0]
    for t in np.arange(0, tf, dt):
        k1x = vx0
        k1y = vy0
        k1vx = fvx(x0, y0)
        k1vy = fvy(x0, y0)
        xaux = x0 + k1x * dt
        yaux = y0 + k1y * dt
        vxaux = vx0 + k1vx * dt
        vyaux = vy0 + k1vy * dt
        k2x = vxaux
        k2y = vyaux
        k2vx = fvx(xaux, yaux)
        k2vy = fvy(xaux, yaux)
        x0 += (k1x + k2x)*(dt/2)
        y0 += (k1y + k2y)*(dt/2)
        vx0 += (k1vx + k2vx)*(dt/2)
        vy0 += (k1vy + k2vy)*(dt/2)
        posx.append(x0)
        posy.append(y0)
        velx.append(vx0)
        vely.append(vy0)
    return posx, posy, velx, vely


def passovarRK(x0, y0, vx0, vy0, tf, dt, gm, tol):
    fvx = lambda x, y: -(gm * x) / (((x ** 2) + (y ** 2)) ** (3 / 2))
    fvy = lambda x, y: -(gm * y) / (((x ** 2) + (y ** 2)) ** (3 / 2))
    posx = [x0]
    posy = [y0]
    velx = [vx0]
    vely = [vy0]
    cont = 0
    t = 0
    while t <= tf:
        if cont % 5 == 0:
            x02, x04 = x0, x0
            y02, y04 = y0, y0
            vx02, vx04 = vx0, vx0
            vy02, vy04 = vy0, vy0
            # RK2 Heun
            k1x2 = vx02
            k1y2 = vy02
            k1vx2 = fvx(x02, y02)
            k1vy2 = fvy(x02, y02)
            xaux2 = x02 + k1x2 * dt
            yaux2 = y02 + k1y2 * dt
            vxaux2 = vx02 + k1vx2 * dt
            vyaux2 = vy02 + k1vy2 * dt
            k2x2 = vxaux2
            k2y2 = vyaux2
            k2vx2 = fvx(xaux2, yaux2)
            k2vy2 = fvy(xaux2, yaux2)
            x02 += (k1x2 + k2x2) * (dt / 2)
            y02 += (k1y2 + k2y2) * (dt / 2)
            vx02 += (k1vx2 + k2vx2) * (dt / 2)
            vy02 += (k1vy2 + k2vy2) * (dt / 2)

            # RK4
            k1x4 = vx04
            k1y4 = vy04
            k1vx4 = fvx(x04, y04)
            k1vy4 = fvy(x04, y04)
            xaux4 = x04 + k1x4 * (dt / 2)
            yaux4 = y04 + k1y4 * (dt / 2)
            vxaux4 = vx04 + k1vx4 * (dt / 2)
            vyaux4 = vy04 + k1vy4 * (dt / 2)
            k2x4 = vxaux4
            k2y4 = vyaux4
            k2vx4 = fvx(xaux4, yaux4)
            k2vy4 = fvy(xaux4, yaux4)
            xaux4 = x0 + k2x4 * (dt / 2)
            yaux4 = y0 + k2y4 * (dt / 2)
            vxaux4 = vx0 + k2vx4 * (dt / 2)
            vyaux4 = vy0 + k2vy4 * (dt / 2)
            k3x4 = vxaux4
            k3y4 = vyaux4
            k3vx4 = fvx(xaux4, yaux4)
            k3vy4 = fvy(xaux4, yaux4)
            xaux4 = x0 + k3x4 * dt
            yaux4 = y0 + k3y4 * dt
            vxaux4 = vx0 + k3vx4 * dt
            vyaux4 = vy0 + k3vy4 * dt
            k4x4 = vxaux4
            k4y4 = vyaux4
            k4vx4 = fvx(xaux4, yaux4)
            k4vy4 = fvy(xaux4, yaux4)
            x04 += (k1x4 + 2 * k2x4 + 2 * k3x4 + k4x4) * (dt / 6)
            y04 += (k1y4 + 2 * k2y4 + 2 * k3y4 + k4y4) * (dt / 6)
            vx04 += (k1vx4 + 2 * k2vx4 + 2 * k3vx4 + k4vx4) * (dt / 6)
            vy04 += (k1vy4 + 2 * k2vy4 + 2 * k3vy4 + k4vy4) * (dt / 6)

            errx = ((x02 - x04)**2)**(1/2)
            erry = ((y02 - y04) ** 2) ** (1 / 2)
            errvx = ((vx02 - vx04)**2)**(1/2)
            errvy = ((vy02 - vy04) ** 2) ** (1 / 2)
            erro = max(errx, erry, errvx, errvy)
            dtnovo= dt * (tol/erro)**(1/3)
            if dtnovo > 2*dt:
                dt = 2 * dt
            if dtnovo < dt/2:
                dt = dt/2
        k1x = vx0
        k1y = vy0
        k1vx = fvx(x0, y0)
        k1vy = fvy(x0, y0)
        xaux = x0 + k1x * dt
        yaux = y0 + k1y * dt
        vxaux = vx0 + k1vx * dt
        vyaux = vy0 + k1vy * dt
        k2x = vxaux
        k2y = vyaux
        k2vx = fvx(xaux, yaux)
        k2vy = fvy(xaux, yaux)
        x0 += (k1x + k2x) * (dt / 2)
        y0 += (k1y + k2y) * (dt / 2)
        vx0 += (k1vx + k2vx) * (dt / 2)
        vy0 += (k1vy + k2vy) * (dt / 2)
        posx.append(x0)
        posy.append(y0)
        velx.append(vx0)
        vely.append(vy0)
        cont += 1
        t += dt
    return posx, posy, velx, vely


x0 = 0
y0 = 4
vx0 = [-1/2, -1/4, -0.65, -(2**(1/2))/2, -1]
vy0 = 0
gm = 1

tf = 51
dt = 0.1

tol = 1e-6

for vx in vx0:
    plt.plot(passovarRK(x0, y0, vx, vy0, tf, dt, gm, tol)[0], passovarRK(x0, y0, vx, vy0, tf, dt, gm, tol)[1], label=r'$v_{0x}=$'+f'{vx:.3f}')
plt.xlabel("x")
plt.ylabel("y")
plt.title('Órbitas em diferentes condições')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.savefig("doiscorpos.png", dpi=300)
