// Encontrando raiz de funções
// Teorema do Ponto Fixo

#include <stdio.h>
#include <math.h>

double f(double x) {
	return cos(x);
}

void fixedPoint(double (*f)(double), double x0, int n) {
	double x1;
	for (int i = 0; i < n; i++) {
		x1 = f(x0);
		printf("x %d = %.16f\n", i + 1, x1);
		x0 = x1;
	}
}

int main() {
	int n = 10;
	double x0 = -0.5;

	fixedPoint(f, x0, n);
}

