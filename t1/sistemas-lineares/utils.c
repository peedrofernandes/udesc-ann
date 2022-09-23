#include <stdio.h>

void printM(int nRows, int nCols, double m[nRows][nCols]) {
  for (int i = 0; i < nRows; i++) {
    printf("[");
    for (int j = 0; j < nCols; j++) {
      double elem = m[i][j];
      if ((int)elem >= 0)
        printf(" ");
      printf("%.8lf", elem);
      if (j != nCols - 1)
        printf(" ");
    }
    printf("]\n");
  }
  printf("\n");
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
  printf("\n\n");
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


void gauss(int nRows, int nCols, double m[nRows][nCols]) {
  for (int j = 0; j < nCols; j++) {

    for (int i = j; i < nRows; i++) {
      if (m[i][j] == 0)
        continue;

      if (i != j)
        swap(nRows, nCols, m, i+1, j+1);

      for (int k = j + 1; k < nRows; k++) {
        double v = -m[k][j] / m[j][j];
        multiplyAndSum(nRows, nCols, m, j+1, k+1, v);
      }
    }

  }
}

void completeGauss(int nRows, int nCols, double m[nRows][nCols]) {
  for (int j = 0; j < nCols; j++) {

    for (int i = j; i < nRows; i++) {
      if (m[i][j] == 0)
        continue;

      if (i != j)
        swap(nRows, nCols, m, i+1, j+1);

      for (int k = 0; k < nRows; k++) {
        if (k == j)
          continue;
          
        double v = -m[k][j] / m[j][j];
        multiplyAndSum(nRows, nCols, m, j+1, k+1, v);
      }

      multiply(nRows, nCols, m, j+1, 1.0 / m[j][j]);
    }
  }
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


void seidel(int t, double m[t][t], double c[t], double est[t], int it[], size_t sizeIt) {
  int currentIt = 0;

  for (int k = 1; k <= it[sizeIt - 1]; k++) {
    double si[t];

    for (int i = 0; i < t; i++) {
      si[i] = c[i];

      for (int j = 0; j < t; j++) {
        if (i != j)
          si[i] -= m[i][j] * est[j];
      }

      si[i] /= m[i][i];
      est[i] = si[i];
    }

    if (it[currentIt] == k) {
      for (int i = 0; i < t; i++) {
        printf("%.8lf", si[i]);
        if (currentIt != sizeIt - 1 || i != t - 1)
          printf(",");
      }
      currentIt++;
    }
  }
  printf("\n");
}