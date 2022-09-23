#include <stdio.h>
#include "../utils.h"

#define r 3
#define c 3

int main() {
  // [
  //   [0.14285714285714285, -1.5, 1.125], 
  //   [-0.4, -3.0, 1.2857142857142858], 
  //   [1.2, 4.0, 0.8571428571428571]
  //   ]
  double m[r][c] = {
    {0.14285714285714285, -1.5, 1.125},
    {-0.4, -3.0, 1.2857142857142858},
    {1.2, 4.0, 0.8571428571428571}
  };

  multiplyAndSum(r, c, m, 1, 2, (double)1 / 2);
  multiply(r, c, m, 3, (double)4 / 5);
  swap(r, c, m, 2, 3);
  swap(r, c, m, 1, 3);

  printMFormatted(r, c, m);
}