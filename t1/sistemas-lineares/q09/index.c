#include <stdio.h>
#include "../utils.h"

#define r 4
#define c 4

int main() {
  // 2⋅L1+L2→L2
  // -1⋅L1+L3→L3
  // 1/2⋅L1+L4→L4
  // 13/4⋅L2+L3→L3
  // -21/8⋅L2+L4→L4
  // 53/82⋅L3+L4→L4

  double m[r][c] = {
    {2, 5, -7, -4},
    {-4, -6, 8, -7},
    {2, -8, -8, -2},
    {-1, 8, 1, 6}
  };

  multiplyAndSum(r, c, m, 1, 2, 2);
  multiplyAndSum(r, c, m, 1, 3, -1);
  multiplyAndSum(r, c, m, 1, 4, (double)1 / 2);
  multiplyAndSum(r, c, m, 2, 3, (double)13 / 4);
  multiplyAndSum(r, c, m, 2, 4, (double)-21 / 8);
  multiplyAndSum(r, c, m, 3, 4, (double)53 / 82);

  printM(r, c, m);
}