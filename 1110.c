#include <stdio.h>

int main(void)
{
	int n;
	int a,b;
	int c;
	int newn = -1;
	int count=0;
	int base;
	scanf("%d", &n);
	base = n;
	while(1){
		count++;
		a = n/10;
		b = n%10;
		newn = b*10 + (a+b)%10;

		if(base == newn){
			printf("%d\n",count);
			break;
		}
		n = newn;
	}
	return 0;
}