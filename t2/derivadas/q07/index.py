import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_value

def func(x):
  return math.sin(math.sqrt(math.pi + x**2))

if __name__ == "__main__":
  x0 = 0.2556
  x = [0.0112, 0.075, 0.1448, 0.2108, 0.2824, 0.36, 0.3864, 0.4434]
  # func = math.sin(math.sqrt(math.pi + x**2))

  c = dif_fin(x, x0, 4)

  val = sum([ci * func(xi) for ci, xi in zip(c, x)])
  print_value(val)