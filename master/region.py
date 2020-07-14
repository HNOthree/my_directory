import region_analysis_lib
import pandas as pd
data=pd.read_csv("/home/shom-research/research/TE_m6A/data/DESeq2_TE_only_modified.txt",sep="\t")
chrom_list=list(set(data.Chromosome))

region=pd.read_csv("/home/shom-research/research/TE_m6A/data/Gene_annotation.txt",sep="\t")
region=region[region.Location!="gene"]
region=region[region.Location!="transcript"]

indexes=[]
for i in data:
    indexes.append(i)
indexes.append("Region")

for chrom in chrom_list:
    print(chrom)
    region_analysis_lib.region(indexes,chrom,data,region)