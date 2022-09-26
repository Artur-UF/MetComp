import numpy as np
import matplotlib.pyplot as plt


l = 6
arr = np.reshape(np.arange(0, l**2), (l, l))
#print(arr)

x, y = np.loadtxt('plotising2d.txt', unpack=True)

plt.plot(x, y)
plt.show()


