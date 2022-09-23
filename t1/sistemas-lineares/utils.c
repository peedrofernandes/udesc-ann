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


void multiply(int nRows, int nCols, double m[nRows][nCols], int l, double k) {
  l--;

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


void multiplyAndSum(int nRows, int nCols, double m[nRows][nCols], int l1, int l2, double k) {
  l1--;
  l2--; 

  if (nRows < l1 || nRows < l2) {
    printf("Operation not permitted - The number of lines must not be smaller than the line to be changed!\n");
    return;
  }

  for (int j = 0; j < nCols; j++)
    m[l2][j] += k * m[l1][j];
}


void jacobi(int t, double m[t][t], double c[t], double est[t], int it[], size_t sizeIt) {
  int currentIt = 0;

  for (int k = 1; k <= it[sizeIt - 1]; k++) {
    double si[t];
    double next[t];

    for (int i = 0; i < t; i++) {
      si[i] = c[i];

      for (int j = 0; j < t; j++) {
        if (i != j)
          si[i] -= m[i][j] * est[j];
      }

      si[i] /= m[i][i];

      next[i] = si[i];
    }

    if (it[currentIt] == k) {
      for (int i = 0; i < t; i++) {
        printf("%.8lf", si[i]);
        if (currentIt != sizeIt - 1 || i != t - 1)
          printf(",");
      }
      currentIt++;
    }

    for (int i = 0; i < t; i++)
      est[i] = next[i];
  }
  printf("\n");
}