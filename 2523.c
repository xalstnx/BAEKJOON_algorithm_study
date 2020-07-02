#include <stdio.h>

int main(void){
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= (2*n-1); i++)
	{
		if(i<=n){
			for (int j = 0; j < i; j++)
			{
				printf("*");
			}
			printf("\n");
		}else{
			for (int j = 0; j < n-(i%n) ; j++)
			{
				printf("*");
			}
			printf("\n");
		}
	}
	return 0;
}