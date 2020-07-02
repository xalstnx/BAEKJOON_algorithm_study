#include <stdio.h>

int main(void)
{
	int n,k;

	for(int i=1;i<=10000;i++,k=0){
		for(int j=1;j<=i;j++){
			n=(j/1000)+((j%1000)/100)+(((j%1000)%100)/10)+(((j%1000)%100)%10)+j;
			if(n==i)
				k=n;
		}
		if(k==0){
			printf("%d\n", i);
		}
	}

	return 0;
}