import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_value

def func(x):
  return math.cos(math.exp(-x**2)) + math.sin(x**2 / 2)

if __name__ == "__main__":
  x0 = -1.8484
  x = [-2.0549, -2.0066, -1.9585, -1.9207, -1.833, -1.8069, -1.737, -1.6696, -1.6328]
  # func = math.cos(math.exp(-x**2)) + math.sin(x**2 / 2)

  c = dif_fin(x, x0)

  val = sum([ci * func(xi) for ci, xi in zip(c, x)])
  print_value(val)