
def region(indexes,chrom,data,region):  
    import pandas as pd
    want_data=pd.DataFrame(columns=indexes)

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
    cut_want_data.to_csv("/home/shom-research/research/TE_m6A/data/deseq2_region_{}.txt".format(chrom),index=False,sep="\t")