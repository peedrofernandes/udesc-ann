#include <stdio.h>
#include <math.h>

#define G 9.81
#define C 28.95
#define V 38.53
#define T 8.3

// double f(double m) {
//   return ((G * m) / C) * (1 - exp(-pow((C / m), T))) - V;
// }
double f(double m) {
  return ((G * m) / C) * (1 - exp(- (C / m) * T)) - V;
}
// m -> x
// G -> y
// C -> z
// V -> w
// T -> t
// double df(double m) {
//   return (G * (1 - 1 / (M_E * (pow(C, T) / pow(m, T)) - (M_E * -(pow(C, T) / pow(m, T)) * T * pow(C, T)) / pow(m, T)))) / C;
// }
double df(double m) {
  return (G * (exp((C * T) / m) * m - m - C * T)) / (exp((C * T) / m) * m * C);
}

void bissection(double (*f)(double), double a, double b, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  printf("\n\nBissection\n\n");

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
  printf("\n");
}

void newton(double (*f)(double), double (*df)(double), double x0, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  printf("\n\nNewton\n\n");

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
  printf("\n");
}

void secant(double (*f)(double), double x0, double x1, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  printf("\n\nSecant\n\n");

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
  printf("\n");
}

void falsePosition(double (*f)(double), double a, double b, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  printf("\n\nFalse position\n\n");

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
  // B = Bissection
  // N = Newton
  // S = Secant
  // F = False Position

  double a, b, x0, x1;
  int itB[] = {2, 4, 8, 12};
  int itN[] = {1, 3, 5};
  int itS[] = {1, 2, 5};
  int itF[] = {2, 4, 7, 11};

  a = 20.34;
  b = 192.58;
  bissection(f, a, b, itB, 4);

  x0 = 21.11;
  newton(f, df, x0, itN, 3);

  x0 = 24.43;
  x1 = 34.42;
  secant(f, x0, x1, itS, 3);

  a = 31.11;
  b = 202.31;
  falsePosition(f, a, b, itF, 4);
}