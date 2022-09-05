import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
from time import time


def fleas_mc(N, r, inter):
    n = 0
    states = [n]
    for i in range(r + int(r/5)):
        if i < r/5:
            flea = sp.randint.rvs(1, N + 1)
            if flea > n:
                n += 1
            else:
                n -= 1
        else:
            states.append(n)
            for j in range(inter):
                flea = sp.randint.rvs(1, N + 1)
                if flea > n:
                    n += 1
                else:
                    n -= 1
    return np.array(states)

start = time()
N = 50
r = 10000
i = 99

y = fleas_mc(N, r, i)
x = np.arange(N+1)

# Histograma
plt.figure(1)
plt.hist(y, bins=N+1, range=(0, N), density=True, stacked=True, align='mid')
plt.xticks(np.arange(0, 51, 5))
plt.grid()
plt.plot(x, sp.binom.pmf(x, N, 0.5))
plt.xlim(0, 50)
plt.title('Histograma: Simulação-MC de Ehrenfest')
plt.savefig('fleaMC.png')

yhist, ybins = np.histogram(y, N+1, range=(0, N))
ymed = yhist/r
yerr = np.sqrt((ymed-ymed**2)/(r-1))
# PLot do erro
plt.figure(2)
plt.errorbar(x, ymed, yerr=yerr, fmt='k.', ecolor='r', barsabove=True)
plt.plot(x, sp.binom.pmf(x, N, 0.5))
plt.grid()
plt.title(f'Ehrenfest descorrelacionado\n M={r} | '+r'$N_{hops}$='+f'{i}')
plt.savefig('erro_fleasMC.png')
end = time()

print(end-start)
