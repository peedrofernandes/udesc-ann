#include <stdio.h>
#include "./operations.h"

void timesK(int nRows, int nCols, double m[nRows][nCols], int l, double k) {
  if (nRows <= l) {
    printf("Operation not permitted - The number of lines must not be smaller than the line to be changed!\n");
    return;
  }

  for (int j = 0; j < nCols; j++)
    m[l][j] *= k;
}

void swap(int nRows, int nCols, double m[nRows][nCols], int l1, int l2) {
  l1--;
  l2--; 

  if (nRows < l1 || nRows < l2) {
    printf("Operation not permitted - The number of lines must not be smaller than the line to be changed!\n");
    return;
  }

  for (int j = 0; j < nCols; j++) {
    double aux = m[l1][j];
    m[l1][j] = m[l2][j];
    m[l2][j] = aux;
  }
}