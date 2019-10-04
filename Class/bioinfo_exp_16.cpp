#include <opencv2/opencv.hpp>
#include<string>
#include<iostream>
#include<math.h>

using namespace std;
using namespace cv;
int Threshold=1;
int pre_x=0;
int pre_y=0;

int gray_calc(Mat img,int i,int j){
 int b = img.at<Vec3b>(i,j)[0];
 int g = img.at<Vec3b>(i,j)[1];
 int r = img.at<Vec3b>(i,j)[2];
 int gray = (r*2+g*4+b)/7;
 return gray;
}

void write_output(Mat *output,Mat img,int i,int j){
 int b= img.at<Vec3b>(i,j)[0];
 int g = img.at<Vec3b>(i,j)[1];
 int r = img.at<Vec3b>(i,j)[2];
 output->at<Vec3b>(i,j)[0]= b;
 output->at<Vec3b>(i,j)[1]= g;
 output->at<Vec3b>(i,j)[2]= r;
}

int start(int now_x,int now_y ,int pre_x,int pre_y){
 int t = now_x-pre_x;
 int u = now_y-pre_y;
 if(u==1){
  if(t==-1){
   return 1;
  }
  else if(t==0){
   return 2;
  }
  else{
   return 3;
  }
 }
 
 else if(u==-1){
  if(t==-1){
   return 7;
  }
  else if(t==0){
   return 6;
  }
  else{
   return 5;
  }
 }
 
 else{
  if(t==-1){
   return 8;
   }
  else{
   return 4;
  }
 }
}

void search_location(Mat img, int *x,int *y){
 int a = *x;
 int b= *y;
 int start_pos=start(a,b,pre_x,pre_y);
 int end_pos=start_pos-1;
 if(end_pos==0){
  end_pos=8;
 }
    
 int for_break=0;
 while(start_pos!=end_pos){
  if(start_pos==1){
   if(gray_calc(img,b-1,a-1)<Threshold){
    pre_x=a;
    pre_y=b;
    a--;
    b--;
    for_break++;
    break;
   }
   else{
    start_pos++;
   }
   if(for_break==1){
    break;
   }
  }
  
  else if(start_pos==2){
   if(gray_calc(img,b,a-1)<Threshold){
    pre_x=a;
    pre_y=b;
    a--;
    for_break++;
    break;
   }
   else{
    start_pos++;
   }
   if(for_break==1){
    break;
   }
  }
  
  else if(start_pos==3){
   if(gray_calc(img,b+1,a-1)<Threshold){
    pre_x=a;
    pre_y=b;
    a--;
    b++;
    for_break++;
    break;
   }
   else{
    start_pos++;
   }
   if(for_break==1){
    break;
   }
  }
  
  else if(start_pos==4){
   if(gray_calc(img,b+1,a)<Threshold){
    pre_x=a;
    pre_y=b;
    b++;
    for_break++;
    break;
   }
   else{
    start_pos++;
   }
   if(for_break==1){
    break;
   }
  }
  
  else if(start_pos==5){
   if(gray_calc(img,b+1,a+1)<Threshold){
    pre_x=a;
    pre_y=b;
    a++;
    b++;
    for_break++;
    break;
   }
   else{
    start_pos++;
   }
   if(for_break==1){
    break;
   }
  }
  
  else if(start_pos==6){
   if(gray_calc(img,b,a+1)<Threshold){
    pre_x=a;
    pre_y=b;
    a++;
    for_break++;
    break;
   }
   else{
    start_pos++;
   }
   if(for_break==1){
    break;
   }
  }
     
  else if(start_pos==7){
   if(gray_calc(img,b-1,a+1)<Threshold){
    pre_x=a;
    pre_y=b;
    a++;
    b--;
    for_break++;
    break;
   }
   else{
    start_pos++;
   }
   if(for_break==1){
    break;
   }
  }
  
  else if(start_pos==8){
   if(gray_calc(img,b-1,a)<Threshold){
    pre_x=a;
    pre_y=b;
    b--;
    for_break++;
    break;
   }
   if(for_break==1){
    break;
   }
   else{
    start_pos=1;
   }
  }
  if(start_pos==end_pos){
   cout<<"ERROR"<<endl;
  }
 }   
 *x=a;
 *y=b;
}

double calc_distance(double distance,int x,int y){
 int a = abs(x-pre_x)*abs(y-pre_y);
 if(a==0){
  distance++;
 }
 else{
  distance=distance+sqrt(2);
 }
 return distance;
}

int main(void){
 string input_file_name = "hokkaido.png";
 cout <<"Input File:"<< input_file_name<<endl;
 Mat img = imread(input_file_name,1);
 int height = img.rows;
 int width = img.cols;
 
 Mat output = imread(input_file_name,1);
 for (int i=0;i<height;i++){
  for(int j=0;j<width;j++){
   output.at<Vec3b>(i,j)[0]= 255;
   output.at<Vec3b>(i,j)[1]= 255;
   output.at<Vec3b>(i,j)[2]= 255;
  }
 }
    
 int start_x,start_y,x,y;

 for(int i=0;i<height;i++){
  int count =0;
  for(int j=0;j<width;j++){
   int gray=gray_calc(img,i,j);
   write_output(&output,img,i,j);
   if(gray<Threshold){
    start_x=j;
    start_y=i;
    pre_x=j;
    pre_y=i;
    x=j-1;
    y=i+1;
    write_output(&output,img,i,j);
    count++;
    break;
   } 
  }  
  if (count!=0){
   break;
  }
 }

 double distance=calc_distance(0,x,y);
  while(x!=start_x || y!=start_y){
   write_output(&output,img,y,x);
   search_location(img,&x,&y); 
   distance=calc_distance(distance,x,y);
  }
 imwrite("output_16.png",output);
 cout<<"Distance: "<<distance<<endl;

 return 0;
}