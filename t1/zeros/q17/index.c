#include <stdio.h>
#include <math.h>

double f(double x) {
  return M_PI * x - exp(x);
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
  double x0 = 0.92398;
  double x1 = 2.04048;
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", secant(f, x0, x1, it[i]));
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("\n");
}