import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as pt
import os
from time import time
start = time()

# Copie essas definições do arquivo info que deseja
#*-*-*-**-Definições-*-*-*-*
dt = 0.01
tf = 10
g = 1
a = 0.25
b = 1
T = 1
cic = 100
POT = 'Duplo'
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*

#Cuidado com os limites dos gráficos em plt.xlim e plt.ylim

if POT == 'Livre':
    path = os.path.join(os.getcwd(), f'BAOAB_livre_g{g}T{T}tf{tf}')
else:
    path = os.path.join(os.getcwd(), f'BAOAB_duplo_g{g}T{T}tf{tf}')
track = np.load(path+f'/langevin_g{g}T{T}tf{tf}.npy')


def gen():
    global track, dt, tf
    t = np.arange(int(tf/dt))
    c = 0
    for x, y, vx, vy, ti in zip(track[0], track[1], track[2], track[3], t):
        yield x, y, vx, vy, ti, c
        c += 1


fig, ax = plt.subplots()


def init():
    '''
    É o inicio de todo frame após o 'run'
    '''
    ax.clear()
    plt.xlabel('x')
    plt.ylabel('y')


def run_livre(data):
    '''
    Roda a animação com os dados fornecidos por 'data'
    '''
    x, y, vx, vy, ti, c = data
    global track, g, T, dt
    l = 10
    r = 0.3
    plt.cla()
    circ = plt.Circle((x, y), r, edgecolor='k')
    arrow = pt.FancyArrow(x, y, vx, vy, head_width=0.05, head_length=0.1)
    ax.add_patch(circ)
    ax.add_patch(arrow)
    plt.grid()
    plt.plot(track[0][:c], track[1][:c], 'r', linewidth=1)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.xlim(0, 6)
    plt.ylim(-4, 2)
    plt.title(f'Equação de Langevin para Partícula Livre: BAOAB\n' + r'$\gamma$ = ' + f'{g}' +
              f' | T = {T} | dt = {dt} | passo = {c:<4}')


def run_duplo(data):
    '''
    Roda a animação com os dados fornecidos por 'data'
    '''
    x, y, vx, vy, ti, c = data
    global track, g, a, b, T
    l = 5
    r = 0.3
    plt.cla()
    circ = plt.Circle((x, y), r, edgecolor='k')
    circ_p = plt.Circle((0, 0), 0.5*np.sqrt(b/a), edgecolor='r', fill=False)
    arrow = pt.FancyArrow(x, y, vx, vy, head_width=0.05, head_length=0.1)
    ax.add_patch(circ)
    ax.add_patch(circ_p)
    ax.add_patch(arrow)
    plt.grid()
    plt.plot(track[0][:c], track[1][:c], 'r', linewidth=1)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.xlim(-l, l)
    plt.ylim(-l, l)
    plt.title(f'Equação de Langevin para poço duplo radial: BAOAB\n' + r'$\gamma$ = ' + f'{g}' +
              f' | T = {T} '+r'$\Delta t = $'+f'{dt} | passo = {c:<4}')


# Selecione o formato desejado (.mp4 é o recomendado e é necessário FFMpeg instalado para rodar)

if POT == 'Livre':
    ani = animation.FuncAnimation(fig, run_livre, gen, interval=20, init_func=init, save_count=1500, blit=True)
    #writergif = animation.PillowWriter(fps=24)
    #ani.save(path+f'/livre_g{g}T{T}.gif', writer=writergif, dpi=300)
    FFwriter = animation.FFMpegWriter(fps=24, bitrate=-1)
    ani.save(path + f'/livre_g{g}T{T}.mp4', writer=FFwriter, dpi=300)
else:
    ani = animation.FuncAnimation(fig, run_duplo, gen, interval=20, init_func=init, save_count=1500, blit=True)
    #writergif = animation.PillowWriter(fps=24, bitrate=-1)
    #ani.save(path+f'/duplo_g{g}T{T}.gif', writer=writergif, dpi=300)
    FFwriter = animation.FFMpegWriter(fps=24, bitrate=-1)
    ani.save(path + f'/duplo_g{g}T{T}.mp4', writer=FFwriter, dpi=300)

plt.close()
print(f'Tempo de execução = {time()-start}')
