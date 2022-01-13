# Fazendo plots com as atividades anteriores
import numpy as np
import matplotlib.pyplot as plt
colt, coly, colv, cola = np.loadtxt('valoresnp.txt', unpack=True, skiprows=1)
figura = plt.figure(figsize=(20, 5))
plt.subplot(131)                        # o () depois do subplot é a configuração da figura | 131 = 1 linha 3 colunas 1 lugar |
plt.plot(colt, coly, 'k:')              # cores | k=preto | b=azul | g=verde |
plt.xlabel('t(s)')                      # linha | : = pontilhada | -- = tracejada | '' = sólida |
plt.ylabel('y(m)')
plt.title('Posição x Tempo')
plt.subplot(132)
plt.plot(colt, colv, 'b--')
plt.xlabel('t(s)')
plt.ylabel('v(m/s)')
plt.title('Velocidade x Tempo')
plt.subplot(133)
plt.plot(colt, cola, 'g.')
plt.xlabel('t(s)')
plt.ylabel('a(m/s²)')
plt.title('Aceleração x Tempo')
plt.suptitle('Queda com resistência')
plt.show()
#plt.savefig('plotsaula6.pdf')