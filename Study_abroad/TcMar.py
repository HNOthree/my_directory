import pandas as pd
data=pd.read_csv("~/sho/Fullset/txt/downstream_Gene_TE_merge_data.txt",sep='\t')
data=data[data.TE_family=="TcMar-Tc1"]
data=data[data.Distance>100000]
data=data[data.Distance<200000]
data.to_csv("TcMar-Tc1_downstream_100k_200k.csv",index=False)
