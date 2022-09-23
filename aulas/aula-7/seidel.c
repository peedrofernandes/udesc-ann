#include <stdio.h>

#define r 3
#define c 4

void seidel(double A[r][c], double est[r], int n) {
  for (int k = 0; k < n; k++) {

    for (int i = 0; i < r; i++) {
      double bi = A[i][c - 1];

      for (int j = 0; j < r; j++) {
        if (j != i)
          bi -= A[i][j] * est[j];
      }

      bi /= A[i][i];

      printf("x%d^(%d) = %.16lf\t", i + 1, k + 1, bi);

      est[i] = bi;
    }
    printf("\n");

  }
}

int main() {
  double A[r][c] = {
    {5, -2, 1, 13},
    {1, 6, 1, -3},
    {1, 2, -8, -8}
  }; // Matriz dos coeficientes extendida

  // double B[r] = {5, 6, 4};
  // // Matriz dos termos independentes

  double est[r] = {0, 0, 0};
  int n = 10;

  seidel(A, est, n);
}