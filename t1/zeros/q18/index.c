#include <stdio.h>

double f(double x) {
  return 2 * (x + 1) * (x - 0.5) * (x - 1);
}

double secant(double (*f)(double), double x0, double x1, int it) {
  double r;

  for (int i = 1; i <= it; i++) {
    r = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0));
    x0 = x1;
    x1 = r;
  }

  return r;
}

int main() {
  int it[] = {1, 3, 5};
  double x0 = -0.22891;
  double x1 = 0.77545;

  for (int i = 0; i < 3; i++) {
    printf("%.8lf", secant(f, x0, x1, it[i]));
    if (i != 2)
      printf(",");
  }
  printf("\n");
}