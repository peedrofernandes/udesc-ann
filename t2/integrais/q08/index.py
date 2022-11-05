from sys import path
path.append("..")

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
  x = [3.113, 3.349, 3.585, 3.871, 4.157]
  y = [2.945, 2.969, 2.589, 1.649, 1.002]

  a, b = x[0], x[len(x) - 1]

  results = simps(x, y)
  print_value(results)

