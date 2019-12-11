import pandas as pd

male_enrich=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/csv/count.csv")
TE_annotation=pd.read_csv("/home/smiyake/shares/Sho/data/Annotation/TE_only_Latipes_annotation_purified.txt",sep='\t')
wantdata=pd.DataFrame()
for i in range(len(male_enrich)):
 male_column=male_enrich.iloc[i]
 TE=TE_annotation[TE_annotation.Name==male_column.Family]
 male_column["Frequency"]=male_column.Count/len(TE)
 wantdata=wantdata.append(male_column)

wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/csv/count_probability.csv",index=False)
