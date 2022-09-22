#include <stdio.h>
#include <math.h>

#define P0 1143646
#define P 2122774
#define T 1
#define V 116298

double f(double lam) {
  return P0 * exp(lam * T) + (V / lam) * (exp(lam * T) - 1) - P;
}
// lam -> x;
// P -> y;
// P0 -> z;
// T -> w;
// V -> t;
// double df(double lam) {
//   return exp(lam * T) * P0 * T + (V * (exp(lam * T) * lam * T - exp(lam * T))) / pow(lam, 2);
// }
double df(double lam) {
  return exp(lam * T) * P0 * T + (V * ((exp(lam * T) * lam * T) + 1 - exp(lam * T))) / pow(lam, 2);
}

void bissection(double (*f)(double), double a, double b, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  printf("Bissection\n\n");

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
  printf("\n\n");
}

void newton(double (*f)(double), double (*df)(double), double x0, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  printf("Newton\n\n");

  for (int i = 1; i <= it[sizeIt - 1]; i++) {
    r = x0 - (f(x0) / df(x0));
    x0 = r;
    if (i == it[currentIt]) {
      printf("%.8lf", r);
      currentIt++;
      if (i != it[sizeIt - 1])
        printf(",");
    }
  }
  printf("\n\n");
}

void secant(double (*f)(double), double x0, double x1, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  printf("Secant\n\n");

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
  printf("\n\n");
}

void falsePosition(double (*f)(double), double a, double b, int it[], size_t sizeIt) {
  double r;
  int currentIt = 0;

  printf("False Position\n\n");

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
  printf("\n\n");
}

int main() {
  int itBissection[] = {2, 4, 8, 12};
  size_t sizeItBissection = sizeof(itBissection) / sizeof(int);
  double aBissection = 0.1;
  double bBissection = 1.52;

  int itNewton[] = {1, 3, 5};
  size_t sizeItNewton = sizeof(itNewton) / sizeof(int);
  double x0Newton = 0.4;

  int itSecant[] = {1, 2, 5};
  size_t sizeItSecant = sizeof(itSecant) / sizeof(int);
  double x0Secant = 0.1;
  double x1Secant = 1.91;

  int itFalsePosition[] = {2, 4, 7, 11};
  size_t sizeItFalsePosition = sizeof(itFalsePosition) / sizeof(int);
  double aFalsePosition = 0.1;
  double bFalsePosition = 1.77;

  bissection(f, aBissection, bBissection, itBissection, sizeItBissection);
  newton(f, df, x0Newton, itNewton, sizeItNewton);
  secant(f, x0Secant, x1Secant, itSecant, sizeItSecant);
  falsePosition(f, aFalsePosition, bFalsePosition, itFalsePosition, sizeItFalsePosition);
}