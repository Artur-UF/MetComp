'''
Escreva um programa que gere a evolução dos seguintes AC's para uma regra possível qualquer. Use condições iniciais nulas à exceção do sítio central.

1) Um AC de dois estados e interação entre primeiros vizinhos

2) Um AC de 3 estados e interação de primeiros vizinhos

3) Um AC de 2 estados e interação com primeiros e segundos vizinhos.
'''
import copy
from random import randint


def atomatauni(rule, n, tf, ci):
    # Decomposição da regra
    R = []
    for i in range(8):
        R.append(rule % 2)
        rule = int(rule/2)

    # Geração da condição inicial
    state = []  # estado do sistema

    if ci == 0:
        for i in range(n):
            state.append(randint(0, 1))
    if ci == 1:
        for i in range(n):
            state.append(0)
        state[int(n/2)] = 1
    statestr = ['#' if i == 1 else ' ' for i in state]
    print(*statestr, sep='')

    # Aplica regra
    statenew = []
    for i in range(n):
        statenew.append(0)
    for t in range(tf):
        for i in range(1, n-1):
            d = 4 * state[i-1] + 2 * state[i] + state[i+1]
            statenew[i] = R[d]
        d = 4 * state[-1] + 2 * state[0] + state[1]
        statenew[0] = R[d]
        d = 4 * state[n-2] + 2 * state[n-1] + state[0]
        statenew[n-1] = R[d]
        state = copy.deepcopy(statenew)
        statestr = ['#' if i == 1 else ' ' for i in state]
        print(*statestr, sep='')


rule = 13
n = 100
tf = 40
ci = 1

atomatauni(rule, n, tf, ci)
