import numpy as np
from numpy.random import randint


def tabuleiro(l):
    # Geração do Espaço
    sist = np.reshape(np.arange(1, l**2+1), (l, l))
    row = np.zeros(l)
    line = np.zeros((l+2, 1))
    sist = np.hstack((np.hstack((line, np.vstack((row, np.vstack((sist, row)))))), line))
    return sist


def mkv_disc(k, sist):
    # Localização do termo inicial
    kloc = np.where(sist == k)[0][0], np.where(sist == k)[1][0]

    # Sorteio do vizinho
    viz = randint(1, 5)

    # Verificação e atribuição da nova pisição
    if viz == 1:
        newloc = kloc[0], kloc[1] + 1
        if sist[newloc[0]][newloc[1]] != 0:
            kloc = newloc
    if viz == 2:
        newloc = kloc[0] - 1, kloc[1]
        if sist[newloc[0]][newloc[1]] != 0:
            kloc = newloc
    if viz == 3:
        newloc = kloc[0], kloc[1] - 1
        if sist[newloc[0]][newloc[1]] != 0:
            kloc = newloc
    if viz == 4:
        newloc = kloc[0] + 1, kloc[1]
        if sist[newloc[0]][newloc[1]] != 0:
            kloc = newloc

    return kloc


def gen_trmtz(sist):
    # Gerando a Matriz
    l = len(sist[0]) - 2
    trmtz = np.zeros((l**2, l**2))

    # Atribuindo valores a matriz
    for j in range(1, 1 + l**2):
        for i in range(1, 1 + l**2):
            kloc = np.where(sist == j)[0][0], np.where(sist == j)[1][0]
            nloc = np.where(sist == i)[0][0], np.where(sist == i)[1][0]
            if j == i:
                zeros = 0
                if sist[kloc[0]][kloc[1]+1] == 0:
                    zeros += 1
                if sist[kloc[0] - 1][kloc[1]] == 0:
                    zeros += 1
                if sist[kloc[0]][kloc[1] - 1] == 0:
                    zeros += 1
                if sist[kloc[0] + 1][kloc[1]] == 0:
                    zeros += 1
                trmtz[j-1][i-1] = zeros/4
            else:
                distx = abs(kloc[1] - nloc[1])
                disty = abs(kloc[0] - nloc[0])
                d = np.hypot(distx, disty)
                if d == 1:
                    trmtz[j-1][i-1] = 1/4
    return trmtz


def trans_mtz(trmt, pi):
    return np.dot(trmt, pi)


sist = tabuleiro(3)
trmtz = gen_trmtz(sist)
pi = np.zeros(9)
pi[-1] = 1
for i in range(15):
    print(pi)
    pi = trans_mtz(trmtz, pi)

