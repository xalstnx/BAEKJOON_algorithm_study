#include<stdio.h>
#include<string.h>
int main(void)
{
    int num;
    char a[1001];
    //처음에는 char *a 로 풀어서 컴퓨터에서 실행하면 정상적으로 출력이 되었는데 백준에서는 컴파일오류가 뜸
    scanf("%d", &num);
    for(int i=0;i<num;i++){
        scanf("%s", a);
        printf("%c%c\n", a[0], a[strlen(a)-1]);
    }
	return 0;
}
