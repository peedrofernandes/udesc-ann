#include <stdio.h>
#include <math.h>

double g(double x) {
  return sqrt((x + 3) / (pow(x, 2) + 2));
}

void fixedPoint(double (*g)(double), double x0, int it[], size_t sizeIt) {
  printf("sizeIt = %ld\n", sizeIt);

  double fp;
  int currentIt = 0;

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    fp = g(x0);
    x0 = fp;

    if (it[currentIt] == i) {
      printf("%.8lf", fp);
      if (it[currentIt] != it[sizeIt - 1])
        printf(",");
      currentIt++;
    }
  }
  printf("\n");
}

int main() {
  double x0 = 0.40602;
  int it[] = {1, 2, 3, 4, 5, 6, 7, 8};
  size_t sizeIt = sizeof(it) / sizeof(int);

  fixedPoint(g, x0, it, sizeIt);
}