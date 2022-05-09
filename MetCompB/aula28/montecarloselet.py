'''
Dada a distribuição de probabilidades: p(x) = b ( 1 - x/a) ; x E [0,a].

    1. Determine o valor de b para que a distribuição fique corretamente definida no intervalo.
    2. Use o método da transformada inversa para obter um gerador de números aleatórios com a distribuição \rho(x)
        no intervalo de definição da distribuição.
    3. Use o gerador obtido para integrar por amostragem por relevância : I=\int_0^a cos(\frac{x\pi}{2a})dx .
    4. A partir da solução exata obtenha o erro da integração numérica e faça uma tabela mostrando a evolução do erro
        com o número de números aleatórios usados na integração.
'''
import numpy as np
import random as rand


def montecarloseletiva(fx, px, a, esq, dir, n):
    dist = np.array(list(dir*(1+np.sqrt(rand.random())) for i in range(n)))
    soma = sum(fx(dist)/px(dist))
    return soma/n


esq = 0
dir, a = 10, 10


fx = lambda x: np.cos((x * np.pi)/(2 * a))
px = lambda x: (2/a) * (1 - x/a)
analitica = (2 * a * np.sin(np.pi/2))/np.pi

print(f'N   | Monte Carlo | Analítica | Erro')
for n in range(4, 12):
    resmontecarlo = montecarloseletiva(fx, px, a, esq, dir, 4**n)
    print(f'4^{n:<2}| {resmontecarlo:<10.9f} | {analitica:<9.6f} | {abs(resmontecarlo - analitica):.10f}')

