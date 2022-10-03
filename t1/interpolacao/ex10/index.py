from math import sin, cos, exp, log

def f1(x):
  return exp(cos(x) ** 2) + exp(-x ** 2) + log(x)
def f2(x):
  return 4 + sin(x) - (x ** 2) / 30
def f3(x):
  return exp(- x ** 2) + cos(x) + 3

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
  lx1 = [3.37, 4.198, 7.061]
  ly1 = [f1(xi) for xi in lx1]
  printCoeffs(lagrange(lx1, ly1))

  lx2 = [0.534, 1.318, 1.924, 2.406, 3.132, 4.153, 4.798]
  ly2 = [f2(xi) for xi in lx2]
  printCoeffs(lagrange(lx2, ly2))

  lx3 = [0.339, 0.748, 1.337, 1.981, 2.565, 3.042, 3.36, 4.013, 4.711, 5.058, 5.493, 6.031, 6.535]
  ly3 = [f3(xi) for xi in lx3]
  printCoeffs(lagrange(lx3, ly3))

