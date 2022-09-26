from numpy.linalg import solve
from math import sin, cos, tan, sqrt, log

def f1(x):
  return sin(sqrt(1 + tan(x)))

def f2(x):
  return cos(x) ** 3 + 2 * cos(x) ** 2 + 1

def f3(x):
  return cos(x + sqrt(log(x ** 2)))

def getPolyCoeffs(x, y):
  A = []
  B = y

  for xi in x:
    row = [1] + [xi ** k for k in range(1, len(x))]
    A.append(row)

  return solve(A, B)



def printResults(coeffs):
  for i, ci in enumerate(coeffs):
    print(f"{ci:.8f}", end = "")
    if i == len(coeffs) - 1:
      print()
    else:
      print(",", end = "")



if __name__ == "__main__":
  x1 = [2.703, 3.34, 4.157]
  y1 = [f1(xi) for xi in x1]
  coeffs1 = getPolyCoeffs(x1, y1)
  
  print("Coeficientes do polinômio interpolador 1:")
  printResults(coeffs1)

  x2 = [-2.214, -1.301, -0.741, -0.065, 1.518, 2.253, 3.458, 4.093]
  y2 = [f2(xi) for xi in x2]
  coeffs2 = getPolyCoeffs(x2, y2)

  print("Coeficientes do polinômio interpolador 2:")
  printResults(coeffs2)

  x3 = [1.501, 1.938, 2.322, 2.475, 2.896, 3.176, 3.65, 3.854, 4.116, 4.443, 4.83]
  y3 = [f3(xi) for xi in x3]
  coeffs3 = getPolyCoeffs(x3, y3)

  print("Coeficientes do polinômio interpolador 3:")
  printResults(coeffs3)
