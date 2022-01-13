def dfx(func, x, delx):
    return (func(x + delx) - func(x))/delx


fx = lambda x: 5*(x**2) - 3*x
for i in range(16):
    delx = 1*(10**-i)
    print(f'Delta x 10^{-i:<3}: {dfx(fx, 1, delx)}')
