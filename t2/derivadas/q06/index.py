import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_value

def func(x):
  return math.sin(x)**4 - 4*math.sin(x)**2 + math.cos(x**2) + math.exp(-x**2) + 5

if __name__ == "__main__":
  x0 = 4.1922
  x = [3.9435, 4.0841, 4.1137, 4.2055, 4.2921, 4.3328, 4.399]
  # func = math.sin(x)**4 - 4*math.sin(x)**2 + math.cos(x**2) + math.exp(-x**2) + 5

  c = dif_fin(x, x0, 3)

  val = sum([ci * func(xi) for ci, xi in zip(c, x)])
  print_value(val)