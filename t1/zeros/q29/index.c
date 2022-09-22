#include <stdio.h>
#include <math.h>

#define G 9.81
#define M 69.21
#define V 56.13
#define T 9.58

// double f(double m) {
//   return ((G * m) / C) * (1 - exp(-pow((C / m), T))) - V;
// }
double f(double c) {
  return ((G * M) / c) * (1 - exp(- (c / M) * T)) - V;
}
// M -> x
// G -> y
// c -> z
// V -> w
// T -> t

// double df(double c) {
//   return (G * (exp((c * T) / M) * M - M - c * T)) / (exp((c * T) / M) * M * c);
// }
double df(double c) {
  return (G * (exp(- ((c * T) / M)) * c * T - M * (-exp(- ((c * T) / M)) + 1))) / pow(c, 2);
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
  // B = Bissection
  // N = Newton
  // S = Secant
  // F = False Position

  double a, b, x0, x1;
  int itB[] = {2, 4, 8, 12};
  int itN[] = {1, 3, 5};
  int itS[] = {1, 2, 5};
  int itF[] = {2, 4, 7, 11};

  a = 0.34;
  b = 56.4;
  bissection(f, a, b, itB, 4);

  printf(",");

  x0 = 0.78;
  newton(f, df, x0, itN, 3);

  printf(",");

  x0 = 0.39;
  x1 = 11.12;
  secant(f, x0, x1, itS, 3);

  printf(",");

  a = 1.18;
  b = 57.42;
  falsePosition(f, a, b, itF, 4);

  printf("\n");
}