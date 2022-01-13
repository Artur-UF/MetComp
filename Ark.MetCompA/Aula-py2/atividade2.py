# Transformar celsius em fahrenheit
def celtofahr(c):
    """
    Essa função converte graus celsius em graus fahrenheit
    :param c: valor em celsius
    :return: valor em fahrenheit
    """
    return (c * 1.8) + 32


t = float(input('Qual o valor de celcius que você quer converter? '))
print(f'{t}°C em fahrenheit é: {celtofahr(t):.2f}°F')
