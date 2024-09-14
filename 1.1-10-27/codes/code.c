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
	double **A,**B,norm;
	A=createMat(3,1);
	A[0][0]=1;
	A[1][0]=1;
	A[2][0]=-1;
        norm = 1/Matnorm(A,3);
	B= Matscale(A,3,1,norm);
	FILE *file;
	file = fopen("output.dat","w");
	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file,"X\n");
	fprintf(file,"%.2lf\n",A[0][0]);
	fprintf(file,"%.2lf\n",A[1][0]);
	fprintf(file,"%.2lf\n",A[2][0]);
	fclose(file);
	printf("The direction cosines are %.2lf %.2lf %.2lf",B[0][0],B[1][0],B[2][0]);
	freeMat(A,3);
	freeMat(B,3);
}	
