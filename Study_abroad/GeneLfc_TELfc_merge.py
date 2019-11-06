import pandas as pd

gene_lfc_data=pd.read_csv("/mnt/Results/FvsM_gene_TE_analysis.txt",sep="\t")
TE_lfc_data=pd.read_csv("/mnt/Results/FvsM_gene_TE_analysis_Name_separated_only_TE.txt",sep="\t")
names=["up","down"]
for name in names:
 read_name="/mnt/Results/{}stream_transcripts_TE_separate_info.txt".format(name)
 write_name="/mnt/Results/{}stream_Gene_TE_merge_data.txt".format(name)
 
 with open(write_name,"w")as f_w:
  f_r=open(read_name,"r")
  line=f_r.readline()
  line=line.replace("\n","")
  line+=("\tGene_log2FoldChange\tGene_pvalue\tTE_log2FoldChange\tTE_pvalue\n")
  f_w.write(line)
  line=f_r.readline()
  while line:
   line=line.replace("\n","")
   line=line.split("\t")
   gene=line[0]
   TE=line[1]
   gene_column=gene_lfc_data[gene_lfc_data.Name==gene].iloc[0]
   TE_column=TE_lfc_data[TE_lfc_data.Name==TE].iloc[0]
   line.append(gene_column.log2FoldChange)
   line.append(gene_column.pvalue)
   line.append(TE_column.log2foldchange)
   line.append(TE_column.pvalue)
   f_w.write(str(line[0]))
   for i in line[1:]:
    f_w.write("\t"+str(i))
   f_w.write("\n")
   line=f_r.readline()
