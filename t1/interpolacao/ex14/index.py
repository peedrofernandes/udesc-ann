from math import cos, sqrt, log

def f1(x):
  return 1 / (1 + 25 * x ** 2)
def f2(x):
  return cos(x) ** 3 + 2 * cos(x) ** 2 + 1
def f3(x):
  return cos(x + sqrt(log(x ** 2)))

def difDiv(x: list[float], y: list[float]) -> list[float]:
  Y = [yi for yi in y]
  coeffs = [Y[0]]
  for j in range(len(x) - 1):
    for i in range(len(x) - 1 - j):
      numer = Y[i + 1] - Y[i]
      denom = x[i + 1 + j] - x[i]
      div = numer / denom
      Y[i] = div
    coeffs.append(Y[0])
  return coeffs

def poly(t, x, coeffs):
  val = 0
  for i in range(len(coeffs)):
    prod = 1
    for j in range(i):
      prod *= (t - x[j])
    val += coeffs[i] * prod
  return val

def buildFunc(x, coeffs):
  def temp(t):
    return poly(t, x, coeffs)
  return temp

def printCoeffs(coeffs):
  for i, ci in enumerate(coeffs):
    print(f"{ci:.8f}", end = "")
    if i == len(coeffs) - 1:
      print()
    else:
      print(",", end = "")

if __name__ == "__main__":
  x1 = [-0.561, 0.11, 0.467]
  x2 = [-2.704, -1.731, -0.203, 0.933, 1.506, 3.298, 4.207]
  x3 = [1.466, 1.74, 2.036, 2.233, 2.5, 2.75, 3.039, 3.186, 3.521, 3.619, 4.006, 4.215, 4.47, 4.679, 4.871]
  y1 = [f1(xi) for xi in x1]
  y2 = [f2(xi) for xi in x2]
  y3 = [f3(xi) for xi in x3]

  printCoeffs(difDiv(x1, y1))
  printCoeffs(difDiv(x2, y2))
  printCoeffs(difDiv(x3, y3))