#include <stdio.h>
#include <math.h>
#include "../methods.c"

#define g 9.81
#define x 3.1
#define t 0.86

// x -> x
// g -> y
// t -> z
// w -> t

double f(double w) {
  return x + (g / (2 * pow(w, 2))) * (sinh(w * t) - sin(w * t));
}

double df(double w) {
  return g * (w * t * (cosh(w * t) - cos(w * t)) - 2 * (sinh(w * t) - sin(w * t))) / (2 * pow(w, 3));
}

int main() {
  double a, b, x0, x1;

  a = -5.98;
  b = 0.62;
  int it1[] = {2, 4, 8, 12};
  bissection(f, a, b, it1, sizeof(it1) / sizeof(int));

  printf(",");

  x0 = -1.46;
  int it2[] = {1, 3, 5};
  newton(f, df, x0, it2, sizeof(it2) / sizeof(int));

  printf(",");

  x0 = -4.52;
  x1 = -1.87;
  int it3[] = {1, 2, 5};
  secant(f, x0, x1, it3, sizeof(it3) / sizeof(int));

  printf(",");

  a = -5.15;
  b = 0.77;
  int it4[] = {2, 4, 7, 11};
  falsePosition(f, a, b, it4, sizeof(it4) / sizeof(int));

  printf("\n");
}