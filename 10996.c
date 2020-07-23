#include <stdio.h>

int main(void) {
  int num;

  scanf("%d", &num);

  if(num == 1)
    printf("*");
  else{
    for(int i=0;i<num;i++){
      for(int j=0;j<(num/2+num%2);j++){
        printf("* ");
      }
      printf("\n");
      for(int k=0;k<(num/2);k++){
        printf(" *");
      }
      printf("\n");
    }
  }
}