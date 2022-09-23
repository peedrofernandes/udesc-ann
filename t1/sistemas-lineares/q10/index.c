#include <stdio.h>
#include "../utils.h"

#define k1 86
#define k2 50
#define k3 31
#define k4 67
#define k5 21

// Sistema linear
// (A) x1 + x2 = k1
// (B) x2 + x3 = k2
// (C) x3 + k5 = k3
// (D) x1 + k5 = k4

// Sistema linear formatado
// [1 1 0 k1]
// [0 1 1 k2]
// [0 0 1 k3-k5]
// [1 0 0 k4-k5]

int main() {
  double x1 = k4 - k5; // 4ª linha
  double x3 = k3 - k5; // 3ª linha
  double x2 = k2 - x3; // 2ª linha

  if (x1 + x2 == k1) // Verificação da primeira equação
    printf("SPD\n");
  else {
    printf("SI\n");
    return 0;
  }

  printf("%.8lf,%.8lf,%.8lf\n", x1, x2, x3);

  return 0;
}