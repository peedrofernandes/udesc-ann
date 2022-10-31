from math import exp
from zeroMethods import bissection, newton, secant, falsePosition

v = 33.4
g = 9.81
c = 23.29
t = 9.02

def f(m: float):
  return ((g * m) / c) * (1 - exp(- (c / m) * t)) - v

def df(m: float):
  return g * (1 - exp(-c * t / m)) / c - g * t * exp(- c * t / m) / m

if __name__ == "__main__":
  a = 28.26
  b = 195.81
  it = [2, 4, 8, 12]
  bissection(f, a, b, it)

  print(",", end="")

  x0 = 26.78
  it = [1, 3, 5]
  newton(f, df, x0, it)

  print(",", end="")

  x0 = 21.69
  x1 = 36.45
  it = [1, 2, 5]
  secant(f, x0, x1, it)

  print(",", end="")

  a = 34.78
  b = 204.06
  it = [2, 4, 7, 11]
  falsePosition(f, a, b, it)

  print()
