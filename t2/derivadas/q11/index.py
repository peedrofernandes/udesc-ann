import math
import sys, os

sys.path.append("..")

from utils import dif_fin, print_values

def func(x):
  return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)

def taylor(f, xs, x0, n = 1):
  def p(x):
    result = f(x0)

    for i in range(1, n + 1):
      cs = dif_fin(xs, x0, i)
      dfix0 = sum([c * f(x) for c, x in zip(cs, xs)])
      result += dfix0 / math.factorial(i) * (x - x0) ** i
    return result

  return p


if __name__ == "__main__":
  # func = x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)
  x0 = 0.4154
  order = 5
  x = [0.2144, 0.2456, 0.2998, 0.3487, 0.3659, 0.4481, 0.4995, 0.5581, 0.5713, 0.6275]
  values = [0.2788, 0.332, 0.5282, 0.5311, 0.5655]

  p = taylor(func, x, x0, 5)

  ps = [p(vi) for vi in values]
  es = [abs(func(vi) - p(vi)) for vi in values]

  results = [item for pair in zip(ps, es) for item in pair]

  print_values(results)