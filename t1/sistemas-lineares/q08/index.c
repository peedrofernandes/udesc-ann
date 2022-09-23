#include <stdio.h>
#include "../utils.h"

#define r 3
#define c 3

int main() {
  // 8⋅L1+L2→L2, 6⋅L1+L3→L3  e  −37/46⋅L2+L3→L3
  double m[r][c] = {
    {1, 5, 3},
    {-8, 6, -6},
    {-6, 7, 2}
  };

  multiplyAndSum(r, c, m, 1, 2, 8);
  multiplyAndSum(r, c, m, 1, 3, 6);
  multiplyAndSum(r, c, m, 2, 3, (double)-37 / 46);

  printM(r, c, m);
}