#include <stdio.h>
#define SIZE 10

int check[SIZE];
int arr[SIZE];
int n,m;

void back(int count){
	if(count == m){
		for(int i=0;i<m;i++){
			printf("%d ", arr[i]);
		}
		printf("\n");
		return;
	}
	for(int i=1;i<=n;i++){
		if(check[i] == 0){
			check[i] = 1;
			arr[count] = i;
			back(count + 1);
			check[i] = 0;
		}
	}
	
}

int main(void){
	scanf("%d %d", &n, &m);
	back(0);
	return 0;
}