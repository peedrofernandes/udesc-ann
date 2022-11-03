import sys

sys.path.append("..")

from math import tan, sin, pi
from utils import richardson, print_values

if __name__ == "__main__":
  h = 0.3917
  x0 = 1.04686
  orders = [4, 5, 6, 7, 8]

  def f(x):
    return x ** (x ** (-x))

  def F1(h):
    return (f(x0 + h) - f(x0)) / h

  col_F1 = [F1(h / 2 ** i) for i in range(0, max(orders) + 1)]

  results = []

  for i in orders:
    col = col_F1[slice(0, i)]
    results.append(richardson(col))
  
  print_values(results)