import scipy.stats as st
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def ftcs_mtz(n, u, d):
    # Montando a matriz
    a = (1 + u)/2
    c = (1 - u)/2
    m1 = np.eye(n, k=-1) * a
    m2 = np.zeros((n, n))
    m3 = np.eye(n, k=1) * c
    mtz = m1 + m2 + m3

    # Arrumando a matriz
    mtz[0][-1] = a
    mtz[-1][0] = c

    #M = np.linalg.inv(mtz)

    fxt = np.dot(mtz, d)
    return fxt


def gen_y():
    x = np.arange(0, 100, 1)
    d = st.norm.pdf(x, loc=30, scale=5)
    n = len(x)
    tf = 100
    dt = .25
    u = .4
    t = np.arange(0, tf, dt)
    for ti in t:
        y = ftcs_mtz(n, u, d)
        d = y
        yield x, y


def init():
    ax.set_ylim(0, .1)
    ax.set_xlim(0, 100)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
plt.title('Método de Lax para Eq. da Deriva')
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)

    line.set_data(xdata[-1:], ydata[-1:])
    return line,


ani = animation.FuncAnimation(fig, run, gen_y, interval=20, init_func=init, save_count=1500)
#plt.show()
writergif = animation.PillowWriter(fps=30)
ani.save(r'D:\Aplicações\GItHub D\MetCompA\MetCompC\aula5\deriva-lax.gif', writer=writergif)
plt.close()
