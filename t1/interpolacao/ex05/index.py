from numpy.linalg import solve


def getPolyCoeffs(x, y):
  A = []
  B = y

  for xi in x:
    row = [1] + [xi ** k for k in range(1, len(x))]
    A.append(row)

  return solve(A, B)


def buildPoly(coeffs):
  def p(x):
    sum = coeffs[0]
    for i, ci in enumerate(coeffs[1:], 1):
      sum += ci * x ** i
    return sum
  return p


def printResults(p, v):
  results = [p(vi) for vi in v]
  for i, ri in enumerate(results):
    print(f"{ri:.8f}", end = "")
    if i == len(results) - 1:
      print()
    else:
      print(",", end = "")


if __name__ == "__main__":
  x1 = [-3.217, -0.418, 2.299]
  y1 = [3.185, 3.613, 1.904]
  v1 = [-0.149, 2.96]

  c1 = getPolyCoeffs(x1, y1)
  p1 = buildPoly(c1)

  printResults(p1, v1)


  x2 = [2.944, 3.092, 3.741, 4.06, 4.255]
  y2 = [0.78, 0.828, 0.963, 0.999, 0.986]
  v2 = [2.634, 3.364, 4.33]

  c2 = getPolyCoeffs(x2, y2)
  p2 = buildPoly(c2)

  printResults(p2, v2)


  x3 = [0.305, 0.709, 1.1, 1.651, 2.03, 2.393, 2.9, 3.363, 3.8]
  y3 = [0.659, 1.071, 1.525, 1.976, 1.882, 1.275, 0.126, 0.412, 1.806]
  v3 = [0.069, 0.601, 0.711, 1.034]

  c3 = getPolyCoeffs(x3, y3)
  p3 = buildPoly(c3)

  printResults(p3, v3)

  