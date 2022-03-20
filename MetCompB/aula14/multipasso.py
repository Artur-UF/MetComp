'''
Método Multipasso aplicado em Oscilador de van der Pool.
 O oscilador de van der Pool envolve um termo linear, como no OHS, e um termo não linear que funciona como fonte e sumidouro de energia:
  d²x/dt² = \mu(1 - x²)dx/dt - x
  Integre numericamente o OvdP usando método multipasso explícito com s=1. Use x(0)=0.5 e v(0)=0

   1. Através de gráficos x \times t, v \times t e x \times v, mostre que o OvdP se reduz ao OHS no limite \mu=0.
   2. Faça os gráficos x \times t, v \times t para \mu=0.5 e \mu=4.0. O que se observa de diferença nesses casos?
   3. Superponha os gráficos do espaço de fases para \mu=0.0, \mu=0.1, \mu=0.5, \mu=1.0, \mu=2.0 e \mu=4.0. Observe as diferenças.

'''
import numpy as np
import matplotlib.pyplot as plt


def multipass(x0, v0, tf, dt, mu):
    d2f = lambda x, v: mu * (1 - x**2) * v - x
    pos = [x0]
    vel = [v0]
    x1 = x0
    v1 = v0
    t0, t1 = 0, 0
    # Caso d2f tenha dependência em t, ele deve ser atualizado também
    for t in np.arange(dt, tf+dt, dt):
        x2 = x1 + dt * ((3*v1/2) - (v0/2))
        v2 = v1 + dt * ((3*d2f(x1, v1)/2) - (d2f(x0, v0)/2))
        x0 = x1
        x1 = x2
        v0 = v1
        v1 = v2
        pos.append(x2)
        vel.append(v2)
    return pos, vel


x0 = 0.5
v0 = 0
tf = 10
dt = 0.01
mu = [0, 0.1, 0.5, 1, 2, 4]

t = np.arange(0, tf+dt, dt)

figura = plt.figure(figsize=(20, 5))
plt.subplot(131)
for muu in mu:
    plt.plot(t, multipass(x0, v0, tf, dt, muu)[0], label=r'$\mu$='+f'{muu}')
#plt.plot(t, multipass(x0, v0, tf, dt, mu[0])[0])
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title(r'x $\times$ t')

plt.subplot(132)
for muu in mu:
    plt.plot(t, multipass(x0, v0, tf, dt, muu)[1], label=r'$\mu$='+f'{muu}')
#plt.plot(t, multipass(x0, v0, tf, dt, mu[0])[1])
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('v(t)')
plt.title(r'v $\times$ t')

plt.subplot(133)
for muu in mu:
    plt.plot(multipass(x0, v0, tf, dt, muu)[0], multipass(x0, v0, tf, dt, muu)[1], label=r'$\mu$='+f'{muu}')
#plt.plot(multipass(x0, v0, tf, dt, mu[0])[0], multipass(x0, v0, tf, dt, mu[0])[1])
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('v')
plt.title(r'x(t) $\times$ v(t)')

plt.savefig('multipassOVDP.png', dpi=300)

