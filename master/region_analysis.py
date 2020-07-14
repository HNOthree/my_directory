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
want_data=pd.DataFrame()

for chrom in chrom_list:
    print(chrom)
    subset_m6A=data[data.Chromosome==chrom]
    subset_region=region[region.Chromosome==chrom]
    for i in range(len(subset_region)):
        region_can=subset_region.iloc[i]
        candidate=subset_m6A[subset_m6A.Start>region_can.Start]
        candidate=candidate[candidate.End<region_can.End]
        candidate=candidate[candidate.Strand==region_can.Strand]
        candidate["Region"]=region_can.Location
        candidate["Region_start"]=region_can.Start
        candidate["Region_end"]=region_can.End
        want_data=want_data.append(candidate)


cut_want_data=want_data[~want_data.duplicated()]
cut_want_data.to_csv("/home/shom-research/research/TE_m6A/data/deseq2_region.txt",index=False,sep="\t")