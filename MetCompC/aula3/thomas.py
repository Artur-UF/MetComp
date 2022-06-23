import numpy as np


def thomas(a, b, c, d):
    n = len(d)

    # Trata os casos das primeiras linhas
    c[0] /= b[0]
    d[0] /= b[0]

    # Fazendo a substituição no resto das linhas
    for i in range(1, n):
        ptemp = b[i] - (a[i] * c[i-])
        c[i] /= ptemp
        d[i] = (d[i] - (d[i-1] * a[i]))/ptemp

    # Atribuindo valor aos x em ordem inversa
    x = np.zeros(n)
    x[-1] = d[-1]
    for i in range(-2, -n-1, -1):
        x[i] = d[i] - (c[i] * x[i+1])

    return x



