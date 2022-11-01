import sys, os

sys.path.append("..")

from utils import generate_png, poly_regression, print_values

if __name__ == "__main__":
  x = [1.8184, 2.7901, 3.7392, 4.5121, 5.4572, 5.5941, 6.858, 7.8493, 8.4024, 9.6488, 10.2587, 11.8329]
  y = [2.0288, 2.7533, 3.1588, 3.3715, 3.4909, 3.5043, 3.5846, 3.6507, 3.6961, 3.805, 3.679, 3.7852]
  values = [2.4316, 5.0243, 8.2445]

  # Translação vertical
  ky = (abs(min(y) + 1)) if (min(y) < 0) else (0)
  y_pos = [yi + ky for yi in y]

  # Translação horizontal
  kx = (abs(min(x) + 1)) if (min(x) < 0) else (0)
  x_pos = [xi + kx for xi in x]

  Y = [1 / yi for yi in y_pos]
  X = [1 / (xi ** 2) for xi in x_pos]

  a0, a1 = poly_regression(X, Y)

  a = 1 / a0
  b = a1 * a

  def f(x):
    return (a * x ** 2) / (b + x ** 2)
  def fc(x):
    return f(x + kx) - ky

  results = [a, b]
  results.extend([fc(vi) for vi in values])

  print_values(results)

  generate_png(x, y, fc, os.path.join(os.path.dirname(__file__), "func_regression.png"))