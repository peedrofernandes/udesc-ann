from sys import path

path.append("..")

import utils

def trapz(x, y):
  soma = 0

  n = len(x)

  for i in range(1, n):
    b1 = y[i - 1]
    b2 = y[i]
    h = abs(x[i] - x[i - 1])
    soma += (b1 + b2) * h / 2
  
  return soma


def simps(x, y):
  if len(x) % 2 == 0 or len(y) % 2 == 0:
    raise ValueError("A lista de pontos deve conter uma quantidade ímpar de pontos!")
  if len(x) < 3:
    raise ValueError("Para que seja possível construir ao menos uma parábola, três pontos devem ser fornecidos!")

  sum = 0
  for k in range(2, len(x), 2):
    x0, x1 = x[k - 2], x[k - 1]
    y0, y1, y2 = y[k - 2], y[k - 1], y[k]
    sum += ((x1 - x0) / 3) * (y0 + 4*y1 + y2)

  return sum

if __name__ == "__main__":
  ts = [0.75 * i for i in range(0, 17)]
  rs = [9.73,9.41,9.03,8.45,8.21,7.7,7.33,6.93,6.48,5.94,5.52,5.24,4.97,4.45,3.9,3.66,3.17]

  results = []

  results.append(trapz(ts, rs))
  results.append(simps(ts, rs))

  utils.print_values(results)