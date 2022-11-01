import sys, os

sys.path.append("..")

from math import exp, log, log2
from utils import poly_regression, generate_png, print_values

if __name__ == "__main__":
  x = [0.5379, 0.8989, 0.9403, 1.2051, 1.5065, 1.5418, 1.9155, 1.991, 2.2972, 2.5563, 2.689, 2.8248]
  y = [0.5894, 2.0193, 1.9991, 6.0418, 14.2559, 15.3864, 33.6831, 39.3438, 66.9427, 98.5976, 121.0922, 145.6688]
  values = [0.9185, 1.0243, 1.1228]

  # Translação para cima
  ky = (abs(min(y)) + 1) if (min(y) < 0) else (0)
  y_pos = [yi + ky for yi in y]

  # Translação para a direita
  kx = (abs(min(x)) + 1) if (min(x) < 0) else (0)
  x_pos = [xi + kx for xi in x]

  Y = [log(yi) for yi in y_pos]
  X = [log(xi) for xi in x_pos]

  a0, a1 = poly_regression(X, Y)
  a = exp(a0)
  b = a1

  def f(x):
    return a * (x + kx) ** b - ky

  results = [a, b]
  results.extend([f(vi) for vi in values])

  print_values(results)

  generate_png(x, y, f, os.path.join(os.path.dirname(__file__), "pow_regression.png"))