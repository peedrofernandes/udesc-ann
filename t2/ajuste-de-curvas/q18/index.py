import sys, os

sys.path.append("..")

from math import exp, log, log2
from utils import poly_regression, generate_png, print_values

if __name__ == "__main__":
  x = [0.4108, 1.2123, 2.0561, 3.3291, 4.0302, 4.7698, 5.8454, 6.6532, 6.7348, 7.7321, 8.41, 9.8755]
  y = [1.3899, 3.2103, 4.1876, 4.5948, 4.5469, 4.2248, 3.7848, 3.349, 3.3197, 2.7895, 2.5113, 1.9065]
  values = [5.5576, 8.291, 8.9744]

  # Translação para cima
  ky = (abs(min(y)) + 1) if (min(y) < 0) else (0)
  y_pos = [yi + ky for yi in y]

  # Translação para a direita
  kx = (abs(min(x)) + 1) if (min(x) < 0) else (0)
  x_pos = [xi + kx for xi in x]

  Y = [log(yi) - log(xi) for yi, xi in zip(y_pos, x_pos)]
  X = [xi for xi in x_pos]

  a0, a1 = poly_regression(X, Y)
  a = exp(a0)
  b = a1

  def f(x):
    return a * (x + kx) * exp(b * (x + kx)) - ky

  results = [a, b]
  results.extend([f(vi) for vi in values])

  print_values(results)

  generate_png(x, y, f, os.path.join(os.path.dirname(__file__), "pow_regression.png"))