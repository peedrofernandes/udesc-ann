import sys
from math import sin, sqrt

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
  return sin(x / sqrt(x ** 2 + 1)) + 1


if __name__ == "__main__":
  intervalo = [-1.417, 1.445]
  subintervalos = [2, 10, 35, 54, 96, 110, 158, 380, 673, 780, 2621, 7546]

  results = [trapz(f, intervalo[0], intervalo[1], si) for si in subintervalos]

  print_values(results)

