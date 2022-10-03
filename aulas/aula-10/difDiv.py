
def difDiv(x: list[float], y: list[float]) -> list[float]:
  Y = [yi for yi in y]
  coeffs = [Y[0]]
  for j in range(len(x) - 1):
    for i in range(len(x) - 1 - j):
      numer = Y[i + 1] - Y[i]
      denom = x[i + 1 + j] - x[i]
      div = numer / denom
      Y[i] = div
    coeffs.append(Y[0])
  return coeffs

def poly(t, x, coeffs):
  val = 0
  for i in range(len(coeffs)):
    prod = 1
    for j in range(i):
      prod *= (t - x[j])
    val += coeffs[i] * prod
  return val

def buildFunc(x, coeffs):
  def temp(t):
    return poly(t, x, coeffs)
  return temp

if __name__ == "__main__":
  # Exemplo
  # (1,0), (2,1), (3,5), (4,1)
  x = [1, 2, 3, 4]
  y = [0, 1, 5, 1]

  coeffs = difDiv(x, y)
  # O polinômio interpolador da lista de pontos
  p = buildFunc(x, coeffs)
  print(p(1), p(2), p(3), p(4))