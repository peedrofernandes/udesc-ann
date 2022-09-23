#include <stdio.h>
#include "../utils.h"

#define r 3

int main() {
  double m[r][r] = {
    {7.29, -3.39, -2.19},
    {4.32, 7.38, -1.35},
    {-2.66, -1.27, -5.64}
  };
  double c[r] = {1.6, 3.9, 2.93};
  double est[r] = {-3.24, 4.8, -4.35};
  int it[] = {7, 8, 11, 12, 15, 17, 18, 19};
  size_t sizeIt = sizeof(it) / sizeof(int);

  seidel(r, m, c, est, it, sizeIt);
}