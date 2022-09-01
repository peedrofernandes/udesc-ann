#include <stdio.h>
#include <math.h>

void newton(
  double (*f)(double),
  double (*df)(double),
  double x0,
  int it) {
  for (int i = 1; i <= it; i++) {
    double dfx0 = df(x0);

    if (fabs(dfx0) < pow(10, -10))
      break;

    double x1 = x0 - f(x0) / df(x0);
    printf("x%d = %.16lf\n", i + 1, x1);
    x0 = x1;
  }
}

double f(double x) {
  return pow(x, 2) - 2;
}

double df(double x) {
  return 2 * x;
}

int main() {
  double x0 = 10;
  int n = 10;

  newton(f, df, x0, n);
}