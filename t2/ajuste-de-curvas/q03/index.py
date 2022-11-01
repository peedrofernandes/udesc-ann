import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [0.6856, 1.3705, 1.5973, 2.6909, 2.8957, 3.5829, 4.7953, 5.2715, 6.1261, 6.9944, 7.6113, 7.8909, 9.016, 9.5464]
  y = [4.927, 4.6142, 4.494, 3.9268, 4.1237, 4.2132, 4.0008, 4.1232, 4.3234, 4.4829, 4.9317, 4.7906, 5.7149, 6.1493]
  values = [0.773, 1.4917, 8.5467]

  coeffs = poly_regression(x, y, 2)
  p = build_poly(coeffs)

  results = [ci for ci in coeffs]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "poly_regression.png"))


