import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# Cole aqui:
#-*-*-*-*-*-*-*-*
checkpoint = 500
tf = 10
r = 0.4
#-*-*-*-*-*-*-*-*
path = os.path.join(os.getcwd(), f'SH_r{r}_t{tf}')
estados = np.load(path+f'/SH-array.npy')


def gen():
    global estados, r, checkpoint
    dt = 0.0001
    ti = 0
    passo = 0
    for u0 in estados:
        yield u0, passo, ti, r
        ti += checkpoint*dt
        passo += checkpoint


fig, ax = plt.subplots()
im = plt.imshow(estados[0], origin='lower', cmap='viridis', vmin=-1, vmax=1)
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
#plt.show()

# Escolha o formato da animação desejado, gif ou mp4:
#writergif = animation.PillowWriter(fps=30)
#ani.save(path+f'/SH-anim.gif', writer=writergif)

FFwriter = animation.FFMpegWriter(fps=10)
ani.save(path+f'/SH-anim.mp4', writer=FFwriter)

plt.close()
