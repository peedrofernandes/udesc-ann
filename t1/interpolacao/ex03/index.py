from numpy.linalg import solve


def getPolyCoeffs(x, y):
  A = []
  B = y

  for xi in x:
    row = [1] + [xi ** k for k in range(1, len(x))]
    A.append(row)

  return solve(A, B)

if __name__ == '__main__':
  x = [0.348, 0.997, 1.358, 1.822, 2.787, 3.255, 3.604, 4.192, 4.741, 5.721, 5.917, 6.907]
  y = [4.337, 4.807, 4.916, 4.858, 4.088, 3.534, 3.121, 2.547, 2.251, 2.376, 2.475, 2.994]

  coeffs = getPolyCoeffs(x, y)

  for i, ci in enumerate(coeffs):
    print(f"{ci:.8f}", end = '')
    if i == len(coeffs) - 1:
      print()
    else:
      print(',', end = '')
