import numpy as np

x = 5
k = -5
u = np.eye(x, k=k)
c = 1
for i in range(2*x-1):
    c *= -1
    k += 1
    u += np.eye(x, k=k)*c
u0 = np.random.uniform(-1, 1, (x, x))
print(u)
print(u0)