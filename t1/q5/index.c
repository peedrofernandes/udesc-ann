#include <stdio.h>
#include <math.h>

double f(double x) {
  return 2 * (x + 1) * (x - 0.5) * (x - 1);
}

int bissection(double (*f)(double), double a, double b, double tol) {
  double m;
  int it = 0;

  if (f(a) * f(b) >= 0)
    printf("Intervalo invalido!");
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
  double a = -1.776648;
  double b = 1.352926;
  double tol = 3.04617 * pow(10, -11);

  printf("%d\n", bissection(f, a, b, tol));
}