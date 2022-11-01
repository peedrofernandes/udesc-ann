import sys, os

sys.path.append("..")

from math import exp, log, log2
from utils import poly_regression, generate_png, print_values

if __name__ == "__main__":
  x = [0.5389, 0.5985, 0.6251, 0.7107, 0.7924, 0.8026, 0.8667, 0.9532, 0.9837, 1.089, 1.1514, 1.1959, 1.2424, 1.3246, 1.3695, 1.4445, 1.4968, 1.5123, 1.606, 1.6527, 1.7318, 1.7926, 1.8492, 1.8754, 1.9334, 2.0277, 2.0694, 2.1428, 2.179, 2.2773, 2.2955, 2.3515, 2.4567, 2.4982, 2.5691, 2.6093, 2.6584, 2.7138, 2.7667, 2.8328, 2.9007, 2.9686]
  y = [0.6572, 0.047, 0.5669, 0.0253, 0.1058, 1.1622, 0.9416, 1.8053, 0.8983, 0.9887, 2.1624, 2.4673, 3.1001, 3.0333, 3.962, 4.8287, 4.734, 5.098, 5.985, 6.7857, 8.8408, 8.9942, 11.0785, 10.985, 12.9235, 14.6345, 13.5487, 18.2498, 18.5918, 19.9965, 21.9335, 23.5935, 26.9482, 28.723, 31.9114, 33.0023, 34.269, 37.5896, 40.2174, 43.941, 46.6189, 51.7571]
  values = [0.6693, 1.3664, 1.5863, 2.0827, 2.8442]

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