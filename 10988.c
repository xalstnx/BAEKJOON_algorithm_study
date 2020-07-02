#include<stdio.h>
#include<string.h>
int main(void)
{
    int torf = 1;
    int len = 0;
    char a[101];
    scanf("%s", a);
    len = strlen(a);
    for(int i=0;i<(len/2);i++){
        if(a[i] != a[len-1-i]){
            torf = 0;
            break;
        }
    }
    printf("%d", torf);
	return 0;
}