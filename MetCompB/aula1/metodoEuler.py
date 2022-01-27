#Método de Euler explícito: decaimento radioativo
# 1 - Faça um programa que calcule a evolução do decaimento radioativo. Use \tau=2, x_0=100 e dt =0.1,  0.5 e 1.
import numpy as np
import matplotlib.pyplot as plt


def met_eulerex(x0, tau, dt, tf):
    '''
    Método de Euler para a resolução de EDO numéricamente.
    Os argumentos dessa função foram criados com base em uma
    EDO, caso a EDO for diferente mude os argumentos e a funcd
    :param x0: valor inicial de x
    :param tau: constante
    :param dt: delta t
    :param tf: tempo final até onde calcular numéricamente
    :return: retorna uma lista com os valores y(x) da solução da EDO
    '''
    funcd = lambda x: -x/tau
    valores = [x0]
    for t in np.arange(0, tf, dt):
        x0 += (funcd(x0))*dt
        valores.append(x0)
    return valores


def met_eulerim(x0, dt, tf, tau):
    '''
    Método de Euler Implícito para plotar a solução de uma EDO.
    a funcd é a EDO depois dos devidos processos matemáticos necessários
    :param x0: valor inicial de x
    :param dt: delta t
    :param tf: tempo final
    :param tau: constante da EDO
    :return: retorna os valores y(x) da solução da EDO
    '''
    funcd = lambda x, t: x/(1+(t/tau))
    val = [x0]
    for t in np.arange(0, tf, dt):
        x0 = funcd(x0, dt)
        val.append(x0)
    return val


def an_decrad(x0, tau, dt, tf):
    x = lambda t: x0*np.exp(-t/tau)
    return x(np.arange(0, tf, dt))


figura = plt.figure(figsize=(17, 10))
plt.subplot(231)
plt.scatter(np.arange(0, 10.1, .1), met_eulerex(100, 2, .1, 10), s=30, c='r', marker='.', label='Euler Ex.')
plt.scatter(np.arange(0, 10.1, .1), met_eulerim(100, .1, 10, 2), s=30, c='b', marker='.', label='Euler Im.')
plt.scatter(np.arange(0, 10, .1), an_decrad(100, 2, .1, 10), s=30, c='k', marker='.', label='Analítico')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('função x(t)')
plt.title('dt=0.1')
plt.legend()
plt.subplot(232)
plt.scatter(np.arange(0, 10.5, .5), met_eulerex(100, 2, .5, 10), s=30, c='r', marker='.', label='Euler')
plt.scatter(np.arange(0, 10.5, .5), met_eulerim(100, .5, 10, 2), s=30, c='b', marker='.', label='Euler Im.')
plt.scatter(np.arange(0, 10, .5), an_decrad(100, 2, .5, 10), s=30, c='k', marker='.', label='Analítico')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('função x(t)')
plt.title('dt=0.5')
plt.legend()
plt.subplot(233)
plt.scatter(np.arange(0, 11), met_eulerex(100, 2, 1, 10), s=30, c='r', marker='.', label='Euler')
plt.scatter(np.arange(0, 11), met_eulerim(100, 1, 10, 2), s=30, c='b', marker='.', label='Euler Im.')
plt.scatter(np.arange(0, 10), an_decrad(100, 2, 1, 10), s=30, c='k', marker='.', label='Analítico')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('função x(t)')
plt.title('dt=1')
plt.legend()
plt.subplot(234)
plt.scatter(np.arange(0, 12, 2), met_eulerex(100, 2, 2, 10), s=30, c='r', marker='.', label='Euler')
plt.scatter(np.arange(0, 12, 2), met_eulerim(100, 2, 10, 2), s=30, c='b', marker='.', label='Euler Im.')
plt.scatter(np.arange(0, 10, 2), an_decrad(100, 2, 2, 10), s=30, c='k', marker='.', label='Analítico')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('função x(t)')
plt.title('dt=2')
plt.legend()
plt.subplot(235)
plt.scatter(np.arange(0, 13, 3), met_eulerex(100, 2, 3, 10), s=30, c='r', marker='.', label='Euler')
plt.scatter(np.arange(0, 13, 3), met_eulerim(100, 3, 10, 2), s=30, c='b', marker='.', label='Euler Im.')
plt.scatter(np.arange(0, 10, 3), an_decrad(100, 2, 3, 10), s=30, c='k', marker='.', label='Analítico')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.grid()
plt.xlabel('t(s)')
plt.ylabel('função x(t)')
plt.title('dt=3')
plt.legend()
plt.suptitle('Comparação do Método de Euler Implícito, Explícito e solução analítica')
plt.savefig('metodoeuler.png')
#plt.show()
