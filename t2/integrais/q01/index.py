import sys
import math

sys.path.append("..")

from utils import print_values


def trapz(f, a, b, n):
  h = (b - a) / n

  soma = 0
  for k in range(1, n):
    soma += f(a + k * h)
  soma *= 2
  soma += (f(a) + f(b))

  return soma * (h / 2)


def f(x):
  return math.sin(math.exp(-x ** 2)) + 1


if __name__ == "__main__":
  intervalo = [-1.134, 1.586]
  subintervalos = [8, 11, 29, 66, 75, 144, 157, 458, 701, 845, 1195, 7103]

  results = [trapz(f, intervalo[0], intervalo[1], si) for si in subintervalos]

  print_values(results)

