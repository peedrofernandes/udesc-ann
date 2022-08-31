#include <stdio.h>
#include <math.h>

double f(double x) {
  return exp(x) - 2 * pow(x, 2) + x - 1.5;
}

double df(double x) {
  return exp(x) - 4 * x + 1;
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
  double x0 = 0.44869;
  int it[] = {1, 3, 5};

  for (int i = 0; i < 3; i++) {
    printf("%.8lf", newton(f, df, x0, it[i]));
    if (i != 2)
      printf(",");
  }
  printf("\n");

  return 0;
}