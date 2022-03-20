'''
Use o método RK45 com passo variável para resolver o problema:

dx/dt = 1 + x^2 ;  x(0)=0

Use uma tolerância de 10^{-5} para o controle do erro.

Coloque em uma tabela os resultados para o tempo, o valor resultante com a integração RK45, a solução exata e o erro
com relação a solução exata.

Note que a solução diverge em \pi/2, portanto use um tempo final menor do que este valor.

'''
import numpy as np
import matplotlib.pyplot as plt


def passovarRK5(x0, tf, dt, tol):
    df = lambda x: 1 + x**2
    xs = [x0]
    ts = [0]
    for t in np.arange(dt, tf+dt, dt):
        ts.append(t)
        k1 = dt * df(x0)
        k2 = dt * df(x0 + ((k1 * dt)/4))
        k3 = dt * df(x0 + ((3 * dt * k1)/32) + ((9 * dt * k2)/32))
        k4 = dt * df(x0 + ((1932 * dt * k1)/2197) - ((7200 * dt * k2)/2197) + ((7296 * dt * k3)/2197))
        k5 = dt * df(x0 + ((439 * dt * k1)/216) - (8 * dt * k2) + ((3680 * dt * k3)/513) - ((845 * dt * k4)/4104))
        k6 = dt * df(x0 - ((8 * dt * k1)/27) + (2 * dt * k2) - ((3544 * dt * k3)/2565) + ((1859 * dt * k4)/4104) - ((11 * dt * k5)/40))

        x5, x6 = x0, x0

        x5 = x5 + ((25 * k1)/216) + ((1408 * k3)/2565) + ((2197 * k4)/4101) - (k5/5)
        x6 = x6 + ((16 * k1)/135) + ((6656 * k3)/12825) + ((28561 * k4)/56430) - ((9 * k5)/50) + ((2 * k6)/55)

        dtnovo = dt*(tol/(abs(x5 - x6)))**(1/6)
        if dtnovo > 2 * dt:
            dt = 2 * dt
        if dtnovo < dt / 2:
            dt = dt / 2
        x0 = x5
        xs.append(x0)
    return ts, xs


x0 = 0
tf = 1.51
tol = 1e-5
dt = 0.01

t = np.linspace(0, tf, 100)
fx = np.tan(t)

plt.plot(passovarRK5(x0, tf, dt, tol)[0], passovarRK5(x0, tf, dt, tol)[1], label='RK45')
plt.plot(t, fx, label='Analítica')
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('f(t)')
plt.savefig('passovarRK5.png', dpi=300)

tt = np.array(passovarRK5(x0, tf, dt, tol)[0])
ft = np.array(passovarRK5(x0, tf, dt, tol)[1])
fan = np.tan(tt)
err = abs(ft - fan)

print(f'|t   |RK45   |Exata  |Erro')
for tmp, rk, an, er in zip(tt, ft, fan, err):
    print(f'|{tmp:.2f}|{rk:<7.3f}|{an:<7.3f}|{er:.3f}')


