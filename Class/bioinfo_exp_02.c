#include<stdio.h>

int main(void)
{
 int x ;
 scanf("%d",&x);
 while(0<=x)
 {
    if(x%3==0)
      printf("Y");
    printf("X");
    x--;
 }
}