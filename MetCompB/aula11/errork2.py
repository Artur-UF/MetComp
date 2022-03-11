import numpy as np
import matplotlib.pyplot as plt


def aj_lin(xi, yi):
    '''
    Realiza o ajuste linear de pontos em uma reta de ajuste no formato "y = ax + b"
    :param xi: coordenadas x dos pontos
    :param yi: coordenadas y dos pontos
    :return: coeficiente angular "a" e coeficiente linear "b" da reta de ajuste
    '''
    n = len(xi)
    mxy = sum(xi * yi) / n
    mx = sum(xi) / n
    my = sum(yi) / n
    mqx = sum(xi ** 2) / n
    a = (mxy - (mx * my)) / (mqx - (mx ** 2))
    b = ((mqx * my) - (mx * mxy)) / (mqx - (mx ** 2))
    return a, b


def rk2heun(x0, v0, tf, dt, w):
    fv = lambda x: -(w ** 2) * x
    pos = [x0]
    vel = [v0]
    for t in np.arange(dt, tf, dt):
        k1x = v0
        k1v = fv(x0)
        xaux = x0 + k1x * dt
        vaux = v0 + k1v * dt
        k2x = vaux
        k2v = fv(xaux)
        x0 += (k1x + k2x) * (dt / 2)
        v0 += (k1v + k2v) * (dt / 2)
        pos.append(x0)
        vel.append(v0)
    return pos, vel


def massamolaan(t, w):
    x = lambda t: np.cos(w * t)
    v = lambda t: -w * np.sin(w * t)
    return x(t), v(t)


def erro(rk2, analitic, n):
    num = np.array(rk2[n])
    an = np.array(analitic[n])
    return abs(sum(an - num) / len(rk2[n]))


x0, v0, tf, w = 1, 0, 1, 1

# Posição
dtx = 0.5e-5
dtsx = []
errosx = []

while dtx < 0.5:
    dtx = dtx * 2
    e = erro(rk2heun(x0, v0, tf, dtx, w), massamolaan(np.arange(0, tf, dtx), w), 0)
    errosx.append(e)
    dtsx.append(dtx)

errx = np.log10(errosx)
deltx = np.log10(dtsx)

parx = aj_lin(deltx[3:-3], errx[3:-3])
yx = parx[0] * deltx[3:-3] + parx[1]

# Velocidade
dtv = 0.5e-5
dtsv = []
errosv = []

while dtv < 0.5:
    dtv = dtv * 2
    e = erro(rk2heun(x0, v0, tf, dtv, w), massamolaan(np.arange(0, tf, dtv), w), 0)
    errosv.append(e)
    dtsv.append(dtv)

errv = np.log10(errosv)
deltv = np.log10(dtsv)

parv = aj_lin(deltv[3:-3], errv[3:-3])
yv = parv[0] * deltv[3:-3] + parv[1]

print(f'Inclinação da reta de Posição: {parx[0]}')
print(f'Inclinação da reta de Velocidade: {parv[0]}')

figura = plt.figure(figsize=(15, 5))
plt.subplot(121)
plt.scatter(deltx, errx, s=30, c='k', marker='.', label='Erros')
plt.plot(deltx[3:-3], yx, 'g', label='Ajuste')
plt.xlabel(r'log($\Delta t$)')
plt.ylabel(r'log(Er)')
plt.legend()
plt.title('Posição')
plt.grid()

plt.subplot(122)
plt.scatter(deltv, errv, s=30, c='k', marker='.', label='Erros')
plt.plot(deltv[3:-3], yv, 'g', label='Ajuste')
plt.xlabel(r'log($\Delta t$)')
plt.ylabel(r'log(Er)')
plt.legend()
plt.title('Velocidade')
plt.grid()

plt.savefig('errork2.png')
