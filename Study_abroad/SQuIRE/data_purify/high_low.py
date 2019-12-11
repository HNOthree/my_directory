import pandas as pd

enrich=pd.read_csv("/home/smiyake/shares/Sho/Bedfiles/25k.bed",sep='\t',header=None,names=("Chr","Start_region","End_region","Sexuality"))

chromosomes=[]

for i in enrich.Chr:
 if i not in chromosomes:
  chromosomes.append(i)


wantdata=[]
for chrom in chromosomes:
 TE_gene_chr=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/txt/{}_GENE_TE_distance.txt".format(chrom),sep='\t')
 indexes=[]
 for index in TE_gene_chr:
  indexes.append(index)
 indexes.append("Region")
 enrich_chr=enrich[enrich.Chr==chrom]
 print(chrom,len(TE_gene_chr),len(enrich_chr))
 for i in range(len(TE_gene_chr)):
  TE_gene_info=TE_gene_chr.iloc[i]
  for j in range(len(enrich_chr)):
   enrich_region=enrich_chr.iloc[j]
   if(TE_gene_info.TE_start>enrich_region.Start_region and TE_gene_info.TE_end<enrich_region.End_region):
    input_line=[]
    for a in TE_gene_info:
     input_line.append(a)
    input_line.append("biased_region")
    wantdata.append(input_line)
    break
   elif(j==len(enrich_chr)-1):
    input_line=[]
    for a in TE_gene_info:
     input_line.append(a)
    input_line.append("non_biased_region")
    wantdata.append(input_line)
wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_distance_bias.txt",sep='\t',index=False)
