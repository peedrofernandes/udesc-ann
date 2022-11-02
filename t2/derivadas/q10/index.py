import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_values

def func(x):
  return math.log(2 + math.cos(math.exp(-x)))

def taylor(f, xs, x0):
  cs1 = dif_fin(xs, x0)
  cs2 = dif_fin(xs, x0, 2)
  cs3 = dif_fin(xs, x0, 3)
  cs4 = dif_fin(xs, x0, 4)
  
  df1x0 = sum([c * f(x) for c, x in zip(cs1, xs)])
  df2x0 = sum([c * f(x) for c, x in zip(cs2, xs)])
  df3x0 = sum([c * f(x) for c, x in zip(cs3, xs)])
  df4x0 = sum([c * f(x) for c, x in zip(cs4, xs)])

  def p(x):
    result = f(x0)
    result += df1x0 * (x - x0)
    result += df2x0 / math.factorial(2) * (x - x0) ** 2
    result += df3x0 / math.factorial(3) * (x - x0) ** 3
    result += df4x0 / math.factorial(4) * (x - x0) ** 4
    return result

  return p


if __name__ == "__main__":
  # func = math.log(2 + math.cos(math.exp(-x)))
  x0 = -1.4675
  order = 4
  x = [-1.7138, -1.6158, -1.5832, -1.4859, -1.4324, -1.3899, -1.3128, -1.2648]
  values = [-1.6349, -1.5363, -1.4885, -1.3328]

  p = taylor(func, x, x0)

  ps = [p(vi) for vi in values]
  es = [abs(func(vi) - p(vi)) for vi in values]

  results = [item for pair in zip(ps, es) for item in pair]

  print_values(results)