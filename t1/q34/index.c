#include <stdio.h>
#include <math.h>

#define r1 2.35
#define r2 7.75
#define H 3.91
#define pt 252.55
#define pw 1000

double f(double h) {
  double Ht = (H * r2) / (r2 - r1);
  double rx = (r2 * (Ht + h - H)) / Ht;
  double V = (((M_PI * H) / 3)) * (pow(r1, 2) + pow(r2, 2) + r1 * r2);
  double Vw = (((M_PI * (H - h)) / 3) * (pow(rx, 2) + pow(r2, 2) + rx * r2));

  return pw * Vw - pt * V;
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
  b = 3.91;
  int it1[] = {2, 4, 8, 12};
  bissection(f, a, b, it1, sizeof(it1) / sizeof(int));

  printf(",");

  x0 = 0.1;
  x1 = 3.52;
  int it2[] = {1, 2, 5};
  secant(f, x0, x1, it2, sizeof(it2) / sizeof(int));

  printf(",");

  a = 0;
  b = 3.91;
  int it3[] = {2, 4, 7, 11};
  falsePosition(f, a, b, it3, sizeof(it3) / sizeof(int));

  printf("\n");
}
