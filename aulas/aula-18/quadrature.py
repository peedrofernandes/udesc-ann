import math

print(f"x_k{'':<20}c_k{'':<20}")

def f(x):
  return math.exp(-x ** 2)

def quadratura(f, a, b, ps):
  def change(f, a, b, u):
    return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

  def g(x):
    return change(f, a, b, x)

  return sum([ck * g(xk) for xk, ck in ps])


