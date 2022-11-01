import sys, os

sys.path.append("..")

from math import exp, log, log2
from utils import poly_regression, generate_png, print_values

if __name__ == "__main__":
  x = [1.3447, 3.895, 4.7717, 6.3989, 8.1172, 10.09, 11.2952, 13.0661, 15.1388, 15.9094, 17.6695, 19.799]
  y = [1.095, 2.1933, 2.398, 2.7189, 2.995, 3.159, 3.2307, 3.355, 3.4466, 3.515, 3.583, 3.6426]
  values = [9.0255, 9.6963, 14.0302]

  # Translação para cima
  ky = (abs(min(y)) + 1) if (min(y) < 0) else (0)
  y_pos = [yi + ky for yi in y]

  # Translação para a direita
  kx = (abs(min(x)) + 1) if (min(x) < 0) else (0)
  x_pos = [xi + kx for xi in x]

  Y = [1 / yi for yi in y_pos]
  X = [1 / xi for xi in x_pos]

  a0, a1 = poly_regression(X, Y)
  a = 1 / a0
  b = a1 * a

  def f(x):
    return (a * (x + kx) / ((x + kx) + b)) - ky

  results = [a, b]
  results.extend([f(vi) for vi in values])

  print_values(results)

  generate_png(x, y, f, os.path.join(os.path.dirname(__file__), "pow_regression.png"))