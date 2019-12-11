import pandas as pd

male_region_TE=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/male_region_TE.txt",sep='\t')
TE_exp=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt",sep='\t')
wantdata=pd.DataFrame()

for i in range(len(male_region_TE)):
 TE_info=male_region_TE.iloc[i]
 TE=TE_exp[TE_exp.Family==TE_info.Family]
 ave_lfc=TE.Log2FoldChange.mean()
 TE_info["Ave_lfc"]=ave_lfc
 wantdata=wantdata.append(TE_info)

wantdata=wantdata.reset_index()
wantdata=wantdata[["Family","Ave_lfc"]]
wantdata=wantdata[~wantdata.duplicated()]

countdata=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/csv/count.csv")
wantdata=pd.merge(wantdata,countdata,on="Family",how="right")
wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/csv/male_region_TE_lfc.csv",index=False)
