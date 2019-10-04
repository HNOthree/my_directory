from Bio import SeqIO
# pd.DataFrame(...)が呼び出せるように書いてください
# "pandasをpdと言う名前でインポート" 
import pandas as pd
# # plt.figure()を実行できるように書いてください
# "matplotlibのpyplotモジュールをpltという名前でインポート"
import matplotlib.pyplot as plt
# import copy


def dictionary_make(length):
    dictionary={}
    DNA=["A","T","G","C"]
    kmer=["A","T","G","C"]
    while (len(kmer[0])<length):
        new_kmer=[]
        for seq in kmer:
            for base in DNA:
                new_kmer.append(seq+base)
        kmer=new_kmer
    for sequence in kmer: 
        dictionary[sequence]=0
    return dictionary

def get_seq():
    path_to_genbank_file = ("GCF_000231385.2_ASM23138v3_genomic.gbff") 
    records = SeqIO.index(path_to_genbank_file, 'gb')
    record = records[list(records.keys())[0]]
    bacteria_sequence=record.seq
    
    return bacteria_sequence

def kmer_count(kmer_dict,length,DNA):
    for i in range(0,len(DNA)-length):
        seq=DNA[i:i+length]
        kmer_dict[seq]+=1
    return kmer_dict

def dict_to_df(dictionary):
    data=[]
    for i,j in dictionary.items():
        data.append([i,j])
    data=pd.DataFrame(data,columns=["kmer","count"])
    return data

def main():
    bacteria_sequence=get_seq()
    length=3
    max_kmer=12
    while(length<=max_kmer):
        kmer_dict=dictionary_make(length)
        kmer_dict=kmer_count(kmer_dict,length,bacteria_sequence)
        kmer_df=dict_to_df(kmer_dict)
        kmer_df.to_csv("{}mer_count.csv".format(length),index=False)
        length+=1

main()