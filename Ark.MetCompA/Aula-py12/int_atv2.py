'''
a) Ler os dados e, usando o método do trapézio, calcular a partir deles, uma
aproximação para a posição da partícula na direção x em função do
tempo.
b) Fazer uma figura que mostre a curva da velocidade em função do tempo
e a posição da partícula em função do tempo.
'''
import numpy as np
import matplotlib.pyplot as plt


def int_pontos(yi, dx):
    fx = (yi[0] + yi[-1])/2 + sum(yi[1:-1])
    return fx*dx


t, v = np.loadtxt('velocidades.dat', unpack=True)
d = list()
sd = 0
for i in range(1, len(t)):
    sd += int_pontos(v[i-1:i+1], 1)
    d.append(sd)

figura = plt.figure(figsize=(15, 5))
plt.subplot(121)
plt.plot(t, v, 'k', label='v(t)')
plt.title('Velocidade com o tempo')
plt.ylabel('v(m/s)')
plt.xlabel('t(s)')
plt.grid()
plt.xlim(0, 100)
plt.legend()
plt.subplot(122)
plt.plot(t[:-1], d, 'g', label='d(t)')
plt.title('Distância com o tempo')
plt.ylabel('d(m)')
plt.xlabel('t(s)')
plt.grid()
plt.xlim(0, 100)
plt.legend()
plt.show()
