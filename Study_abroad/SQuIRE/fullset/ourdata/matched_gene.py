import pandas as pd

family=input()

TE_data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/SQUIRE_data/squire_fetch/TE_only_Latipes_annotation_file_modified_unknown.txt",sep='\t')

gene_data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/Gene.txt",sep='\t')

family_TE=TE_data[TE_data.repName==family]


matched_data=pd.DataFrame()

for i in range(len(family_TE)):
 print(i,len(family_TE))
 TE_col=family_TE.iloc[i]
 gene_candidate=gene_data[gene_data.Chr==TE_col.genoName]
 can=gene_candidate[TE_col.genoStart>gene_candidate.Gene_start]
 can=can[TE_col.genoEnd<can.Gene_end]
 can=can[can.Strand==TE_col.strand]
 can=can[can.Gene_end-can.Gene_start<2000]
 matched_data=matched_data.append(can)

print(matched_data)
