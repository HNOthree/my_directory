import pandas as pd

nearest_data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/TE_nearest_gene_ref.txt",sep='\t')

expressed_data=pd.read_csv("/home/smiyake/shares/Sho/data/Annotation/TE_only_Latipes_annotation_purified.txt",sep='\t')
#expressed_data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/DESeq2_TE_separated.txt",sep='\t')

TE_family=[]

for i in expressed_data.Name:
 if i not in TE_family:
  TE_family.append(i)

wantdata=[]
threshold=5

indexes=["Family","Expressing_location"]
for i in range(1,threshold+1):
 indexes.append("Morethan{}".format(str(i)))


for family in TE_family:
 TE_nearest=nearest_data[nearest_data.Family==family]
 TE_expressed=expressed_data[expressed_data.Name==family]
 input_data=[]
 input_data.append(family)
 input_data.append(len(TE_expressed))
 for i in range(1,threshold+1):
  if(len(TE_nearest)==0):
   input_data.append(0)
  else:
   lendata=TE_nearest[abs(TE_nearest.Gene_log2FoldChange)>i]
   lendata=TE_nearest[abs(TE_nearest.TE_log2FoldChange)>i]
   input_data.append(len(lendata))
 wantdata.append(input_data)


wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/family_nearestgene_count_ref.txt",index=False,sep='\t')
