import sys

sys.path.append("..")

from utils import poly_regression
from math import log, exp
import numpy as np
import random

x = np.linspace(1, 10, 40)

def fake(x):
  a, b = -1, 1
  erro = a + (b - a) + random.random() * 20
  return -100 + 2 * x ** 2.231 + erro

y = [fake(xi) for xi in x]


# Translação para cima
ky = abs(min(y)) + 1 if (min(y) < 0) else 0
y_pos = [yi + ky for yi in y]

# Translação para a direita
kx = abs(min(x)) + 1 if (min(x) < 0) else 0
x_pos = [xi + kx for xi in x]

X = [log(xi) for xi in x_pos]
Y = [log(yi) for yi in y_pos]

a0, a1 = poly_regression(X, Y)

# a0 = ln(a) => a = exp(a0)
a = exp(a0)
# a1 = b => b = a1
b = a1

# Apenas para visualização
import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return a * x ** b
def f_corrected(x):
  return f(x + kx) - ky

t = np.linspace(min(x), max(x), 200)
ft = [f(ti) for ti in t]
f_corrected_t = [f_corrected(ti) for ti in t]

plt.scatter(x, y)

plt.plot(t, f_corrected_t, color="red")
plt.savefig("pow.png")