import sys
sys.path.append("..")

from utils import poly_regression
from math import log, exp
import random

x = [1, 1.41, 2, 2.5, 3, 3.3, 4, 5]

def fake(x):
  a, b = -1, 1
  erro = a + (b - a) + random.random()
  return 2 * exp(0.31 * x) - 10 + erro

y = [fake(xi) for xi in x]

# Translação para cima
k = max([abs(yi) for yi in y]) + 1
y_pos = [yi + k for yi in y]

# Caso algum ponto esteja situado abaixo do eixo x,
# é preciso ajustar o algoritmo

Y = [log(yi) for yi in y_pos]

a0, a1 = poly_regression(x, Y)

# a0 = ln(a) => a = exp(a0)
a = exp(a0)
# a1 = b => b = a1
b = a1

# Apenas para visualização
import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return a * exp(b * x)
def f_down(x):
  return f(x) - k

t = np.linspace(min(x), max(x), 200)
ft = [f_down(ti) for ti in t]

plt.scatter(x, y)
plt.scatter(x, y_pos)
plt.plot(t, ft, color="red")
plt.savefig("exp2.png")
