'''

    1. Divida em 1000 partes intervalo  do parâmetro  a do mapa logístico e obtenha as trajetórias da variável x para
    cada um desses valores.
    2. Guarde apenas os últimos 100 valores para cada a.
    3. Coloque em um gráfico x\times a esses valores assintóticos para cada valor de a.
    4. Faça um zoom nos intervalos de a e procure determinar visualmente os intervalos de a para o quais ocorrem os
     ciclos 3 e 5.

ciclo 3:
a (3.447, 3.542)

ciclo 5:
a (3.741, 3.742)

'''
import numpy as np
import matplotlib.pyplot as plt


alist = np.arange(0, 4, .001)
for a in alist:
    x = 0.2
    alist = []
    xlist = []
    for i in range(200):
        x = a * x * (1 - x)
    for i in range(100):
        x = a * x * (1 - x)
        alist.append(a)
        xlist.append(x)
    plt.scatter(alist, xlist, marker='.', s=1)
    plt.xlabel('a')
    plt.ylabel('x*')
    plt.title('Diagrama de Bifurcações')
plt.show()
