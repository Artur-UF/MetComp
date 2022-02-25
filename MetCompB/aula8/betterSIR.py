'''
Integre numericamente o sistema de equações do modelo SIR usando método de RK2. Para simplificar a exploração do
 modelo use como parâmetros \gamma=0.5  e varie o parâmetro \beta e as condições iniciais.

     Trace um gráfico para e evolução de S, I e R para \beta=1, S=99, I=1 e R=0.
'''
import numpy as np
import matplotlib.pyplot as plt


def rk2SIR(s0, i0, r0, tf, dt, b, g):
    n0 = s0 + i0 + r0
    fs = lambda i0, s0: -(b * i0 * s0 / n0)
    fi = lambda i0, s0: (b * i0 * s0) / n0 - (g * i0)
    fr = lambda i0: g * i0
    s, i, r, n = [s0], [i0], [r0], [n0]
    for t in np.arange(0, tf, dt):
        saux = s0 + fs(i0, s0)*(dt/2)
        iaux = i0 + fi(i0, s0) * (dt / 2)
        s0 += fs(iaux, saux)*dt
        s.append(s0)
        i0 += fi(iaux, saux)*dt
        i.append(i0)
        r0 += fr(iaux)*dt
        r.append(r0)
        n0 = s0 + i0 + r0
        n.append(n0)
    return s, i, r, n


s0, i0, r0, tf, dt, b, g = 99, 1, 0, 25, 0.1, 1, 0.5
t = np.arange(0, tf+dt, dt)


plt.plot(t, rk2SIR(s0, i0, r0, tf, dt, b, g)[0], label='Suscetível')
plt.plot(t, rk2SIR(s0, i0, r0, tf, dt, b, g)[1], label='Infectados')
plt.plot(t, rk2SIR(s0, i0, r0, tf, dt, b, g)[2], label='Removidos')
plt.plot(t, rk2SIR(s0, i0, r0, tf, dt, b, g)[3], label='População')
plt.grid()
plt.legend()
plt.title('SIR: Runge-Kutta\n'+r'$\beta=$'+f'{b}'+r' | $\gamma=$'+f'{g}')
plt.savefig('rk2SIR.png')
#plt.show()
