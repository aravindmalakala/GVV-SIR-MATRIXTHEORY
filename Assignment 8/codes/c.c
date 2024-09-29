#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"  // Include your matrix function library
#include "libs/geofun.h"
// Function to find the values of a based on the quadratic equation
double **findValuesOfA() {
    // Coefficients for the quadratic equation a^2 - 8a + 15 = 0
    double A = 1;  // Coefficient of a^2
    double B = -8; // Coefficient of a
    double C = 15; // Constant term

    // Call your Matquad function to find roots
    double **roots = Matquad(A, B, C);

    return roots; // Return the matrix containing the roots
}

int main() {
    // Find the values of a
    double **roots = findValuesOfA();

    // Output the results
    FILE *file;
    file = fopen("values.tex", "w");  // Updated file name
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file,"a1: %.2f\n", roots[0][0]);
    fprintf(file,"a1: %.2f\n", roots[1][0]);

    // Free allocated memory
    freeMat(roots, 2);

    return 0;
}

