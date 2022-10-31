import numpy as np


def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi ** 2 for xi in x)

    A = [
        [n, sum_x],
        [sum_x, sum_x2]
    ]

    sum_y = sum(y)
    sum_yx = sum(yi * xi for yi, xi in zip(y, x))

    B = [
        sum_y,
        sum_yx
    ]

    return np.linalg.solve(A, B)


if __name__ == "__main__":
    # Gera pontos "mais ou menos" em uma reta para critérios de teste do algoritmo
    def dummy(a, b):
        def func(x):
            erro = -4 + 2 * np.random.random() / 10
            # erro = 0
            return a + b * x + erro
        return func

    points = dummy(2, 1)

    x = np.linspace(0, 2, 50)
    y = [points(xi) for xi in x]

    a0, a1 = linear_regression(x, y)

    def p(x):
      return a0 + a1 * x

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    # Visualização
    from matplotlib.pyplot import scatter, savefig, plot

    scatter(x, y)
    plot(t, pt, color="red")
    savefig("linear_regression.png")
