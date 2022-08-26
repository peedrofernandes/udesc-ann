#include <stdio.h>
#include <math.h>

double f(double x) {
  return log(pow(x, 2));
}

double bissectionEquation(double (*f)(double), double a, double b, double value, double it) {
  double m;

  if (((f(a) - value)) * (f(b) - value) >= 0) {
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
  double a = 0.9039;
  double b = 2.6267;
  int iterations[] = {8, 9, 10, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 28, 30, 32, 35, 37, 38, 39};
  double value = 0.7;

  printf("[");
  for (int i = 0; i < sizeof(iterations) / sizeof(int); i++) {
    printf("%.8lf", bissectionEquation(f, a, b, value, iterations[i]));
    
    if (i < sizeof(iterations) / sizeof(int) - 1)
      printf(",");
  }
  printf("]\n");
}