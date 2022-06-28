import numpy as np


def mtzthomas(k, s, dd):
    # Matriz B
    a1 = np.eye(s, k=-1) * k
    b1 = np.eye(s) * (2 - (2 * k))
    c1 = np.eye(s, k=1) * k
    B = a1 + b1 + c1

    # Produto da matriz B
    g = np.dot(B, dd)

    # Matriz C
    a2 = np.eye(s, k=-1) * (-k)
    b2 = np.eye(s) * (2 + (2 * k))
    c2 = np.eye(s, k=1) * (-k)
    C = a2 + b2 + c2

    Cinv = np.linalg.inv(C)

    x = np.dot(Cinv, g)
    return x


