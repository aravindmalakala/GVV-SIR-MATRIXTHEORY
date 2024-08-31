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
	double **AINV,**B,**X;
	AINV=createMat(2,2);
	B=createMat(2,1);
	X=createMat(2,1);
	AINV[0][0]=1;
	AINV[0][1]=0;
	AINV[1][0]=(float) 4/3;
	AINV[1][1]=(float) -1/3;
	B[0][0]=2;
	B[1][0]=2;
	X[0][0]=(AINV[0][0]*B[0][0])+(AINV[0][1]*B[1][0]);//a=2,3b-2a=2 are the two equations. converting them into a matrix form
	X[1][0]=(AINV[1][0]*B[0][0])+(AINV[1][1]*B[1][0]);//AX=B, X=AINV*B        
	FILE *file = fopen("output.dat", "w");
        if (file == NULL) {
            printf("Error opening file!\n");
            return 1;
    }
        fprintf(file, "The value of a is: %f\n", X[0][0]);
        fprintf(file, "The value of b is: %f\n", X[1][0]);
        fclose(file);

	freeMat(AINV,2);
	freeMat(B,2);
	freeMat(X,2);
        return 0;
}

