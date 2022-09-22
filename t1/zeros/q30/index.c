#include <stdio.h>
#include <math.h>

// #define G 9.81
// #define M 69.21
// #define V 56.13
// #define T 9.58

// h -> x
// g -> y
// v -> z
// t -> w
// l -> t

double sech(double x) {
  return 1 / cosh(x);
}

#define y 9.81
#define z 11.93
#define w 8.03
#define t 5.56

// double f(double h) {
//   return sqrt(2 * g * h) * tanh(sqrt(2 * g * h) * t / (2 * l)) - v;
// }
double f(double x) {
  return sqrt(2 * y * x) * tanh((sqrt(2 * y * x) / (2 * t)) * w) - z;
}
// double df(double x) {
//   return (y * w * pow(sech(w * sqrt(y * x) / sqrt(2) * t),2)) / (2 * t) + (sqrt(y) * tanh((w * sqrt(y) * sqrt(x)) / (sqrt(2) * t))) / (sqrt(2) * sqrt(x));
// }
double df(double x) {
  return ((y * w * pow(sech((w * sqrt(y * x)) / (sqrt(2) * t)),2)) / (2 * t)) + (sqrt(y) * tanh((w * sqrt(y) * sqrt(x)) / (sqrt(2) * t))) / (sqrt(2) * sqrt(x));
}

// h -> x
// G -> y
// V -> z
// T -> w
// L -> t

// double df(double c) {
//   return (G * (exp((c * T) / M) * M - M - c * T)) / (exp((c * T) / M) * M * c);
// }

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

  a = 0.24;
  b = 18.21;
  bissection(f, a, b, itB, 4);

  printf(",");

  x0 = 0.47;
  newton(f, df, x0, itN, 3);

  printf(",");

  // x0 = 0.14;
  // x1 = 17.41;
  // secant(f, x0, x1, itS, 3);

  // printf(",");

  a = 0.19;
  b = 17.3;
  falsePosition(f, a, b, itF, 4);

  printf("\n");
}