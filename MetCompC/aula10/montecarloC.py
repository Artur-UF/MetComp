'''
Estudando a divergência de x**l usando Monte Carlo
'''
import numpy as np
import random as rand


def montecarlo(fx, inf, sup, n):
    xi = np.asarray(list(rand.uniform(inf, sup) for i in range(n)))
    fxi = fx(xi)
    integ = (sup - inf) * (sum(fxi)/n)
    var = np.var(fxi, ddof=1)
    std = np.sqrt(var)
    return integ, std, var


lamb = np.arange(0, -1.1, -0.1)

inf = 0
sup = 1
n = 10000
print(f'Lambda | Monte Carlo | std')
for l in lamb:
    fx = lambda x: x ** l
    intg, std, var = montecarlo(fx, inf, sup, n)
    print(f'{l:<6.1f} | {intg:.8f}  | {std}')
