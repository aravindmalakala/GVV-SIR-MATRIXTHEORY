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
	double **A;
	A=createMat(3,3);
	float x;
	A[0][1]=-1;
	A[0][2]=1;
	A[1][0]=2;
	A[1][1]=1;
	A[1][2]=1;
	A[2][0]=4;
	A[2][1]=5;
	A[2][2]=1;
	A[0][0]=(A[1][1]*A[2][0]-A[1][0]*A[2][1]+A[0][1]*(A[1][0]-A[2][0]))/(A[1][1]-A[2][1]);//det of A is 0
        FILE *file=fopen("output.dat","w");
	if (file == NULL)  {
		printf("Error opening file!\n");
		return 1;
        }
        fprintf(file,"X \n");
	fprintf(file,"%.2f\n",A[0][0]);
	fclose(file);
	freeMat(A,3);
	return 0;
}	

