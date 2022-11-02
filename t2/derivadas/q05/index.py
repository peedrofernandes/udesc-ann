import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_value

def func(x):
  return math.sqrt(math.cos(x**2) + x)

if __name__ == "__main__":
  x0 = 4.9407
  x = [4.6969, 4.794, 4.8298, 4.8884, 4.971, 5.0075, 5.1114, 5.16]
  # func = math.sqrt(math.cos(x**2) + x)

  c = dif_fin(x, x0, 2)

  val = sum([ci * func(xi) for ci, xi in zip(c, x)])
  print_value(val)