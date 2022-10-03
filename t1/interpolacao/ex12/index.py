
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
  x = [1.481, 2.295, 2.525, 3.177, 3.888, 4.185, 4.669]
  y = [-0.715, -0.904, -0.735, -0.015, 0.734, 0.919, 0.99]

  printCoeffs(difDiv(x, y))