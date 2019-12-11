import pandas as pd
threshold=1
enrichdata=pd.read_csv("/home/smiyake/shares/Sho/Bedfiles/25k.bed",sep='\t',names=("Chr","Start_region","End_region","Sexuality"))
closest_data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/TE_nearest_gene.txt",sep='\t')

wantdata=[]
for i in range(len(enrichdata)):
 enrich_column=enrichdata.iloc[i]
 candidate=closest_data[closest_data.Chr==enrich_column.Chr]
 same_count=0
 dif_count=0
 for j in range(len(candidate)):
  close_info=candidate.iloc[j]
  startpos=min(close_info.TE_start,close_info.TE_end,close_info.Gene_start,close_info.Gene_end)
  endpos=max(close_info.TE_start,close_info.TE_end,close_info.Gene_start,close_info.Gene_end)
  if(startpos>enrich_column.Start_region and endpos<enrich_column.End_region):
   if(enrich_column.Sexuality=="male" and close_info.TE_log2FoldChange>threshold and close_info.Gene_log2FoldChange>threshold):
    same_count+=1
   elif(enrich_column.Sexuality=="female" and close_info.TE_log2FoldChange<-threshold and close_info.Gene_log2FoldChange<-threshold):
    same_count+=1
   elif(enrich_column.Sexuality=="male" and close_info.TE_log2FoldChange<-threshold and close_info.Gene_log2FoldChange<-threshold):
    dif_count+=1
   elif(enrich_column.Sexuality=="female" and close_info.TE_log2FoldChange>threshold and close_info.Gene_log2FoldChange>threshold):
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
wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/probability.txt",sep='\t',index=False)
