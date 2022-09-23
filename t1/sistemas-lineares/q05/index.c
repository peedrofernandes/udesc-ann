#include <stdio.h>
#include "../utils.h"

#define t 4

int main() {
  double m[t][t] = {
    {-9.44, 1.05, 4.03, 2.67},
    {3.87, -8.41, 0.12, 2.74},
    {-3.76, -2.74, -11.01, -2.82},
    {-4.62, 0.18, -3.54, 10.03}
  };
  double c[t] = {3.4, 2.71, -2.29, 3.72};
  double est[t] = {2.96, -4.27, 0.83, -1.33};
  int it[] = {2, 10, 11, 12, 13, 15, 17, 19, 20, 22, 24, 26};
  size_t sizeIt = sizeof(it) / sizeof(int);

  jacobi(t, m, c, est, it, sizeIt);
}