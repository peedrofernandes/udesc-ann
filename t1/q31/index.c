#include <stdio.h>
#include <math.h>

// Q -> x
// y -> y
// g -> z
// B -> w
// Ac -> t

#define x 72.79
#define z 9.81

double f(double y) {
  double w = 4 + y;
  double t = 4 * y + pow(y, 2) / 2;

  return 1 - (pow(x, 2) / (z * pow(t, 3))) * w;
}

void bissection(double (*f)(double), double a, double b, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    r = (a + b) / 2;

    if (f(a) * f(r) < 0)
      b = r;
    else
      a = r;

    if (it[currentIt] == i) {
      printf("%.8lf", r);
      currentIt++;
      if (i != it[sizeIt - 1])
        printf(",");
    }
  }
  printf("\n");
}

void falsePosition(double (*f)(double), double a, double b, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    r = (a * f(b) - b * f(a)) / (f(b) - f(a));

    if (f(a) * f(r) < 0)
      b = r;
    else
      a = r;

    if (i == it[currentIt]) {
      printf("%.8lf", r);
      currentIt++;
      if (i != it[sizeIt - 1])
        printf(",");
    }
  }
  printf("\n");
}

int main() {
  double a, b;

  a = 0.25;
  b = 8.4;
  int it1[] = {2, 4, 8, 12};

  bissection(f, a, b, it1, sizeof(it1) / sizeof(int));

  a = 0.12;
  b = 9.8;
  int it2[] = {2, 4, 7, 11};

  falsePosition(f, a, b, it2, sizeof(it2) / sizeof(int));
}