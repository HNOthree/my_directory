

void svg_make(int seq1_length,int seq2_length){
    //string a = "1test" ;
    cout<< seq1_length <<endl;
    output_file <<"<svg width='3000' height='2000' xmlns='http://www.w3.org/2000/svg'>"<<endl;
    output_file <<"<line x1 ='30' y1 = '50' x2='"<<30+seq1_length<<"' y2 = '50' height = '100' stroke-width = '10' stroke='blue'/>"<<endl;
    output_file <<"<line x1 ='30' y1 = '700' x2='"<<30+seq2_length<<"' y2 = '700' stroke-width = '10' stroke='red'/>"<<endl;

}

void svg_make(int feature[4],double energy,int seq2_length){
    int seq1_start = feature[0];
    int seq1_end = feature[1];
    int seq2_start = seq2_length -feature[2];
    int seq2_end = seq2_length - feature[3];
    output_file << "<polygon points = '" 
        << seq1_start << ",50 "
        << seq2_end << ",700 "
        << seq2_start << ",700 "
        << seq1_end << ",50 ' "
        <<"stroke-opacity = '"
        << - energy/20.0
        <<"'/>" << endl;

    output_file << seq1_start << seq1_end<<endl;
    //return b ;
}