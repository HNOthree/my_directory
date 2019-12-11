import pandas as pd
threshold="25"
enrich_region=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/{}k.txt".format(threshold),sep='\t')

result=pd.read_csv("/home/smiyake/shares/Sho/data/Annotation/TE_only_Latipes_annotation_purified.txt",sep='\t')
indexes=[]
for i in result:
 indexes.append(i)
indexes.append("Sexuality")
wantdata=pd.DataFrame(columns=["index","Sexuality"])

result=result.reset_index()
for i in range(len(enrich_region)):
 columns=enrich_region.iloc[i]
 print(columns.Sexuality)
 candidate=result[result.Chr==columns.Chr]
 candidate=candidate[candidate.TE_start>columns.Start_region]
 candidate=candidate[candidate.TE_end<columns.End_region]
 candidate["Sexuality"]=columns.Sexuality#+"actived"
 candidate=candidate[["index","Sexuality"]]
 wantdata=wantdata.append(candidate)

print(len(wantdata))
merge_data=pd.merge(result, wantdata, on='index', how='left')
merge_data=merge_data.drop("index", axis=1)
sexuality_data=merge_data.Sexuality.fillna("Other")

merge_data=merge_data.reset_index()

merge_data=merge_data.drop("Sexuality", axis=1)
sexuality_data=sexuality_data.reset_index()
merge_data=pd.merge(merge_data, sexuality_data, on='index', how='left')
merge_data=merge_data.drop("index", axis=1)
print(merge_data)
result=result.drop("index",axis=1)
result["Sexuality"]="ALL"
merge_data=merge_data.append(result)
print(result)

print(len(merge_data))
merge_data.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_in_enrichregion_{}k_all.txt".format(threshold),sep='\t',index=False)
