import numpy as np
import matplotlib.pyplot as plt

r = 0.4
tf = 20
u = np.load(f'SH-r{r}-t{tf}.npy')
c = 0
for ui in u:
    c += 1
    plt.imshow(ui, origin='lower', vmin=-1, vmax=1)
    plt.title(f'Swift-Hohenberg\narray = {c}')
    plt.pause(0.0001)
    plt.cla()
