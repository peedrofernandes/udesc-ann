def lagrange(lx, ly):
  coeffs = []

  for i in range(len(lx)):
    prod = 1
    for j in range(len(lx)):
      if i != j:
        prod *= (lx[i] - lx[j])
    ci = ly[i] / prod
    coeffs.append(ci)

  return coeffs


def printCoeffs(coeffs):
  for i, ci in enumerate(coeffs):
    print(f"{ci:.8f}", end = "")
    if i == len(coeffs) - 1:
      print()
    else:
      print(",", end = "")


if __name__ == "__main__":
  lx = [0.351, 0.955, 1.418, 1.993, 2.76, 3.356, 3.622, 4.149, 4.881, 5.323, 6.189, 6.902]
  ly = [4.823, 3.979, 3.286, 2.609, 2.072, 2.023, 2.113, 2.466, 3.168, 3.573, 3.996, 3.815]


  coeffs = lagrange(lx, ly)

  printCoeffs(coeffs)