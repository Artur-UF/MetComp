'''
Link do colab da aula:
https://colab.research.google.com/drive/1K8TjQLOaDhfcsqn5tBsvM_yP-OEpAl9P?authuser=2
A seguir é um código vendo a tendência do método de euler implícito.
A atividade foi fazer o mesmo da demostração do colab só que com o
método implícito e o resultado foi:
z > 0
z < -2 (não faz sentido então só o anterior vale)
'''
import matplotlib.pyplot as plt
import numpy as np


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
    time = np.arange(0, tf+dt, dt)
    for t in np.arange(0, tf, dt):
        x0 = funcd(x0, dt)
        val.append(x0)
    return time, val


def an_decrad(x0, tau, dt, tf):
    x = lambda t: x0*np.exp(-t/tau)
    return x(np.arange(0, tf, dt))


plt.plot(np.arange(0, 10, .1), an_decrad(100, 2, .1, 10), 'k+')
for dt in [.1, .5, 1, 2, 3]:
    plt.plot(met_eulerim(100, dt, 10, 2)[0], met_eulerim(100, dt, 10, 2)[1])
plt.show()
