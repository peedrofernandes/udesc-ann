import math

def simps(f, a, b, n):
  if n % 2 != 0 or n < 1:
    raise ValueError("n deve ser par e maior do que 1!")

  h = (b - a) / n

  sum_even = sum([f(a + k * h) for k in range(2, n, 2)])
  sum_odd = sum([f(a + k * h) for k in range(1, n, 2)])

  return (h / 3) * (f(a) + 2 * sum_even + 4 * sum_odd + f(b))


if __name__ == "__main__":
  a, b = 0, 1

  n = 50
  # n: Número de subintervalos
  # n / 2: número de parábolas
  # n + 1: número de pontos na partição

  def f(x):
    return math.exp(-x ** 2)

  i1 = simps(f, a, b, n)
  print(i1)

  a, b = 0, math.pi / 2
  n = 6

  def g(x):
    return math.cos(x ** 2)