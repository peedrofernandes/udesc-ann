#include <stdio.h>
#include "../utils.h"

// 4382, 4666 e 4752

// 	Areia %	Cascalho fino %	Cascalho grosso %
// Mina 1	58	19	23
// Mina 2	31	51	18
// Mina 3	15	27	58

#define a11 0.58
#define a12 0.31
#define a13 0.15
#define a21 0.19
#define a22 0.51
#define a23 0.27
#define a31 0.23
#define a32 0.18
#define a33 0.58

#define b1 4382
#define b2 4666
#define b3 4752

int main() {
  // double m[3][4] = {
  //   {0.58,0.31,0.15,4382},
  //   {0.19,0.51,0.27,4666},
  //   {0.23,0.18,0.58,4752}
  // };
  double m[3][4] = {
    {a11, a12, a13, b1},
    {a21, a22, a23, b2},
    {a31, a32, a33, b3}
  };
  completeGauss(3, 4, m);
  printM(3, 4, m);
}