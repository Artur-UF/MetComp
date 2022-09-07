import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as pt

track = np.load('tracker_langavin.npy')


def gen():
    global track
    dt = 0.05
    tf = 20
    t = np.arange(0, tf, dt)
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


def run(data):
    '''
    Roda a animação com os dados fornecidos por 'data'
    '''
    x, y, vx, vy, ti, c = data
    global track
    l = 10
    gamma = 1
    Gamma = .5
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
    plt.xlim(0, l)
    plt.ylim(0, l)
    plt.title(f'Equação de Langevin\n' + r'$\gamma$ = ' + f'{gamma}'
                  + r' | $\Gamma$ = ' + f'{Gamma}' + f' | t = {ti:<4.1f}')


ani = animation.FuncAnimation(fig, run, gen, interval=20, init_func=init, save_count=1500, blit=True)
#plt.show()

writergif = animation.PillowWriter(fps=24)
ani.save(r'langevinanim.gif', writer=writergif)

plt.close()