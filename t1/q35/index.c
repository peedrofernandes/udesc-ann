#include <stdio.h>
#include <math.h>

#define L 7.3
#define r1 2.13
#define V 4.21

double f(double h) {
  return L * (0.5 * M_PI * pow(r1, 2) - pow(r1, 2) * asin(h / r1) - h * sqrt(pow(r1, 2) - pow(h, 2))) - V;
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
  b = 2.13;
  int it1[] = {2, 4, 8, 12};
  bissection(f, a, b, it1, sizeof(it1) / sizeof(int));

  printf(",");

  x0 = 0.43;
  x1 = 2.13;
  int it2[] = {1, 2, 5};
  secant(f, x0, x1, it2, sizeof(it2) / sizeof(int));

  printf(",");

  a = 0;
  b = 2.13;
  int it3[] = {2, 4, 7, 11};
  falsePosition(f, a, b, it3, sizeof(it3) / sizeof(int));

  printf("\n");
}