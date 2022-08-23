#include <stdio.h>
#include <math.h>

double f(double x) {
  return sqrt(x) - cos(x);
}

double bissection(double (*f)(double), double a, double b, double it) {
  if (f(a) * f(b) >= 0) {
    printf("Intervalo escolhido nao contem raiz!\n");
  } else {
    double m;

    for (int i = 1; i <= it; i++) {
      m = (a + b) / 2;

      if (f(a) * f(m) < 0)
        b = m;
      else
        a = m;
    }

    return m;
  }
}

int main() {
  double a = 0.24512;
  double b = 1.28808;

  double b4 = bissection(f, a, b, 4);
  double b8 = bissection(f, a, b, 8);
  double b11 = bissection(f, a, b, 11);
  double b15 = bissection(f, a, b, 15);
  double b18 = bissection(f, a, b, 18);

  printf("Resultado das iteracoes [4, 8, 11, 15, 18]:\n");

  printf("%.8lf,%.8lf,%.8lf,%.8lf,%.8lf\n", b4, b8, b11, b15, b18);
}