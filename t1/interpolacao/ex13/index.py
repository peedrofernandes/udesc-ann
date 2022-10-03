
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
  x = [0.338, 0.516, 1.321, 1.819, 1.926, 2.526, 3.201, 3.672, 3.899, 4.439, 4.871, 5.336, 5.966, 6.259, 6.602]
  y = [4.835, 4.636, 3.422, 2.791, 2.677, 2.185, 2.002, 2.137, 2.273, 2.73, 3.158, 3.584, 3.95, 4.0, 3.95]

  printCoeffs(difDiv(x, y))