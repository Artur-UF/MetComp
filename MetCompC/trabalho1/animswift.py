import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def gen():
    estados = np.load('swiftanimgen.npy')
    dt = 0.0001
    ti = 0
    r = 0
    passo = 0
    for u0 in estados:
        yield u0, passo, ti, r
        ti += 15*dt
        passo += 15


fig, ax = plt.subplots()


def init():
    '''
    É o inicio de todo frame após o 'run'
    '''
    plt.cla()
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
plt.show()

#writergif = animation.PillowWriter(fps=30)
#ani.save(r'SHFFT.gif', writer=writergif)

plt.close()
