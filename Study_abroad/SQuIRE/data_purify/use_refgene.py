import pandas as pd

def connect(ref,df):
 merge=pd.merge(ref,df,on="Gene_id")
 return merge

refgene=pd.read_csv("/home/smiyake/shares/Sho/data/refGenes.list",header=None,names=("G")) 
refgene=refgene.rename(columns={"G":"Gene_id"})

data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/Gene_TE_distance.txt",sep='\t')
merge=connect(refgene,data)
merge.to_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/Gene_TE_distance_ref.txt",index=False,sep='\t')

data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/Gene_TE_number.txt",sep='\t')
merge=connect(refgene,data)
merge.to_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/Gene_TE_number_ref.txt",index=False,sep='\t')

data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/TE_nearest_gene.txt",sep='\t')
merge=connect(refgene,data)
merge.to_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/TE_nearest_gene_ref.txt",index=False,sep='\t')


