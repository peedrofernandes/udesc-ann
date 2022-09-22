#include <stdio.h>
#include <math.h>

double f(double x) {
  return x - pow(2, -x);
}

double falsePosition(double (*f)(double), double a, double b, int it) {
  double r;

  for (int i = 0; i < it; i++) {
    r = (a * f(b) - b * f(a)) / (f(b) - f(a));
    if (f(a) * f(r) < 0)
      b = r;
    else
      a = r;
  }

  return r;
}

int main() {
  double a = -0.115;
  double b = 1.1141;

  int it[] = {1, 2, 3, 4, 5};
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", falsePosition(f, a, b, it[i]));
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("\n");
}