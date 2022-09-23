#include <stdio.h>
#include "../utils.h"

#define g 9.81
#define v 6.35

#define m1 79.59
#define m2 64.35
#define m3 55.43

#define c1 9.68
#define c2 14.94
#define c3 18.61

// Variáveis do sistema linear
// 1: a
// 2: R
// 3: T

// m1*g - T - c1*v = m1*a
// m2*g + T - c2*v - R = m2*a
// m3*g + R - c3*v = m3*a
// --------------------------------
// m1*a + T = m1*g - c1*v
// m2*a + R - T = m2*g - c2*v
// m3*a - R = m3*g - c3*v

int main() {
  double m[3][4] = {
    {m1, 0, 1, m1 * g - c1 * v},
    {m2, 1, -1, m2 * g - c2 * v},
    {m3, -1, 0, m3 * g - c3 * v}
  };

  completeGauss(3, 4, m);
  printM(3, 4, m);
}
