'''
Script do professor
'''
import numpy as np
import numpy.linalg as lin
import matplotlib
import matplotlib.pyplot as plt
import copy
matplotlib.use('TkAgg') # do this before importing pylab

fig = plt.figure()
ax = fig.add_subplot(111)

L=400
#D=1.
#dt=.5
#dx=1.
#k= D*dt/dx/dx
S = 0.002
sigma = 10.0
s0 = 10.0
x0 = 100.0
s2 = 1.0/(sigma*sigma)
x = np.linspace(0, L, 400)
sx = s0*np.exp(-(x-x0)*(x-x0)*s2)
#for[i in x print(i,s[i])]
#plt.plot(x,s)
#plt.show()
#
k = 0.4
a = k
b = 1-k*(2+S)
c = k
Cmat = np.zeros((L, L))

Cmat = Cmat + np.eye(L)*b
#print(Cmat)
Cmat = Cmat + np.eye(L, k=1)*c
#print(Cmat)
Cmat = Cmat + np.eye(L, k=-1)*a
Cmat[0][0] = 1.0;Cmat[0][1] = 0.0;
Cmat[L-1][L-1] = 1.0 ; Cmat[L-1][L-2] = 0.0;
#print(Cmat)


fvec = np.zeros(L) 
f0 = 0.0
fL = 0.0
fvec[0] = f0
fvec[L-1] = fL
f1 = copy.deepcopy(fvec)
tmax = 7000
t = 0
while t < tmax:
    f1 = np.dot(Cmat, fvec)+k*sx
    fvec = copy.deepcopy(f1)
    t = t+1


def sol_est_rad():
    a = -1    
    b = +2+S
    c = -1
    Cmat = np.zeros((L, L))
    fvec = sx
    f0 = 0.0
    fL = 0.0
    fvec[0] = f0
    fvec[L-1] = fL
    Cmat = Cmat + np.eye(L)*b
    Cmat = Cmat + np.eye(L, k=1)*c
    Cmat = Cmat + np.eye(L, k=-1)*a
    Cmat[0][0] = 1.0 ; Cmat[0][1] = 0.0;
    Cmat[L-1][L-1]=1.0;Cmat[L-1][L-2]=0.0;
    Cmat_inv = np.linalg.inv(Cmat)
    sol = np.dot(Cmat_inv, fvec)

    return sol


est = sol_est_rad()

plt.plot(x, est)
plt.scatter(x[::10], fvec[::10], marker="x", alpha=0.3, color='red')
plt.show()
