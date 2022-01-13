# Erro de integrais
import numpy as np
import matplotlib.pyplot as plt


def int_trap(func, a, b, n):
    '''Calcula a integral de uma função entre os
    limites a e b pela área de n trapézios.
    func: função analítica
    a, b: limites inferior e superior
    n: número de secções da área sob a função
    return: o valor da integral
    '''
    dx = (b - a)/n
    sdx = ((func(a) + func(b))/2)
    for i in range(1, n):
        sdx += func(a + i*dx)
    return sdx*dx


def int_simpson(fx, a, b, n):
    '''Integração pelo Método de Simpson.
    fx: função a ser integrada
    a, b: limites inferior e superior para a integração
    n: número de secções da área integrada
    return: o valor da integral definida de fx
    '''
    if n % 2 != 0:
        n += 1
    h = (b-a)/n
    x = list(a+(j*h) for j in range(n+1))
    si = 4*sum(map(fx, x[1:n:2]))
    sp = 2*sum(map(fx, x[2:n-1:2]))
    return (h/3)*(fx(a) + fx(b) + si + sp)


def erro_int(ia, inum):
    '''
    Função que calcula o erro entre o método analítico
    e algum numérico de integral.
    :param ia: valor analítico da integral
    :param inum: valor numérico da integral
    :return: módulo do erro entre eles
    '''
    return abs(ia - inum)


def aj_lin(xi, yi):
    '''
    Realiza o ajuste linear de pontos em uma reta de
    ajuste no formato "y = ax + b".
    :param xi: coordenadas x dos pontos
    :param yi: coordenadas y dos pontos
    :return: coeficiente angular "a" e coeficiente
             linear "b" da reta de ajuste
    '''
    n = len(xi)
    mxy = sum(xi*yi)/n
    mx = sum(xi)/n
    my = sum(yi)/n
    mqx = sum(xi**2)/n
    a = (mxy - (mx*my))/(mqx - (mx**2))
    b = ((mqx*my) - (mx*mxy))/(mqx - (mx**2))
    return a, b


fx = lambda x: 1/((x**2) + 1)   # Função dada pela atividade
n = 2**np.arange(2, 21, 2)
ia = np.arctan(3)-np.arctan(-3)   # Valor analítico da integral de fx
logdx = np.log10(6/n)   # array com os valores de dx dimensionados pelo log

# || Método do Trapézio ||
# função que retorna a integral de fx com dependência
# com o valor de intervalos
trap = lambda nn: int_trap(fx, -3, 3, nn)
# lista com os valores das interais com cada numero de intervalos
itrap = list(map(trap, n))

# log da função erro entre o método do trapézio e analítico
logetpz = np.log10(erro_int(ia, itrap))
# coeficientes da reta que melhor aproxima os
# dados de (logdx, logetpz)
parstpz = aj_lin(logdx, logetpz)
# função que representa essa reta
ftpz = lambda delx: parstpz[0]*delx + parstpz[1]


# || Método de Simpson ||
# função que retorna o valor da integral por simspon
# dependendo do n
simp = lambda nn: int_simpson(fx, -3, 3, nn)
# lista com todos os valores correspondentes a cada n
isimp = list(map(simp, n))

# log da função do erro entre o método de Simpson e analítico
logesimp = np.log10(erro_int(ia, isimp))
# coeficientes da reta que melhor aproxima
# a parte linear dos dados (logdx, logesimp)
parssimp = aj_lin(logdx[:6], logesimp[:6])
# função que representa essa erta
fsimp = lambda delx: parssimp[0]*delx + parssimp[1]

plt.figure(figsize=(20, 5))
plt.subplot(131)
plt.scatter(logdx, logetpz, s=30, c='r', marker='.', label='Dados')
plt.plot(logdx, ftpz(logdx), 'b', label='Reta de ajuste')
plt.ylim(-13, 0)
plt.title('Erro pelo método do trapézio')
plt.ylabel('log(|erro|)')
plt.xlabel(r'log($\Delta x$)')
plt.text(-5, -4, f'a = {parstpz[0]:.3f}\nb = {parstpz[1]:.3f}',
         bbox=dict(boxstyle='square', ec='k', color='white'))
plt.legend()
plt.grid()
#plt.savefig('errtpz.jpeg')
#plt.show()

plt.subplot(132)
plt.scatter(logdx, logesimp, s=30, c='k', marker='.', label='Dados')
plt.plot(logdx[:6], fsimp(logdx[:6]), 'magenta', label='Reta de ajuste')
plt.text(-5, -4.5, f'a = {parssimp[0]:.3f}\nb = {parssimp[1]:.3f}',
         bbox=dict(boxstyle='square', ec='k', color='white'))
plt.title('Erro pelo método de Simpson')
plt.ylim(-15.5, 0)
plt.ylabel('log(|erro|)')
plt.xlabel(r'log($\Delta x$)')
plt.legend()
plt.grid()
#plt.show()
#plt.savefig('errsimp.jpeg')

plt.subplot(133)
plt.scatter(logdx, logetpz, s=30, c='r', marker='.', label='Trapézio')
plt.plot(logdx, ftpz(logdx), 'b', label='Ajuste do trapézio')
plt.scatter(logdx, logesimp, s=30, c='k', marker='.', label='Simpson')
plt.plot(logdx[:6], fsimp(logdx[:6]), 'magenta', label='Ajuste de simpson')
plt.title('Comparação dos métodos de Simpson e do Trapézio')
plt.ylim(-15.5, 0)
plt.ylabel('log(|erro|)')
plt.xlabel(r'log($\Delta x$)')
plt.grid()
plt.legend()
plt.show()
#plt.savefig('errcomp.jpeg')
