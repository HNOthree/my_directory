import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d', help='input directory')
args = parser.parse_args()
input_dir=args.d

distance_file=input_dir+"/Gene_TE_distance_bias_100k.txt"

TE_data=pd.read_csv(distance_file,sep='\t')

superfamily_list=[]
for i in TE_data.Superfamily:
 if i not in superfamily_list:
  superfamily_list.append(i)

distance_list=[1000,5000,10000,25000,50000,100000,500000]
dist=0.0
lessthan_cc_list=[]
between_cc_list=[]
for distance in distance_list:
 subset_less=TE_data[TE_data.Distance<distance]
 print(dist)
 subset_bet=TE_data[TE_data.Distance>dist]
 subset_bet=subset_bet[subset_bet.Distance<distance]
 for SF in superfamily_list:
  all_superfamily_less=subset_less[subset_less.Superfamily==SF]
  malebiased_less=all_superfamily_less[all_superfamily_less.Region=="male"]
  femalebiased_less=all_superfamily_less[all_superfamily_less.Region=="female"]
  biased_less=malebiased_less.append(femalebiased_less)
  non_biased_less=all_superfamily_less[all_superfamily_less.Region=="non_biased_region"]
  all_superfamily_less=all_superfamily_less[["Gene_log2FoldChange","TE_log2FoldChange"]]
  biased_less=biased_less[["Gene_log2FoldChange","TE_log2FoldChange"]]
  non_biased_less=non_biased_less[["Gene_log2FoldChange","TE_log2FoldChange"]]

 
  all_superfamily_bet=subset_bet[subset_bet.Superfamily==SF]
  malebiased_bet=all_superfamily_bet[all_superfamily_bet.Region=="male"]
  femalebiased_bet=all_superfamily_bet[all_superfamily_bet.Region=="female"]
  biased_bet=malebiased_bet.append(femalebiased_bet)
  non_biased_bet=all_superfamily_bet[all_superfamily_bet.Region=="non_biased_region"]

  all_superfamily_bet=all_superfamily_bet[["Gene_log2FoldChange","TE_log2FoldChange"]]
  biased_bet=biased_bet[["Gene_log2FoldChange","TE_log2FoldChange"]]
  non_biased_bet=non_biased_bet[["Gene_log2FoldChange","TE_log2FoldChange"]]

  if(len(all_superfamily_less)>5): 
   all_corr_less=all_superfamily_less.corr()
   lessthan_cc_list.append([SF,distance,len(all_superfamily_less),all_corr_less.iloc[0,1],"ALL"])
  if(len(biased_less)>5):
   biased_corr_less=biased_less.corr()
   lessthan_cc_list.append([SF,distance,len(biased_less),biased_corr_less.iloc[0,1],"biased_region"])
  if(len(non_biased_less)>5):
   non_biased_corr_less=non_biased_less.corr()
   lessthan_cc_list.append([SF,distance,len(non_biased_less),non_biased_corr_less.iloc[0,1],"non_biased_region"])
  
  if(len(all_superfamily_bet)>5):
   all_corr_bet=all_superfamily_bet.corr()
   between_cc_list.append([SF,distance,len(all_superfamily_bet),all_corr_bet.iloc[0,1],"ALL"])
  if(len(biased_bet)>5):
   biased_corr_bet=biased_bet.corr()
   between_cc_list.append([SF,distance,len(biased_bet),biased_corr_bet.iloc[0,1],"biased_region"])
  if(len(non_biased_bet)>5):
   non_biased_corr_bet=non_biased_bet.corr()
   between_cc_list.append([SF,distance,len(non_biased_bet),non_biased_corr_bet.iloc[0,1],"non_biased_region"])
  dist=distance
lessthan_cc_list=pd.DataFrame(lessthan_cc_list,columns=["Superfamily","Distance","Data_count","Correlation_coefficiency","Region"])
between_cc_list=pd.DataFrame(between_cc_list,columns=["Superfamily","Distance","Data_count","Correlation_coefficiency","Region"])
lessthan_cc_list.to_csv("{}/correlation_coefficiency_lessthan_ornon.txt".format(input_dir),sep='\t',index=False)
between_cc_list.to_csv("{}/correlation_coefficiency_between_ornon.txt".format(input_dir),sep='\t',index=False)


