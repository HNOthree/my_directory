from scipy import stats
import pandas as pd
region=["biased_region","non_biased_region"]
length_list=[1000,5000,10000,25000,50000,100000,500000]

data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/correlation_coefficiency_lessthan_ornon.txt",sep='\t')
with open("/home/smiyake/sho/Fullset/SQuIRE/txt/cc_stat.txt","w")as f:
 f.write("Groups\tDistance\tPvalue\n")
 for length in length_list:
  print(length)
  len_data=data[data.Distance==length]
  for i in range(len(region)):
   for j in range(i+1,len(region)):
    print(region[i],region[j])
    a=stats.mannwhitneyu(len_data[len_data.Region==region[i]].Correlation_coefficiency, len_data[len_data.Region==region[j]].Correlation_coefficiency, alternative='two-sided')
    print(a)
    f.write("{}\t{}\t{}\n".format(region[i]+"_"+region[j],length,a.pvalue))

