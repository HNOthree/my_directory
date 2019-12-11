import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e', help='bed file(enrich region)')
#parser.add_argument('-t', help='TE annotation file')
parser.add_argument('-o', help='output directory')

args = parser.parse_args()
#TE_path=args.t
enrich_path=args.e
output_dir=args.o


enrich_region=pd.read_csv(enrich_path,sep='\t',header=None,names=("Chr","Start_region","End_region","Sexuality"))
result=pd.read_csv("{}/DESeq2_TE_separated.txt".format(output_dir),sep='\t')
indexes=[]
for i in result:
 indexes.append(i)
indexes.append("Sexuality")
wantdata=pd.DataFrame(columns=["index","Sexuality"])

result=result.reset_index()
#result=result.rename(columns={'genoName':'Chr','genoStart': 'TE_start','strand':'Strand','genoEnd':'TE_end','repName':'Family','repClass':'Class','repFamily':'Superfamily'})
#result=result[["index","Chr","Start_TE","End_TE","Family","Superfamily","Class","Strand"]]
for i in range(len(enrich_region)):
 columns=enrich_region.iloc[i]
 candidate=result[result.Chr==columns.Chr]
 candidate=candidate[candidate.Start_TE>columns.Start_region]
 candidate=candidate[candidate.End_TE<columns.End_region]
 candidate["Sexuality"]=columns.Sexuality#+"actived"
 candidate=candidate[["index","Sexuality"]]
 wantdata=wantdata.append(candidate)

merge_data=pd.merge(result, wantdata, on='index', how='left')
merge_data=merge_data.drop("index", axis=1)
sexuality_data=merge_data.Sexuality.fillna("Other")

merge_data=merge_data.reset_index()

merge_data=merge_data.drop("Sexuality", axis=1)
sexuality_data=sexuality_data.reset_index()
merge_data=pd.merge(merge_data, sexuality_data, on='index', how='left')
merge_data=merge_data.drop("index", axis=1)
result=result.drop("index",axis=1)
result["Sexuality"]="ALL"
merge_data=merge_data.append(result)

merge_data.to_csv("{}/TE_in_enrichregion.txt".format(output_dir),sep='\t',index=False)
