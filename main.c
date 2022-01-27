#include <stdio.h>
#include <math.h>

double intpow(double a, int b) {
	double r = 1.0;
	if (b < 0) {
		a = 1.0 / a;
		b = -b;
	}
	while (b) {
		if (b & 1) {
			r *= a;
		}
		a *= a;
		b >>= 1;
	}
	return r;
}

int main() {
	// Variables
	int current_x;
	int current_z;
	int dest_x;
	int dest_z;
	float output;
	float distance;
	double distance_dependant;

	// Collect needed information
	// Current coordiantes
	printf("Current X coordinate: ");
	scanf("%d", &current_x);
	printf("Current Z coordinate: ");
	scanf("%d", &current_z);
	// Destination coordinates
	printf("Destination X coordinate: ");
	scanf("%d", &dest_x);
	printf("Destination Z coordinate: ");
	scanf("%d", &dest_z);

	distance_dependant = intpow(dest_x - current_x, 2) + intpow(dest_z - current_z, 2);
	distance = sqrt(distance_dependant);
	output = distance / 20160;
	printf("Your journey will take %f hours.\n", output);
	return 0;
}
