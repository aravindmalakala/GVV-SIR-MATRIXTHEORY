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
	double **A,**B,**C;
	A=createMat(2,2);
	B=createMat(2,1);
	C=createMat(2,1);
	A[0][0]=1;
	A[0][1]=0;
	A[1][0]=(float) 4/3;
	A[1][1]=(float) -1/3;
	B[0][0]=2;
	B[1][0]=2;
	C[0][0]=(A[0][0]*B[0][0])+(A[0][1]*B[1][0]);
	C[1][0]=(A[1][0]*B[0][0])+(A[1][1]*B[1][0]);
	FILE *file = fopen("output.dat", "w");
        if (file == NULL) {
            printf("Error opening file!\n");
            return 1;
    }
        fprintf(file, "The value of a is: %f\n", C[0][0]);
        fprintf(file, "The value of b is: %f\n", C[1][0]);
        fclose(file);

	freeMat(A,2);
	freeMat(B,2);
	freeMat(C,2);
        return 0;
}

