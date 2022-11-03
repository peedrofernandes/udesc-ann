import sys

sys.path.append("..")

from math import tan, sin, pi
from utils import richardson, print_values

if __name__ == "__main__":
  h = 0.27347
  x0 = 0.5807
  orders = [2, 3, 4, 5, 6]

  def f(x):
    return x ** 2 * tan(sin(x / pi))

  def F1(h):
    return (f(x0 + h) - f(x0)) / h

  col_F1 = [F1(h / 2 ** i) for i in range(0, max(orders) + 1)]

  results = []

  for i in orders:
    col = col_F1[slice(0, i)]
    results.append(richardson(col))
  
  print_values(results)