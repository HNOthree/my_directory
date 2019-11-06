import pandas as pd
with open("/mnt/Annotation/Latipes_merged_exon_sorted.gtf") as f:
 line=f.readline()

 exon_all_data=[]
 while line:
  input_line=[]
  line=line.replace("\n","")
  sep_line=line.split("\t")
  for j in sep_line[:-1]:
   input_line.append(j)
  exon_info=sep_line[-1]
  exon_info=exon_info.split('"')
  for j in exon_info:
   if(len(j)>0):
    input_line.append(j)
  exon_all_data.append([input_line[11],input_line[9],input_line[3],input_line[4],input_line[13],input_line[0],input_line[6]])
  line=f.readline()
indexes=["Transcript_id","Gene_id","Exon_start","Exon_end","Exon_number","Chr","Strand"]
exon_all_data_pd=pd.DataFrame(exon_all_data,columns=indexes)

exon_all_data_pd.to_csv("/mnt/Annotation/Latipes_merged_exon.txt",sep="\t",index=False)
