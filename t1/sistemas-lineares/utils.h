#ifndef UTILS_H
#define UTILS_H

void printM(int nRows, int nCols, double m[nRows][nCols]);

void printMFormatted(int nRows, int nCols, double m[nRows][nCols]);

void multiply(int nRows, int nCols, double m[nRows][nCols], int l, double k);

void swap(int nRows, int nCols, double m[nRows][nCols], int l1, int l2);

void multiplyAndSum(int nRows, int nCols, double m[nRows][nCols], int l1, int l2, double k);

void jacobi(int t, double m[t][t], double c[t], double est[t], int it[], size_t sizeIt);

void seidel(int t, double m[t][t], double c[t], double est[t], int it[], size_t sizeit);

#endif