import numpy as np

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

if __name__ == '__main__':
  x = [0.447, 0.941, 1.514, 1.826, 2.473, 3.293, 3.879, 4.577, 4.857, 5.51, 6.155, 6.67]
  y = [5.682, 4.879, 3.402, 3.514, 2.813, 2.055, 2.52, 3.656, 3.87, 4.213, 4.981, 4.538]

  eqs = spline(x, y)