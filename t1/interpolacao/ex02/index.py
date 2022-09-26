from numpy.linalg import solve

def vandermonde(x, y):
  A = []
  B = y

  for xi in x:
    row = [1] + [xi ** k for k in range(1, len(x))]
    A.append(row)

  coeffs = solve(A, B)
  return coeffs


if __name__ == "__main__":
  x = [0.745, 1.187, 2.326, 3.794, 4.72, 5.646, 6.833]
  y = [4.659, 4.88, 4.548, 2.913, 2.257, 2.342, 2.966]
  coeffs = vandermonde(x, y)
  
  for i, ci in enumerate(coeffs):
    print(f"{ci:.8f}", end = '')
    if i != len(coeffs) - 1:
      print(',', end = '')
    else:
      print()