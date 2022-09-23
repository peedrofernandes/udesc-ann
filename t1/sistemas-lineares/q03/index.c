#include <stdio.h>
#include "../utils.h"

#define r 4
#define c 3

int main() {
  double m[r][c] = {
    {1.3333333333333333, 0.2, 1.25},
    {-1.6666666666666667, -0.5714285714285714, -1.2857142857142858},
    {-6.0, 2.6666666666666665, -0.7777777777777778},
    {0.4, 0.5, 1.5}
  };

  swap(r, c, m, 1, 3);
  swap(r, c, m, 1, 2);
  multiply(r, c, m, 4, (double)-2/3);
  multiplyAndSum(r, c, m, 3, 2, (double)-3 / 8);
  multiplyAndSum(r, c, m, 4, 3, (double)5 / 9);
  multiply(r, c, m, 3, (double)9 / 8);

  printMFormatted(r, c, m);
}