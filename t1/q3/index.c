#include <stdio.h>
#include <math.h>

double f(double x) {
  return pow(x, 4) - 2 * pow(x, 3) - 3 * pow(x, 2) + 3 * x + 2;
}

double bissection(double (*f)(double), double a, double b, int it) {
  double fa, fb, m, fm;

  if (f(a) * f(b) >= 0)
    printf("Intervalo invalido!");
  else {
    for (int i = 1; i <= it; i++) {
      m = (a + b) / 2;
      fa = f(a);
      fb = f(b);
      fm = f(m);
      if (fa * fm < 0)
        b = m;
      else if (fb * fm < 0)
        a = m;
    }
  }

  return m;
}

int main() {
  int iterations[] = {4, 11, 17, 22, 27, 29, 32, 36, 37, 39};

  double a = -1.64235;
  double b = 1.90171;

  for (int i = 0; i <= 9; i++) {
    printf("%.8lf,", bissection(f, a, b, iterations[i]));
  }
  printf("\n");

  return 0;
}