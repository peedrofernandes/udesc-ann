
from math import log


def F1(h, f, x0):
  return (f(x0 + h) - f(x0)) / h

def F2(h, f, x0):
  return (f(x0) - f(x0 - h)) / h

def F3(h, f, x0):
  return (f(x0 + h) - f(x0 - h)) / (2 * h)

if __name__ == "__main__":
  # exemplo 1: f(x) = x^x, f'(2) = 4 + log(16)

  def f(x):
    return x ** x
  x0 = 2

  exato = 4 + log(16)

  hs = [10 ** (-i) for i in range(1, 10)]

  for h in hs:
    df1x0 = F1(h, f, x0)
    df2x0 = F2(h, f, x0)
    df3x0 = F3(h, f, x0)
    print(f"h: {h}")
    print(f"[F1] f'({x0}) ~ {df1x0} com erro {abs(df1x0 - exato)}")
    print(f"[F2] f'({x0}) ~ {df2x0} com erro {abs(df2x0 - exato)}")
    print(f"[F3] f'({x0}) ~ {df3x0} com erro {abs(df3x0 - exato)}")

  print(f"f'(2) = {exato}")