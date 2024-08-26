#include <stdio.h>

// Function to compute the inverse of a 2x2 matrix
void inverse2x2(double A[2][2], double A_inv[2][2]) {
    double determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0];
    if (determinant == 0) {
        printf("Matrix is singular and cannot be inverted.\n");
        return;
    }
    double invDet = 1.0 / determinant;
    A_inv[0][0] = A[1][1] * invDet;
    A_inv[0][1] = -A[0][1] * invDet;
    A_inv[1][0] = -A[1][0] * invDet;
    A_inv[1][1] = A[0][0] * invDet;
}

// Function to multiply two 2x2 matrices
void multiply2x2(double A[2][2], double B[2], double result[2]) {
    result[0] = A[0][0] * B[0] + A[0][1] * B[1];
    result[1] = A[1][0] * B[0] + A[1][1] * B[1];
}

int main() {
    // Define the coefficient matrix A and the constant matrix B
    double A[2][2] = {{2, 0}, 
                      {0, 1}};
    double B[2] = {4, 2};
    double A_inv[2][2];  // Matrix to hold the inverse of A
    double X[2];         // Solution vector

    // Compute the inverse of matrix A
    inverse2x2(A, A_inv);

    // Compute the solution vector X = A_inv * B
    multiply2x2(A_inv, B, X);

    // Write the results to a file
    FILE *file = fopen("output.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(file, "The value of a is: %.2f\n", X[0]);
    fprintf(file, "The value of b is: %.2f\n", X[1]);
    fclose(file);

    return 0;
}

