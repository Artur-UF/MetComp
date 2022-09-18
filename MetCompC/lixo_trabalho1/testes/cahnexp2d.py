import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)

xmin = 0

xmax = 1

tmin = 0

tmax = 10

dt = 0.5*(10**-6)

dx = 1/128

gamma = 0.01

difd = 1

t = 0

l = int((xmax/dx))

cc = np.random.rand(l, l)*2 - 1

c1 = difd*dt/(dx**2)

c2 = (gamma**2)*c1/(dx**2)

fig = plt.figure()

plt.title(t)

plt.imshow(cc, cmap="RdYlBu", vmin=-1, vmax=1)

plt.pause(0.1)
u = 0
while (t < tmax):
    cc1 = np.copy(cc)*c1
    cc2 = np.copy(cc)*c2
    cc3 = np.copy(cc**3)*c1
    for i in range(l):
        for j in range(l):
            n = i - 2
            m = j - 2
            cc[n][m] =(   (( -4* (cc3[n][m] - cc1[n][m]) 
                             +  (cc3[n+1][m] + cc3[n][m+1] + cc3[n-1][m] + cc3[n][m-1]
                                  -cc1[n+1][m] - cc1[n][m+1] - cc1[n-1][m] - cc1[n][m-1])
                                )
                            )
                            -( 12*cc2[n][m]
                                - 6*(cc2[n+1][m] + cc2[n][m+1] + cc2[n-1][m] + cc2[n][m-1])
                                + 2*(cc2[n+1][m+1] + cc2[n-1][m+1] + cc2[n+1][m-1] + cc2[n-1][m-1])
                                + 1*(cc2[n+2][m] + cc2[n][m+2] + cc2[n-2][m] + cc2[n][m-2])
                                )
                        ) + cc[n][m]
    t = round(t + dt, int(-np.log10(dt) + 2))
    u += 1
    plt.cla()
    plt.title(t)
    plt.imshow(cc, cmap="RdYlBu", vmin=-1, vmax=1)
    if u%(2*180) == 0:
        fig.savefig(".\\compara\\a%.2f.png" % int(25*u/9), dpi=fig.dpi)
    plt.pause(0.01)
    if u == 18000:
        break
plt.show(block=False)
