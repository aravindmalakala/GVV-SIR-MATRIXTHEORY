#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    int A = 1, B = 2, C = 6;
    double **d, **n;
    n = createMat(2, 1);
    d = createMat(2, 1);
    n[0][0] = A;
    n[1][0] = B;
    d[0][0] = B;
    d[1][0] = -A;

    FILE *file;
    file = fopen("values.tex", "w");  // Updated file name
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "d: %.2f\n", d[0][0]);
    fprintf(file, "d: %.2f\n", d[1][0]);
    fprintf(file, "n: %.2f\n", n[0][0]);
    fprintf(file, "n: %.2f\n", n[1][0]);
    fclose(file);

    freeMat(d, 2);
    freeMat(n, 2);
}
