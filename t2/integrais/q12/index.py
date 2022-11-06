from sys import path
import math

path.append("..")

import utils

def quadratura(f, a, b, ps):
  def change(f, a, b, u):
    return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

  def g(x):
    return change(f, a, b, x)

  return sum([ck * g(xk) for xk, ck in ps])

def f(val):
  def f(x):
    return eval(val)
  return f

if __name__ == "__main__":
  funcs = ['math.exp(x)*math.sin(x)/(1+x**2)', 'math.cos(-x**2/3)', '(x+1/x)**2', 'math.log(math.sqrt(1+x**2))', 'math.exp(-x**2)']
  a = [0.411, -1.315, 0.988, 1.695, -0.863]
  b = [2.56, 1.877, 2.906, 3.122, 1.252]
  exact_for_degree_less_than = [12, 6, 10, 8, 4]

  results = [quadratura(f(vi), ai, bi, utils.legendre[int(psi / 2)]) for vi, ai, bi, psi in zip(funcs, a, b, exact_for_degree_less_than)]

  utils.print_values(results)