import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

estados = np.load('swiftanimgen.npy')


def gen():
    global estados
    dt = 0.0001
    ti = 0
    r = 0
    passo = 0
    for u0 in estados:
        yield u0, passo, ti, r
        ti += 15*dt
        passo += 15


fig, ax = plt.subplots()
im = plt.imshow(estados[0], cmap='viridis', vmin=0, vmax=.8)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')


def run(data):
    '''
    Roda a animação com os dados fornecidos por 'data'
    '''
    u, passo, ti, r = data
    im.set_array(u)
    plt.title(f'Swift-Hohenberg\n r = {r} | passo = {passo} | t = {ti:.3f}')


ani = animation.FuncAnimation(fig, run, gen, interval=10, save_count=1500, blit=True)
plt.show()

#writergif = animation.PillowWriter(fps=30)
#ani.save(r'SHFFT.gif', writer=writergif)

plt.close()
