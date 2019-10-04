#include<iostream>
#include <fstream>
#include<sstream>
#include<map>
#include<string>
using namespace std;


int main(void)
{
   //ファイルを開く
 string file_name= "friend_list.txt";
 ifstream ist(file_name);
 if(!ist)
 {
  cerr << "Cannot open friend_list.txt" << endl;
  exit(1);
 }
//ファイルを一行づつ取得
 int row = 1;
 map<string, int> name_count;

 while(!ist.eof())
 {
  string s;
  getline(ist,s);
  //スペースで分割
  string name1, name2;
  int pos = s.find(' ');
  name1 = s.substr(0, pos);
  name2 = s.substr(pos + 1);

  if (name_count.count(name1))
   name_count[name1]++;
  else
   name_count[name1]= 0;
  if (name_count.count(name2))
   name_count[name2]++;
  else
   name_count[name2]= 0;
}
 int max_count = 0;
 string max_name ="0";
 for (map<string, int> ::const_iterator i = name_count.begin();
  i != name_count.end(); ++i)
  {
   if (max_count < i -> second)
   {
    max_count = i -> second;
    max_name = i -> first;
   }
  }
 cout << max_name << endl;   
}