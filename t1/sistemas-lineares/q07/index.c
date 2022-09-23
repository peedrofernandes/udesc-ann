#include <stdio.h>
#include "../utils.h"

#define t 4

int main() {
  double m[t][t] = {
    {-8.44, 4.28, -0.29, 2.35},
    {-3.27, -12.01, 3.63, -3.57},
    {-0.59, -2.6, 5.61, -0.9},
    {0.19, -3.69, 4.43, -9.84}
  };
  double c[t] = {-3.07, -0.45, -1.98, -3.59};
  double est[t] = {1.7, -4.99, 1.23, -4.42};
  int it[] = {1, 3, 4, 5, 6, 7, 11, 12, 16, 17, 23, 25};
  size_t sizeIt = sizeof(it) / sizeof(int);

  seidel(t, m, c, est, it, sizeIt);
}