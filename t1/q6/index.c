#include <stdio.h>
#include <math.h>

double f(double x) {
  return M_PI * x - exp(x);
}

int bissectionIterations(double (*f)(double), double a, double b, double tol) {
  double m;
  int it = 0;

  if (f(a) * f(b) >= 0)
    printf("Intervalo invalido!\n");
  else {
    while (1) {
      m = (a + b) / 2;

      if (f(a) * f(m) < 0)
        b = m;
      else
        a = m;

      it++;

      if (fabs(f(m)) <= tol)
        break;
    }
  }

  return it;
}

int main() {
  double a = 0.08637;
  double b = 1.068717;
  double tol = tol = 2.90376 * pow(10, -9);

  printf("%d\n", bissectionIterations(f, a, b, tol));
}