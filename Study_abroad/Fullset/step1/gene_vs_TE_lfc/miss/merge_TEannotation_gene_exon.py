import pandas as pd
TEdata=pd.read_csv("/mnt/Annotation/TE_only_Latipes_annotation_file_purified.gtf",sep="\t",header=None)
Genedata=pd.read_csv("/mnt/Annotation/Latipes_merged_exon_sorted.gtf",sep="\t",header=None)

TEdata=pd.DataFrame(TEdata.loc[:,[0,3,4,6,8]].values,columns=["chr","TE_start","TE_end","TE_strand","TE_info"])
Genedata=pd.DataFrame(Genedata.loc[:,[0,3,4,6,8]].values,columns=["chr","Exon_start","Exon_end",\
"Exon_strand","Exon_info"])
chr_list=[]

for i in  Genedata.chr:
 if i not in chr_list:
  chr_list.append(i)

#chr_list=chr_list[1:2]
#windows=[100,500,1000,5000,10000,50000,100000,500000]
TE_list=[]
TE_transcript_data=[]
for i in chr_list:
 print(i)
 TE_sub_data=TEdata[TEdata.chr==i]
 Gene_sub_data=Genedata[Genedata.chr==i]
 for j in range(len(TE_sub_data)):
  TE_column=TE_sub_data.iloc[j]
  for k in range(len(Gene_sub_data)):
   Gene_column=Gene_sub_data.iloc[k]
   if(TE_column.TE_start<Gene_column.Exon_start and \
   Gene_column.Exon_end>TE_column.TE_end and \
   TE_column.TE_strand==Gene_column.Exon_strand):
    append_data=[]
    if TE_column.TE_info not in TE_list:
     TE_list.append(TE_column.TE_info)
    for l in Gene_column:
     append_data.append(l)
    for l in TE_column[1:]:
     append_data.append(l)
    TE_transcript_data.append(append_data)
   elif(TE_column.TE_end<Gene_column.Exon_start):
    break
index_list=[]
for i in Gene_sub_data:
 index_list.append(i)
for i in TE_sub_data:
 if i=="chr":
  continue
 else:
  index_list.append(i)
TE_transcript_data=pd.DataFrame(TE_transcript_data,columns=index_list)
TE_transcript_data.to_csv("/mnt/Results/exon_TE.txt",sep="\t",index=False)
