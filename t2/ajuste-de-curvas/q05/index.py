import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [-4.6512, -4.0475, -2.3562, -2.0005, -1.0875, -0.0159, 0.809, 2.0644, 2.4221, 3.7566, 4.8069]
  y = [6.4666, 5.4386, 6.1246, 6.0387, 5.089, 4.2869, 3.113, 2.1738, 2.432, 2.525, 4.0224]
  values = [-2.2628, -0.2216, 4.7449]

  coeffs = poly_regression(x, y, 3)
  p = build_poly(coeffs)

  results = [ci for ci in coeffs]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "poly_regression.png"))


