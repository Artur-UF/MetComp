import numpy as np
import matplotlib.pyplot as plt
import os

# Cole aqui:
#-*-*-*-*-*-*-*-*
checkpoint = 500
tf = 100
r = 0.25
#-*-*-*-*-*-*-*-*
path = os.path.join(os.getcwd(), f'SH_r{r}_t{tf}')
u = np.load(path+f'/SH-array.npy')

fig, axs = plt.subplots(2, 2, figsize=(7, 7))

axs[0, 0].imshow(u[0], origin='lower', vmin=-1, vmax=1)
axs[0, 0].set_title(f't = 0')

axs[0, 1].imshow(u[501], origin='lower', vmin=-1, vmax=1)
axs[0, 1].set_title(f't = 25')


axs[1, 0].imshow(u[1001], origin='lower', vmin=-1, vmax=1)
axs[1, 0].set_title(f't = 50')

im = axs[1, 1].imshow(u[-1], origin='lower', vmin=-1, vmax=1)
axs[1, 1].set_title(f't = 100')

fig.suptitle(f'Swift-Hohenberg\nr = {r}')
cb_ax = fig.add_axes([.1, .04, .8, .03])
fig.colorbar(im, orientation='horizontal', cax=cb_ax, aspect=10)

#plt.show()
plt.savefig(path+'/SH-OFplot.png')
