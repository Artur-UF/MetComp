'''
É o exercício da urna:
Consider two urns A and B and a certain number N of balls numbered from 1 to N.
Initially, the balls are placed on urn A. Next, one of the balls is chosen at random
and transferred to the other urn. This procedure is then repeated at each time step.
We wish to determined the probability Pl(n) of having n balls in urn A at time l.
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


def dogflea(n, tf):
    '''
    1 = urna A
    0 = urna B
    '''
    bolas = np.ones(n)
    prob = []
    for t in range(tf):
        ind = np.random.randint(0, n)
        if bolas[ind] == 1:
            bolas[ind] = 0
        else:
            bolas[ind] = 1
        prob.append(sum(bolas)/n)
    return prob


n = 100
tf = 10000
probs = np.array(dogflea(n, tf))
x = np.linspace(0, 1, n)
rv = st.binom(n, 0.5)
plt.hist(probs, bins=n+1, range=(0, 1), density=True, stacked=True)
plt.grid()
plt.xlabel('P')
plt.ylabel('frequnência')
#plt.plot(x, st.binom.pmf(x, n, 0.5))
#plt.xlim(0, 1)
plt.savefig('MC_dogsflea.png')

