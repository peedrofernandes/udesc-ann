import sys, os

sys.path.append("..")

from math import exp, log, log2
from utils import poly_regression, generate_png, print_values

if __name__ == "__main__":
  x = [1.2387, 1.6763, 1.917, 2.6825, 2.8169, 3.659, 4.0144, 4.5514, 4.6592, 5.3123, 5.8514, 5.9879, 6.4853, 7.1261, 7.6449, 7.8461, 8.4119, 8.6914, 9.4741, 9.8524, 10.2426, 10.6224, 11.1732, 11.6076, 12.074, 12.3932, 12.9311, 13.2768, 13.8792, 14.4571, 14.7951, 15.205, 15.8783, 16.1438, 16.6309, 17.1236, 17.5798, 18.1068, 18.2503, 18.8861, 19.2386, 19.809]
  y = [1.4575, 1.6775, 1.8142, 1.98, 2.0885, 2.2641, 2.3044, 2.3871, 2.359, 2.4698, 2.4792, 2.5083, 2.5655, 2.5791, 2.6216, 2.6322, 2.6537, 2.6703, 2.6746, 2.7132, 2.7329, 2.7289, 2.7535, 2.7519, 2.7586, 2.7868, 2.7736, 2.7462, 2.831, 2.8179, 2.8125, 2.8207, 2.8625, 2.8537, 2.8278, 2.8595, 2.8553, 2.8571, 2.8505, 2.8676, 2.9502, 2.8984]
  values = [3.7454, 4.5824, 4.7338, 12.7546, 14.4137]

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