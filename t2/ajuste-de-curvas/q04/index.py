import sys, os

sys.path.append("..")

from utils import poly_regression, build_poly, print_values, generate_png

if __name__ == "__main__":
  x = [0.0213, 0.3638, 0.651, 0.971, 1.1647, 1.4802, 1.7037, 2.1922, 2.4623, 2.5266, 2.8262, 3.1367, 3.5777, 3.6347, 4.0271, 4.3172, 4.5985, 4.8262, 5.2624, 5.3404, 5.8218, 5.8502, 6.2371, 6.4043, 6.7269, 7.1984, 7.4884, 7.5726, 7.8429, 8.1561, 8.3507, 8.8771, 8.9358, 9.2975, 9.698, 9.863]
  y = [5.6136, 6.054, 5.3382, 5.2676, 5.0722, 4.961, 4.6962, 4.3363, 4.1703, 4.1945, 4.344, 3.8875, 3.6757, 3.622, 3.5296, 3.4738, 3.2242, 3.37, 3.3727, 3.3666, 3.0282, 3.3767, 3.5834, 3.5094, 3.6415, 3.7269, 3.8984, 3.8657, 4.0554, 4.2139, 4.2281, 4.6174, 4.7055, 4.9288, 5.2702, 5.353]
  values = [4.0918, 6.6283, 7.2824, 7.8437, 9.3928]

  coeffs = poly_regression(x, y, 2)
  p = build_poly(coeffs)

  results = [ci for ci in coeffs]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "poly_regression.png"))


