#ifndef BIOINFO_EXP_011_H
#define BIOINFO_EXP_011_H

using namespace std;

int N ;

class QueenLocation{

    public:
    stack<int> location_i;
    stack<int> location_j;

    QueenLocation(){}
    
    void display(){
        int queen_matrix[N][N];
        for (int i =0;i<N;i++){
            for(int j=0;j<N;j++){
                queen_matrix[i][j]=0;
            }
        }

        stack<int> ref_i ;
        stack<int> ref_j ;

        while(location_j.size()!=0){
            int location_x =location_i.top();
            int location_y =location_j.top();
            queen_matrix[location_x][location_y]=1;
            ref_i.push(location_x);
            ref_j.push(location_y);
                //cout<<"poped"<<location_i.top()<<endl;
            location_i.pop();
            location_j.pop();
                //cout<<"Latter size"<<location_i.size()<<endl;
            //cout<<judge<<endl;
        }   
        for (int i =0;i<N;i++){
            for(int j=0;j<N;j++){
                cout<<queen_matrix[i][j];
            }
            cout<<endl;        
        }
        while(ref_i.size()!=0){
            location_i.push(ref_i.top());
            location_j.push(ref_j.top());
            ref_i.pop();
            ref_j.pop();
        }
        cout<<endl;

    }

    void set_queen(int i ,int j){
        int index[3] ;
        index[0]=column_search(i);
        index[1]=row_search(j);
        index[2]=diagonal_search(i,j);
        //cout<<"index"<<index[0]<<index[1]<<index[2]<<endl;
        int total_index=(index[0]*index[1]*index[2]);
        if(total_index==1){
            //cout<<"Pushed"<<i<<" "<<j<<endl;
            location_i.push(i);
            location_j.push(j);
        }
    //cout<<"End"<<endl;
    }

    bool column_search(int i){
        stack<int> ref ;
        int judge=true;
        while(location_i.size()!=0){
            //cout<<"Former Size"<<location_i.size()<<endl;
            int location =location_i.top();
            if (location ==i){
                //cout<<"Find same value"<<endl;
                judge = false;
                break;
            }
            else{
                ref.push(location);
                //cout<<"poped"<<location_i.top()<<endl;
                location_i.pop();
                //cout<<"Latter size"<<location_i.size()<<endl;
                judge=true;
            }
            //cout<<judge<<endl;
        }   
        while(ref.size()!=0){
            location_i.push(ref.top());
            ref.pop();
        }
    return judge;
    }
    bool row_search(int j){
        stack<int> ref ;
        int judge=true;
        while(location_j.size()!=0){
            //cout<<"Former Size"<<location_i.size()<<endl;
            int location =location_j.top();
            if (location ==j){
                //cout<<"Find same value"<<endl;
                judge = false;
                break;
            }
            else{
                ref.push(location);
                //cout<<"poped"<<location_i.top()<<endl;
                location_j.pop();
                //cout<<"Latter size"<<location_i.size()<<endl;
                judge=true;
            }
            //cout<<judge<<endl;
        }   
        while(ref.size()!=0){
            location_j.push(ref.top());
            ref.pop();
        }
    return judge;

    }
    bool diagonal_search(int i,int j){
        stack<int> ref_i ;
        stack<int> ref_j ;
        //cout<<"Turn"<<i<<j<<endl;
        //int distance=abs(i-j);
        int judge=true;
        while(location_j.size()!=0){
            //cout<<"Former Size"<<location_i.size()<<endl;
            int location_x =location_i.top();
            int location_y =location_j.top();
            //cout<<"abs i-j:"<<abs(i-j)<<endl;
            //cout<<"abs ref i-j:"<<abs(location_x-location_y)<<endl;
            if (abs(location_x-i)==abs(location_y-j)){
                //cout<<"Find same value"<<endl;
                judge = false;
                break;
            }
            else{
                ref_i.push(location_x);
                ref_j.push(location_y);
                //cout<<"poped"<<location_i.top()<<endl;
                location_i.pop();
                location_j.pop();
                //cout<<"Latter size"<<location_i.size()<<endl;
                judge=true;
            }
            //cout<<judge<<endl;
        }   
        while(ref_i.size()!=0){
            location_i.push(ref_i.top());
            location_j.push(ref_j.top());
            ref_i.pop();
            ref_j.pop();
        }
    return judge;
    }


};

#endif