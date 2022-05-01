'''
1 - Faça um programa para gerar o teste espectral do gerador random() do python em duas dimensões (x_{n+1} \times x_n}.

2 - Dado um gerador uniforme com distribuição contínua que gere números no intervalo [-5,5]:

    a. Determine analiticamente o n-ésimo momento dessa distribuição.
    b. Faça um programa que calcule os momentos para n=0,1,2,3,4,5 e compare com o resultado analítico.
'''
import matplotlib.pyplot as plt
import random as rand
import numpy as np

n = 10000
l = 100
x = list(rand.randint(0, l) for i in range(n))
'''
plt.scatter(x[:-1], x[1:], marker='.')
plt.title('Teste espectral da biblioteca Random')
plt.xlabel(r'$x_{n}$')
plt.ylabel(r'$x_{n+1}$')
plt.savefig('testeespecrandom.png')
'''
x2 = list(rand.uniform(-5, 5) for i in range(n))
x2 = np.array(x2)
medanalitica = lambda n: (5**(n+1)-(-5)**(n+1))/(10*(n+1))
ns = [0, 1, 2, 3, 4, 5]

for i in ns:
    print(f'n = {i} || Analítica = {medanalitica(i)} || Programa = {sum(x2**i)/n}')
