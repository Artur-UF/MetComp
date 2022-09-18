import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import warnings

warnings.simplefilter("ignore", np.ComplexWarning)


def shrodinger(n, dt, tf, hb, m, xf, dx, psi):
    # Operador Hamiltoniano
    h1 = np.eye(n, k=1)
    h2 = np.eye(n) * -2
    h3 = np.eye(n, k=-1)
    H = h1 + h2 + h3
    H[0][-1] = 1
    H[-1][0] = 1
    H *= -(hb**2)/(2*m)

    # Matriz E inversa
    E = np.eye(n) + (1j * dt * H)/2
    Einv = np.linalg.inv(E)

    # Matriz E*
    Estr = np.eye(n) + (-1j * dt * H)/2

    x = np.arange(0, xf, dx)

    for t in np.arange(0, tf, dt):
        g = np.dot(Einv, Estr)
        psi = np.dot(g, psi)
        plt.plot(x, np.real(psi), 'r', label='Real')
        plt.plot(x, np.imag(psi), 'b', label='Imagnária')
        plt.ylim(-.1, .1)
        plt.xlim(0, xf)
        plt.grid()
        plt.legend()
        plt.title(f'Shrödinger\nt = {t:>4.1f}')
        plt.pause(0.01)
        plt.cla()


xf = 300
dx = 1
x = np.arange(0, xf, dx)

n = len(x)
dt = 2
tf = 400
hb = 1
m = 1

# Estado inicial do pacote de onda
sigma = 10
k0 = .5
x0 = 150
#psi = (np.exp(1j * k0 * x) * np.exp((-(x-x0)**2))/(2 * sigma**2))/(np.sqrt(sigma * np.sqrt(np.pi)))
psi = d = st.norm.pdf(x, loc=150, scale=10) # Um pacote gaussiano usando uma Gaussiana

shrodinger(n, dt, tf, hb, m, xf, dx, psi)
