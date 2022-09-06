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
    duhatx2 = kpx2 * uhat
    duhaty2 = kpy2 * uhat
    duhatx4 = kpx4 * uhat
    duhaty4 = kpy4 * uhat
    duhatxy = kpx2 * kpy2 * uhat
    dux2 = ifft2(duhatx2)
    duy2 = ifft2(duhaty2)
    dux4 = ifft2(duhatx4)
    duy4 = ifft2(duhaty4)
    duxy = ifft2(duhatxy)
    dut = (r - 1)*u - 2*dux2 - 2*duy2 - dux4 - duy4 - 2*duxy - u**3
    return dut.real


def gen():
    N = 128
    L = 50
    dx = L/N
    dy = dx
    r = -.01
    x = np.arange(-L/2, L/2, dx)
    y = np.arange(-L/2, L/2, dy)
    size = len(x)

    # Os coeficientes
    kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    ky = 2 * np.pi * np.fft.fftfreq(N, d=dy)
    kappax, kappay = np.meshgrid(kx, ky)

    # Vetor de estado
    u0 = np.random.rand(size, size)

    dt = 0.0001
    tf = 1
    t = np.arange(0, tf, dt)
    for ti in t:
        passo = np.where(t == ti)[0][0]
        if passo % 15 == 0:
            yield u0, passo, ti, r
        u0 += dt * rhs(u0, kappax, kappay, r)


fig, ax = plt.subplots()


def init():
    '''
    É o inicio de todo frame após o 'run'
    '''
    ax.clear()
    plt.xlabel('x')
    plt.ylabel('y')


def run(data):
    '''
    Roda a animação com os dados fornecidos por 'data'
    '''
    u, passo, ti, r = data

    # Colormap
    plt.imshow(u, cmap='viridis', vmin=0, vmax=.8)
    if ti == 0:
        plt.colorbar()
    plt.ylabel('y')
    plt.xlabel('x')
    plt.title(f'Swift-Hohenberg\n r = {r} | passo = {passo} | t = {ti:.3f}')


ani = animation.FuncAnimation(fig, run, gen, interval=10, init_func=init, save_count=1500)
#plt.show()

writergif = animation.PillowWriter(fps=30)
ani.save(r'SHFFT.gif', writer=writergif)

plt.close()
