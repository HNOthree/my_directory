import pandas as pd

data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/DESeq2_TE_separated.txt",sep='\t')

TE_list=[]

for i in data.Family:
 if i not in TE_list:
  TE_list.append(i)

want_data=[]
for i in TE_list:
 TE_data=data[data.Family==i]
 male=float(len(TE_data[TE_data.Log2FoldChange>1]))
 female=float(len(TE_data[TE_data.Log2FoldChange<-1]))
 want_data.append([i,TE_data.iloc[0].Superfamily,TE_data.iloc[0].Class,len(TE_data),male,female,len(TE_data)-(male+female)])

want_data=pd.DataFrame(want_data,columns=["Family","Superfamily","Class","Data_count","Male","Female","Neutral"])
want_data.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_count_family_expressed.txt",index=False,sep='\t')
