#include <stdio.h>
#include <math.h>
#include "../methods.c"

#define y 19.34
#define z 8.24

double f(double x) {
  return 12 * pow(x, 2) - 4 * x * y - 4 * x * z + y * z;
}

double df(double x) {
  return 24 * x - 4 * y - 4 * z;
}

int main() {
  double a, b, x0, x1;

  a = 0;
  b = 4.12;
  int it1[] = {2, 4, 8, 12};
  bissection(f, a, b, it1, sizeof(it1) / sizeof(int));

  printf(",");

  x0 = 2.98;
  int it2[] = {1, 3, 5};
  newton(f, df, x0, it2, sizeof(it2) / sizeof(int));

  printf(",");

  x0 = 0.04;
  x1 = 3.26;
  int it3[] = {1, 2, 5};
  secant(f, x0, x1, it3, sizeof(it3) / sizeof(int));

  printf(",");

  a = 0;
  b = 4.12;
  int it4[] = {2, 4, 7, 11};
  falsePosition(f, a, b, it4, sizeof(it4) / sizeof(int));

  printf("\n");
}