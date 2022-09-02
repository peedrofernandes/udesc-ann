#include <stdio.h>

#define l 4
#define c 5

void jacobi(double E[l][c], double kick[l], int it) {
  for (int i = 0; i < it; i++) {
    double resp[l] = {};
    for (int j = 0; j < l; j++) {
      double bj = E[j][c - 1];
      double soma = 0;
      for (int k = 0; k < c; k++) {
        if (k != j) {
          E[j][k] * kick[k];
        }
      }
      double xj = (bj + soma) / E[j][j];
      temp[j] = xj;
      printf("")
    }
  }
}

int main() {
  double E[l][c] = {
    {4, 2, -1, 11},
    {1, -5, 1, -4},
    {1, 1, -6, 9}
  };

  double kick[c] = {0, 0, 0};
}