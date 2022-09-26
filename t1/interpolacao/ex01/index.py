from numpy.linalg import solve


def vandermonde(x, y):
  B = y
  A = []

  for xi in x:
    row = [1] + [xi ** k for k in range(1, len(x))]
    A.append(row)

  coeffs = solve(A, B)
  return coeffs


def buildPoly(coeffs):
  def func(x):
    sum = coeffs[0]
    for i, ci in enumerate(coeffs[1:], 1):
      sum += ci * x ** i
  return func


if __name__ == "__main__":
  x = [0.367, 3.72, 6.687]
  y = [4.354, 2.992, 2.902]

  coeffs = vandermonde(x, y)
  p = buildPoly(coeffs)

  for i, ci in enumerate(coeffs):
    print(f"{ci:.8f}", end = '')
    if i != len(coeffs) - 1:
      print(',', end = '')
    else:
      print()
