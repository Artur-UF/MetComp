import numpy as np
import matplotlib.pyplot as plt
import random as rand


def montecarlo(fx, inf, sup):
    xi = list()    

l = np.arange(0, -1, -1)

fx = lambda x: x**l
sup = 1
inf = 0
esq = 
dir
n = 1000

ns = np.arange(1, n)
itent = []
imed = []
for i in ns:
    itent.append(montecarlotnterr(fx, 10, 0, 0, np.pi, i))
    imed.append(montecarlomed(fx, 0, np.pi, i))


plt.plot(ns, itent, label='Tentativa e Erro')
#plt.plot(ns, imed, label='Amostragem Média')
plt.xlabel('N')
plt.ylabel('Integral')
plt.legend()
plt.grid()
plt.savefig("funcaomontecarlo.png")

