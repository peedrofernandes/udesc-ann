#include <stdio.h>

void printM(int nRows, int nCols, double m[nRows][nCols]) {
  for (int i = 0; i < nRows; i++) {
    printf("[");
    for (int j = 0; j < nCols; j++) {
      double elem = m[i][j];
      if (elem >= 0)
        printf(" ");
      printf("%.8lf", elem);
      if (j != nCols - 1)
        printf(" ");
    }
    printf("]\n");
  }
}

void printMFormatted(int nRows, int nCols, double m[nRows][nCols]) {
  for (int i = 0; i < nRows; i++) {
    for (int j = 0; j < nCols; j++) {
      double elem = m[i][j];
      printf("%.8lf", elem);
      if (i != nRows - 1 || j != nCols - 1)
        printf(",");
    }
  }
  printf("\n");
}