import numpy as np
import matplotlib.pyplot as plt


def dvdir(func, x, dx):
    return (func(x + dx) - func(x))/dx


def dvcen(func, x, dx):
    return (func(x + dx) - func(x - dx))/(2*dx)


def erro(dfx, dvan):
    return abs(dvan - dfx)/abs(dvan)


fx = lambda x: (x**3)*np.sin(x)
dx = np.logspace(-16, 0, 100)
dfxdir = dvdir(fx, 3, dx)
dfxcen = dvcen(fx, 3, dx)
dfxan = lambda x: (x**3)*np.cos(x) + 3*(x**2)*np.sin(x)
dvan = np.ones(100) * dfxan(3)

plt.plot(dx, dfxdir, 'b', label='Direita')
plt.plot(dx, dfxcen, 'r', label='Centrada')
plt.hlines(dfxan(3), 1e-16, 1, 'k', label='Analítica')
plt.title('Comparação das derivadas')
plt.xlabel(r'$\Delta x$')
plt.ylabel("f \'(x)")
plt.xscale('log')
plt.grid()
plt.legend()
plt.xlim(1e-16, 1)
plt.show()
#plt.savefig('comp_derivadas.png')

erro_cen = erro(dfxcen, dvan)
erro_dir = erro(dfxdir, dvan)
plt.plot(dx, erro_cen, 'r', label='Centrada')
plt.plot(dx, erro_dir,  'b', label='Direita')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$\Delta x$')
plt.ylabel('Erro')
plt.xlim(1e-16, 1)
plt.grid()
plt.legend()
plt.title('Comparação de erros das derivadas')
plt.show()
#plt.savefig('erro_derivadas.png')
