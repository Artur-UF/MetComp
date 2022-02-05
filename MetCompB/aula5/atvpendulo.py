'''
Use a plataforma colab para escrever um programa que integre numericamente o problema do pêndulo simples a partir de
condições iniciais x_0 e v_0. Faça um relatório (pode ser no colab ou latex) para descrever o problema e interpretar os
resultados encontrados. Use w=1, g=10m/s^2,  l=10m, tf=24s e as seguintes condições iniciais:

  1.  v_0=0, x_0=0.1
  2.  v_0=0, x_0=0.5
  3.  v_0=0, x_0=1.0
  4.  v_0=0, x_0=3.0
  5.  v_0=-0.1, x_0=3*3.14159
  6.  v_0=0.1, x_0=-3*3.14159

1) Faça gráficos de x por t para os ítens 1, 2, 3 e 4. Calcule o valor do período no caso de pequenos ângulos e
comente o que ocorre com o período a medida que o ângulo inicial aumenta.

2) Faça gráficos do espaço de fases, x por v. Compare os comportamentos encontrados para os ítens 1, 2 ,3 e 4 com o
encontrado nos ítens 5 e 6.

3) Faça gráficos da energia total para cada item e compare com o valor que se espera analiticamente.

Anexe o pdf de seu relatório latex ao moodle.

'''
import numpy as np
import matplotlib.pyplot as plt


def eulercr2(x0, v0, tf, dt, w):
    '''
    Método de Euler-Cromer para equações diferencais de 2 ordem.
    funcd é a função doferencial da vez
    :param x0: valor inicial
    :param v0: outro valor inicial
    :param tf: intervalo de tempo a ser calculado
    :param dt: delta t
    :param w, m: parâmetros para a funcd
    :return: retorna duas listas com os valores de y e y'
    '''
    funcd = lambda x, w: -(w**2)*np.sin(x)
    pos = []
    vel = []
    for t in np.arange(0, tf, dt):
        x0 += v0*dt
        pos.append(x0)
        v0 += funcd(x0, w)*dt
        vel.append(v0)
    return pos, vel


def energia(x0, v0, tf, dt, w, l, g, m):
    v = np.array(eulercr2(x0, v0, tf, dt, w)[1])
    x = np.array(eulercr2(x0, v0, tf, dt, w)[0])
    e = (m*(l**2)*(v**2)/2) + m*g*l*(1-np.cos(x))
    return e


tf, w, g, l = 24, 1, 10, 10
t = np.arange(0, tf, .01)

lx0s = [0.1, 0.5, 1, 3]
'''
nos = []
for xi in lx0s:
    print(f'Valores da intersecção para o X0={xi}:')
    for xos, ti in zip(eulercr2(xi, 0, tf, .1, w)[0], t):
        if xi == .1:
            if -0.01 < xos < 0.01:
                print(f'f({ti:.3f})={xos:.3f}')
        elif -0.1 < xos < 0.1:
            print(f'f({ti:.3f})={xos:.3f}')
'''

print(f'Períodos para cada escolha de x0:\n'
      f'T(0.1)=6.2 s\n'
      f'T(0.5)=6.4 s\n'
      f'T(1)=6.7 s\n'
      f'T(3)=16.2 s')
'''
figura = plt.figure(figsize=(20, 5))
plt.subplot(131)
for xo in lx0s:
    plt.plot(t, eulercr2(xo, 0, tf, .1, w)[0], label='$x_{0}=$'+f'{xo}')
plt.legend()
plt.title(r'Tempo $\times$ Posição')
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.grid()
#plt.savefig('pendxt.png')
plt.subplot(132)

for xo in lx0s:
    plt.plot(eulercr2(xo, 0, tf, .1, w)[0], eulercr2(xo, 0, tf, .1, w)[1], label='$x_{0}=$'+f'{xo}')
plt.plot(eulercr2(np.pi, -0.1, tf, .1, w)[0], eulercr2(np.pi, -0.1, tf, .1, w)[1], label=r'$x_{0}=\pi$')
plt.plot(eulercr2(-np.pi, 0.1, tf, .1, w)[0], eulercr2(-np.pi, 0.1, tf, .1, w)[1], label=r'$x_{0}=-\pi$')

plt.legend()
plt.title(r'Posição $\times$ Velocidade')
plt.xlabel('x')
plt.ylabel('V(x)')
plt.grid()
#plt.show()
plt.savefig('pendvt.png')

plt.subplot(133)
'''
for xo in lx0s:
    plt.plot(t, energia(xo, 0, tf, .01, w, l, g, 1), label='$x_{0}$'+f'={xo}')
plt.plot(t, energia(np.pi, -0.1, tf, .01, w, l, g, 1), label='$x_{0}=\pi$')
plt.plot(t, energia(-np.pi, 0.1, tf, .01, w, l, g, 1), label='$x_{0}=-\pi$')
plt.legend()
plt.xlabel('t(s)')
plt.ylabel('E(t)')
plt.grid()
plt.title(r'Tempo $\times$ Energia')
plt.savefig('pendenerg2.png')
#plt.savefig('penduloEXPIV.png')
