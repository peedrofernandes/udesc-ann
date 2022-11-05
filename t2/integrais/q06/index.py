from sys import path
path.append("..")

from math import sin, sqrt
from utils import print_values

def simps(f, a, b, n):
  if n % 2 != 0 or n < 1:
    raise ValueError("n deve ser par e maior do que 1!")

  h = (b - a) / n

  sum_even = sum([f(a + k * h) for k in range(2, n, 2)])
  sum_odd = sum([f(a + k * h) for k in range(1, n, 2)])

  return (h / 3) * (f(a) + 2 * sum_even + 4 * sum_odd + f(b))


if __name__ == "__main__":
  intervalo = [-1.716, 1.79]
  subintervalos = [8, 16, 30, 74, 88, 106, 138, 156, 178, 242, 438]

  def f(x):
    return sin(x / sqrt(x ** 2 + 1)) + 1

  a = intervalo[0]
  b = intervalo[1]

  results = [simps(f, a, b, n) for n in subintervalos]
  print_values(results)

