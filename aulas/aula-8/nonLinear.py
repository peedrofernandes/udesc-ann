from math import pow

def f1(x: float, y: float) -> float:
  return pow(x, 2) + pow(y, 2) - 5

def f2(x: float, y: float) -> float:
  return pow(x, 2) - pow(y, 2) - 3

def df1x(x: float, y: float) -> float:
  return 2 * x

def df1y(x: float, y: float) -> float:
  return 2 * y

def df2x(x: float, y: float) -> float:
  return 2 * x

def df2y(x: float, y: float) -> float:
  return -2 * y

n = 5
x0 = 2.0
y0 = 3.0

for i in range(n):
  # Jacobiano
  # [df1x df1y]
  # [df2x df2y]

  # Inversa
  # (1 / det) * [df2y -df1y] * [f1]
  #             [-df2x df1x] * [f2]

  a = df1x(x0, y0)
  b = df1y(x0, y0)
  c = df2x(x0, y0)
  d = df2y(x0, y0)
  det = a * d - b * c
  xk = x0 - (df2y(x0, y0) * f1(x0, y0) - df1y(x0, y0) * f2(x0, y0)) / det
  yk = y0 - (-df2x(x0, y0) * f1(x0, y0) + df1x(x0, y0) * f2(x0, y0)) / det

  x0 = xk
  y0 = yk
  print(f'[{x0:.12f},{y0:.12f}]')



