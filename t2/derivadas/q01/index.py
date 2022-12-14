import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_value

def func(x):
  return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)

if __name__ == "__main__":
  x0 = 8.2936
  x = [8.2001, 8.2624, 8.4715]

  c = dif_fin(x, x0)

  val = sum([ci * func(xi) for ci, xi in zip(c, x)])
  print_value(val)




