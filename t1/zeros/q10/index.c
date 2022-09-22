#include <stdio.h>
#include <math.h>

double f(double x) {
  return pow(x, 2) - 3.8885 * x + 1.7925;
}

void solveEquation(double a, double b, double c) {
  double delta = pow(b, 2) - 4 * a * c;
  double x1 = (-b + sqrt(delta)) / 2 * a;
  double x2 = (-b - sqrt(delta)) / 2 * a;

  printf("Equation: %.6lfx² + %.6lfx + %.6lf\n", a, b, c);
  printf("Solutions: \n");
  printf("x1 = %.8lf\n", x1);
  printf("x2 = %.8lf\n", x2);
}

double bissection(double (*f)(double), double a, double b, double it, double value) {
  double m;

  if ((f(a) - value) * (f(b) - value) >= 0) {
    printf("Intervalo invalido!\n");
  } else {
    for (int i = 1; i <= it; i++) {

      m = (a + b) / 2;

    if ((f(a) - value) * (f(m) - value) < 0)
      b = m;
    else
      a = m;
    }
  }

  return m;
}

int main() {
  double a = 1.9506;
  double b = 5.2084;

  solveEquation(1, -3.8885, 1.7925);

  int it[] = {4, 7, 11, 12, 13, 17, 19, 20, 21, 22, 25, 26, 27, 28, 29, 30, 32, 36, 37, 38};

  printf("[");
  for (int count = 0; count < sizeof(it) / sizeof(int); count++) {
    printf("%.8lf", bissection(f, a, b, it[count], 0));

    if (count < sizeof(it) / sizeof(int) - 1)
      printf(",");
  }
  printf("]\n");
}