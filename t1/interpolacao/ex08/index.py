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
  lx = [2.728, 2.905, 3.183, 3.482, 3.734, 4.014, 4.303, 4.483]
  ly = [0.681, 0.765, 0.852, 0.918, 0.962, 0.996, 0.97, 0.747]

  coeffs = lagrange(lx, ly)

  printCoeffs(coeffs)