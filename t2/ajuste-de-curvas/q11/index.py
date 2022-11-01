import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [0.2119, 1.4144, 1.8888, 2.7829, 4.1546, 4.6419, 5.3565, 5.875, 6.8681, 7.74, 8.8036, 9.3776]
  y = [5.8933, 4.625, 4.5357, 3.9594, 3.4888, 3.4901, 3.4717, 3.5457, 3.7467, 4.0997, 4.6688, 5.13]
  values = [4.8281, 7.2026, 9.3228]

  k = 2
  A = []
  B = []
  coeffs = poly_regression(x, y, k)
  p = build_poly(coeffs)

  for i in range(k + 1):
    for j in range(k + 1):
      A.append(sum(xi ** (i + j) for xi in x) if (i+j > 0) else len(x))

    B.append((sum(yi * xi ** i for xi, yi in zip(x, y))) if (i > 0) else (sum(y)))

  results = A
  results.extend(coeffs)
  results.extend(B)
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "poly_regression.png"))


