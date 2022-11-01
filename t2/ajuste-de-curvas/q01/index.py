import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [0.3474, 1.1366, 1.9035, 2.7913, 3.8577, 4.9856, 5.3436, 6.2147, 6.7886, 7.7113, 8.9724, 9.8364]
  y = [3.9202, 5.847, 7.6635, 9.8452, 11.7415, 13.6175, 14.3493, 16.7086, 17.9038, 19.866, 22.4531, 24.357]
  values = [1.9052, 5.9962, 8.9575]

  coeffs = poly_regression(x, y)
  p = build_poly(coeffs)

  vs = [ci for ci in coeffs]
  vs.extend([p(vi) for vi in values])

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "linear_regression.png"))

  print_values(vs)
