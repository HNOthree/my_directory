import pandas as pd

result=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_nearest_gene.txt",sep='\t')
TE_data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt",sep='\t')
gene_data=pd.read_csv("/home/smiyake/shares/Sho/Latipes_Expression_table.csv",sep='\t')
threshold=[0.01,0.05,0.1,0.15,0.2,0.25,0.3,0.5]

wantdata=[]
for i in threshold:
 input_line=[]
 for j in threshold:
  TE_thre=TE_data.Log2FoldChange.quantile(1-i)
  gene_thre=gene_data.logFC.quantile(1-j)
  print(1-i,1-j)
  data=result[result.TE_log2FoldChange>TE_thre]
  data=data[data.Gene_log2FoldChange>gene_thre]
  print(len(data))
  input_line.append(len(data))
 wantdata.append(input_line)

wantdata=pd.DataFrame(wantdata,columns=threshold)
wantdata.to_csv("satisdfied_TE_andgene.csv",index=False)
