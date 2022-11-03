def richardson(x, b = 1):
  n = len(x)

  for k in range(1, n):
    for i in range(n - k):
      numer = 2 ** (k * b) * x[i + 1] - x[i]
      denom = 2 ** (k * b) - 1
      aprox = numer / denom
      x[i] = aprox
  return x[0]

if __name__ == "__main__":
  from math import log
  exato = 4 + log(16)

  def f(x):
    return x ** x
    
  x0 = 2
  h = 1
  ordem = 10
  
  def F1(h):
    return (f(x0 + h) - f(x0)) / h

  col_F1 = [F1(h / (2 ** i)) for i in range(0, ordem)]

  aprox = richardson(col_F1)
  print(f"Aprox f'({x0}) = {aprox} com erro O(H^{len(col_F1)})")
  print(f"Valor exato = {exato}")