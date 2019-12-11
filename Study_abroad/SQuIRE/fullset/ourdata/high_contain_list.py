import pandas as pd

data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/probability.txt",sep='\t')
TE=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt",sep='\t')

high_contain=data[data.Same_frequency>10]
print(high_contain)

wantdata=pd.DataFrame()

for i in range(0,len(high_contain)):
 high_col=high_contain.iloc[i]
 candidate=TE[TE.Chr==high_col.Chr]
 candidate=candidate[candidate.Start_TE>high_col.Start_region]
 candidate=candidate[candidate.End_TE<high_col.End_region]
 wantdata=wantdata.append(candidate)
wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/male_region_TE.txt",sep='\t',index=False)
