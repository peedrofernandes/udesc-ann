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
  x = [0.066, 0.182, 0.298, 0.4395, 0.581, 0.784, 0.987, 1.468, 1.949, 2.099, 2.249, 2.305, 2.361, 2.4035, 2.446, 2.456, 2.466, 2.664, 2.862, 2.9715, 3.081, 3.096, 3.111, 3.133, 3.155, 3.159, 3.163, 3.349, 3.535, 3.5595, 3.584, 3.7235, 3.863, 3.8975, 3.932, 4.095, 4.258, 4.38, 4.502, 4.5415, 4.581, 4.588, 4.595, 4.639, 4.683]
  y = [1.436, 1.837, 2.242, 2.649, 2.904, 2.996, 2.855, 2.279, 2.003, 2.01, 2.062, 2.093, 2.13, 2.162, 2.198, 2.206, 2.215, 2.427, 2.677, 2.81, 2.92, 2.932, 2.944, 2.959, 2.972, 2.974, 2.976, 2.969, 2.707, 2.651, 2.591, 2.17, 1.677, 1.557, 1.443, 1.052, 1.074, 1.42, 1.977, 2.175, 2.369, 2.403, 2.436, 2.63, 2.793]

  a, b = x[0], x[len(x) - 1]

  results = simps(x, y)
  print_value(results)

