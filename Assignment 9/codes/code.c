#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to calculate the area enclosed by the circle and the line
double calculateArea(double a) {
    return a * a * (1 + M_PI / 2); // Area = a^2 * (1 + pi/2)
}

int main() {
    // Set the value of radius 'a' to 3
    double a = 3.0;

    // Calculate the area using the formula
    double area = calculateArea(a);

    // Open file to write results
    FILE *file = fopen("values.tex", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    // Write results to the file
    fprintf(file, "Radius : %lf\n", a);
    fprintf(file, "Area : %.2f\n", area);

    fclose(file);

    // Print the area to the console
   

    return 0;
}

