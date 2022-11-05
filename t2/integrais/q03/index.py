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
  x = [0.102, 0.581, 2.788, 2.884, 4.39, 4.714, 4.842]
  y = [1.555, 2.904, 2.582, 2.704, 1.459, 2.883, 2.975]

  print_value(trapz(x, y))