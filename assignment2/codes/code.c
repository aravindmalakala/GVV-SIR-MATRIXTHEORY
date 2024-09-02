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
	double **EINV,**D,**X, **E;
	double **A,**B,**C;
	EINV=createMat(2,2);
	E = createMat(2,2);
	D=createMat(2,1);
	X=createMat(2,1);
	E[0][0]=1;
	E[0][1]=-2;
	E[1][0]=0;
	E[1][1]=3;
	EINV = Matinv(E,2);
	D[0][0]=2;
	D[1][0]=2;
	X = Matmul(EINV,D,2,2,1);// EX=D, X = EINV*D

	A=createMat(2,1);
	B=createMat(2,1);
	C=createMat(2,1);
	A[0][0]=4;
	A[1][0]=4;
	B[0][0]=-2;
	B[1][0]=6;
	C=Matsec(A,B,2,1);
      
	FILE *file = fopen("output.dat", "w");
        if (file == NULL) {
            printf("Error opening file!\n");
            return 1;
    }
        fprintf(file,"X Y\n");
        fprintf(file," %.2f %.2lf\n",A[0][0],A[1][0]);
        fprintf(file," %.2f %.2lf\n",B[0][0],B[1][0]);
        fprintf(file," %.2f %.2lf\n",C[0][0],C[1][0]);
        fclose(file);

	freeMat(EINV,2);
	freeMat(D,2);
	freeMat(X,2);
	freeMat(E,2);
	freeMat(A,2);
	freeMat(B,2);
	freeMat(C,2);
        return 0;
}

