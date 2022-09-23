#include <stdio.h>
#include <math.h>
#include "../utils.h"

#define F 2403

double toRad(double deg) {
  return deg * M_PI / 180.0;
}

#define a toRad(45) // alfa (rad)
#define b toRad(20) // beta (rad)

// 1) a soma de todas as forças horizontais agindo em cada nó é zero;
// 2) a soma de todas as forças verticais agindo em cada nó é zero.
// Fi,h = Soma das componentes horizontais das forças externas



// Cada um dos 3 nós dará duas equações do sistema linear

// 1.
// (vert) -F - F1sen(a) - f3sen(b) = 0
// (hor) -F1cos(a) + F3cos(b) = 0
// 2.
// (vert) V2 + F1sen(a) = 0
// (hor) H2 + F2 + F1cos(a) = 0
// 3.
// (vert) V3 + F3sen(b) = 0
// (hor) -F2 -F3cos(b) = 0

int main() {
  // // Variáveis do sistema linear:
  // F1,F2,F3,H2,V2,V3
  double m[6][7] = {
      {-sin(a), 0, -sin(b), 0, 0, 0, F},
      {-cos(a), 0, cos(b), 0, 0, 0, 0},
      {sin(a), 0, 0, 0, 1, 0, 0},
      {cos(a), 1, 0, 1, 0, 0, 0},
      {0, 0, sin(b), 0, 0, 1, 0},
      {0, -1, -cos(b), 0, 0, 0, 0}};
  completeGauss(6, 7, m);
  printM(6, 7, m);
}