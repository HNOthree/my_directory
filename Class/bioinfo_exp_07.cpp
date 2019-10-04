#include<iostream>
#include <cstdlib> 
#include <ctime>  
#include <vector>
#include <ios>    
#include <iomanip>
#include <memory>
#include "bioinfo_exp_07.h"
#include <malloc/malloc.h>

using namespace std;

int main() {
    //probability=0.1;
    srand((unsigned) time(NULL) ); // 乱数の初期化
    while(probability<1){
        global_count=0;
        for (int q = 0;q<iteration;q++){
            //cout <<"iteration: "<<q<<endl;
            UnionFind unionfind(size);
            //unionfind.printing();
            unionfind.percolation();
            //unionfind.printing_clust();
            unionfind.confirm();
        //assert( malloc_zone_check(NULL) );
        }
    cout<<probability<<","<<global_count<<endl;
    //length++;
    probability=probability+0.01;
    }

    return 0;
}