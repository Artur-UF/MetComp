'''
Gerar um gráfico do expoente de Lyapunov
'''
import numpy as np
import matplotlib.pyplot as plt


ain = 0.00001
asu = 4
da = .001
n = 400


alist = np.arange(ain, asu, da)
lylist = []
for a in alist:
    x = 0.2
    dx = 0
    ly = 0
    for i in range(n):
        x = a * x * (1 - x)
        dx = a - 2 * a * x
        ly += np.log(abs(a - 2 * a * x))
    lylist.append(ly/n)
plt.scatter(alist, lylist, marker='.', s=0.1)
plt.show()
