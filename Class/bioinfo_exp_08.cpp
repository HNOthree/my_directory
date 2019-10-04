
#include <iostream>
#include <fstream>
#include <math.h>
#include<sstream>
#include<map>
#include<string>


using namespace std;
string output_file_name="output.svg";
ofstream output_file(output_file_name);
int five_prime_x[2] = {30,30};
int five_prime_y[2] = {50,700};
string color[2] ={"blue","red"};
int second_five_prime_x = 30;
int second_five_prime_y = 700;

double sigmoid(double x) {
    return 1.0 / (1.0 + exp( x+11 ));
}

void svg_make(int seq1_length,int seq2_length){
    int seq_length[2];
    seq_length[0] = seq1_length;
    seq_length[1] = seq2_length;
    output_file <<"<svg width='3000' height='2000' xmlns='http://www.w3.org/2000/svg'>"<<endl;
    for (int i = 0 ; i<2 ; i++){
        if (i ==0){
            output_file<<"<text x = '"
                <<five_prime_x[i]-20 <<"' y='"
                <<five_prime_y[i]<<"' font-size='40' > 5' </text> c"<<endl;
            output_file<<"<text x = '"
                <<five_prime_x[i]+20+seq_length[i] <<"' y='"
                <<five_prime_y[i]<<" ' font-size='40' > 3' </text>"<<endl;
                
            }
        else{
                output_file<<"<text x = '"
                    <<seq_length[i]- five_prime_x[i]+50 <<"' y='"
                    <<five_prime_y[i]<<" ' font-size='40' > 5' </text>"<<endl;
                output_file<<"<text x = '"
                    <<five_prime_x[i]-20 <<"' y='"
                    <<five_prime_y[i]<<" ' font-size='40' > 3' </text>"<<endl;
        }
    }
    for (int i = 0 ;i<2 ;i++){
        output_file <<"<line x1 ='" <<five_prime_x[i]
                    <<    "' y1 = '"<<five_prime_y[i]
                    <<    "' x2='"<<five_prime_x[i] + seq_length[i]
                    <<    "' y2 = '" << five_prime_y[i]
                    <<"' height = '100' stroke-width = '10' stroke='"
                    << color[i]
                    <<"'/>"<<endl;
    }
}

void svg_make(int feature[4],double energy,int seq2_length){
    int seq1_start = feature[0];
    int seq1_end = feature[1];
    int seq2_start = seq2_length - feature[2];
    int seq2_end = seq2_length -  feature[3];
    output_file << "<polygon points = '" 
        << five_prime_x[0] + seq1_start << ","
        << five_prime_y[0] << " "
        << five_prime_x[0] + seq2_end << ","
        << five_prime_y[1] << " "
        << five_prime_x[1] + seq2_start << ","
        << five_prime_y[1] << " "
        << five_prime_x[1] +seq1_end << ","
        << five_prime_y[0] << " ' "
        <<"fill-opacity = '"
        << sigmoid(energy)
        <<"'/>" << endl;
}





int main(void){
    string file_name= "figure_list.txt";
    
    ifstream ist(file_name);
    if(!ist){
        cerr << "Cannot open friend_list.txt" << endl;
        exit(1);
    }
    int row = 1;

    while(!ist.eof()){
        string s;
        getline(ist,s);
        
        int  seq1_length, seq2_length;
        int feature[4];
        double energy;

        if (row == 1 ){ 
            istringstream num_list(s);
            num_list>>seq1_length >> seq2_length;
            svg_make(seq1_length,seq2_length);
            row ++;
        }
        else{
            istringstream num_list(s);
            for (int i =0;i<4;i++){
                num_list>>feature[i];
            }
            num_list>> energy;
            svg_make(feature,energy,seq2_length);
        }
    }

    
        
    
    output_file <<"</svg>"<<endl;
    output_file.close();

    return 0;

}
