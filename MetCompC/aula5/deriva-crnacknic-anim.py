import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def crancknic_deriva(n, k, d):
    # Montando a matriz M
    a = k
    c = -k
    m1 = np.eye(n, k=-1) * a
    m2 = np.eye(n)
    m3 = np.eye(n, k=1) * c
    Mmtz = m1 + m2 + m3

    Mmtz[0][-1] = a
    Mmtz[-1][0] = c

    # Montando a matriz E
    e1 = np.eye(n, k=-1) * c
    e3 = np.eye(n, k=1) * a
    Emtz = e1 + m2 + e3

    Emtz[0][-1] = c
    Emtz[-1][0] = a

    Einv = np.linalg.inv(Emtz)

    fxt = np.dot(Einv, np.dot(Mmtz, d))
    return fxt


def gen_y():
    x = np.arange(0, 200, 1)
    d = st.norm.pdf(x, loc=40, scale=10)
    n = len(x)
    tf = 200
    dt = .25
    k = .4
    t = np.arange(0, tf, dt)
    for ti in t:
        y = crancknic_deriva(n, k, d)
        d = y
        yield x, y, ti


def init():
    ax.set_ylim(-.01, .05)
    ax.set_xlim(0, 200)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
plt.title('Método Cranck-Nicolson para Eq. da Deriva\nk = 0.4')
xdata, ydata = [], []


def run(data):
    # update the data
    x, y, t = data
    xdata.append(x)
    ydata.append(y)
    plt.title(f'Método Cranck-Nicolson para Eq. da Deriva\nk = 0.4 | t = {t:5<.2f}')
    line.set_data(xdata[-1:], ydata[-1:])
    return line,


ani = animation.FuncAnimation(fig, run, gen_y, interval=20, init_func=init, save_count=1500)
#plt.show()
writergif = animation.PillowWriter(fps=30)
ani.save(r'D:\Aplicações\GItHub D\MetCompA\MetCompC\aula5\deriva-cranck.gif', writer=writergif)
plt.close()
