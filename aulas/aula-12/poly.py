import numpy as np


# Sistema linear da regressão polinomial
def poly_regression(x, y, k=1):
  # Matriz [K+1] x [K+1] com elementos nulos
  A = [[0 for _ in range(k+1)] for _ in range(k+1)]
  B = []

  for i in range(k + 1):
    for j in range(k + 1):
      A[i][j] = sum(xi ** (i + j) for xi in x)

    if i == 0:
      B.append(sum(y))
    else:
      B.append(sum(yi * xi ** i for xi, yi in zip(x, y)))

  return np.linalg.solve(A, B)


# Pontos "mais ou menos" no polinômio
def dummy():
  def func(x):
    erro = -4 + 2 * np.random.random()
    return 0.2 * x ** 3 + 2 * x ** 2 - 3 * x + 4 + erro

  return func


# Construtor do polinômio
def build_poly(coeffs):
  def func(x):
    soma = coeffs[0]
    for i, ci in enumerate(coeffs[1:], 1):
      soma += ci * x ** i 
    return soma
  
  return func


if __name__ == '__main__':

  # Geração dos pontos espalhados
  x = np.linspace(-3, 3)
  d = dummy()
  y = [d(xi) for xi in x]


  # Geração do polinômio ajustado aos pontos
  coeffs = poly_regression(x, y, k = 3)
  p = build_poly(coeffs)
  t = np.linspace(min(x), max(x), 200)
  pt = [p(ti) for ti in t]


  # Apenas para visualização
  import matplotlib.pyplot as plt

  plt.scatter(x, y)
  plt.plot(t, pt, color='red')
  plt.savefig('poly_regression.png')
  

