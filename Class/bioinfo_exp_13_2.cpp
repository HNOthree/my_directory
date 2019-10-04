#include<iostream>
#include <fstream>
#include<sstream>
#include<map>
#include<string>
#include <algorithm>
#include<math.h>
#include<time.h>


using namespace std;
int N =51;

int main (void){
 clock_t start = clock();
 double T =2000;
 double terminate = 0.00001;
 double r=0.99999;
 int city_information[N][2];
    //ファイルを開く
 string file_name= "eil51-tsp.txt";

 string output_file_name="a.txt";
 ofstream output_file(output_file_name);

 ifstream ist(file_name);
 if(!ist){
  cerr << "Cannot open friend_list.txt" << endl;
  exit(1);
 }

 int row =0;
 int traveling[N];
 while(!ist.eof()){
     row++;
     string s;
     getline(ist,s);
     string s_city,s_location,s_x_location,s_y_location;
     int city, x_location,y_location;
     int pos = s.find(' ');
     s_city = s.substr(0, pos);
     city = stoi(s_city);
     s_city="city"+s_city;
     s_location = s.substr(pos + 1);
     pos = s_location.find(' ');
     s_x_location=s_location.substr(0,pos);
     s_y_location=s_location.substr(pos+1);

     traveling[row-1]=row;
     city_information[city][0]=stoi(s_x_location);
     city_information[city][1]=stoi(s_y_location);
     
 }

 srand((unsigned) time(NULL) ); // 乱数の初期化

for (int count=0;count<100;count++){
    cout<<count<<endl;
 for (int i = 0; i<N; i++){
	// リストの中のランダムな番目を取得
	int j = rand() % N;
	// i 番目の要素とランダムな番目の要素を入れ替える
	int index = traveling[i];
	traveling[i] = traveling[j];
	traveling[j] = index;
  } 
  int best_score=0;
  int from,to,distance;
  for (int i = 0; i<N; i++){
    from =traveling[i];
    to = traveling[i+1];
    distance=sqrt(pow(city_information[from][0]-city_information[to][0],2.0)+pow(city_information[from][1]-city_information[to][1],2.0));
    best_score+=distance;
  }
  cout<<best_score<<endl;
 
 
  while(true){
   int j = rand() % N;
   int candidate=0;
   int rewrite=0;
   for (int i =0;i<N;i++){//近傍の計算
      swap(traveling[i] ,traveling[j]);
      
      for (int k=0;k<N;k++){//コスト計算
        from =traveling[k];
        to = traveling[k+1];
        distance=sqrt(pow(city_information[from][0]-city_information[to][0],2.0)+pow(city_information[from][1]-city_information[to][1],2.0));
        candidate+=distance;
      }

      if (best_score>candidate){
          cout<<i<<"   "<<j<<endl;
          best_score= candidate;
          rewrite++;
          break;
      }
      else{
          swap(traveling[i] ,traveling[j]);
      }
        //cout<<candidate<<"  "<<best_score<<endl; 
    }  
    if (rewrite==0){
         break;
     }
    
    
   }
   cout<<best_score<<endl;
 }


return 0;
}