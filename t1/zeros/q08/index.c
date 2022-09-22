#include <stdio.h>
#include <math.h>

double f(double x) {
  return pow(x, 3) - 7 * pow(x, 2) + 14 * x - 7;
}

int bissectionIterations(double (*f)(double), double a, double b, double tol) {
  double m;
  int it = 0;

  if (f(a) * f(b) >= 0) {
    printf("Intervalo inválido!\n");
  } else {
    it++;
    while (fabs(b - a) >= tol) {
      it++;

      m = (a + b) / 2;

      if (f(a) * f(m) < 0)
        b = m;
      else
        a = m;
    }
  }

  return it;
}

int main() {
  double a = 3.202275;
  double b = 4.212628;
  double tol = 2.50291 * pow(10, -10);

  printf("Numero de iteracoes: %d\n", bissectionIterations(f, a, b, tol));
}