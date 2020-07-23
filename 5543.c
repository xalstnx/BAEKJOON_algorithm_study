#include <stdio.h>

int main(void) {
  int a[5];
  int cb = 2000;
  int cd = 2000;

  for(int i=0;i<5;i++){
    scanf("%d", &a[i]);

    if(i<3){
      if(a[i] < cb)
        cb = a[i];
    }else{
      if(a[i] < cd)
        cd = a[i];
    }
  }

  printf("%d", cd+cb-50);
}