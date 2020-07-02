#include <stdio.h>

int main(void){
	int a,b;
	scanf("%d", &a);
	scanf("%d", &b);

	printf("%0.9f\n", (double)((double)a/(double)b));
	return 0;
}