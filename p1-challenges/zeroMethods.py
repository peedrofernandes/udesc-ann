def bissection(f, a, b, itArray):
  r = 0
  nextIt = 0
  lastIt = itArray[len(itArray) - 1]

  for i in range(1, lastIt + 1):
    r = (a + b) / 2
    if (f(a) * f(r) < 0):
      b = r
    else:
      a = r
    if i == itArray[nextIt]:
      print(f"{r:.8f}", end="")
      nextIt += 1
      if i != it[len(itArray) - 1]:
        print(",", end="")

def newton(f, df, x0, itArray):
  r = 0
  nextIt = 0
  lastIt = itArray[len(itArray) - 1]

  for i in range(1, lastIt + 1):
    r = x0 - f(x0) / df(x0)
    x0 = r
    if i == itArray[nextIt]:
      print(f"{r:.8f}", end="")
      nextIt += 1
      if i != it[len(itArray) - 1]:
        print(",", end="")

def secant(f, x0, x1, itArray):
  r = 0
  nextIt = 0
  lastIt = itArray[len(itArray) - 1]

  for i in range(1, lastIt + 1):
    r = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
    x0 = x1
    x1 = r
    if i == itArray[nextIt]:
      print(f"{r:.8f}", end="")
      nextIt += 1
      if i != it[len(itArray) - 1]:
        print(",", end="")

def falsePosition(f, a, b, itArray):
  r = 0
  nextIt = 0
  lastIt = itArray[len(itArray) - 1]

  for i in range(1, lastIt + 1):
    r = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if (f(a) * f(r) < 0):
      b = r
    else:
      a = r
    if i == itArray[nextIt]:
      print(f"{r:.8f}", end="")
      nextIt += 1
      if i != it[len(itArray) - 1]:
        print(",", end="")