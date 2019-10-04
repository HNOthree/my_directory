#include<iostream>
#include<vector>
#include<time.h>
using namespace std;

int zero_count(vector<int>& data_vector)
{
 int count=0;
 int vector_size = data_vector.size();

  for(int i =0 ; i< vector_size; i++)
  {
   if(data_vector[i]== 0)
    {
     count+=1;
    }
   }
   return(count);
}

int main (void)
{
 clock_t start = clock();
 int vector_size = 1000000000;
 vector<int> temp_vector;
 temp_vector.resize(vector_size,0);

 for(int i =0; i < vector_size ; i++)
  {
   temp_vector[i]= i%10;
  }
  int c = zero_count(temp_vector);
  clock_t end = clock();
  cout << "count" << c << endl;
  cout << "time" << (double)(end-start) / CLOCKS_PER_SEC << endl;
  return (0);
}