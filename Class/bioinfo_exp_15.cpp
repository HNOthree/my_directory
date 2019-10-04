#include <opencv2/opencv.hpp>
#include<string>
#include<iostream>
using namespace std;
using namespace cv;

int main(void){
    string input_file_name = "15.png";
    Mat img = imread(input_file_name,1);
    Mat output;
    Mat Gray;
    int height = img.rows;
    int width = img.cols;
    int mean = height*width/(256);
    int hist[256];
    for (int i=0 ;i<256;i++){
        hist[i]=0;
    }
    cout<<height<<endl<<width<<endl<<mean<<endl;
    
    for (int x=0;x<width;x++){
        for(int y = 0;y<height;y++){
            int b = img.at<Vec3b>(y,x)[0];
            int g = img.at<Vec3b>(y,x)[1];
            int r = img.at<Vec3b>(y,x)[2];
            int gray = (r*2+g*4+b)/7;
            hist[gray]++;
            for(int i =0;i<=2;i++){
                img.at<Vec3b>(y,x)[i]=gray;
            }
        }
    }
    cout<<hist<<endl;
    cvtColor(img, Gray, COLOR_RGB2GRAY);
    equalizeHist(Gray, output);
    imwrite("output.png",img);
    imwrite("output_hist.png",output);
    return 0;
}