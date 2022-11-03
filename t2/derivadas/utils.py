import numpy as np
import matplotlib.pyplot as plt
from math import factorial


def poly_regression(x, y, k = 1):
  n = len(x)

  A = [[0 for _ in range(k+1)] for _ in range(k+1)]
  B = []

  for i in range(k + 1):
    for j in range(k + 1):
      A[i][j] = (sum(xi ** (i + j) for xi in x)) if (i + j > 0) else (n)

    B.append((sum(yi * xi ** i for xi, yi in zip(x, y))) if (i > 0) else (sum(y)))

  return np.linalg.solve(A, B)


def build_poly(coeffs):
  def p(x):
    return sum((ci*x**i if (i > 0) else (ci)) for i, ci in enumerate(coeffs))
  return p


def print_value(x):
  print(f"{x:.8f}")


def print_values(x):
  for i, xi in enumerate(x):
    print(f"{xi:.8f}", end="")
    if (i != len(x) - 1):
      print(",", end="")
    else:
      print()


def generate_png(x, y, p, path):
  t = np.linspace(min(x), max(x), 200)
  pt = [p(ti) for ti in t]

  plt.scatter(x, y)
  plt.plot(t, pt, color="red")
  plt.savefig(path)


def dif_fin(x, x0, k = 1):
  n = len(x)

  A = [[1] * n]
  B = [0]
  for i in range(1, n):
    row = [xi ** i for xi in x]
    A.append(row)
    if i < k:
      B.append(0)
    else:
      B.append(factorial(i) / factorial(i - k) * x0 ** (i - k))
  
  return np.linalg.solve(A, B)


def richardson(x, b = 1):
  n = len(x)

  for k in range(1, n):
    for i in range(n - k):
      numer = 2 ** (k * b) * x[i + 1] - x[i]
      denom = 2 ** (k * b) - 1
      aprox = numer / denom
      x[i] = aprox
  return x[0]