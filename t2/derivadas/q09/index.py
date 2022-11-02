import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_values

def func(x):
  return 3 * math.cos((x**2-1)**(1/3))

def taylor(f, xs, x0):
  cs1 = dif_fin(xs, x0)
  cs2 = dif_fin(xs, x0, 2)
  cs3 = dif_fin(xs, x0, 3)
  
  df1x0 = sum([c * f(x) for c, x in zip(cs1, xs)])
  df2x0 = sum([c * f(x) for c, x in zip(cs2, xs)])
  df3x0 = sum([c * f(x) for c, x in zip(cs3, xs)])

  def p(x):
    result = f(x0)
    result += df1x0 * (x - x0)
    result += df2x0 / math.factorial(2) * (x - x0) ** 2
    result += df3x0 / math.factorial(3) * (x - x0) ** 3
    return result

  return p


if __name__ == "__main__":
  # func = 3 * math.cos((x**2-1)**(1/3))
  x0 = 8.9362
  order = 3
  x = [8.6963, 8.7973, 8.9058, 8.9469, 9.0619, 9.1057]
  values = [8.8503, 8.8854, 8.8933]

  p = taylor(func, x, x0)

  ps = [p(vi) for vi in values]
  es = [abs(func(vi) - p(vi)) for vi in values]

  results = [item for pair in zip(ps, es) for item in pair]

  print_values(results)