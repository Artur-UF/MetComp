import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import *
import matplotlib.animation as animation


def rhs(u, kappax, kappay, r):
    '''
    Calcula o lado direito da EDP
    '''
    kpx2 = np.power(kappax, 2)
    kpx4 = np.power(kappax, 4)
    kpy2 = np.power(kappay, 2)
    kpy4 = np.power(kappay, 4)
    uhat = fft2(u)
    uhat3 = fft2(u ** 3)
    duhatx2 = kpx2 * uhat
    duhaty2 = kpy2 * uhat
    duhatx4 = kpx4 * uhat
    duhaty4 = kpy4 * uhat
    duhatxy = kpx2 * kpy2 * uhat
    duhat = (r - 1) * uhat + 2 * duhatx2 + 2 * duhaty2 - duhatx4 - duhaty4 - 2 * duhatxy - uhat3
    dut = ifft2(duhat)
    return dut.real


N = 64
L = 50
dx = L/N
dy = dx
r = -.01
x = np.arange(-L/2, L/2, dx)
y = np.arange(-L/2, L/2, dy)
size = len(x)
u0 = np.random.randn(size, size)


def gen():
    global N, dx, dy, r, u0
    # Os coeficientes
    kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    ky = 2 * np.pi * np.fft.fftfreq(N, d=dy)
    kappax, kappay = np.meshgrid(kx, ky)

    dt = 0.0001
    tf = 1.5
    t = np.arange(0, tf, dt)
    for ti in t:
        passo = np.where(t == ti)[0][0]
        if passo % 15 == 0:
            yield u0, passo, ti
        u0 += dt * rhs(u0, kappax, kappay, r)


fig, ax = plt.subplots()
im = plt.imshow(u0, vmin=-1, vmax=1)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')


def run(data):
    '''
    Roda a animação com os dados fornecidos por 'data'
    '''
    global r
    u, passo, ti = data
    # Colormap
    im.set_array(u)
    plt.title(f'Swift-Hohenberg\n r = {r} | passo = {passo} | t = {ti:.3f}')


ani = animation.FuncAnimation(fig, run, gen, interval=5, save_count=1500, blit=True)
#plt.show()

writergif = animation.PillowWriter(fps=30)
ani.save(r'SHFFT.gif', writer=writergif)

plt.close()
