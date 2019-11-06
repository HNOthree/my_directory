import pandas as pd
TE_list=pd.read_csv("/mnt/Result/DESeq2_TE_separated.txt",sep='\t')
gene_list=pd.read_csv("/mnt/Annotation/ourLat_gene_transcript.txt",sep='\t')
gene_expression=pd.read_csv("/mnt/Result/DESeq2_RefSeq_separated.txt",sep='\t')
chr_list=[]
for i in TE_list.Chr:
 if i not in chr_list:
  chr_list.append(i)

want_data=[]
index_list=["Gene_id","Transcript_id","Chr","Gene_log2FoldChange","Gene_lfcSE","Gene_pvalue","Gene_padj","TE_number","Family","Superfamily","Class","TE_start","TE_end","TE_log2FoldChange","TE_lfcSE","TE_pvalue","TE_padj"]
for chromosome in chr_list:
 print(chromosome)
 TE_sub=TE_list[TE_list.Chr==chromosome]
 gene_sub=gene_list[gene_list.Chr==chromosome]
 TE_sub=TE_sub.sort_values("Start_TE")
 gene_sub=gene_sub.sort_values("Transcript_start")
 #print(gene_sub.head(10))
 #print(TE_sub.head(10))
 flag=0 
 for i in range(len(gene_sub)):
  count=0
  if(i%100==0):
   print(i,len(gene_sub))
  gene_col=gene_sub.iloc[i]
  for j in range(flag,len(TE_sub)):
   TE_col=TE_sub.iloc[j]
   if(TE_col.Start_TE>gene_col.Transcript_end):
    break
   elif(gene_col.Transcript_start<TE_col.Start_TE and gene_col.Transcript_end>TE_col.End_TE):
    #print(gene_col,TE_col)
    if(count==0):
     count=1
     flag=j
    if (gene_col.Strand==TE_col.Strand):
     input_line=[]
     gene_ex_col=gene_expression[gene_expression.Gene==gene_col.Gene_id]
     if(len(gene_ex_col)>1):
      print(gene_ex_col)
     gene_ex_col=gene_ex_col.iloc[0]
     input_line.append(gene_col.Gene_id)
     input_line.append(gene_col.Transcript_id)
     input_line.append(gene_col.Chr)
     input_line.append(gene_ex_col.Log2FoldChange)
     input_line.append(gene_ex_col.LfcSE)
     input_line.append(gene_ex_col.Pvalue)
     input_line.append(gene_ex_col.Padj)
     input_line.append(TE_col.number)
     input_line.append(TE_col.Start_TE)
     input_line.append(TE_col.End_TE)
     input_line.append(TE_col.Family)
     input_line.append(TE_col.Superfamily)
     input_line.append(TE_col.Class)
     input_line.append(TE_col.Log2FoldChange)
     input_line.append(TE_col.LfcSE)
     input_line.append(TE_col.Pvalue)
     input_line.append(TE_col.Padj)
     want_data.append(input_line)

want_data=pd.DataFrame(want_data,columns=index_list)
want_data.to_csv("/mnt/Result/TE_transcript_merge.txt",sep='\t',index=False)
