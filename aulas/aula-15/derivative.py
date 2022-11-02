
from math import log


def F1(h, f, x0):
  # Usada para calular f'(x0) com erro O(h)
  return (f(x0 + h) - f(x0)) / h

def F2(h, f, x0):
  # Usada para calcular f''(x0) com erro O(h)
  return (f(x0) - f(x0 - h)) / h

def F3(h, f, x0):
  # Usada para calcular f''(x0) com erro O(h²)
  return (f(x0 + h) - f(x0 - h)) / (2 * h)

def F4(h, f, x0):
  return (f(x0 - h) - 2 * f(x0) + f(x0 + h)) / (h ** 2)

if __name__ == "__main__":
  # exemplo: f(x) = x^x, f'(2) = 4 + log(16)
  # exemplo: f(x) = x^x, f''(2) = 2 + 4 * (1 + log(2)) ** 2

  def f(x):
    return x ** x
  x0 = 1
  ddfx0 = 2 + 4 * (1 + log(2)) ** 2

  hs = [10 ** (-i) for i in range(0, 10)]

  for h in hs:
    value = F4(h, f, x0)
    print(f"f''({x0}) ~ {value} com erro = {abs((value - ddfx0))}")

  print(f"f'(2) = {ddfx0}")