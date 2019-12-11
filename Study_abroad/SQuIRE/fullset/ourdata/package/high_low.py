import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d', help='input directory')
parser.add_argument('-e', help='enrichment file')
args = parser.parse_args()
input_dir=args.d
enrichment_file=args.e
out_dir=input_dir+"/Gene_TE_distance_bias_ref.txt"


enrich=pd.read_csv(enrichment_file,sep='\t',header=None,names=("Chr","Start_region","End_region","Sexuality"))

chromosomes=[]

for i in enrich.Chr:
 if i not in chromosomes:
  chromosomes.append(i)


wantdata=[]
for chrom in chromosomes:
 TE_gene_chr=pd.read_csv("{}/{}_GENE_TE_distance_ref.txt".format(input_dir,chrom),sep='\t')
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
    input_line.append(enrich_region.Sexuality)
    wantdata.append(input_line)
    break
   elif(j==len(enrich_chr)-1):
    input_line=[]
    for a in TE_gene_info:
     input_line.append(a)
    input_line.append("non_biased_region")
    wantdata.append(input_line)
wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv(out_dir,sep='\t',index=False)
