import sys

sys.path.append("..")

from utils import print_value

def trapz(x, y):
  soma = 0

  n = len(x)

  for i in range(1, n):
    b1 = y[i - 1]
    b2 = y[i]
    h = abs(x[i] - x[i - 1])
    soma += (b1 + b2) * h / 2
  
  return soma

if __name__ == "__main__":
  x = [0.005, 0.173, 0.177, 0.25, 0.282, 0.3, 0.385, 0.398, 0.561, 0.678, 0.768, 0.828, 0.844, 1.377, 1.5, 1.528, 1.567, 1.588, 1.62, 1.768, 2.109, 2.341, 2.399, 2.481, 2.496, 2.534, 2.541, 2.702, 2.914, 2.967, 3.019, 3.06, 3.283, 3.518, 3.976, 3.983, 4.031, 4.142, 4.175, 4.182, 4.389, 4.516, 4.64, 4.643, 4.724, 4.799, 4.932]
  y = [1.256, 1.805, 1.819, 2.079, 2.189, 2.249, 2.508, 2.544, 2.878, 2.984, 2.999, 2.981, 2.973, 2.378, 2.247, 2.221, 2.186, 2.169, 2.144, 2.054, 2.012, 2.116, 2.159, 2.229, 2.244, 2.281, 2.289, 2.473, 2.742, 2.805, 2.862, 2.902, 2.997, 2.743, 1.309, 1.289, 1.168, 1.008, 1.0, 1.001, 1.455, 2.047, 2.634, 2.646, 2.907, 3.0, 2.737]

  print_value(trapz(x, y))