#include <stdio.h>
#include <math.h>

// h -> x;
// pw -> y;
// r -> z;
// ps -> w;

#define y 1000
#define z 3.98
#define w 348.94

double f(double x) {
  return 4 * pow(z, 3) * (y - w) + y * pow(x, 2) * (x - 3 * z);
}
double df(double x) {
  return y * (3 * pow(x, 2) - 6 * z * x);
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

    if (i == it[currentIt]) {
      printf("%.8lf", r);
      currentIt++;
      if (i != it[sizeIt - 1])
        printf(",");
    }
  }
}

void newton(double (*f)(double), double (*df)(double), double x0, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    r = x0 - f(x0) / df(x0);
    x0 = r;
    if (i == it[currentIt]) {
      printf("%.8lf", r);
      currentIt++;
      if (i != it[sizeIt - 1])
        printf(",");
    }
  }
}

void secant(double (*f)(double), double x0, double x1, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    r = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0));
    x0 = x1;
    x1 = r;
    if (i == it[currentIt]) {
      printf("%.8lf", r);
      currentIt++;
      if (i != it[sizeIt - 1])
        printf(",");
    }
  }
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
}

int main() {
  double a, b, x0, x1;

  a = 0;
  b = 7.96;
  int it1[] = {2, 4, 8, 12};
  bissection(f, a, b, it1, sizeof(it1) / sizeof(int));

  printf(",");

  x0 = 4.91;
  int it2[] = {1, 3, 5};
  newton(f, df, x0, it2, sizeof(it2) / sizeof(int));

  printf(",");

  x0 = 1.74 ;
  x1 = 6.11;
  int it3[] = {1, 2, 5};
  secant(f, x0, x1, it3, sizeof(it3) / sizeof(int));

  printf(",");

  a = 0;
  b = 7.96;
  int it4[] = {2, 4, 7, 9};
  falsePosition(f, a, b, it4, sizeof(it4) / sizeof(int));

  printf("\n");
}