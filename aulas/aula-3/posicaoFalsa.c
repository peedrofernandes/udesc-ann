// Encontrando Raíz de funções
// Método da Posição falsa

#include <stdio.h>

void secant(double (*f)(double), double a, double b, int n) {
	for (int i = 0; i < n; i++) {
		double fa = f(a);
		double fb = f(b);
		if (fa * fb >= 0) {
			printf("O teorema de bolzano nao sabe dizer se existe ou nao raiz neste intervalo.\n");
			break;
		}
		double x1 = (a * fb - b * fa) / (fb - fa);
		printf("x %d = %.16f\n", i + 2, x1);
		double fx1 = f(x1);
		if (fa * fx1 < 0)
			b = x1;
		else {
			a = x1;
			fa = fx1;
		}
	}
}

double f(double x) {
	return x * x - 2;
}

int main() {
	double a = 1;
	double b = 2;
	int n = 10;

	secant(f, a, b, n);

	return 0;
}


