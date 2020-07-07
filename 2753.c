#include <stdio.h>

int main(void)
{
	int year;
	scanf("%d", &year);
	int torf=0;
	if((year%4==0&&year%100!=0) || year%400==0){
		torf=1;
	}
	printf("%d", torf);
	return 0;
}