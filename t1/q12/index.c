#include <stdio.h>
#include <math.h>

double f(double x) {
  return M_PI * x - exp(x);
}

double dfdx(double x) {
  return M_PI - exp(x);
}

double newton(double (*f)(double), double(*dfdx)(double), double x0, int it) {
  double r;

  for (int i = 1; i <= it; i++) {
    r = x0 - f(x0) / dfdx(x0);
    x0 = r;
  }

  return r;
}

int main() {
  double x0 = 1.06219;
  int it[] = {1, 3, 5};
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", newton(f, dfdx, x0, it[i]));
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("\n");

  return 0;
}