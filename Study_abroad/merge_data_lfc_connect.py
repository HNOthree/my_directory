import pandas as pd

gene_lfc_data=pd.read_csv("/mnt/Results/FvsM_gene_TE_analysis.txt",sep="\t")
TE_lfc_data=pd.read_csv("/mnt/Results/FvsM_gene_TE_analysis_Name_separated_only_TE.txt",sep="\t")

read_name="/mnt/Results/merge_transcript_TE_downstream_overlap.txt"
write_name=read_name.split(".txt")
write_name=write_name[0]
write_name=write_name+"_lfc.txt"
read_pd=pd.read_csv(read_name,sep='\t')

index_list=[]

for i in read_pd:
 index_list.append(i)
index_list.append("Gene_log2FoldChange")
index_list.append("Gene_pvalue")
index_list.append("Gene_padj")
index_list.append("TE_log2FoldChange")
index_list.append("TE_pvalue")
index_list.append("TE_padj")


want_data=[]
for i in range(len(read_pd)):
 col=read_pd.iloc[i]
 Gene=col.Gene_id
 TE=col.TE_name
 Gene_col=gene_lfc_data[gene_lfc_data.Name==Gene]
 TE_col=TE_lfc_data[TE_lfc_data.Name==TE]
 if(len(Gene_col)==0 or len(TE_col)==0):
  continue
 Gene_col=Gene_col.iloc[0]
 TE_col=TE_col.iloc[0]
 input_line=[]
 for j in col:
  input_line.append(j)
 
 input_line.append(Gene_col.log2FoldChange)
 input_line.append(Gene_col.pvalue)
 input_line.append(Gene_col.padj)
 input_line.append(TE_col.log2foldchange)
 input_line.append(TE_col.pvalue)
 input_line.append(TE_col.padj)
 want_data.append(input_line)

want_data_pd=pd.DataFrame(want_data,columns=index_list)
want_data_pd.to_csv(write_name,sep="\t",index=False)

