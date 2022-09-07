#include <stdio.h>
#include <math.h>

double g(double x) {
  return (x / 2) + (1 / x);
}

double fixedPoint(double (*g)(double), double x0, double it) {
  double x1;

  for (int i = 1; i <= it; i++) {
    x1 = g(x0);
    x0 = x1;
  }

  return x1;
}

int main() {
  double x0 = 1.1269;
  int it[] = {1, 2, 3, 4, 5, 6, 7, 8};
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", fixedPoint(g, x0, it[i]));
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("\n");
}