import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
symb = {
    'alpha':'\u03B1',
    'Alpha':'\u0391',
    'beta':'\u03B2',
    'Beta':'\u0392',
    'gamma':'\u03B3',
    'Gamma':'\u0393',
    'delta':'\u03B6',
    'Delta':'\u0394',
    'epsilon':'\u03B5',
    'Epsilon':'\u0395',
    'zeta':'\u03B6',
    'Zeta':'\u0396',
    'eta':'\u03B7',
    'Eta':'\u0397',
    'theta':'\u03B8',
    'Theta':'\u0398',
    'iota':'\u03B9',
    'Iota':'\u0399',
    'kappa':'\u03BA',
    'Kappa':'\u039A',
    'lambda':'\u03BB',
    'Lambda':'\u039B',
    'mu':'\u03BC',
    'Mu':'\u039C',
    'nu':'\u03BD',
    'Nu':'\u039D',
    'xi':'\u03BE',
    'Xi':'\u039E',
    'omicron':'\u03BF',
    'Omicron':'\u039F',
    'pi':'\u03C0',
    'Pi':'\u03A0',
    'rho':'\u03C1',
    'Rho':'\u03A1',
    'varsigma':'\u03C2',
    'sigma':'\u03C3',
    'Sigma':'\u03A3',
    'tau':'\u03C4',
    'Tau':'\u03A4',
    'upsilon':'\u03C5',
    'Upsilon':'\u03A5',
    'phi':'\u03C6',
    'Phi':'\u03A6',
    'chi':'\u03C7',
    'Chi':'\u03A7',
    'psi':'\u03C8',
    'Psi':'\u03A8',
    'omega':'\u03C9',
    'Omega':'\u03A9',
    'vartheta':'\u03F4',
    'ihat':'i\u0302',
    'jhat':'j\u0302',
    'khat':'k\u0302',
    'uhat':'u\u0302'
}


def sup_relax(n, w, l1, l2, fxy):
    #fxy = np.zeros((n, n))
    for i in range(n):
        fxy[i][0] = 1.
        fxy[i][-1] = 0.0
        fxy[0][i] = np.exp(-l1 * i)
        fxy[-1][i] = np.exp(-l2 * i)
        fxy[0][0] = 0.
        fxy[0][-1] = 0.
        fxy[-1][0] = 0.
        fxy[-1][-1] = 0.

    #print(fxy)
    for j in range(1, n - 1):
        for i in range(1, n - 1):
            fxy[j][i] = fxy[j][i] * (1 - w) + (w / 4 * (fxy[j][i + 1] + fxy[j][i - 1] + fxy[j + 1][i] + fxy[j - 1][i]))
    return fxy


fig, ax = plt.subplots()

n = 50
w = 1.7
l1 = 10
l2 = 9


def gen():
    '''
    Gera os dados para cada frame
    '''
    global n, w, l1, l2
    fxy = np.zeros((n, n))
    '''
    xx = np.arange(50)
    yy = np.arange(50)
    x, y = np.meshgrid(xx, yy)
    '''
    t = np.arange(0, 400)
    for ti in t:
        z = sup_relax(n, w, l1, l2, fxy)
        fxy = z
        if ti % 2 == 0:
            yield z, ti


def init():
    '''
    É o inicio de todo frame após o 'run'
    '''
    ax.clear()
    plt.xlabel('x')
    plt.ylabel('y')


def run(data):
    '''
    Roda a animação com os dados fornecidos por 'data'
    '''
    z, ti = data
    '''
    # 3D
    fig.plot_surface(x, y, z, cmap='magma', label=f'')
    fig.set(xlabel='x', ylabel='y', zlabel='z')
    '''
    # Colormap
    plt.imshow(z, cmap='plasma', vmax=.8)
    plt.ylabel('y')
    plt.xlabel('x')

    plt.title(f'Eq. de Laplace: Super Relaxação'
              f'\n{symb["omega"]} = {w} | {symb["lambda"] + "1"} = {l1} | '
              f'{symb["lambda"] + "2"} = {l2} | t = {ti:>5}')


ani = animation.FuncAnimation(fig, run, gen, interval=10, init_func=init, save_count=1500)
#plt.show()

writergif = animation.PillowWriter(fps=30)
ani.save(r'D:\Aplicações\GItHub D\MetCompA\MetCompC\aula6\laplace_suprelax.gif', writer=writergif)

plt.close()
