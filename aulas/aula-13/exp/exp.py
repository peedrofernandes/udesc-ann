import sys

sys.path.append("..")

from utils import poly_regression
from math import log, exp

x = [1, 2, 3, 4, 5]
y = [3, 10, 25, 90, 250]

# Caso algum ponto esteja situado abaixo do eixo x,
# é preciso ajustar o algoritmo

Y = [log(yi) for yi in y]

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

t = np.linspace(min(x), max(x), 200)
ft = [f(ti) for ti in t]

plt.scatter(x, y)
plt.plot(t, ft, color="red")
plt.savefig("exp.png")
