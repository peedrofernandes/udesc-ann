#include <stdio.h>
#include <math.h>

double fixedPoint(double (*f)(double), double(*g)(double), double x0, int n) {
  for (int i = 0; i < n; i++) {
    x0 = g(x0);
    printf("x %d = %.16lf, f(x%d) = %.16lf\n", i + 1, x0, i, f(x0));
  }
}

double f(double x ) {
  return pow(x, 2) - 2;
}

double g(double x) {
  return x / 2.0 + 1 / x;
}

int main() {
  int n = 10;
  double x0 = 1.23456;

  fixedPoint(f, g, x0, n);
}