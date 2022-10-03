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
		eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
		s[k] = {'eq': eq, 'domain': [x[k], x[k + 1]]}

	return s


def s(x):
	for key, value in eqs.items():
		if value['domain'][0] <= x <= value['domain'][1]:
			return eval(value['eq'])

if __name__ == '__main__':
  x = [0.505, 1.097, 1.327, 1.813, 2.683, 2.999, 3.756, 4.519, 4.975, 5.606, 5.926, 6.837]
  y = [5.422, 4.047, 3.793, 3.198, 2.2, 2.215, 2.321, 3.295, 3.409, 4.575, 4.383, 4.676]
  valores = [1.352, 3.968, 4.286, 5.524, 6.74]

  eqs = spline(x, y)

  for valor in valores:
    print('{:.16f},'.format(s(valor)), end=" ")
  print()