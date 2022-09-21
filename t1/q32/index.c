#include <stdio.h>
#include <math.h>

// R -> x
// V -> y
// h -> z

#define x 3.47
#define y 82.28

double f(double z) {
  return M_PI * pow(z, 2) * (3 * x - z) / 3 - y;
}

double df(double z) {
  return M_PI * z * (2 * x - z);
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
  double a, b, z0, z1;

  a = 0;
  b = 6.94;
  int it1[] = {2, 4, 8, 12};
  bissection(f, a, b, it1, sizeof(it1) / sizeof(int));

  printf(",");

  z0 = 1.77;
  int it2[] = {1, 3, 5};
  newton(f, df, z0, it2, sizeof(it2) / sizeof(int));

  printf(",");

  z0 = 0.21;
  z1 = 5.55;
  int it3[] = {1, 2, 5};
  secant(f, z0, z1, it3, sizeof(it3) / sizeof(int));

  printf(",");

  a = 0;
  b = 6.94;
  int it4[] = {2, 5, 7, 11};
  falsePosition(f, a, b, it4, sizeof(it4) / sizeof(int));
}