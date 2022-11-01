import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [-4.5081, -3.7338, -2.8019, -2.4512, -1.4185, -0.9417, -0.453, 0.4035, 1.4938, 2.2727, 2.4375, 3.7875, 3.9644, 4.8567, 5.9412]
  y = [-2.8027, 1.0484, 2.2294, 3.6855, 0.6954, -0.082, -0.1824, -0.6761, 0.6014, 2.2262, 3.6752, 4.5262, 3.3192, 2.9443, -11.1025]
  values = [-4.4667, 4.0663, 4.9889]

  coeffs = poly_regression(x, y, 4)
  p = build_poly(coeffs)

  results = [ci for ci in coeffs]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "poly_regression.png"))


