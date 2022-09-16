import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

r = 0.35
tf = 20
estados = np.load(f'SH-r{r}-t{tf}.npy')


def gen():
    global estados, r
    dt = 0.0001
    ti = 0
    passo = 0
    for u0 in estados:
        yield u0, passo, ti, r
        # Lembra de ajustar os passos !!!
        ti += 500*dt
        passo += 500


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

writergif = animation.PillowWriter(fps=30)
ani.save(f'SH-r{r}-t{tf}.gif', writer=writergif)

plt.close()
