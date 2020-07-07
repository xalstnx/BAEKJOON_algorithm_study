#include <stdio.h>

int main(void)
{
	int n,m;
	scanf("%d %d", &n, &m);
	int a[n];
	for(int q=0;q<n;q++){
		scanf("%d", &a[q]);
	}
	int check[n];
	int sum=0;
	int best=0;

	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			for(int k=j+1;k<n;k++){
				sum = a[i]+a[j]+a[k];
				if(sum<=m && sum>=best){
					best = sum;
				}
				sum = 0;
			}
		}
	}
	printf("%d\n", best);
	return 0;
}