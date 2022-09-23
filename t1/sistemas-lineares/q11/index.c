#include <stdio.h>
#include "../utils.h"

#define k1 785
#define k2 818
#define k3 287
#define k4 214
#define k5 668
#define k6 630
#define k7 675
#define k8 753

double bissection(double (*f)(double), double a, double b, int qtdIt) {
  double r;

  for (int i = 1; i <= qtdIt; i++) {
    r = (a + b) / 2;

    if (f(a) * f(r) < 0)
      b = r;
    else
      a = r;
  }

  return r;
}

// Sistema linear
// x1 + k2 = x4 + k1
// x4 + k8 = x3 + k7
// x2 + k4 = x1 + k3
// x3 + k6 = x2 + k5
// -----------------
// x1 - x4 = k1 - k2
// x4 - x3 = k7 - k8
// x2 - x1 = k3 - k4
// x3 - x2 = k5 - k6

double x2(double x3) {
  return x3 + k6 - k5;
}
double x1(double x3) {
  return x2(x3) + k4 - k3;
}
double x4(double x3) {
  return x1(x3) + k2 - k1;
}

int main() {
  printf("x1(x3): %.8lf\n", bissection(x1, -10000, 10000, 100));
  printf("x2(x3): %.8lf\n", bissection(x2, -10000, 10000, 100));
  printf("x4(x3): %.8lf\n", bissection(x4, -10000, 10000, 100));
  // A bisseção determina o valor quando o fluxo é zero. Como procura-se o valor mínimo,
  // deve ser adicionado 1 a esse valor
}