#include <stdio.h>
#include <math.h>

double f(double x) {
  return exp(x) - 2 * pow(x, 2) + x - 1.5;
}

int bissectionIterations(double (*f)(double), double a, double b, double tol) {
  double m;
  int it = 1;

  if (f(a) * f(b) >= 0) {
    printf("Intervalo inválido!\n");
  } else {
    while (fabs(b - a) > tol) {
      it++;

      m = (a + b) / 2;

      if (f(a) * f(m) < 0) {
        b = m;
      } else {
        a = m;
      }
    }
  }

  return it;
}

int main() {
  double a = 0.77916;
  double b = 1.963506;
  double tol = 3.51779 * pow(10, -11);

  printf("Numero de iteracoes: %d\n", bissectionIterations(f, a, b, tol));
}