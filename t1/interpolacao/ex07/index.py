def lagrange(lx, ly):
  coeffs = []

  for i in range(len(lx)):
    prod = 1
    for j in range(len(lx)):
      if i != j:
        prod *= (lx[i] - lx[j])
    ci = ly[i] / prod
    coeffs.append(ci)

  # def p(x):
  #   sum = 0
  #   for i in range(len(lx)):
  #     prod = 1
  #     for j in range(len(lx)):
  #       if i != j:
  #         prod *= (x - lx[j])
  #     sum += coeffs[i] * prod
  #   return sum
  # return p
  return coeffs

if __name__ == "__main__":
  lx = [0.699, 2.021, 3.863]
  ly = [1.06, 1.891, 1.924]

  coeffs = lagrange(lx, ly)

  print(f"{coeffs[0]:.8f},{coeffs[1]:.8f},{coeffs[2]:.8f}")