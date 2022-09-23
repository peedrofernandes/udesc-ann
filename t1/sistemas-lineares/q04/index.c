#include <stdio.h>
#include "../utils.h"

#define t 3

int main() {
  double m[t][t] = {
    {-9.06, 4.37, 3.17},
    {-3.66, -8.21, -3.02},
    {-0.03, 2.38, -3.93}
  };
  double c[t] = {-2.38, -2.85, 0.21};
  double est[t] = {3.85, -0.57, -3.88};
  int it[] = {1, 5, 6, 7, 10, 12, 17, 19};
  int sizeIt = sizeof(it) / sizeof(int);

  jacobi(t, m, c, est, it, sizeIt);
}