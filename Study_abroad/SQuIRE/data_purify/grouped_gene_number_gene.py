import pandas as pd

data=pd.read_csv("SQuIRE_gene_TE_distance.txt",sep='\t')
indexes=[]
wantdata=[]
for i in data:
 indexes.append(i)
indexes.append("Number")
indexes.append("Direction_number")
gene_list=[]
for i in data.Gene_id:
 if i not in gene_list:
  gene_list.append(i)

locations=["upstream","downstream"]

for location in locations:
 d_data=data[data.Location==location]
 for gene in gene_list:
  gene_data=d_data[d_data.Gene_id==gene]
  sort_gene_data=gene_data.sort_values("Distance")
  for i in range(0,len(sort_gene_data)):
    columns=sort_gene_data.iloc[i]
    col=[]
    for j in columns:
     col.append(j)
    col.append(i+1)
    if(location=="upstream"):
     col.append(-(i+1))
    else:
     col.append(i+1)
    wantdata.append(col)

wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv("SQuIRE_gene_TE_number_gene.txt",index=False)
