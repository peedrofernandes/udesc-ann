import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_value

def func(x):
  return x**2 * math.exp(-x) * math.cos(x) + 1

if __name__ == "__main__":
  x0 = 2.8896
  x = [2.6655, 2.6866, 2.7373, 2.7712, 2.8005, 2.8382, 2.8623, 2.8985, 2.9247, 2.945, 3.0024, 3.0308, 3.0415, 3.1061, 3.1389]
  # func = x**2 * math.exp(-x) * math.cos(x) + 1

  c = dif_fin(x, x0, 5)

  val = sum([ci * func(xi) for ci, xi in zip(c, x)])
  print_value(val)