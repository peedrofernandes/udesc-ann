import sys, os

sys.path.append("..")

from math import exp, log, log2
from utils import poly_regression, generate_png, print_values

if __name__ == "__main__":
  x = [0.2488, 0.3678, 0.645, 1.0314, 1.2121, 1.4074, 1.6781, 1.8866, 2.0511, 2.3149, 2.592, 2.8375, 3.1452, 3.3129, 3.6449, 3.7341, 4.0271, 4.1608, 4.4535, 4.78, 5.011, 5.2695, 5.482, 5.552, 5.9938, 6.1988, 6.2761, 6.4912, 6.7367, 7.1546, 7.2981, 7.4648, 7.8418, 8.03, 8.1357, 8.3938, 8.7308, 8.9118, 9.2596, 9.3732, 9.6136, 9.7939]
  y = [0.8742, 1.2582, 1.8726, 2.4523, 2.6594, 2.8247, 2.977, 3.0075, 3.0393, 3.0201, 3.0191, 2.8676, 2.7883, 2.7178, 2.5063, 2.4958, 2.3644, 2.276, 2.1754, 1.9464, 1.8928, 1.7713, 1.7683, 1.546, 1.3567, 1.2792, 1.3489, 1.2496, 1.0826, 1.0226, 0.9631, 0.836, 0.8135, 0.8318, 0.6893, 0.7538, 0.5717, 0.5517, 0.5485, 0.4376, 0.5514, 0.4029]
  values = [2.5616, 3.3196, 4.7431, 7.5081, 7.6192]

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