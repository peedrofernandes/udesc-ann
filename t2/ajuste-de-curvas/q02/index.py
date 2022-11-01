import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [0.2559, 0.434, 0.6454, 0.9449, 1.5298, 1.6762, 2.0382, 2.3168, 2.5365, 2.8608, 3.331, 3.4761, 4.0, 4.3357, 4.6097, 4.7444, 5.128, 5.4361, 5.676, 6.226, 6.3256, 6.7842, 6.9717, 7.368, 7.6721, 8.1242, 8.2643, 8.607, 8.806, 9.0643, 9.516, 9.8267]
  y = [3.9511, 4.0592, 3.9561, 4.8554, 5.7281, 5.7654, 6.3836, 6.8377, 7.1702, 7.7251, 8.1433, 7.7448, 9.242, 9.9009, 10.0124, 10.4313, 10.8201, 11.4226, 11.5991, 12.5193, 13.2286, 13.3435, 13.2339, 14.03, 14.4903, 15.2663, 15.3705, 15.2543, 16.2227, 16.9605, 17.5947, 17.5248]
  values = [2.9195, 3.1437, 3.8013, 6.3875, 8.2271]

  coeffs = poly_regression(x, y)
  p = build_poly(coeffs)

  results = [ci for ci in coeffs]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "poly_regression.png"))


