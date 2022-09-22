#include <stdio.h>

#define r 3

void jacobi(double A[r][r], double B[r], double est[r], int n) {
  double next[r];

  for (int k = 0; k < n; k++) {
    // Para cada iteração
    for (int i = 0; i < r; i++) {
      // Para cada linha
      double bi = B[i];
      for (int j = 0; j < r; j++) {
        // Para cada coluna
        if (j != i)
          bi -= A[i][j] * est[j];
      }
      bi /= A[i][i];

      printf("x%d^(%d) = %.16lf\t", i + 1, k + 1, bi);

      next[i] = bi;
    }
    printf("\n");

    for (int i = 0; i < r; i++)
      est[i] = next[i];
    // atualizar a estimativa
  }
}

int main() {
  double A[r][r] = {
    {4, 1, -1},
    {-1, 3, 1},
    {1, -1, 5}
  }; // Matriz dos coeficientes

  double B[r] = {5, 6, 4};
  // Matriz dos termos independentes

  double est[r] = {0, 0, 0};
  int n = 10;

  jacobi(A, B, est, n);
}