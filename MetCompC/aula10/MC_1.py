'''
Pedras e pi
'''
import numpy as np
import random as rand


def montecarlotnterr(fx, infx, supx, infy, supy, n):
    xs = list(rand.uniform(infx, supx) for i in range(n))
    ys = list(rand.uniform(infy, supy) for i in range(n))
    ni = 0
    for x, y in zip(xs, ys):
        if y <= fx(x):
            ni += 1
    return (ni/n) * ((supx - infx) * (supy - infy))


fx = lambda x: np.sqrt(1-x**2)
infx = 0
supx = 1
infy = 0
supy = 1
n = [100, 1000, 10000, 100000, 1000000]
print(' n    |  Pi/4  | Monte Carlo')
for ni in n:
    integ = montecarlotnterr(fx, infx, supx, infy, supy, ni)
    print(f'{ni:7<} | {np.pi/4:.6f} | {integ:.6f}')
