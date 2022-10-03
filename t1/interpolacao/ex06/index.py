from math import sin, cos, tan, sqrt


def f1(x):
  return sin(sqrt(1 + tan(x)))

def f2(x):
  return sin(x) ** 3 - 3 * sin(x) ** 2 + sin(x ** 2) + 4

def f3(x):
  return cos(x) ** 3 + 2 * cos(x) ** 2 + 1

def lagrange(lx, ly):
  coeffs = []

  for i in range(len(lx)):
    prod = 1
    for j in range(len(lx)):
      if (i != j):
        prod *= (lx[i] - lx[j])
    ci = ly[i] / prod
    coeffs.append(ci)

  def p(x):
    sum = 0
    for i in range(len(coeffs)):
      prod = 1
      for j in range(len(coeffs)):
        if i != j:
          prod *= (x - lx[j])
      prod *= coeffs[i]
      sum += prod
    return sum

  return p


def printErrors(p, f, lv):
  errors = [abs(f(vi) - p(vi)) for vi in lv]

  for i, err in enumerate(errors):
    print(f"{err:.8f}", end = "")
    if i == len(errors) - 1:
      print()
    else:
      print(",", end = "")


if __name__ == "__main__":
  lx1 = [2.756, 3.724, 4.381]
  ly1 = [f1(xi) for xi in lx1]
  lv1 = [2.984, 3.95]
  p1 = lagrange(lx1, ly1)

  printErrors(p1, f1, lv1)

  lx2 = [-2.703, -1.303, -0.044, 2.161, 3.191]
  ly2 = [f2(xi) for xi in lx2]
  lv2 = [0.879, 1.638, 3.708]
  p2 = lagrange(lx2, ly2)

  printErrors(p2, f2, lv2)

  lx3 = [-2.498, -1.737, -0.859, 0.075, 0.62, 1.514, 2.217, 3.082, 4.058]
  ly3 = [f3(xi) for xi in lx3]
  lv3 = [-2.691, -0.643, 1.421, 2.289, 3.775]
  p3 = lagrange(lx3, ly3)

  printErrors(p3, f3, lv3)