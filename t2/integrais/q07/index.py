from sys import path
path.append("..")

from math import sqrt, sin, cos, log
from utils import print_values

def simps(f, a, b, n):
  if n % 2 != 0 or n < 1:
    raise ValueError("n deve ser par e maior do que 1!")

  h = (b - a) / n

  sum_even = sum([f(a + k * h) for k in range(2, n, 2)])
  sum_odd = sum([f(a + k * h) for k in range(1, n, 2)])

  return (h / 3) * (f(a) + 2 * sum_even + 4 * sum_odd + f(b))


if __name__ == "__main__":
  intervalo = [-1.327, 1.915]
  subintervalos = [6, 16, 32, 68, 86, 120, 128, 152, 178, 218, 358]

  def f(x):
    return sqrt(sin(cos(log(x ** 2 + 1) + 2) + 3) + 4)

  a = intervalo[0]
  b = intervalo[1]

  results = [simps(f, a, b, n) for n in subintervalos]
  print_values(results)

