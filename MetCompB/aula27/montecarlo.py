'''
Dada a função f(x)=A.sen(x)/x

onde A = 10. Calcule \int_0^\pi f(x) dx

    1. Use o método de tentativa e erro
    2. Use o método de amostragem média
'''
import numpy as np
import matplotlib.pyplot as plt
import random as rand


def montecarlotnterr(fx, sup, inf, esq, dir, n):
    xs = list(rand.uniform(esq, dir) for i in range(n))
    ys = list(rand.uniform(inf, sup) for i in range(n))
    ni = 0
    for x, y in zip(xs, ys):
        if y <= fx(x):
            ni += 1
    return (ni/n)*((dir-esq)*(sup-inf))


def montecarlomed(fx, esq, dir, n):
    xs = np.array(list(rand.uniform(esq, dir) for i in range(n)))
    ym = sum(fx(xs))/n
    return (dir - esq) * ym


a = 10
n = 1000
fx = lambda x: a * np.sin(x)/x

# Atividade
print('Integração por Monte Carlo')
print(f'N = {n}')
print(f'Tentativa e Erro = {montecarlotnterr(fx, 10, 0, 0, np.pi, n)}')
print(f'Amostragem Média = {montecarlomed(fx, 0, np.pi, n)}')

ns = np.arange(1, n)
itent = []
imed = []
for i in ns:
    itent.append(montecarlotnterr(fx, 10, 0, 0, np.pi, i))
    imed.append(montecarlomed(fx, 0, np.pi, i))


plt.plot(ns, itent, label='Tentativa e Erro')
plt.plot(ns, imed, label='Amostragem Média')
plt.xlabel('N')
plt.ylabel('Integral')
plt.legend()
plt.grid()
plt.savefig("funcaomontecarlo.png")
