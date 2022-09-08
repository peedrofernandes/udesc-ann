#include <stdio.h>
#include <math.h>

double g(double x) {
  return (3 * pow(x, 4) + 2 * pow(x, 2) + 3) / (4 * pow(x, 3) + 4 * x - 1);
}

void fixedPoint(double (*g)(double), double x0, int it[], size_t sizeIt) {
  double fp;

  int currentIt = 0;

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    fp = g(x0);
    x0 = fp;

    if (i == it[currentIt]) {
      printf("%.8lf", fp);
      currentIt++;
      if (i != it[sizeIt - 1])
        printf(",");
    }
  }
  printf("\n");
}

int main() {
  int it[] = {1, 2, 3, 4, 5, 6, 7, 8};
  size_t sizeIt = sizeof(it) / sizeof(int);
  double x0 = 1.44709;

  fixedPoint(g, x0, it, sizeIt);
}