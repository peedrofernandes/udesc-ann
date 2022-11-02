from numpy.linalg import solve
from math import factorial, log
import random


# xs = Lista de coordenadas x dos pontos escolhidos
# x0 = Ponto sobre o qual se calculará a derivada
# k = Ordem da derivada a ser calculada
def dif_fin(xs, x0, k = 1):
  n = len(xs)

  A = [[1] * n]
  B = [0]
  for i in range(1, n):
    row = [x ** i for x in xs]
    A.append(row)
    if i < k:
      B.append(0)
    else:
      B.append(factorial(i) / factorial(i - k) * x0 ** (i - k))
  
  return solve(A, B)


if __name__ == "__main__":

  exato_1 = 4 + log(16)
  exato_2 = 2 + 4 * (1 + log(2)) ** 2
  def f(x):
    return x ** x

  tol = 0.00001
  a = 2 - tol
  b = 2 + tol
  N = 5

  xs = [a + (b - a) * random.random() for _ in range(N)]
  x0 = 2

  cs = dif_fin(xs, x0)
  val = sum([c * f(x) for c, x in zip(cs, xs)])
  print(f"Aproximação: {val}")
  print(f"Valor exato: {exato_1}")

  cs = dif_fin(xs, x0, 2)
  val = sum([c * f(x) for c, x in zip(cs, xs)])
  print(f"Aproximação: {val}")
  print(f"Valor exato: {exato_2}")

