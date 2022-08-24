#include <stdio.h>

double f(double x) {
  return x * x - 3;
}

double bissection(double (*f)(double), double a, double b, int it) {
  double m, fa, fb, fm;
  fa = f(a);
  fb = f(b);

  if (fa * fb >= 0)
    printf("Intervalo invalido!");
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
  int iterations[] = { 2, 4, 5, 6, 11, 12, 13, 16, 21, 22, 23, 24, 28, 29, 31, 33, 35, 36, 37, 38 };
  double a = 0.64385;
  double b = 2.15145;

  for (int i = 0; i < sizeof(iterations) / sizeof(int); i++) {
    printf("%.12lf", bissection(f, a, b, iterations[i]));
    i == sizeof(iterations) / sizeof(int) - 1 ? printf("\n") : printf(",");
  }

  return 0;
}