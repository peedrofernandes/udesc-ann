#include <stdio.h>
#include <math.h>

double g(double x) {
  return (pow(x, 2) - 1) / 3;
}

void fixedPoint(double (*g)(double), double x0, int it[], size_t sizeIt) {
  printf("x0 = %.8lf\n", x0);
  printf("sizeIt = %ld\n", sizeIt);
  printf("it[sizeIt - 1] = %d\n\n", it[sizeIt - 1]);

  printf("Iterations recognized: \n[");
  for (int i = 0; i < sizeIt; i++) {
    printf("%d", it[i]);
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("]\n\n");

  double pf, initialx0 = x0;
  int currentIt = 0;

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    pf = g(x0);

    if (i == it[currentIt]) {
      printf("x%d = %.8lf\n", it[currentIt], pf);
      currentIt++;
    }

    x0 = pf;
  }

  printf("\n\nCSV\n\n");
  currentIt = 0, x0 = initialx0;

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    pf = g(x0);

    if (i == it[currentIt]) {
      printf("%.8lf", pf);
      if (i != it[sizeIt - 1])
        printf(",");
      currentIt++;
    }

    x0 = pf;
  }
  printf("\n\n");
}

int main() {
  int it[] = {1, 2, 3, 4, 5, 6, 7, 8};
  size_t sizeIt = sizeof(it) / sizeof(int);
  double x0 = -0.27087;

  fixedPoint(g, x0, it, sizeIt);

  return 0;
}