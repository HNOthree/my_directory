#include<iostream>
#include<cmath>
#include<string>
#include<fstream>

using namespace std;

double euler(float t,float r, float K,float h,float pre){
 double value;
 value=pre+h*(r*pre*(1-pre/K));
 return value;
}

double exact_calculate(float t,float r,float K,float N_0){
 double value;
 value=K*exp(r*t)/((K- N_0)/ N_0+exp(r*t));
 return value;
}
int main(void){
 float r,K,h;
 string output_file_name="simulation.csv";
 ofstream output_file(output_file_name);
 cout<<"Input r,K,h:"<<endl;
 cin >> r>>K>>h;
 double pre_approximate_value=150,approximate_value,exact,N_0;
 N_0 = pre_approximate_value;

 for(double t=0;t<5;t=t+0.01){
  approximate_value=euler(t,r,K,h,pre_approximate_value);
  exact=exact_calculate(t,r,K,N_0);
  pre_approximate_value=approximate_value;
  //cout<<"Euler"<<approximate_value<<" EXACT"<<exact<<endl;
  cout<<approximate_value<<endl;
  output_file<<approximate_value<<","<<exact<<endl;
 }

 return 0;
}