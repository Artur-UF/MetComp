'''
Trace o mapa de recorrência para o mapa logístico:

x_{n+1}=ax_n(1-x_n)

Use a=1.2, 3.1, 3.55, 4.

'''
import matplotlib.pyplot as plt


def recor(a, x0, n, r0):
    def theta(ri, rj):
        if r0 > abs(ri - rj):
            return True
        else:
            return False

    xlist = []
    nx = []
    ny = []
    for i in range(n):
        xlist.append(x0)
        x0 = a * x0 * (1 - x0)

    for i, j in enumerate(xlist):
        for k, m in enumerate(xlist):
            if theta(j, m):
                nx.append(i)
                ny.append(k)

                nx.append(k)
                ny.append(i)
    return nx, ny


a = [1.2, 3.1, 3.55, 4]
x0 = .2
n = 50
r0 = 10**(-3)

for p, a in enumerate(a, start=1):
    nome = 'recor-a'+str(p)+'.png'
    plt.figure(p)
    plt.scatter(recor(a, x0, n, r0)[0], recor(a, x0, n, r0)[1], marker='.', s=10)
    plt.xlabel(r'$n_x$')
    plt.ylabel(r'$n_y$')
    plt.title('Gráfico de Recorrência')
    plt.grid()
    plt.savefig(nome)
