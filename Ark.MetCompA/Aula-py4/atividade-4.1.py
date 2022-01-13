"""Escrevendo a atividade-4 em um arquivo"""
import numpy as np


def acterm(t, vterm, tao):
    """
    Função para determinar a aceleração terminal de um objeto sofrendo resistência (usa o numpy)
    :param t: tempo
    :param vterm: velocidade terminal do objeto
    :param tao: constante tao
    :return: retorna a aceleração em t
    """
    aterm = (-vterm/tao) * np.exp(-t/tao)
    return aterm


def velterm(t, vterm, tao):
    """
    Determina a velocidade de um objeto sofrendo resistência (usa o numpy)
    :param t: tempo
    :param vterm: velocidade terminal
    :param tao: constante tao
    :return: retorna a velocidade em t
    """
    v = -vterm + (vterm * np.exp(-t/tao))
    return v


def yterm(t, vterm, tao, y0):
    """
    Função para determinar a ordenada de um objeto sofrendo resistência no movimento (usa o numpy)
    :param t: tempo
    :param vterm: velocidade terminal
    :param tao: constante tao
    :param y0: ordenada inicial
    :return: retorna a coordenada y(t)
    """
    c = y0 + (vterm * tao)
    yterm = (-vterm) * (t + (tao * np.exp(-t/tao))) + c
    return yterm


tm = np.arange(0, 10.5, 0.5)
ac = list(acterm(tm, 20, 5))
yt = list(yterm(tm, 20, 5, 150))
vt = list(velterm(tm, 20, 5))
valores = open('valoresnp.txt', 'w')
valores.write(f'{"t(s)":<5} {"y(m)":<8} {"v(m/s)":<8} {"a(m/s²)"}\n')
for t, a, y, v in zip(tm, ac, yt, vt):
    valores.write(f'{t:<5} {y:<8.3f} {v:<8.3f} {a:<8.3f}\n')
valores.close()
