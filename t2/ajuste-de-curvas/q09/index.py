import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [-4.0582, -3.7669, -3.011, -2.2666, -1.7049, -1.4652, -1.0641, -0.2239, 0.2608, 0.8927, 1.3249, 2.2407, 2.4645, 3.1387, 3.6099, 4.0999]
  y = [-0.4193, 0.9807, 0.8927, 0.3546, -0.1643, -0.6704, -0.8055, -0.3254, -0.5405, 0.5671, 0.7806, -0.5345, -0.9431, -2.0831, -1.7956, 0.9152]
  values = [-3.9688, -2.7605, -0.8286]

  coeffs = poly_regression(x, y, 5)
  p = build_poly(coeffs)

  results = [ci for ci in coeffs]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "poly_regression.png"))


