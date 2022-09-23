#include <stdio.h>
#include "../utils.h"


#define m1 5.98
#define m2 3.02
#define m3 5.71
#define k1 55.51
#define k2 52.78
#define k3 68.39

#define g 9.81

int main() {
  double m[3][4] = {
    {k1+k2, -k2, 0, m1*g},
    {-k2, k2 + k3, -k3, m2 * g},
    {0, -k3, k3, m3 * g}
  };

  completeGauss(3, 4, m);
  printM(3, 4, m);
}