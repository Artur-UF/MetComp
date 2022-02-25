'''
Integre numericamente o sistema de equações do modelo SIR usando método de Euler-Cromer. Para simplificar a exploração
do modelo use como parâmetros \gamma=0.5  e varie o parâmetro \beta e as condições iniciais como indicado nos ítens abaixo:

    1. Use a solução analítica para estimar um valor para \Delta t. Para testar se seu \Delta t está adequado, use
     \beta=1, S=99., I=1. e R=0.. Verifique se N se conserva em torno de 1\%.
    2. A partir da solução analítica encontre valores iniciais de S e I para os quais a infecção não se propaga.
     Integre o sistema a partir desses valores e mostre os gráficos respectivos de S,I,R . Mantenha os valores de \beta e \gamma do item 1.
    3. A partir da solução analítica encontre valores iniciais de S e I para os quais a infecção se propaga.
     Integre o sistema a partir desses valores e mostre os gráficos respectivos de S,I,R . Mantenha os valores de \gamma e \beta do item 1.
    4. Usando os dados do item 1 acima, variando apenas o parâmetro \beta, mostre que a infecção pode ser
    extinta sem que toda a população seja contaminada.
'''
import numpy as np
import matplotlib.pyplot as plt


def modsir(s0, i0, r0, tf, dt, b, g):
    n0 = s0 + i0 + r0
    fs = lambda i0, s0: -(b*i0*s0/n0)
    fi = lambda i0, s0: (b*i0*s0)/n0 - (g*i0)
    fr = lambda i0: g*i0
    s = [s0]
    i = [i0]
    r = [r0]
    n = [n0]
    for t in np.arange(0, tf, dt):
        s0 += fs(i0, s0)*dt
        s.append(s0)
        i0 += fi(i0, s0)*dt
        i.append(i0)
        r0 += fr(i0)*dt
        r.append(r0)
        n0 = s0 + i0 + r0
        n.append(n0)
    return s, i, r, n


g, b, s0, i0, r0, tf, dt = 0.5, 0.5, 99, 1, 0, 100, 0.01
t = np.arange(0, tf+dt, dt)

par1 = s0/(s0+i0)
par2 = g/b
print(par1 - par2)


plt.plot(t, modsir(s0, i0, r0, tf, dt, b, g)[0], c='purple', label='Suscetíveis')
plt.plot(t, modsir(s0, i0, r0, tf, dt, b, g)[1], c='r', label='Infectados')
plt.plot(t, modsir(s0, i0, r0, tf, dt, b, g)[2], c='orange', label='Removidos')
plt.plot(t, modsir(s0, i0, r0, tf, dt, b, g)[3], c='b', label='População')
plt.xlabel('t')
plt.ylabel('Pessoas(t)')
plt.grid()
plt.legend()
plt.title('Modelo SIR'+'\n'+r'$\beta$='+f'{b}'+r' | $\gamma$='+f'{g} | '+r'$I_{0}=$'+f'{i0}'+r' | $S_{0}=$'+f'{s0}')
plt.savefig('SIR4.png')
#plt.show()




