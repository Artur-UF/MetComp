'''
Seja um grupo de M=1000 caminhantes aleatórios que se propagam simultaneamente com passos síncronos que variam
uniformemente no intervalo contínuo L=[-5,5].

1 - Faça um programa para calcular o valor médio de posição e o desvio quadrático médio desses caminhantes como função
 do número de passos N.

2 - Encontre a função da distribuição de probabilidades para um passo dos caminhantes.

3 - Use o teorema do limite central para calcular analiticamente o valor médio de posição e o desvio quadrático médio
 como função do número de passos.

4 - Compare os resultados analíticos com a simulação.
'''
from random import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sc


class Walker:
    x = 0.0

    def __init__(self, l, ident):
        self.passo = l
        self.ident = ident

    def mov(self):
        self.x += self.passo * (10 * random() - 5)


l = 1
n = 1000
m = 10000
cams = list(Walker(l, i) for i in range(m))

meds = []
desvs = []

for i in range(n):
    med = 0
    dq = 0
    for c in cams:
        c.mov()
        med += c.x
        dq += c.x**2
    meds.append(med/m)
    desvs.append(dq/m)

regr = sc.linregress(range(n), desvs)
ajuste = np.arange(n)*regr.slope + regr.intercept

plt.plot(range(n), desvs,
         label=r'$\left\langle X^{2} \right\rangle'
               r'=N\left\langle x^{2} \right\rangle$')
plt.plot(range(n), ajuste,
         label='Ajuste: '+r'$\left\langle '
                         r'x^{2} \right\rangle=$'+f'{regr.slope:.2f}')
plt.plot(range(n), meds, label='Média')
plt.xlabel('N')
plt.ylabel(r'$\left\langle X^{2} \right\rangle$')
plt.title(r'Variação do $\left\langle X^{2} \right'
          r'\rangle$ em função de N passos')
plt.legend()
plt.savefig('caminhantes-plot.png')
