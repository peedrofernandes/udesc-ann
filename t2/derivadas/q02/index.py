import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_value

def func(x):
  return math.sin(math.cos(math.exp(-x)))

if __name__ == "__main__":
  x0 = 1.4654
  x = [1.3008, 1.3225, 1.5095, 1.546, 1.707]

  c = dif_fin(x, x0)

  val = sum([ci * func(xi) for ci, xi in zip(c, x)])
  print_value(val)




