#include <stdio.h>

int main(void)
{
	int h,m;
	scanf("%d %d", &h, &m);
	if(m>=45){
		m-=45;
		printf("%d %d", h, m);
	}
	else{
		if(h == 0){
			h = 23;
			m+=15;
			printf("%d %d", h, m);
		}else{
			h-=1;
			m+=15;
			printf("%d %d", h, m);
		}
	}
	return 0;
}