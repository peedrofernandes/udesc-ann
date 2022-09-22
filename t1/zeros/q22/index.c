#include <stdio.h>
#include <math.h>

double f(double x) {
  return exp(5 * x) - 2;
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
  double a = -0.9449417;
  double b = 1.9356486;
  int it[] = {1, 25, 50, 100, 200, 400, 800, 1600, 3200, 4800, 6400, 8000, 10000};
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", falsePosition(f, a, b, it[i]));
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("\n");
}