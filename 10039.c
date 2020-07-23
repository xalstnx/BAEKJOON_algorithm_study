#include <stdio.h>

int main(void) {
  int a[5];
  int avg=0;
  for(int i=0;i<5;i++){
    scanf("%d", &a[i]);
    if(a[i] < 40){
      a[i] = 40;
    }
    avg += a[i];
  }
  printf("%d", avg/5);
}