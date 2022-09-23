#include <stdio.h>
#include "../utils.h"

#define k1 356
#define k2 628
#define k3 1047
#define k4 306
#define k5 358
#define k6 327

#define k7 342

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
// k4 + k5 = x2 + x3
// x3 + k7 = x + k6
// k1 + k2 = x1 + k7
// x1 + x2 = k3
// --------------------
// x2 + x3 = k4 + k5
// x3 - x = k6 - k7
// x1 = k1 + k2 - k7
// x1 + x2 = k3
int main() {
  double m[4][5] = {
    {0, 0, 1, 1, k4 + k5},
    {-1, 0, 0, 1, k6 - k7},
    {0, 1, 0, 0, k1 + k2 - k7},
    {0, 1, 1, 0, k3}
  };

  completeGauss(4, 5, m);
  printM(4, 5, m);
}