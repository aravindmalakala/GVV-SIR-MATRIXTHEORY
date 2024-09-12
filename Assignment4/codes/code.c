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
	double **A,**B,**C,**D,**dist;
	A=createMat(2,1);
	B=createMat(2,1);
	A[0][0]=-7.0/3.0;
	A[1][0]=5;
	B[0][0]=2.0/3.0;
	B[1][0]=5;
	C=Matsub(A,B,2,1);
	D=transposeMat(C,2,1);
	dist=Matmul(C,D,2,1,1);
	FILE *file = fopen("output.dat", "w");
	if (file == NULL)  {
		printf("Error openning file\n ");
		return 1;
	}
	fprintf(file,"The distance between A and B is %f",sqrt(dist[0][0]));
	fclose(file);
	freeMat(A,2);
	freeMat(B,2);
	freeMat(C,2);
	freeMat(D,2);
	freeMat(dist,1);
	return 0;
}	
