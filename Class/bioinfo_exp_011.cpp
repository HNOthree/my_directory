#include<iostream>
#include <stack>
#include <cstdlib>
#include "bioinfo_exp_011.h"
using namespace std;


int main(void){
    cout << "Input N:"<<endl;
    cin >> N ;
    int i=0;
    int j=0;
    int count=0;
    int before_length,after_length;

    QueenLocation queen;
    while(true){
        
       
        while(j==N){
            if (i==0){
                cout<<endl;
                cout<<"Kinds:"<<count<<endl;
                return 0;
            }
            i=queen.location_i.top();
            j=queen.location_j.top();
            //cout<<"end"<<i<<j<<endl;
            queen.location_i.pop();
            queen.location_j.pop();
            j++;
            }
            //continue;
           
        
       
        
        before_length=queen.location_i.size();
        queen.set_queen(i,j);
        after_length=queen.location_i.size();
        if (after_length!=before_length){
            //cout<<"Go deep"<<endl;
            i++;
            j=0;
            continue;
        }
        
        //cout<<i<<" "<<j<<endl;
        else if(queen.location_i.size()==N){
            //cout<<"matched"<<endl;
           
            //queen.display();
            count++;
            queen.location_i.pop();
            j=queen.location_j.top();
            queen.location_j.pop();
            j++;
        }
        else
                j++;
    }

    
    return 0;
}