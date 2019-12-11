import pandas as pd
name_list=["/mnt/Annotation/Latipes_merged_transcript.gtf",\
"/mnt/Annotation/Latipes_merged_exon.gtf"]

for name in name_list:
 with open(name+"sorted.gtf","w")as f:

  print(name)
  data_pd=pd.read_csv(name,sep="\t",header=None, skiprows=2)
  data_pd = data_pd.sort_values(3)
  for i in range(len(data_pd)):
   column=data_pd.iloc[i]
   w_data=str(column[0])
   for j in range(1,len(column)):
    w_data=w_data+"\t"+str(column[j])
   w_data+="\n"
   f.write(w_data)

