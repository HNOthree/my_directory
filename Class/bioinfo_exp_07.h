#ifndef BIOINFO_EXP_07_H
#define BIOINFO_EXP_07_H
using namespace std;
double probability=0;
int iteration =1000;
int global_count=0;
int length=10;
int size=length*length;

class UnionFind{
   
    public:
    vector <int> cluster;
    vector <int> rank;
    vector <int> firing;

    UnionFind(int N):cluster(N),rank(N),firing(N){
        
        for(int i = 0; i < N; i++) {
            cluster[i] = i ;
            rank[i] = 1;
            //cout<<(double)rand()<<endl;

            if( ((double)rand()+1.0)/(RAND_MAX+2.0) < probability ) {
                firing[i]=1;
            }
            else{
                firing[i]=0;
                //cout<<"not fire"<<i<<size<<endl;
            }
        }
    }
    int find (int i){
        if (i==cluster[i])
            return i;
        else 
            cluster[i]=find(cluster[i]);
            return cluster[i];
        
    }

    void unite (int a,int b){
        int root_a=find(a);
        int root_b=find(b);

        if(rank[root_a]==rank[root_b]){
           
           // cout <<"From " <<cluster[a]<<" "<<cluster[b]<<endl;
            cluster[root_b]=root_a;
            //cout <<"To "<<cluster[a]<<" "<<cluster[b]<<endl;
            //rank[root_a]++;
            rank[root_b]++;
        }
        else{
            if(rank[root_a]>rank[root_b]){
              //  cout <<"From "<<cluster[a]<<" "<<cluster[b]<<endl;
                cluster[root_b]=root_a;
                //cout <<"To "<<cluster[a]<<" "<<cluster[b]<<endl;
                //rank[root_b]++;
            }
            else{
                //cout <<"From "<<cluster[a]<<" "<<cluster[b]<<endl;
                cluster[root_a]=root_b;
                //cout <<"To "<<cluster[a]<<" "<<cluster[b]<<endl;
                //rank[root_a]++;
            }

        }
    }

    void printing(){
        for (int i=0;i < size;i++){
            if(i%length==0)
                cout<<endl;
            cout<<right<<setw(3)<<firing[i];
        }
    }
    void printing_clust(){
        cout<<endl;
        for (int i=0;i < size;i++){
            if(i%length==0)
                cout<<endl;
            cout<<right<<setw(3)<<find(i);
        }
        cout<<endl;
    }
    void printing_root(){
        cout<<endl;
        for (int i=0;i < size;i++){
            if(i%length==0)
                cout<<endl;
            cout<<right<<setw(3)<<find(cluster[i]);
        }
        cout<<endl;
    }

    void connect_check(int ref,int i){
        int index;
        index=i;
            if(firing[ref]==1 && firing[index]==1){
                    unite(ref,index);
            }

    }
    void connect_check(int ref,int i ,int j){
        int index[2];
        index[0]=i;
        index[1]=j;
        for(int a=0;a<2;a++){
            if(firing[ref]==1 && firing[index[a]]==1){
                    unite(ref,index[a]);
            }
        }
    }

    void connect_check(int ref,int i ,int j,int k){
        int index[3];
        index[0]=i;
        index[1]=j;
        index[2]=k;
        for(int a=0;a<3;a++){
            if(firing[ref]==1 && firing[index[a]]==1){
                    unite(ref,index[a]);
            }
        }
    }


    void percolation(){
        for (int i=1;i < size;i++){
            if(i < length){
                connect_check(i,i-1);
            }
            else if (i%length==0){
                connect_check(i,i-length);
            }
            else {
                connect_check(i,i-length,i-1);
            }
        }
    }

    void confirm(){
        int count=0;
        for (int i=0;i<length;i++){
            for (int j=size-length;j<size;j++){
                count = same(i,j);
                
                if (count ==1){
                    //cout<<i<<j<<"return"<<count<<endl;
                    global_count++;
                    //cout<<"Count: "<<global_count<<endl;
                    return ;
                }
                
            }
        // if (count==1){
        //             break;
        //         }
        }

    }

     bool same(int i ,int j){
        int root_i = find(i);
        int root_j = find(j);
        //cout << i <<" cluster:"<<cluster[i]<<" root:"<<root_i<<" "<<j <<" cluster:"<<cluster[j]<<" root:"<<root_j<<endl;
        //if(root_i==root_j){
            //cout << i <<" and "<<j <<" are Same Group."<<endl;
            return root_i==root_j;
        //}
        //else 
          //  return 0;
       /* else
            cout << i <<" and "<<j <<" are Wrong Group"<< endl;
    */
    }

};

#endif