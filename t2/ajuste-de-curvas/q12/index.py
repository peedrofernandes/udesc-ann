import sys, os

sys.path.append("..")

from math import exp, log
from utils import poly_regression, generate_png, print_values

if __name__ == "__main__":
  x = [0.1101, 0.1872, 0.4087, 0.5276, 0.6904, 0.8452, 1.1232, 1.305, 1.4602, 1.5598, 1.74, 1.9733]
  y = [5.0322, 6.5973, 8.8791, 11.9613, 14.5056, 18.9252, 28.5722, 40.3093, 51.8281, 61.7057, 84.3234, 123.7021]
  values = [0.1809, 0.8236, 0.8641]

  # Translação para cima
  ky = abs(min(y)) + 1 if (min(y) < 0) else 0
  y_pos = [yi + ky for yi in y]

  Y = [log(yi) for yi in y_pos]

  a0, a1 = poly_regression(x, Y)
  a = exp(a0)
  b = a1

  def p(x):
    return a * exp(b * x) - ky

  results = [a, b]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "exp_regression.png"))