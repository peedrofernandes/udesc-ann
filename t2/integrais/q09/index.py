from sys import path
path.append("..")

from math import sqrt, sin, cos, log
from utils import print_value

def simps(x, y):
  if len(x) % 2 == 0 or len(y) % 2 == 0:
    raise ValueError("A lista de pontos deve conter uma quantidade ímpar de pontos!")
  if len(x) < 3:
    raise ValueError("Para que seja possível construir ao menos uma parábola, três pontos devem ser fornecidos!")

  sum = 0
  for k in range(2, len(x), 2):
    x0, x1 = x[k - 2], x[k - 1]
    y0, y1, y2 = y[k - 2], y[k - 1], y[k]
    sum += ((x1 - x0) / 3) * (y0 + 4*y1 + y2)

  return sum


if __name__ == "__main__":
  x = [0.055, 0.359, 0.663, 0.9715, 1.28, 1.7285, 2.177, 2.183, 2.189, 2.358, 2.527, 2.738, 2.949, 2.9985, 3.048, 3.0495, 3.051, 3.508, 3.965, 4.1285, 4.292]
  y = [1.402, 2.434, 2.977, 2.871, 2.495, 2.074, 2.031, 2.033, 2.036, 2.128, 2.274, 2.518, 2.784, 2.84, 2.89, 2.892, 2.893, 2.763, 1.341, 1.016, 1.143]

  a, b = x[0], x[len(x) - 1]

  results = simps(x, y)
  print_value(results)

