import pandas as pd

tr_data=pd.read_csv("/mnt/Latipes_merged_transcript.txt",sep='\t')
gene_list=[]

for i in tr_data.Gene_id:
 if i not in gene_list:
  gene_list.append(i)

wantdata=[]
for gene in gene_list:
 tr_list=tr_data[tr_data.Gene_id==gene]
 start=tr_list.sort_values(by=["Transcript_start"]).iloc[0].Transcript_start
 end=tr_list.sort_values(by=["Transcript_end"],ascending=False).iloc[0].Transcript_end
 wantdata.append([gene,start,end,tr_list.iloc[0].Chr,tr_list.iloc[0].Strand])

wantdata=pd.DataFrame(wantdata,columns=["Gene_id","Gene_start","Gene_end","Chr","Strand"])
wantdata.to_csv("Gene.txt",sep='\t',index=False)
