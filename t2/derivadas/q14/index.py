import sys

sys.path.append("..")

from math import tan, cos, sin, pi, log
from utils import richardson, print_value

if __name__ == "__main__":
  x0 = 2.28476
  approximations = [0.0025693956371486415, 0.03246744316225758, 0.046530159839100804]

  def f(x):
    return cos(sin(log(x ** 2)))

  def F1(h):
    return (f(x0 + h) - f(x0)) / h

  col_F1 = approximations

  result = richardson(approximations)

  print_value(result)