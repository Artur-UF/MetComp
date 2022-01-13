# Função para achar as raízes de uma função quadrática
def bahsk(a, b=0., c=0.):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return print('Essa função tem raízes não reais (complexas).')
    elif a == 0:
        return print('A variável "a" é zero então não é uma função quadrática.')
    else:
        x1 = (-b + delta ** (1/2))/2 * a
        x2 = (-b - delta ** (1/2))/2 * a
        return x1, x2


print('Vou calcular pra você as raízes de uma equação de segundo grau nesse formato: ax^2+bx+c=0')
print('Coloque os valores para a, b e c:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
print(bahsk(a, b, c))

