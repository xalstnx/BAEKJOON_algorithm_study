#include<stdio.h>
#include<string.h>
int main(void)
{
    int num;
    char a[1001];
    scanf("%d", &num);
    for(int i=0;i<num;i++){
        scanf("%s", a);
        printf("%c%c\n", a[0], a[strlen(a)-1]);
    }
	return 0;
}