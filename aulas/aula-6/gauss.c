#include <stdio.h>

#define numRows 4
#define numCols 5

void print_matrix(double m[numRows][numCols]) {
  for (int i = 0; i < numRows; i++) {
    for (int j = 0; j < numCols; j++) {
      printf("%.8lf\t", m[i][j]);
    }
    printf("\n");
  }
}

// apenas funciona para sistemas n x n
void gauss(double E[numRows][numCols]) {
  for (int j = 0; j < numCols - 1; j++) { 
    // percorrer todas as linhas da matriz
    for (int i = j; i < numRows; i++) { 
      // para cada linha, percorrer todas as colunas a partir da diagonal

      if (E[i][j] == 0)
        continue;
      // não faz nada se o elemento já for zero

      if (i != j) {
        // Se o elemento não pertence à diagonal
        for (int k = 0; k < numCols; k++) {
          // Trocar linhas
          double temp = E[i][k];
          E[i][k] = E[j][k];
          E[j][k] = temp;
        }
      }

      for (int k = 0; k < numRows; k++) {
        if (k == j)
          continue;

        double m = -E[k][j] / E[j][j];
        for (int p = j; p < numCols; p++)
          E[k][p] = m * E[j][p] + E[k][p];
        // Operação elementar com todos os elementos da linha
      } // zerar todos os elementos da coluna j que não estão na diagonal

      printf("\n");
      print_matrix(E);
      break;
    }
  }

  // soluções do sistema
  printf("\n");
  for (int i = 0; i < numRows; i++) {
    double xi = E[i][numCols - 1] / E[i][i];
    printf("x_%d = %.16lf\t", i + 1, xi);
  }
}

int main() {
  double E[numRows][numCols] = {
    {2, 4, 6, 2, 4},
    {1, 2, -1, 3, 8},
    {-3, 1, -2, 1, -2},
    {1, 3, -3, -2, 6}
  }; // solução exata: 2, 1, -1, 1

  print_matrix(E);
  gauss(E);
}