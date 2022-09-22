#include <stdio.h>
#include <math.h>

double f(double x) {
  return sqrt(x) - cos(x);
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
  double x0 = 0.4637;
  double x1 = 1.09011;

  int it[] = { 1, 3, 5 };
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", secant(f, x0, x1, it[i]));
    if (i != 2)
      printf(",");
  }
  printf("\n");
}