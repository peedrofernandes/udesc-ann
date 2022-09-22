#include <stdio.h>
#include <math.h>

double f(double x) {
  return M_PI * x - exp(x);
}

double falsePosition(double (*f)(double), double a, double b, int it) {
  double r;

  for (int i = 0; i < it; i++) {
    r = (a * f(b) - b * f(a)) / (f(b) - f(a));
    if (f(a) * f(r) < 0)
      b = r;
    else
      a = r;
  }

  return r;
}

int main() {
  double a = 0.339;
  double b = 1.0476;

  int it[] = {2, 4, 5, 6, 10, 11, 14, 15, 17, 18};
  size_t sizeIt = sizeof(it) / sizeof(int);

  for (int i = 0; i < sizeIt; i++) {
    printf("%.8lf", falsePosition(f, a, b, it[i]));
    if (i != sizeIt - 1)
      printf(",");
  }
  printf("\n");
}