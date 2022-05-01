'''
1 - Partindo do valor inicial x=0.7, faça um gráfico da evolução temporal do mapa logístico até 30 passos para os
 seguintes valores do parâmetro a:

    1. a=0.1
    2. a=1.2
    3. a=3.1
    4. a=4

Use pontos obtidos para fazer o gráfico, não use linhas para ligar os pontos, pois essas não tem sentido físico.

2- Use os mesmos parâmetros para fazer um gráfico de primeiro retorno do mapa logístico x_n+1 \times x_n.

x_n+1 = ax_n(1-x_n)
'''
import matplotlib.pyplot as plt


def mapa(x0, a, n):
    f = lambda x: a * x * (1 - x)
    xn1 = []
    xn = [x0]
    ns = [0]
    for ni in range(1, n+1):
        ns.append(ni)
        x1 = f(x0)
        xn1.append(x1)
        x0 = x1
        xn.append(x0)
    return xn1, xn[:-1], ns[:-1]


a = [.1, 1.2, 3.1, 4]
x0 = .7
n = 30

plt.figure(1)
for ai in a:
    plt.scatter(mapa(x0, ai, n)[2], mapa(x0, ai, n)[0], marker='o', label=f'a = {ai}')
plt.grid()
plt.legend()
plt.ylim(-0.1, 1.1)
plt.xlabel('n')
plt.ylabel(r'$x_{n+1}$')
plt.title(r'$x_{n+1} \times n$')
plt.savefig('mapalogstc1.png', dpi=300)

plt.figure(2)
for ai in a:
    plt.scatter(mapa(x0, ai, n)[1], mapa(x0, ai, n)[0], marker='o', label=f'a = {ai}')
plt.grid()
plt.legend()
plt.ylim(-0.1, 1.1)
plt.xlabel(r'$x_{n}$')
plt.ylabel(r'$x_{n+1}$')
plt.title(r'$x_{n+1} \times x_{n}$')
plt.savefig('mapalogstc2.png', dpi=300)
