import sys, math

sys.path.append("..")

import utils


def double_trapz(f, a, b, c, d, n1, n2):
  if b < a or d < c:
    raise ValueError("Nos intervalos de integração, B deve ser maior que A e C deve ser maior que D!")
  if n1 <= 0 or n2 <= 0:
    raise ValueError("A quantidade de subintervalos precisa ser maior do que zero!")

  h1 = (b - a) / n1
  h2 = (d - c) / n2

  s = 0
  for i in range(0, n1 + 1):
    border_x = i == 0 or i == n1
    for j in range(0, n2 + 1):
      border_y = j == 0 or j == n2
      fij = f(a + i * h1, c + j * h2)
      if (border_x and border_y):
        s += fij
      elif (border_x or border_y):
        s += 2 * fij
      else:
        s += 4 * fij

  return ((h1 * h2) / 4) * s


if __name__ == "__main__":
  intervalo1 = [-1.42, 1.231]
  intervalo2 = [-1.161, 1.944]
  n1 = 6
  n2 = 8

  def f(x, y):
    return math.cos(x ** 2) * math.sin(y ** 2 * x) * math.exp(-y ** 2) + 1

  result = double_trapz(f, intervalo1[0], intervalo1[1], intervalo2[0], intervalo2[1], n1, n2)

  utils.print_value(result)

  