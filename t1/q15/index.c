#include <stdio.h>
#include <math.h>

double f(double x) {
  return x * (x - 1) * (x - 2) + 0.42;
}

double df(double x) {
  return 3 * pow(x, 2) - 6 * x + 2;
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
  double x0 = 2.09572175;
  int it[] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195};
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", newton(f, df, x0, it[i]));
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("\n");

  return 0;
}