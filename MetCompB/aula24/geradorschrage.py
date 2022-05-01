'''
1) Escreva um gerador para o método de Schrage

2) Faça gráficos para o teste espectral do gerador
'''
import matplotlib.pyplot as plt


def randger(m, a, xi):
    r = m % a
    q = int(m/a)
    while True:
        if (a * xi) % m >= 0:
            xi = (a * xi) % m
            yield xi
        else:
            xi = a * (xi % q) - r * int(xi/q) + m
            yield xi


m = 2147483647
a = 16807
xi = 5
n = 500
gerador = randger(m, a, xi)
xp = [xi/m]
for i in range(n):
    xp.append(next(gerador)/m)
xm = xp[1:]
plt.scatter(xm, xp[:n], marker='.', label=f'seed={xi}')
plt.xlabel(r'$x_{i+1}$')
plt.ylabel(r'$x_{i}$')
plt.title('Números aleatórios pelo\nMétodo de Schrage')
plt.grid()
plt.legend()
plt.savefig('random.png')
