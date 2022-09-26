from numpy import linspace
from numpy.linalg import solve
from matplotlib.pyplot import plot, scatter, savefig


def vandermonde(x, y):
  # x = Lista das coordenadas x
  # y = Lista das coordenadas y
  # Retorna os coeficientes do polinômio interpolador
  # da lista de pontos x, y

  A = []
  B = y

  for xi in x:
    row = [1] + [xi ** k for k in range(1, len(x))]
    A.append(row)

  coeffs = solve(A, B)
  return coeffs


def buildPoly(coeffs):
  def func(x):
    soma = coeffs[0]
    for i, ci in enumerate(coeffs[1:], 1):
      soma += ci * x ** i
    return soma
  return func


def example1():
  # Exemplo 1: (1, 2) e (3, -1)
  x = [1, 3]
  y = [2, -1]

  coeffs = vandermonde(x, y)

  print(f"Coeficientes do polinômio 1: {coeffs}")
  p = buildPoly(coeffs)

  print(f"{p(1) = } e {p(3) = }")

  # Visualização
  t = linspace(-1, 4, 100)
  pt = [p(ti) for ti in t]
  plot(t, pt, color="red")
  scatter(x, y, color="blue")
  savefig("interp1.png")


def example2():
  # Exemplo 2: (-1, 1), (0, 0) e (1, 1)
  x = [-1, 0, 1]
  y = [1, 0, 1]
  coeffs = vandermonde(x, y)
  p = buildPoly(coeffs)
  [print(f"p({xi}) = {p(xi)}") for xi in x]

  # Visualização
  vx = 1.1 * min(x)
  vy = 1.1 * max(x)
  t = linspace(vx, vy, 100)
  pt = [p(ti) for ti in t]
  plot(t, pt, color="red")
  scatter(x, y, color="blue")
  savefig("interp2.png")


if __name__ == '__main__':
  example2()




