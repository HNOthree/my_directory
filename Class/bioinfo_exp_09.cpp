#include<iostream>
#include <sstream> 
#include <fstream> 
#include <bitset> 
#include <string>
#include <vector>
using namespace std;
int t= 200 ;
int cell = 500;
string output_file_name="cell_automaton_output.svg";
ofstream output_file(output_file_name);


class automaton{
    public:
    vector <int> cell_number;
    automaton(int cell):cell_number(cell){
        for(int i = 0; i < cell+1; i++) {
            cell_number[i] = 0 ;
        }
    }

    void svg_write(int j){
        for(int i=0;i<cell;i++){
            if(cell_number[i]==1){
                output_file<<"<line x1='"<<i<<"' "
                    <<" y1=' "<<j<<"' "
                    <<" x2=' "<<i+1<<"' "
                    <<" y2=' "<<j<<"' "
                    <<" stroke='black' stroke-width='1'/>"<<endl;
            }
        }
    }

    void overwrite(int input_number,int row){
        automaton present(cell);
        int rule[2][2][2];
        int input_str[8];
        for (int i =7;i>=0;i--){//二進数変換
            int j = input_number%2;
            input_str[i] = j;
            input_number=input_number/2;
        }

        int digit = 8;
        for(int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                for(int k=0;k<2;k++){
                    rule[i][j][k]=input_str[digit-1];
                    digit --;
                    }     
            }
        }
        
        for (int i=0;i<cell;i++){
            if (i==0){
                int t =cell_number[0];
                int t_minus =cell_number[cell-1];
                int t_plus = cell_number[1];
                present.cell_number[i]=rule[t_minus][t][t_plus];
            }
            else if (i ==cell-1){
                int t =cell_number[i];
                int t_minus =cell_number[i-1];
                int t_plus = cell_number[0];
                present.cell_number[i]=rule[t_minus][t][t_plus];
            }
            else {
                int t =cell_number[i];
                int t_minus =cell_number[i-1];
                int t_plus = cell_number[i+1];
                present.cell_number[i]=rule[t_minus][t][t_plus];
            }
        }
        present.svg_write(row);

        for (int i =0;i<cell;i++){
            cell_number[i]=present.cell_number[i];
        }

    }

};


int main(void){
    output_file <<"<svg width='500' height='200' xmlns='http://www.w3.org/2000/svg'>"<<endl;
    automaton past_automaton(cell);
    past_automaton.cell_number[cell/2]=1;
    //present_automaton.cell_number[cell/2]=1;
    
    int input_number;
    cout << "input a rule: "<<endl;
    cin >> input_number;
    


    for (int i =0 ; i<t; i++){
        past_automaton.overwrite(input_number,i);
    
    }

    output_file <<"</svg>"<<endl;
    output_file.close();

    return 0;
}
