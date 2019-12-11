import pandas as pd
exp_data=pd.read_csv("Latipes_Expression_table.csv",sep='\t')
TE_data=pd.read_csv("DESeq2_TE_separated.txt",sep='\t')
annotation=pd.read_csv("SQuIRE_gene_TE_distance.txt",sep='\t')
indexes=[]
for i in annotation:
 indexes.append(i)
want_data=[]
for i in range(0,len(annotation)):
 an_annotation=annotation.iloc[i]
 gene=an_annotation.Gene_id
 TE=an_annotation.Family
 Start=an_annotation.TE_start
 gene_lfc_data=exp_data[exp_data.Gene==gene].iloc[0]
 gene_lfc=gene_lfc_data.logFC
 TE_lfc_data=TE_data[TE_data.Family==TE]
 TE_lfc_data=TE_lfc_data[TE_lfc_data.Start_TE==Start].iloc[0]
 TE_lfc=TE_lfc_data.Log2FoldChange
 
 want_data.append([an_annotation.Gene_id,an_annotation.Distance,an_annotation.Gene_start,an_annotation.Gene_end,an_annotation.Family,an_annotation.Class,an_annotation.Superfamily,an_annotation.TE_start,an_annotation.TE_end,gene_lfc,TE_lfc,gene_lfc-TE_lfc,an_annotation.Location,an_annotation.Strand])

want_data=pd.DataFrame(want_data,columns=indexes)
want_data.to_csv("Gene_TE_distance_lfc.txt",index=False,sep='\t')
