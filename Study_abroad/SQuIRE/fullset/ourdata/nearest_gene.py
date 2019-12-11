import pandas as pd

data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_number.txt",sep='\t')
#data=data.head(1000)
near_gene=data[data.Number==1]

i_near_gene = near_gene.groupby(["Family","TE_start"])
nearest=near_gene.loc[i_near_gene['Distance'].idxmin(),:]
print(nearest)
nearest.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_nearest_gene.txt",sep='\t',index=False)
