#include <stdio.h>
#include "../operations.h"
#include "../handleMatrix.h"

#define R 3
#define C 3

int main() {
  // matriz = [[-0.14285714285714285, 0.5, 0.2857142857142857], [-1.0, -0.2222222222222222, 1.3333333333333333], [0.7777777777777778, -0.6, 0.6]]
  double m[R][C] = {
      {-0.14285714285714285, 0.5, 0.2857142857142857},
      {-1.0, -0.2222222222222222, 1.3333333333333333},
      {0.7777777777777778, -0.6, 0.6}};

  printM(R, C, m);
  printf("\n");

  timesK(R, C, m, 2 - 1, 5);

  printM(R, C, m);
  printf("\n");

  swap(R, C, m, 1, 2);

  printM(R, C, m);
  printf("\n");

  printMFormatted(R, C, m);
}
