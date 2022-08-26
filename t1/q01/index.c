#include <stdio.h>
#include <math.h>

double f(double x) {
  // return exp(x) - 2 * pow(x, 2) + x - 1.5;
  return exp(x) - 2 * x * x + x - 1.5;
}

double bissection(double (*f)(double), double a, double b, double it) {
  double m;
  if (f(a) * f(b) >= 0)
    printf("Voce nao pode usar este intervalo.\n");
  else {
    for (int i = 1; i <= it; i++) {
      m = (a + b) / 2;
      if (f(a) * f(m) < 0)
        b = m;
      else
        a = m;
    }
  }
    return m;
}

int main() {
  double a = 1.78303;
  double b = 2.48124;

  double b1 = bissection(f, a, b, 1);

  double b4 = bissection(f, a, b, 4);

  double b7 = bissection(f, a, b, 7);

  printf("%.12lf,%.12lf,%.12lf\n", b1, b4, b7);

  return 0;
}