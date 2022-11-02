import math
import sys, os

sys.path.append("../../")

from utils import print_values

def func(x):
  return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)

def F3(h, f, x0):
  return (f(x0 + h) - f(x0 - h)) / (2 * h)

if __name__ == "__main__":
  x0 = 8.7178
  x = [8.5691, 8.7292, 8.8799]

  hs = [abs(xi - x0) for xi in x]
  results = [F3(h, func, x0) for h in hs]

  print_values(results)






