import sys

sys.path.append("..")

from math import tan, cos, sin, pi, log
from utils import richardson, print_value

if __name__ == "__main__":
  x0 = 2.6359
  approximations = [-0.21244985707766606, -0.1744000642765755, -0.155236797693469, -0.14565783317418024, -0.1408734642661571, -0.1384830999255513]

  def f(x):
    return cos(sin(log(x ** 2)))

  def F1(h):
    return (f(x0 + h) - f(x0)) / h

  col_F1 = approximations

  result = richardson(approximations)

  print_value(result)