import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [-4.72, -4.6819, -4.2975, -3.8664, -3.7541, -3.2657, -2.9498, -2.6693, -2.5938, -2.0755, -1.9073, -1.5292, -1.2369, -0.9678, -0.7564, -0.3054, -0.0131, 0.2599, 0.5438, 0.7953, 1.1614, 1.3924, 1.7216, 1.8042, 2.2149, 2.3769, 2.7348, 3.0303, 3.3575, 3.7854, 3.835, 4.3564, 4.4128, 4.7388]
  y = [3.749, 3.4678, 4.3661, 4.965, 5.3908, 6.0303, 6.043, 6.4555, 5.8991, 6.0273, 6.3628, 6.2445, 6.029, 5.7204, 5.9465, 5.6132, 5.9735, 5.2286, 4.9785, 5.9252, 4.9811, 4.5532, 4.5042, 4.7794, 4.3325, 4.9383, 4.7092, 3.2684, 5.2103, 5.7107, 5.901, 6.3465, 6.6558, 7.464]
  values = [-3.0055, -2.512, -1.0125, -0.9781, 2.4514]

  coeffs = poly_regression(x, y, 3)
  p = build_poly(coeffs)

  results = [ci for ci in coeffs]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "poly_regression.png"))


