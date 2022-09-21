import numpy as np
import scipy.fft as sp
from scipy.integrate import odeint
import os
seed = 666
np.random.seed(seed)


def rhs(u0, t, kappa, r):
    '''
    Resolve o lado direito da equação
    '''
    uhat = sp.fft(u0)
    uhat3 = sp.fft(u0**3)
    duhat2 = (kappa**2) * uhat
    duhat4 = (kappa**4) * uhat
    duhat = (r - 1)*uhat + 2*duhat2 - duhat4 - uhat3
    dut = sp.ifft(duhat).real
    return dut


# Todos os parâmetros estão aqui:
N = 128
L = 150
dx = L/N
r = -0.1
dt = 0.01
tf = 100
#*-*-*-*-*--*-*-*-*-
x = np.arange(-L/2, L/2, dx)
size = len(x)

# Os coeficientes
kappa = 2 * np.pi * sp.fftfreq(N, d=dx)

# Vetor das condições iniciais
u0 = np.random.uniform(-1, 1, size)

# Integração usando o método do Scipy
t = np.arange(0, tf, dt)
u = odeint(rhs, u0, t, args=(kappa, r))

# Criação do arquivo de resultados
path = os.path.join(os.getcwd(), f'SH-1D-results')
try:
    os.mkdir(path)
except FileExistsError:
    pass
np.save(path+f'/SH-1D-array-r{r}.npy', u)
