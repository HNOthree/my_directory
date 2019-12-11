import pandas as pd
with open("/home/smiyake/shares/Sho/data/Annotation/TE_only_Latipes_annotation_file.unknown.ucsc") as f:
 line=f.readline()
 line=f.readline()
 TE_all_data=[]
 while line:
 #for i in range(10):
  input_line=[]
  line=line.replace("\n","")
  sep_line=line.split("\t")
  for j in sep_line[:-1]:
   input_line.append(j)
  TE_info=sep_line[-1]
  TE_info=TE_info.split('"')
  for j in TE_info:
   if(len(j)>0):
    input_line.append(j)
  #print(input_line)
  TE_all_data.append([input_line[10],input_line[11],input_line[12],input_line[6],input_line[7],input_line[5].replace("chr",""),input_line[9]])
  line=f.readline()
indexes=["Name","TE_class","TE_family","TE_start","TE_end","Chr","Strand"]

TE_all_data_pd=pd.DataFrame(TE_all_data,columns=indexes)
TE_all_data_pd.to_csv("/home/smiyake/shares/Sho/data/Annotation/TE_only_Latipes_annotation_file_unknown.txt",sep="\t",index=False)

         
