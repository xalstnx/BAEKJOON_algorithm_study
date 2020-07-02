#include <stdio.h>

int main(void)
{
	int n;
	int a,b,c;
	int ab,bc;
	int count=0;
	scanf("%d", &n);
	if(n <= 99)
		count = n;
	else{
		count+=99;
		for(int i=100;i<=n;i++){
			a=i/100;
			b=(i%100)/10;
			c=(i%100)%10;
			ab = b - a;
			bc = c - b;
			if(ab == bc){
				count++;
			}
		}
	}
	printf("%d\n", count);

	return 0;
}