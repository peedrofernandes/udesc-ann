from math import exp

def trapz(f, a, b, h):
  n = int((b - a) / h)
  s = sum([f(a + k * h) for k in range(1, n)])
  return (h / 2) * (f(a) + 2 * s + f(b))

def richardson(x, b = 1):
  n = len(x)

  for k in range(1, n):
    for i in range(n - k):
      numer = 2 ** (k * b) * x[i + 1] - x[i]
      denom = 2 ** (k * b) - 1
      aprox = numer / denom
      x[i] = aprox
  return x[0]

# O método da Integração de Romberg é, basicamente, o método da extrapolação de Richardson
# aplicado sobre a Regra dos Trapézios, que possui erro com ordem O(h²)
def romberg(c1):
  return richardson(c1, 2)

def f(x):
  return exp(-x ** 2)

if __name__ == "__main__":
  a, b = [0, 1]
  h = 0.5

  h = 0.5
  k = 5
  hs = [h / 2 ** i for i in range(k)]
  c1 = [trapz(f, a, b, h) for h in hs]
  r = romberg(c1)
  print(r)
  # Encontrar uma aproximação O(h^10) (Aproximação inicial pela regra dos trapézios: O(h²))
  
