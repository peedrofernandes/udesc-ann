import numpy as np
import matplotlib.pyplot as plt


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