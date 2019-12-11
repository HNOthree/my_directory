import pandas as pd
windows=[500,1000,5000,10000,50000]
all_upstream_data=pd.read_csv("/home/smiyake/scp/step1/Results/step1/merge_transcript_TE_upstream_50000_lfc.txt",sep='\t')


minimum=0
for window in windows:
 want_data=[]
 candidate=all_upstream_data[all_upstream_data.Distance>minimum]
 candidate=candidate[candidate.Distance<window]
 gene_mean=candidate.groupby(["TE_name","TE_family","TE_Class"]).mean()
 gene_mean=gene_mean.reset_index()
 for i in range(len(gene_mean)):
  col=gene_mean.iloc[i]
  want_data.append([col.TE_name,col.TE_family,col.TE_Class,col.TE_log2FoldChange,col.Gene_log2FoldChange])
 want_data=pd.DataFrame(want_data,columns=["TE_family","TE_superfamily","TE_class","TE_log2FC","Gene_log2FC_mean"])
 want_data.to_csv("/home/smiyake/sho/Fullset/txt/step2/upstream_{}_{}_groupby_family.txt".format(minimum,window),sep='\t',index=False)
 minimum=window
