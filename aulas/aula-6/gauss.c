#include <stdio.h>

#define l 4
#define c 5

void gauss(double E[l][c]) {
  for (int j = 0; j < c - 2; j++) {
    for (int i = j; i < l; i++) {
      if (E[i][j] != 0) {
        if (i != j) {
          // Troca as linhas i e j
          for (int k = 0; k < c; k++) {
            double temp[c] = {};
            temp[k] = E[i][k];
            E[i][k] = E[j][k];
            E[j][k] = *temp;
          }
        }
        // Zerar todos os elementos da coluna j abaixo do elemento na posição j, j
        for (int k = j; k < c; k++) {
          double m = -E[k][j] / E[j][j];
          for (int p = j; p < c; p++)
            E[k][p] = m * E[j][p] + E[k][p];
        }
        break;
      }
    }
  }
}

void printMatrix(double m[l][c]) {
  for (int i = 0; i < l; i++) {
    for (int j = 0; j < c; j++)
      printf("%.2lf", m[i][j]);
  }
}

int main() {
  double E[l][c] = {
    { 2,  4,  6,  2,  4},
    { 1,  2, -1,  3,  8},
    {-3,  1, -2,  1, -2},
    { 1,  3, -3, -2,  4}
  };

  
}