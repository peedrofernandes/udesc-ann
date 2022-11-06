from sys import path

path.append("..")

from utils import print_values, legendre

def trapz(f, a, b, n):
  h = (b - a) / n
  s = sum([f(a + k * h) for k in range(1, n)])
  return (h / 2) * (f(a) + 2 * s + f(b))


def simps(f, a, b, n):
  if n % 2 != 0 or n < 1:
    raise ValueError("n deve ser par e maior do que 1!")

  h = (b - a) / n

  sum_even = sum([f(a + k * h) for k in range(2, n, 2)])
  sum_odd = sum([f(a + k * h) for k in range(1, n, 2)])

  return (h / 3) * (f(a) + 2 * sum_even + 4 * sum_odd + f(b))


def richardson(x, b = 1):
  n = len(x)

  for k in range(1, n):
    for i in range(n - k):
      numer = 2 ** (k * b) * x[i + 1] - x[i]
      denom = 2 ** (k * b) - 1
      aprox = numer / denom
      x[i] = aprox
  return x[0]


def romberg(f, a, b, h, k):
  hs = [h / 2 ** i for i in range(int(k / 2))]
  c1 = [trapz(f, a, b, int((b - a) / h)) for h in hs]

  return richardson(c1, 2)


def quadratura(f, a, b, ps):
  def change(f, a, b, u):
    return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

  def g(x):
    return change(f, a, b, x)

  return sum([ck * g(xk) for xk, ck in ps])


if __name__ == "__main__":
  def f(t):
    return -t * (t - 21) * (t + 1)

  a = 0
  b = 12

  results = []

  results.append(trapz(f, a, b, 31))
  results.append(simps(f, a, b, 14))
  results.append(romberg(f, a, b, 12 / 10, 8))
  results.append(quadratura(f, a, b, legendre[6]))

  print_values(results)