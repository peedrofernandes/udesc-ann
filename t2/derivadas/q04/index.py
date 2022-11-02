import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_value

def func(x):
  return math.sin(x)**3 - 3*math.sin(x)**2 + math.sin(x**2) + 4

if __name__ == "__main__":
  x0 = -4.3623
  x = [-4.5636, -4.4201, -4.2569, -4.2065]
  # func = math.sin(x)**3 - 3*math.sin(x)**2 + math.sin(x**2) + 4

  c = dif_fin(x, x0, 2)

  val = sum([ci * func(xi) for ci, xi in zip(c, x)])
  print_value(val)