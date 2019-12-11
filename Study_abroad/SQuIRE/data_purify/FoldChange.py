import pandas as pd
import math
data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/SQuIRE_gene_TE_number_purified.txt",sep='\t')
indexes=[]
for i in data:
 indexes.append(i)
indexes.append("Log2gene_over_TE")
wantdata=[] 
for i in range(0,len(data)):
 columns=data.iloc[i]
 input_line=[]
 for j in columns:
  input_line.append(j)
 input_line.append(math.log2((2**columns.Gene_log2FoldChange)/(2**columns.TE_log2FoldChange)))
 wantdata.append(input_line)

wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/SQuIRE_gene_TE_number_purified_division.txt",sep='\t',index=False)
