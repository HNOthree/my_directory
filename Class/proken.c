#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lim1,lim2;



int max(int a,int b,int c){
  int A=a;
  if(b>A) A=b;
  if(c>A) A=c;
  return A;
}

int comp(int a,int b, int c,char d,char e){
  if(d==e) a=a+2;
  else if(d!=e) a=a-1;
  b=b-2;
  c=c-2;
 int Max=max(a,b,c);
 if(Max==a)return 1;
 else if(Max==b)return 2;
 else if (Max==c)return 3;
}

int hikaku(int a,int b,int c,char d,char e){
  if(d==e) a=a+2;
  else a=a-1;
  b=b-2;
  c=c-2;
  int A=max(a,b,c);
  return A;
}


int main(void){
  char seq1[1000],seq2[1000];
  int length1,length2,compa=0,compb=0,compc=0;
  printf("Type 1st DNA(Small letters)\n");
  scanf("%s",seq2);
  printf("Type 2nd DNA(Small letters)\n");
  scanf("%s",seq1);

  length1=strlen(seq2);
  length2=strlen(seq1);

  printf("The length of first DNA is %d\n",length1);
  printf("The length of second DNA is %d\n\n",length2);
  int mat1[length2+1][length1+1];
  int mat2[length2+1][length1+1];
  for(int i=-1;i<length1;i++){if (i==-1) printf("      "); else printf("%3c",seq2[i]);}
  printf("\n");
  for(int i=0;i<length2+1;i++){
    for(int j=-1;j<length1+1;j++){
    
     if(i==0&&j==0){mat1[i][j]=0; mat2[0][0]=0;}
	else if(i==0)mat1[i][j]=-2*j;mat2[i][j]=0;
     
      if(i>0&&j>0){ mat1[i][j]=hikaku(mat1[i-1][j-1],mat1[i-1][j]
,mat1[i][j-1],seq1[i-1],seq2[j-1]);
	mat2[i][j]=comp(mat1[i-1][j-1],mat1[i-1][j],mat1[i][j-1],seq1[i-1],seq2[j-1]);}
    }


    mat1[i+1][0]=-2*(i+1);
    mat2[i+1][0]=0;
}

    
    for(int i=0;i<length2+1;i++){
      for(int j=-1;j<length1+1;j++){
	if(j==-1&&i==0) printf("   ");
	else if(j==-1) printf("%3c",seq1[i-1]);
	else printf("%3d",mat1[i][j]);}
	printf("\n");}
      printf("\n");



 char nseq1[1000],nseq2[1000];
 int l1=length2;
 int l2=length1;
 int N=max(l1,l2,0)-1;
 int SW=0;

 printf("The original DNAs\n");
 for(int i=0;i<l2;i++){printf("%c",seq2[i]);}
 printf("\n");
 for(int i=0;i<l1;i++){printf("%c",seq1[i]);}
 printf("\n");
 while(l2>=0&&l1>=0){

   if (mat2[l1][l2]==1){
     nseq1[N]=seq1[l1-1];
     nseq2[N]=seq2[l2-1];
       l1=l1-1; l2=l2-1; SW=0; 
       N--; continue;}
     else if(mat2[l1][l2]==2){
       nseq2[N]='-';
       nseq1[N]=seq1[l1-1];
       l1=l1-1;SW=1; N--;  continue;}
     else if(mat2[l1][l2]==3){ 
     nseq1[N]='-';
     nseq2[N]=seq2[l2-1];
     l2=l2-1;  SW=2; N--;  continue;}
     else   break;}
 printf("\n");


 printf("The first optimal alignment is\n");
 printf("%s",nseq2);
 printf("\nThe second optimal alignment is\n");
 printf("%s",nseq1);
 printf("\n");
  return 0;
}
 
