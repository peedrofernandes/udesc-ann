from xml.etree.ElementTree import XML


def f1(x, y):
  return 4 * x ** 2 + y ** 2 - 5
def f2(x, y):
  return x ** 2 + y ** 3 - 4

def df1x(x, y):
  return 8 * x
def df1y(x, y):
  return 2 * y
def df2x(x, y):
  return 2 * x
def df2y(x, y):
  return 3 * y ** 2

x0 = -1.3421
y0 = 1.6462
it = [1, 2, 3, 4, 5]

currentIt = 0
for i in range(1, it[len(it) - 1] + 1):
  # Jacobiano:
  # [df1x df1y]
  # [df2x df2y]
  # Inversa:
  # [df2y -df1y]
  # [-df2x df1x]
  det = df1x(x0,y0) * df2y(x0,y0) - df1y(x0,y0) * df2x(x0,y0)
  xk = x0 - (df2y(x0,y0) * f1(x0,y0) - df1y(x0,y0) * f2(x0,y0)) / det
  yk = y0 - (-df2x(x0,y0) * f1(x0,y0) + df1x(x0,y0) * f2(x0,y0)) / det
  x0 = xk
  y0 = yk

  if i == it[currentIt]:
    print(f'{xk:.8f},{yk:.8f}', end='')
    currentIt += 1
    if (i != it[len(it) - 1]):
      print(',', end='')
    else:
      print()