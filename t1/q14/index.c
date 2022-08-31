#include <stdio.h>
#include <math.h>

double f(double x) {
  return exp(5 * x) - 2;
}

double df(double x) {
  return 5 * exp(5 * x);
}

double newton(double (*f)(double), double (*df)(double), double x0, int it) {
  double r;

  for (int i = 1; i <= it; i++) {
    r = x0 - f(x0) / df(x0);
    x0 = r;
  }

  return r;
}

int main() {
  double x0 = -1.16985713;
  int it[] = {1, 25, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700};
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", newton(f, df, x0, it[i]));
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("\n");
}