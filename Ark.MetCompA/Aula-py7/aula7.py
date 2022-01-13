# -*- coding: utf-8 -*-
"""Aula_Python_8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wdj-lQTeUJ8_6rHRe5B1DXqY6O_PRltP

#Funções, variáveis globais e classes
"""

a = 5.  # esta é uma variável global

if a > 0:
  b = 10.    # esta é outra variável global


def func(c):
  d = 0.    # esta é uma variável local
  print('a=',a,' b=',b)
  print('c=',c,' d=',d)


func(3.)   # chamando a função func

print('a=',a,' b=',b)    # a e b ainda existem, pois são globais
print('c=',c,' d=',d)    # c e d não existem mais

"""Quando usamos funções corretamente, é muito comum acabar passando vários argumentos para a função. Por exemplo:



> def particula(indice,x,y,z,vx,vy,vz,m,q,s,nome,taxa_decaimento):



Uma alternativa para evitar passar tantas variáveis é usar variáveis globais. 
"""

a = 5

def funcao_boa(b):
  a = 10 * b  # essa é uma variável local 'a'
  print("Na funcao_boa 'a' é:", a)

def funcao_hacky(b):
  global a
  a = 10 * b   # essa é uma variável global 'a'
  print('Na funcao_hacky "a" é:', a)

print("Antes de iniciar 'a' é:", a)

funcao_boa(2)
print("Após funcao_boa 'a' é:", a)

funcao_hacky(2)
print('Após funcao_hacky "a" é:', a)

"""Entretanto, nem sempre é recomendado usar variáves globais. Uma solução melhor é usar **Classes**.

#Uma brevíssima introdução a Classes em Python

Em Python, toda informação que já usamos é representada na forma de um objeto. Por exemplo, o número 1 é um objeto da classe int, 2.75 é um objeto da classe float e assim por diante.

Classes permitem organizar dados e funcionalidades juntos. Criar uma nova classe significa criar um novo “tipo” de objeto, permitindo que novas “instâncias” (exemplos) desse tipo sejam produzidas. Esse mecanismo de classes constitui a chamada **programação orientada a objetos**. Linguagens orientadas a objetos como o Python permitem a definição de novas classes quando se programa.

Classes são abstrações de alguma 'coisa'. Essa 'coisa' possui um estado e um comportamento. Um estado é definido por um conjunto de variáveis, que chamamos de **atributos**. Os estados podem ser modificados por meio de ações sobre o objeto, que definem o seu comportamento. Essas ações correspondem a funções e são chamadas de **métodos**. Então, cada instância de uma classe pode ter atributos anexados a ela ou métodos.

Por exemplo, podemos definir uma classe Veiculo. 

Os atributos podem ser:

*   Tipo (avião, carro, barco, ...)
*   Ano
*   Modelo
*   Cor
*   Número de passageiros que comporta 
*   velocidade

Os métodos podem ser:

*   acelera(vel): acelera até velocidade vel
*   pare():  faz velocidade = 0

Assim como definições de funções (com comando def), é preciso definir e executar as classes antes para que elas tenham qualquer efeito.
"""

#definição de classe

class Carro:
    pass

"""A classe Carro não possui nenhum atributo nem métodos, mas com ela já podemos criar objetos, ou seja, novas instâncias desta classe. 

Para a instanciação de uma classe (“invocar” um objeto classe), usamos a mesma sintaxe de chamar uma função. É como se o objeto classe do exemplo acima fosse uma função sem parâmetros, que devolve uma nova instância da classe.
"""

onix = Carro()
hb20 = Carro()
onix

"""Além de instanciação, as classes também permitem outro tipo de operação: as referências a atributos. Para criar atributos, basta fazer atribuições usando objeto.atributo e usar os atributos como variáveis. """

onix.ano = 2017
onix.cor = 'preto'
onix.modelo = 'Onix'

hb20.ano = 2015
hb20.cor = 'branco'
hb20.modelo = 'HB20'

hb20.ano += 5
print(hb20.ano)

"""
A operação de instanciação (“invocar” um objeto classe) acima criou um objeto vazio.  Mas também podemos criar novos objetos com um estado inicial já  pré-determinado. No caso da classe Carro, podemos deixar as propriedades de modelo, ano e cor como atributos da classe e inicializá-las quando um objeto é criado (instanciado). Para isso, usamos na definição da classe um método especial chamado \_\_init\_\_(), conhecido como construtor da classe. 



"""

class Carro:

  def __init__(self,m,a,c):
    self.ano = a
    self.cor = c
    self.modelo = m

# Novas instâncias são criadas e nelas os atributos ‘modelo’, ‘ano’ e ‘cor’
# são criados automaticamente com os valores passados como argumentos do construtor

renegade = Carro('Renegade',2019, 'marrom')
t_cross = Carro('T-Cross',2021,'cinza')

renegade.ano += 2    # podemos acessar e modificar os atributos do objeto renegade
print(renegade.ano)

"""Você deve estar se perguntando o que é esse tal de *self*. 

Cada método de uma classe recebe como primeiro argumento uma referência à instância que chama o método. Isso permite que o objeto acesse os seus próprios atributos e métodos. Por convenção, chamamos esse primeiro argumento de self.

Desta forma, ao definirmos qualquer método dentro da classe, um atributo pode ser criado, acessado ou modificado usando self.atributo.

**Métodos**
"""

