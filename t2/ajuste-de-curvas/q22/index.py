import sys, os

sys.path.append("..")

from utils import generate_png, poly_regression, print_values
from math import log, sqrt

if __name__ == "__main__":
  x = [0.7852, 1.5788, 2.1255, 3.354, 3.7941, 5.0762, 5.5862, 6.1227, 7.6073, 7.7428, 8.5053, 9.7214]
  y = [3.6711, 2.193, 1.7807, 1.3218, 1.2545, 1.0466, 1.0291, 0.9463, 0.7869, 0.7973, 0.7827, 0.7357]
  values = [3.4646, 3.7945, 7.2805]

  # Translação vertical
  ky = (abs(min(y) + 1)) if (min(y) < 0) else (0)
  y_pos = [yi + ky for yi in y]

  # Translação horizontal
  kx = (abs(min(x) + 1)) if (min(x) < 0) else (0)
  x_pos = [xi + kx for xi in x]

  X = [(1 / sqrt(xi)) for xi in x_pos]
  Y = [sqrt(yi) for yi in y_pos]

  a0, a1 = poly_regression(X, Y)

  b = 1 / a0
  a = b * a1

  def f(x):
    return ((a + sqrt(x)) / (b * sqrt(x))) ** 2
  def fc(x):
    return f(x + kx) - ky

  results = [a, b]
  results.extend([fc(vi) for vi in values])

  print_values(results)

  generate_png(x, y, fc, os.path.join(os.path.dirname(__file__), "func_regression.png"))