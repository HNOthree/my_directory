#A script to make a data grouped by family
import pandas as pd

data=pd.read_csv("/mnt/Results/step2/upstream_transcripts_TE_overlap_lfc.txt",sep='\t')
print(data.head(5))
mean_data=data.groupby(['TE_name','TE_family',"TE_Class"]).mean()
mean_data=mean_data.reset_index()
print(mean_data.head(5))

mean_family=[]
for i in range(len(mean_data)):
 col=mean_data.iloc[i]
 TE_name=col.TE_name
 lfc_mean=col.Gene_log2FoldChange
 mean_family.append([TE_name,col.TE_family,col.TE_Class,lfc_mean,col.TE_log2FoldChange])

mean_family=pd.DataFrame(mean_family,columns=["TE_family","TE_superfamily","TE_Class","gene_log2FC_mean","TE_log2FC"])
mean_family.to_csv("/mnt/Results/step2/upstream_overlap_groupby_family.txt",sep='\t',index=False)
