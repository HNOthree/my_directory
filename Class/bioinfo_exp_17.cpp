#include<iostream>
#include<math.h>
using namespace std;

float consider_calculate(float a,float b,float c){
 float x;
 if(b>0){
  x=-(b+sqrt(b*b-4*a*c))/(2*a);
 }
 else{
  b=-b;
  x=-(b+sqrt(b*b-4*a*c))/(2*a);
 }
 return x;
}


int main(void){
 float a,b,c;
 cout<<"Input a,b,c"<<endl;
 cin>>a>>b>>c;
 cout<<a<<"x^2+"<<b<<"x+"<<c<<endl;
 float x_1_1,x_1_2,x_2_1,x_2_2;
 x_1_1=(-b-sqrt(b*b-4*a*c))/(2*a);
 x_1_2=(-b+sqrt(b*b-4*a*c))/(2*a);
 x_2_1=consider_calculate(a,b,c);
 x_2_2=c/(a*x_2_1);
 cout<<"Not Consider:"<<endl;
 printf("%.16f\t%.16f\n", x_1_1,x_1_2);
 cout<<"Consider:"<<endl;
 printf("%.16f\t%.16f\n", x_2_1,x_2_2);
 //cout<<x_2_1<<"\t"<<x_2_2<<endl;


 return 0;
}