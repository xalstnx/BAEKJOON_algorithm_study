#include <stdio.h>

int main(void)
{
	int num;
	scanf("%d", &num);
	int a[num];
	int count=0;
	for (int i = 0; i < num; i++)
	{
		scanf("%d", &a[i]);
	}
	for(int i=0;i<num;i++){
		if(a[i] == 1)count++;
		else{
			for(int j=2;j<a[i]-1;j++){
				if((a[i]%j) == 0){
					count++;
					break;
				}
			}
		}
	}
	printf("%d\n", num - count);
	return 0;
}