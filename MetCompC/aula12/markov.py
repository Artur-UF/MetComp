import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt
symb = {
    'alpha':'\u03B1',
    'Alpha':'\u0391',
    'beta':'\u03B2',
    'Beta':'\u0392',
    'gamma':'\u03B3',
    'Gamma':'\u0393',
    'delta':'\u03B6',
    'Delta':'\u0394',
    'epsilon':'\u03B5',
    'Epsilon':'\u0395',
    'zeta':'\u03B6',
    'Zeta':'\u0396',
    'eta':'\u03B7',
    'Eta':'\u0397',
    'theta':'\u03B8',
    'Theta':'\u0398',
    'iota':'\u03B9',
    'Iota':'\u0399',
    'kappa':'\u03BA',
    'Kappa':'\u039A',
    'lambda':'\u03BB',
    'Lambda':'\u039B',
    'mu':'\u03BC',
    'Mu':'\u039C',
    'nu':'\u03BD',
    'Nu':'\u039D',
    'xi':'\u03BE',
    'Xi':'\u039E',
    'omicron':'\u03BF',
    'Omicron':'\u039F',
    'pi':'\u03C0',
    'Pi':'\u03A0',
    'rho':'\u03C1',
    'Rho':'\u03A1',
    'varsigma':'\u03C2',
    'sigma':'\u03C3',
    'Sigma':'\u03A3',
    'tau':'\u03C4',
    'Tau':'\u03A4',
    'upsilon':'\u03C5',
    'Upsilon':'\u03A5',
    'phi':'\u03C6',
    'Phi':'\u03A6',
    'chi':'\u03C7',
    'Chi':'\u03A7',
    'psi':'\u03C8',
    'Psi':'\u03A8',
    'omega':'\u03C9',
    'Omega':'\u03A9',
    'vartheta':'\u03F4',
    'ihat':'i\u0302',
    'jhat':'j\u0302',
    'khat':'k\u0302',
    'uhat':'u\u0302'
}


def markov(n, x0, y0, dmax):
    '''
    Para calcular pi/4 usando o jogo das pedrinhas
    '''
    hits = 0
    x, y = x0, y0
    num = 0
    for i in range(n):
        dx, dy = uniform(-dmax, +dmax, 2)
        if abs(x + dx) < 1 and abs(y + dy) < 1:
            x, y = x + dx, y + dy
            num += 1
        if x**2 + y**2 < 1:
            hits += 1
    return hits, hits/n, hits/num


n = [100, 1000, 10000, 100000]
x0, y0 = 1, 1
dmax = .3
'''
print(f'n     |   {symb["pi"]}    | Markov | Hits |')
for ni in n:
    hits, pi4 = markov(ni, x0, y0, dmax)
    print(f'{ni:<6d}| {np.pi:<6.4f} | {pi4*4:<6.4f} | {hits:<5d} |')
'''
x = np.arange(10, 1000)
yon = []
yoff = []
for i in x:
    hits, on, off = markov(i, x0, y0, dmax)
    yon.append(on*4)
    yoff.append(off*4)

plt.plot(x, yoff, 'g', linewidth=.2, label='Sem Pilhas')
plt.plot(x, yon, 'r', linewidth=.2, label='Com Pilhas')
plt.hlines(np.pi, 0, 1000, colors='k')
plt.grid()
plt.legend()
plt.xlabel('N')
plt.title('Cadeia Markoviana')
plt.ylabel(r'Estimativa de $\pi$')
plt.savefig('markov_pilhas.png')
