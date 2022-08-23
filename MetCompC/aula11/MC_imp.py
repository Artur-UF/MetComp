import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
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


def mcselet(inf, sup, l, z, n):
    fx = lambda x: x**(l - z)
    inv = lambda r: r**(1/(1 + z))
    xi = np.array(list(inv(rand.uniform(inf, sup)) for i in range(n)))
    integ = sum(fx(xi))/n
    dsvq = sum(fx(xi)**2)/n
    erro = np.sqrt((dsvq - integ**2)/n)
    return integ, erro


inf = 0
sup = 1
l = np.array([-.4, -.6, -.7, -.8])
z = np.array([0, -.4, -.6, -.7])
n = 10000
analitica = lambda lamb, zeta: (1 + zeta)/(1 + lamb)
print(f'{symb["lambda"]:^4} | {symb["zeta"]:^4} | Integral +- std  | Analítico')
for li, zi in zip(l, z):
    integ, err = mcselet(inf, sup, li, zi, n)
    an = analitica(li, zi)
    print(f'{li:<4} | {zi:<4} | {integ:.4f} +- {err:.4f} | {an:.3f}')
