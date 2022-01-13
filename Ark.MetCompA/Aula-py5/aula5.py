# -*- coding: utf-8 -*-
"""Aula_Python_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hic2dd6R1Sy-L73rx7tYWL6rJraLwTX_

#Revisão
"""

# criando um dicionário
d = {'João': 1.85, 'Maria': 1.70, 'José': 1.68}

for nome, altura in d.items():
    print('{quem} tem {a:.3f} m de altura'.format(quem=nome, a=altura))

# alternativamente podemos usar as f-strings
for nome, altura in d.items():
    print(f'{nome} tem {altura:.2f} m de altura')

"""

---




"""

import numpy as np
import matplotlib.pyplot as plt


def posicao(t, a, x0=0., v0=0.):
    x = x0 + v0 * t + a * t ** 2 / 2
    return x


def velocidade(t, a, v0=0.):
    v = v0 + a * t
    return v


# Podemos usar as funções para encontrar a posiçãão e velocidade para valores específicos

t = 10.
a = 5.
print(posicao(t, a))
print(velocidade(t, a))

# determinando as posições para a=5m/s e t variando de 0 a 10s em
# intervalos de 1s usando listas

posicoes = []
for t in range(11):
    posicoes.append(posicao(t, a=5))

print(posicoes)

# podemos converter uma lista para um array
posicoes_array = np.array(posicoes)
print(posicoes_array)

# algoritmo similar ao anterior, só que em vez de criar uma lista
# criamos um array e vamos 'populando' ele

t_a = np.arange(0, 11, 1)
# print(t_a.shape)
posicoes_array = np.zeros(t_a.shape)

for i in range(len(posicoes_array)):
    posicoes_array[i] = posicao(t_a[i], a=5)

print(posicoes_array)

# print(np.zeros(t_a.shape))

# Finalmente utilizando operações com arrays - muito mais simples!!!

t_a = np.arange(0, 11, 1)
pos = posicao(t_a, a=5)

print(pos)

# determinando a velocidade com arrays
vel = velocidade(t_a, a=5)
print(vel)

# escrevendo resultados em arquivos

output = open('mruv.txt', 'w')

output.write(f'#t pos vel\n')

for j in range(len(t_a)):
    output.write(f'{t_a[j]:2d} {pos[j]:.2f} {vel[j]:.2f}\n')

output.close()

"""# Matplotlib

O Matplotlib é um pacote que permite criar figuras estáticas, animadas e interativas em Python. 

De acordo com https://matplotlib.org/, "Matplotlib makes easy things easy and hard things possible".
"""

import matplotlib.pyplot as plt

a = 5.  # aceleração, em m/s
d = a * t_a ** 2 / 2
print(d)

plt.plot(t_a, d)

plt.show()

plt.plot(t_a, d, linewidth=1.0, color='red')
plt.xlabel('t (s)')
plt.ylabel('d (m)')
plt.show()

plt.plot(t_a, d, '-.g', linewidth=3)
plt.xlabel('t (s)')
plt.ylabel('d (m)')
plt.title('Titulo')
plt.show()

y = np.random.rand(50) * 4
x = np.random.rand(50) * 10

plt.scatter(x, y, marker='^', c='orange')

plt.show()

z = np.arange(0., 5., 0.2)

plt.plot(z, z, 'b--', z, z ** 2, 'r^', z, z ** 3, 'gd')
plt.show()

plt.plot(z, z, 'k-.', label='linear')
plt.plot(z, z ** 2, 'cd', label='quadrático')
plt.plot(z, z ** 3, 'm.', label='cúbico')
plt.legend()
plt.show()

figura = plt.figure(figsize=(20, 5))

plt.subplot(131)
plt.plot(t_a, d, 'k.')
plt.xlabel('t (s)')
plt.ylabel('d (m)')
plt.title('Titulo subplot')
plt.subplot(132)
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.subplot(133)
plt.plot(z, z, 'b--', z, z ** 2, 'r^', z, z ** 3, 'gs')
plt.xlabel('z')
plt.ylabel('f(z)')
plt.suptitle('Titulo principal')
figura.show()

tt_a, xx_a, vv_a = np.loadtxt('mruv.txt', unpack=True, comments='#')

print(xx_a)

f_input = open('mruv.txt', 'r')

# criando listas vazias para armazenar os dados a serem lidos
tt = []
xx = []
vv = []

for l in f_input:  # loop sobre as linhas de f_input
    if '#' in l:  # pula linhas que possuem o símbolo # de comentário
        continue
    dados = l.split()

    tt.append(float(dados[0]))
    xx.append(float(dados[1]))
    vv.append(float(dados[2]))

print(xx)

plt.plot(t_a, vel, label='MRUV')
plt.xlabel('t')
plt.ylabel('v(t)')
plt.legend()
plt.show()

# fazendo gráficos
plt.plot(t_a, pos, label='MRUV')
plt.xlabel('t')
plt.ylabel('d(t)')
plt.legend()
plt.show()