from sys import path

path.append("..")

import math
from utils import print_values, print_value

def trapz(f, a, b, h):
  n = int((b - a) / h)
  s = sum([f(a + k * h) for k in range(1, n)])
  return (h / 2) * (f(a) + 2 * s + f(b))

def richardson(x, b = 1):
  n = len(x)

  for k in range(1, n):
    for i in range(n - k):
      numer = 2 ** (k * b) * x[i + 1] - x[i]
      denom = 2 ** (k * b) - 1
      aprox = numer / denom
      x[i] = aprox
  return x[0]

# O método da Integração de Romberg é, basicamente, o método da extrapolação de Richardson
# aplicado sobre a Regra dos Trapézios, que possui erro com ordem O(h²)
def romberg(f, a, b, n, k):
  h = (b - a) / n
  hs = [h / 2 ** i for i in range(int(k / 2))]
  c1 = [trapz(f, a, b, h) for h in hs]

  return richardson(c1, 2)

def f(val):
  def f(x):
    return eval(val)
  return f

if __name__ == "__main__":
  func = ['math.exp(-x**2)', 'math.sqrt(1+x**2)', 'math.exp(x)*math.sin(x)/(1+x**2)', '(x+1/x)**2', 'math.cos(-x**2/3)']
  a = [-0.884, 0.851, 0.793, 0.922, 0.186]
  b = [0.116, 1.851, 1.793, 1.922, 1.186]
  order = [10, 8, 8, 10, 8]
  n = [2, 3, 4, 4, 4]

  results = [romberg(f(vi), ai, bi, ni, ki) for vi, ai, bi, ni, ki in zip(func, a, b, n, order)]

  print_values(results)