class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano = a
        self.cor = c
        self.vel = 0   # o objeto carro é iniciado com velocidade zero
        self.vmax = vm  # velocidade limite (máxima)


    def imprime_info(self):
        if self.vel == 0: # carro está parado e podemos ver o modelo e a cor
            print( f'O carro {self.modelo} {self.cor} está parado.')
        elif self.vel < self.vmax:
            print( f'O {self.modelo} {self.cor} está andando a {self.vel:.1f} km/h')
        else:
            print( f'Perigo! O {self.modelo} {self.cor} está desgovernado!')

    def acelera(self, v):
        self.vel = v
        if self.vel > self.vmax:
            self.vel = self.vmax
        Carro.imprime_info(self)

    def para(self):
        self.vel = 0
        Carro.imprime_info(self)

g = Carro('Gol', 1998, 'preto', 180.)   # g é uma instância de Carro
Carro.acelera(g,80.) # chama o método acelera de Carro

"""O método *acelera* tem dois argumentos: *self* e *v*. Quando o método é executado, *self* é o objeto g e *v* é 60. """

Carro.para(g) # chama o método para de Carro

"""Note que na chamada do método *para* apenas a instância *self* é passada, já que este método só recebe um argumento.

Esse notação deixa explícita a passagem dos objetos como primeiro argumento de cada método, mas ela é redundante, pois todo objeto sabe a que classe ele pertence. (Mas lembre do Zen do Python: 'Explícito é melhor que implícito')

Uma maneira mais enxuta de chamar os métodos é semelhante a dos atributos (usando '.'). Como o primeiro argumento é sempre o próprio objeto, ele pode ser evitado. Por exemplo:
"""

g.acelera(50.)
print(g.vel)

"""Nesse caso em que o objeto é diretamente invocado, o argumento para self é desnecessário e só *v* é passado. 

"""

g.para()
print(g.vel)

"""Abaixo mostramos o mesmo código que define a classe de antes, só que agora com uma notação mais enxuta. """

class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano = a
        self.cor = c
        self.vel = 0
        self.vmax = vm  # velocidade limite (máxima)


    def imprime_info(self):
        if self.vel == 0: # carro está parado e podemos ver o modelo e a cor
            print( f'O carro {self.modelo} {self.cor} está parado.')
        elif self.vel < self.vmax:
            print( f'O {self.modelo} {self.cor} está andando a {self.vel:.1f} km/h')
        else:
            print( f'Perigo! O {self.modelo} {self.cor} está desgovernado!')

    def acelera(self, v):
        self.vel = v
        if self.vel > self.vmax:
            self.vel = self.vmax
        self.imprime_info()    #chama o método imprime_info para exibir o estado da instância

    def para(self):
        self.vel = 0
        self.imprime_info()   #chama o método imprime_info para exibir o estado da instância

"""# Caminhante Aleatório
Um modelo físico fundamental na Mecânica Estatística é o do Caminhante Aleatório. Na sua versão mais simples, trata-se de uma partícula movendo-se em um espaço unidimensional que a tempos fixos (por exemplo, t=1,2,3,4,...) desloca-se com um passo l de tamanho fixo (por exemplo, l=1) com igual probabilidade para um lado ou para o outro nesse espaço unidimensional.

Podemos usar a ideia de classes em Python para explorar o movimento de caminhantes aleatórios.
"""

import random as rand
class RandomWalker:
  x = 0      #todos os caminhantes começam na origem
  def mov(self):
    self.x += 2*rand.randint(0,1)-1

#criando uma instância, um elemento, da classe Walker
c1 = RandomWalker()
print(f"Posição inicial de c1, c1.x = {c1.x:2d}")  # verificando a posição
for i in range(10): # movendo c1 10 passos
  c1.mov()
print(f"Posição de c1 após 10 passos c1.x = {c1.x:2d}" )  # verificando a nova posição

#criando o elemento c2
c2 = RandomWalker()
print(f"Posição inicial de c2, c2.x= {c2.x:2d}")  # verificando a posição de c2
for i in range(10): # movendo c2 10 passos
  c2.mov()
print(f"Posição de c2 após 10 passos c2.x = {c2.x:2d}")  # verificando a nova posição de c2

#Criando uma lista de M caminhantes
M =10
c = list(RandomWalker() for i in range(M))

#acessando a posição do quinto elemento da lista
print(f"A posição inicial do elemento 5 da lista é: {c[4].x:2d}")

#Movendo N passos todos os elementos da lista
N=20
for i in range(N):
  for j in c:
    j.mov()
pos=list(c[i].x for i in range(M))
print(pos)

# a mesma coisa de forma mais sintética, usando map e a função lambda
list(map(lambda i:i.mov(), c)) #movendo todos de um passo
pos=list(map(lambda i:i.x,c))  #escrevendo a posição na lista pos
print(pos)

#Agora um grande número de caminhantes e muitos passos.
M= 10000  # número de caminhantes
N= 1000  # número de passos
c = list(RandomWalker() for i in range(M))
for i in range(N):
  list(map(lambda i:i.mov(), c))
pos = list(map(lambda i:i.x,c))

#Façamos um histogram da distribuição de posições
import matplotlib.pyplot as plt

plt.hist(pos,bins=30,align='left')
plt.show()

"""Para saber mais sobre esse assunto, pesquise por programação orientada a objetos em Python nas referências bibliográficas da disciplina. Você também pode consultar em:
https://docs.python.org/pt-br/3/tutorial/classes.html

Nota: Este conteúdo não será avaliado na prova.  

"""