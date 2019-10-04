#!/usr/bin/env python
#$ -S $HOME/.pyenv/shims/python
#$ -l debug
#$ -cwd
import pandas as pd

def get_seq(chromosome,start,end,strand,window):
    test_data = open("/home/shom-research/research/m6A/{}.txt".format(chromosome), "r")
    sequence=test_data.read()
    target_seq=sequence[start-window:end+window]
    target_seq=bigletter(target_seq)
    if(strand=="-"):
        target_seq=convert(target_seq)
    return target_seq

def bigletter(seq):
    new_seq=""
    for i in seq:
        if(i=="a"):
            new_seq+="A"
        elif(i=="g"):
            new_seq+="G"
        elif(i=="c"):
            new_seq+="C"
        elif(i=="t"):
            new_seq+="T"
        else:
            new_seq+=i
    return new_seq

def convert(sequence):
    
    i=len(sequence)-1
    convert_seq=""
    while(i>=0):
        letter=sequence[i]
        if(letter=="A"):
            convert_seq+="T"
        elif(letter=="T"):
            convert_seq+="A"
        elif(letter=="G"):
            convert_seq+="C"
        elif(letter=="C"):
            convert_seq+="G"
        else:
            print("ERROR")
        i-=1
    
   
    return convert_seq

def for_miRNA(seq):
    new_seq=""
    for i in seq:
        if(i=="A"):
            new_seq+="U"
        elif(i=="T"):
            new_seq+="A"
        elif(i=="G"):
            new_seq+="C"
        elif(i=="C"):
            new_seq+="G"
    new_seq=new_seq[::-1]
    return new_seq

def miRNA_combine(sequence,miRNA):
    seed=miRNA[1:8]
    location=[]
    for i in range(0,len(sequence)-len(seed)+1):
        candidate=for_miRNA(sequence[i:i+7])
        
        if(seed==candidate):
            print(sequence,candidate,seed)
            over=float(i)+len(seed)
            under=float(len(sequence))
            loc=over/under
            location.append(loc)
    

    return location



def calculate(ythdf1_list,miRNA):
     

    window=0
    while(window<=500):
        count_list=[]
        for i in range(len(ythdf1_list)):
            if(i%1000==0):
                print(i,len(ythdf1_list))
            row=ythdf1_list.iloc[i]
            chromosome=row.Chromosome.lower()
            if ("m" in chromosome):
                chromosome=chromosome.replace("m","M")
            elif ("x" in chromosome):
                chromosome=chromosome.replace("x","X")
            elif ("y" in chromosome):
                chromosome=chromosome.replace("y","Y")
            start=int(row.Start)
            end=int(row.End)
            strand=row.Strand
            gene=row.Gene_symbol
            sequence=get_seq(chromosome,start,end,strand,window)

            miRNA_bind_list=miRNA_combine(sequence,miRNA)
            if (len(miRNA_bind_list)!=0):
                for k in miRNA_bind_list:
                    count_list.append([gene,chromosome,start,end,strand,k])
                    print(gene,chromosome,start,end,strand,sequence,k)

        
        count_list=pd.DataFrame(count_list,columns=["Gene_symbol","Chromosome","Start","End","Strand","location"])
        count_list.to_csv("/home/shom-research/research/m6A/miRNA155_{}overlap_count.csv".format(window),index=False)
        window+=25

def main():
    rep1_ythdf1_list=pd.read_csv("/home/shom-research/research/m6A/PARCLIP_1.csv")
    rep2_ythdf1_list=pd.read_csv("/home/shom-research/research/m6A/PARCLIP_2.csv")
    ythdf1_list=rep1_ythdf1_list.append(rep2_ythdf1_list)

    miRNA155="UUAAUGCUAAUCGUGAUAGGGGUU"
    miRNA1="UGGAAUGUAAAGAAGUAUGUAU"

    #calculate(ythdf1_list,miRNA1)
    calculate(ythdf1_list,miRNA155)


main()