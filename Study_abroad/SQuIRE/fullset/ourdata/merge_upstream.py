import pandas as pd

upstream_data=pd.read_csv("/mnt/Annotation/merge_transcript_TE_upstream.txt",sep='\t')
gene_expression=pd.read_csv("/mnt/Result/DESeq2_RefSeq_separated.txt",sep='\t')
TE_expression=pd.read_csv("/mnt/Result/DESeq2_TE_separated.txt",sep='\t')

want_data=[]
index_list=[]
for i in upstream_data:
 index_list.append(i)
for i in gene_expression:
 index_list.append(i)
for i in TE_expression:
 index_list.append(i)
for i in range(0,len(upstream_data)):
 if(i%50000==0):
  print(i,len(upstream_data))
 annotation_col=upstream_data.iloc[i]
 gene_candidate=gene_expression[gene_expression.Gene==annotation_col.Gene_id]
 if(len(gene_candidate)==0):
  continue
 gene_candidate=gene_candidate.iloc[0]
 TE_candidate=TE_expression[TE_expression.Family==annotation_col.TE_name]
 TE_candidate=TE_candidate[TE_candidate.Start_TE==annotation_col.TE_start]
 if(len(TE_candidate)==0):
  continue
 TE_candidate=TE_candidate.iloc[0]
 input_line=[]
 for i in annotation_col:
  input_line.append(i)
 for i in gene_candidate:
  input_line.append(i)
 for i in TE_candidate:
  input_line.append(i)
 want_data.append(input_line)

want_data=pd.DataFrame(want_data,columns=index_list)
want_data.to_csv("/mnt/Result/SQ_upstream_TE_lfc.txt",index=False,sep='\t')
