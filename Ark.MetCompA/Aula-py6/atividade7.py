import numpy as np
import matplotlib.pyplot as plt
from random import randint


def med(nums):
    '''
    Calcula a média aritmética de um comjunto de números
    :param nums: tupla, lista ou array
    :return: retorna a média
    '''
    soma = 0
    for i in nums:
        soma += i
    med = soma / len(nums)
    return med


def desvp(nums):
    '''
    Calcula o desvio padrão de um conjunto de números
    :param nums: tupla, lista ou array
    :return: retorna o desvio padrão
    '''
    soma = 0
    for i in nums:
        soma += i
    med = soma / len(nums)
    desvio = 0
    for i in nums:
        desvio += (i - med)**2
    desvp = (desvio/len(nums))**(1/2)
    return desvp


n = int(input('Quantidade de jogadas: '))
x1 = np.array(list([randint(1, 6) for i in range(n)]))
x2 = np.array(list([randint(1, 6) for j in range(n)]))
y = x1 + x2
media = med(y)
desviop = desvp(y)
print(f'{"-~"*25}\nA média da soma das jogadas é:')
print(f'Pela minha função = {media}')
print(f'Pela função do numpy = {np.mean(y)}')
print(f'{"-~"*25}\nO desvio padrão da soma das jogadas:')
print(f'Pela minha função = {desviop}')
print(f'Pela função do numpy = {np.std(y)}\n{"-~"*25}')
plt.hist(y, bins=11, range=(2, 13), align='left', rwidth=0.95)
plt.title(f'Histograma com {n} jogadas')
plt.show()
#plt.savefig('hist.png')
