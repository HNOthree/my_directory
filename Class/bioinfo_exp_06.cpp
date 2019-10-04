#include<iostream>
#include <vector>
using namespace std;

class UnionFind{
   
    public:
    vector <int> cluster;
    vector <int> rank;

    UnionFind(int N):cluster(N),rank(N){
        for(int i = 0; i < N+1; i++) {
            cluster[i] = i ;
            rank[i] = 1;
        }
    }
    void unite (int a,int b){
        int root_a=find(a);
        int root_b=find(b);
        
        if(rank[root_a]==rank[root_b]){
           
          
            cluster[root_b]=root_a;
            rank[root_a]++;
        }
        else{
            if(rank[root_a]>rank[root_b]){
                cluster[root_b]=root_a;
            }
            else{
                cluster[root_a]=root_b;
            }

        }
    }

    void print(int N){
        for (int i =0;i<N+1;i++){
            cout <<"number:"<< i<< " cluster:"<<cluster[i]<<" rank:"<<rank[i]<<endl;
        }
        cout << endl;
    }
    int find (int i){
        if (i==cluster[i])
            return i;
        else 
            return cluster[i]=find(cluster[i]);
        
    }
    void same(int i ,int j){
        int root_i = find(i);
        int root_j = find(j);
        if (root_i==root_j)
            cout << i <<" and "<<j <<" are Same Group."<<endl;
        else
            cout << i <<" and "<<j <<" are Wrong Group"<< endl;
    }

};

int main(void){
    int size = 30;
    UnionFind unionfind(size);

    unionfind.unite(2,10);
    unionfind.unite(3,10);
    unionfind.unite(8,10);
    unionfind.unite(10,7);
    //unionfind.print(size);
    unionfind.unite(10,20);
    //unionfind.print(size);
    unionfind.unite(5,2) ;
    //unionfind.print(size);
    cout <<"Root is " << unionfind.find(10)<< endl;
    unionfind.same(5,10);
    unionfind.same(2,16);
    return 0;
}