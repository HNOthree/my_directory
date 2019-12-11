import pandas as pd
threshold=1
enrichdata=pd.read_csv("/home/smiyake/shares/Sho/Bedfiles/25k.bed",sep='\t',names=("Chr","Start_region","End_region","Sexuality"))
closest_data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/DESeq2_TE_separated.txt",sep='\t')

wantdata=[]
for i in range(len(enrichdata)):
 enrich_column=enrichdata.iloc[i]
 candidate=closest_data[closest_data.Chr==enrich_column.Chr]
 same_count=0
 dif_count=0
 for j in range(len(candidate)):
  close_info=candidate.iloc[j]
  startpos=min(close_info.Start_TE,close_info.End_TE)
  endpos=max(close_info.Start_TE,close_info.End_TE)
  if(startpos>enrich_column.Start_region and endpos<enrich_column.End_region):
   if(enrich_column.Sexuality=="male" and close_info.Log2FoldChange>threshold):
    same_count+=1
   elif(enrich_column.Sexuality=="female" and close_info.Log2FoldChange<-threshold):
    same_count+=1
   elif(enrich_column.Sexuality=="male" and close_info.Log2FoldChange<-threshold):
    dif_count+=1
   elif(enrich_column.Sexuality=="female" and close_info.Log2FoldChange>threshold):
    dif_count+=1

 sameprob=same_count/(enrich_column.End_region-enrich_column.Start_region)*100000
 difprob=dif_count/(enrich_column.End_region-enrich_column.Start_region)*100000
 wantdata.append([enrich_column.Chr,enrich_column.Start_region,enrich_column.End_region,enrich_column.Sexuality,sameprob,difprob])

indexes=[]
for i in enrichdata:
 indexes.append(i)
indexes.append("Same_frequency")
indexes.append("Different_frequency")

wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/probability_TE.txt",sep='\t',index=False)
