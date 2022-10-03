import numpy as np
import math

def spline(x, y):
	n = len(x)
	a = {k: v for k, v in enumerate(y)}
	h = {k: x[k + 1] - x[k] for k in range(n - 1)}

	A = [[1] + [0] * (n - 1)]
	for i in range(1, n - 1):
		row = [0] * n
		row[i - 1] = h[i - 1]
		row[i] = 2 * (h[i - 1] + h[i])
		row[i + 1] = h[i]
		A.append(row)
	A.append([0] * (n - 1) + [1])

	B = [0]
	for k in range(1, n - 1):
		row = 3 * (a[k + 1] - a[k]) / h[k] - 3 * (a[k] - a[k - 1]) / h[k - 1]
		B.append(row)
	B.append(0)

	c = dict(zip(range(n), np.linalg.solve(A, B)))

	b = {}
	d = {}
	for k in range(n - 1):
		b[k] = (1 / h[k]) * (a[k + 1] - a[k]) - (h[k] / 3) * (2 * c[k] + c[k + 1])
		d[k] = (c[k + 1] - c[k]) / (3 * h[k])

	s = {}
	for k in range(n - 1):
		print('{:.16},{:.16},{:.16},{:.16},'.format(a[k], b[k], c[k], d[k]))
		eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
		s[k] = {'eq': eq, 'domain': [x[k], x[k + 1]]}

	return 

def f(x):
	# return math.pow(x,5)-4*pow(x,2)+2*math.sqrt(x+1)+np.cos(x)
  # return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)
  return 1.0/(1+25*pow(x,2))

if __name__ == '__main__':
	x = [-0.898, -0.738, -0.631, -0.415, -0.293, -0.068, 0.129, 0.291, 0.382, 0.568, 0.726, 0.964]
	y = [f(xi) for xi in x]

	eqs = spline(x, y)