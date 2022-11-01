import sys, os

sys.path.append("..")

from utils import generate_png, poly_regression, print_values
from math import log

if __name__ == "__main__":
  x = [1.2913, 2.0024, 3.1979, 3.7648, 4.7143, 4.8472, 5.507, 6.6648, 7.5949, 7.936, 8.9701, 9.4364]
  y = [4.6029, 5.0898, 5.7201, 6.0187, 6.3654, 6.3172, 6.4578, 6.8324, 6.7671, 6.8254, 6.996, 7.0973]
  values = [3.4963, 7.5302, 8.444]

  # Translação vertical
  ky = (abs(min(y) + 1)) if (min(y) < 0) else (0)
  y_pos = [yi + ky for yi in y]

  # Translação horizontal
  kx = (abs(min(x) + 1)) if (min(x) < 0) else (0)
  x_pos = [xi + kx for xi in x]

  X = [log(xi) for xi in x_pos]
  Y = [yi for yi in y_pos]

  a0, a1 = poly_regression(X, Y)

  a = a1
  b = a0

  def f(x):
    return a * log(x) + b
  def fc(x):
    return f(x + kx) - ky

  results = [a, b]
  results.extend([fc(vi) for vi in values])

  print_values(results)

  generate_png(x, y, fc, os.path.join(os.path.dirname(__file__), "func_regression.png"))