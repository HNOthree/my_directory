import pandas as pd
TE_gene=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/Result/Gene_TE_distance.txt",sep='\t')

enrich=pd.read_csv("/home/smiyake/shares/Sho/Bedfiles/25k.bed",sep='\t',header=None,names=("Chr","Start_region","End_region","Sexuality"))

chroms=[]
for i in enrich.Chr:
 if i not in chroms:
  chroms.append(i)

for chrom in chroms:
 chrom_data=TE_gene[TE_gene.Chr==chrom]
 chrom_data.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/{}_GENE_TE_distance.txt".format(chrom),sep='\t',index=False)
