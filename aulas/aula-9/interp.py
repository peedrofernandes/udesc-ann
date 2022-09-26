import numpy as np


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

  return np.linalg.solve(A,B)

  
def buildPoly(coeffs):
  def func(x):
    soma = coeffs[0]
    for i, ci in enumerate(coeffs[1:], 1):
      soma += ci * x ** i
    return soma
  return func


if __name__ == '__main__':
  # exemplo 1 (1, 2)
  x = [1,3]
  y = [2,-1]

  coeffs = vandermonde(x, y)

  print(coeffs)
  p = buildPoly(coeffs)

  print(f"{p(1) = } e {p(3) = }")

  # Apenas para visualização:
  import matplotlib.pyplot as plt
  t = np.linspace(-1, 4, 100)
  pt = [p(ti) for ti in t]
  plt.plot(t, pt, color="red")
  plt.scatter(x, y, color="blue")
  plt.savefig("interp.png")

  #exemplo 2 (-1, 1), (0, 0), (1, 1)
  x = [-1, 0, 1]
  y = [1, 0, 1]
  coeffs = vandermonde(x, y)
  print(coeffs)
  p = buildPoly(coeffs)
  [print(f"p({xi}) = {p(xi)}") for xi in x]

  # Apenas para visualização:
  import matplotlib.pyplot as plt
  t = np.linspace(-1, 4, 100)
  pt = [p(ti) for ti in t]
  plt.plot(t, pt, color="red")
  plt.scatter(x, y, color="blue")
  plt.savefig("interp.png")



