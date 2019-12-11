import pandas as pd

intron_data=pd.read_csv("/mnt/Annotation/Latipes_merged_intron.txt",sep="\t")
TE_data=pd.read_csv("/mnt/Annotation/TE_only_Latipes_annotation_sig_diff.txt",sep="\t")

merge_all_data=[]
threshold=4
for i in range(0,int(len(intron_data)/4)):
#for i in range(1000):
 if(i%1000==0):
  print(i,len(intron_data))
 intron_col=intron_data.iloc[i]
 candidate=TE_data[TE_data.Chr==intron_col.Chr]
 for j in range(len(candidate)):
  candidate_col=candidate.iloc[j]
  satisfied=[]
  if(intron_col.Intron_end<candidate_col.TE_start):
   break

  elif(candidate_col.TE_start>intron_col.Intron_start and \
   candidate_col.TE_end<intron_col.Intron_end and \
   candidate_col.Strand==intron_col.Strand):
    candidate_col=candidate_col.drop("Chr")
    candidate_col=candidate_col.drop("Strand")
    for k in candidate_col:
     satisfied.append(k)

    input_data=[]
    for k in intron_col:
     input_data.append(k)
    for k in satisfied:
     input_data.append(k)
    merge_all_data.append(input_data)

indexes=[]
for i in intron_data:
 indexes.append(i)
for i in TE_data:
 if(i!="Chr" and i!="Strand"):
  indexes.append(i)

merge_all_data_pd=pd.DataFrame(merge_all_data,columns=indexes)

merge_all_data_pd.to_csv("/mnt/Results/intron_Gene_TE_merge_data.txt",sep='\t',index=False)

