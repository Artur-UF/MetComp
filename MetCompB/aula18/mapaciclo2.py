'''
1- Dado o mapa logístico:

x_{n+1} = f(x_n) = a * x_n * (1 - x_n)

Encontre analiticamente função g(x)=f(f(x)) e sua derivada.

2- Faça um gráfico de g(x) e da função identidade.

    Use a=2.9
    Use a=3.1

A partir da análise do gráfico, encontre os pontos fixos.

3- Usando a expressão analítica da derivada de g(x) e os pontos fixos obtidos em 2 determine a estabilidade desses
 pontos fixos.
'''
import matplotlib.pyplot as plt
import numpy as np

a = [2.9, 3.1]
f = lambda x, ai: ai * x * (1 - x)
fof = lambda x, ai: ai * f(x, ai) * (1 - f(x, ai))

x = np.linspace(0, 1, 100)

plt.plot(x, fof(x, a[0]), label='a = 2.9')
plt.plot(x, fof(x, a[1]), label='a = 3.1')
plt.plot(x, x)
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('fof')
plt.show()
