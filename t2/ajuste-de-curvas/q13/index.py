import sys, os

sys.path.append("..")

from math import exp, log, log2
from utils import poly_regression, generate_png, print_values

if __name__ == "__main__":
  x = [0.0209, 0.0694, 0.1626, 0.2191, 0.2293, 0.2978, 0.3544, 0.426, 0.4883, 0.5224, 0.596, 0.6241, 0.7031, 0.7248, 0.7915, 0.848, 0.9143, 0.9792, 1.0135, 1.1057, 1.1318, 1.2021, 1.2558, 1.2841, 1.3758, 1.432, 1.4454, 1.5275, 1.6061, 1.647, 1.7195, 1.7424, 1.8203, 1.8349, 1.9432, 1.9606]
  y = [1.7181, 4.3426, 5.7116, 5.1814, 4.9474, 6.0203, 6.8681, 4.5797, 6.5301, 7.0531, 9.374, 5.7039, 10.2808, 8.9208, 9.3557, 10.4338, 11.0915, 11.6713, 9.5543, 12.8936, 13.5096, 14.8859, 15.8814, 15.5921, 17.4366, 18.3121, 16.8119, 20.4893, 22.2286, 23.4285, 25.4407, 26.0798, 28.0273, 28.5972, 33.3838, 33.1299]
  values = [0.5402, 0.6679, 0.9289, 1.5961, 1.7004]

  # Translação para cima
  ky = abs(min(y)) + 1 if (min(y) < 0) else 0
  y_pos = [yi + ky for yi in y]

  Y = [log2(yi) for yi in y_pos]

  a0, a1 = poly_regression(x, Y)
  a = 2 ** a0
  b = a1

  def p(x):
    return a * 2 ** (b * x) - ky

  results = [a, b]
  results.extend([p(vi) for vi in values])

  print_values(results)

  generate_png(x, y, p, os.path.join(os.path.dirname(__file__), "exp_regression.png"))