# -*- coding: utf-8 -*-
"""Intergral-atv2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1caFaNxwvShBNHFVQvbFLeNqzJvhV-No-
"""

import numpy as np
import matplotlib.pyplot as plt

# Integral pelo traapézio

def int_trap(func, a, b, n):
  '''Calcula a integral de uma função entre os limites a e b pela área de n
  trapézios.
  func: função analítica
  a, b: limites inferior e superior
  n: número de secções da área sob a função
  '''
  dx = (b - a)/n
  sdx = (func(a) + func(b))/2
  for i in range(1, n):
    sdx += func(a + i*dx)
  return sdx*dx

# Método de Simpson

def int_simpson(fx, a, b, n):
  '''Integração pelo Método de Simpson.
  fx: função a ser integrada
  a, b: limites inferior e superior para a integração
  n: número de secções da área integrada
  return: o valor da integral definida de fx
  '''
  if n % 2 != 0:
    n += 1
  h = (b-a)/n
  x = list(a+(j*h) for j in range(n+1))
  si = 4*sum(map(fx, x[1:n:2]))
  sp = 2*sum(map(fx, x[2:n-1:2]))
  return (h/3)*(fx(a) + fx(b) + si + sp)

fx = lambda x: x**5 + 3*x + 5
print(int_simpson(fx, 0, 1, 1000))
print(int_trap(fx, 0, 1, 1000))

"""#Atividade 2"""

def int_simpson(fx, a, b, n):
  '''Integração pelo Método de Simpson.
  fx: função a ser integrada
  a, b: limites inferior e superior para a integração
  n: número de secções da área integrada
  return: o valor da integral definida de fx
  '''
  if n % 2 != 0:
    n += 1
  h = (b-a)/n
  x = list(a+(j*h) for j in range(n+1))
  si = 4*sum(map(fx, x[1:n:2]))
  sp = 2*sum(map(fx, x[2:n-1:2]))
  return (h/3)*(fx(a) + fx(b) + si + sp)


def bessel(m, x):
  pi = np.pi
  fx = lambda th: np.cos(m*th - x*np.sin(th))
  return (1/pi)*int_simpson(fx, 0, pi, 1000)

xi = np.linspace(0, 20, 100)
y0 = bessel(0, xi)
y1 = bessel(1, xi)
y2 = bessel(2, xi)

plt.plot(xi, y0, 'k', label=r'$J_{0}(x)$')
plt.plot(xi, y1, 'b', label=r'$J_{1}(x)$')
plt.plot(xi, y2, 'g', label=r'$J_{2}(x)$')
plt.legend()
plt.grid()
plt.xlim(0, 20)
plt.show()

def intdif(l, r):
  pi = np.pi
  k = (2*pi)/l
  return (bessel(1, k*r)/(k*r))**2


r = np.linspace(-1e-6, 1e-6, 1000)
yi = intdif(450e-9, r)

plt.plot(r, yi, 'g', label='I(r)')
plt.legend()
plt.xlim(-1e-6, 1e-6)
plt.grid()
plt.show()

x = np.linspace(-1e-6, 1e-6, 100)
y = np.linspace(-1e-6, 1e-6, 100)
xx, yy = np.meshgrid(x, y)
mr = lambda i, j: ((i**2) + (j**2))**(1/2)

plt.imshow(intdif(450e-9, mr(xx, yy)), cmap='viridis', vmax=0.01)
plt.axis('off')
plt.colorbar()
plt.show()