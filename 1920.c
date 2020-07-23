#include <stdio.h>
#include <stdlib.h>

int compare(void *first, void *second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else 
        return 0;
}

int main(void) {
  int n,m;
  scanf("%d", &n);
  int nnum[n];
  for(int i=0;i<n;i++){
    scanf("%d", &nnum[i]);
  }
  qsort(nnum,(sizeof(nnum)/sizeof(int)),sizeof(int), compare);
  scanf("%d", &m);
  int mnum;
  int torf[m];
  for(int i=0;i<m;i++){
    scanf("%d", &mnum);
    if(bsearch(&mnum, nnum, n, sizeof(int), compare) != NULL){
      torf[i] = 1;
    }else{
      torf[i] = 0;
    }
  }

  for(int i=0;i<m;i++)
    printf("%d\n", torf[i]);
}