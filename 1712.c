#include <stdio.h>

int main(void)
{
	int a,b,c;
	int i=1;
	scanf("%d %d %d", &a, &b, &c);
	if(c-b<=0)
		printf("-1");
	else
		printf("%d", (a/(c-b) + 1));
	return 0;
}