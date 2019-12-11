import pandas as pd
data=pd.read_csv("~/Index/TE_only_Latipes_annotation_file_chr1.gtf",sep="\t")

name_list=[]
name_dict={}
for i in data.repName:
 if i not in name_list:
  name_list.append(i)
  name_dict[i]=1

with open("TE_only_Latipes_annotation_file_chr1_purified.gtf",mode='w') as f: 
 f.write("chr\t"+"program\t"+"attribute\t"+"start_pos\t"+"end_pos\t"+"score\t"+"strand\t"+"frame\t"+"id_info\n")

 for i in range(len(data)):
  column=data.iloc[i]
  chromosome=column.genoName
  chromosome=chromosome[3:]
  program="."
  attribute="TE"
  start_pos=column.genoStart
  end_pos=column.genoEnd
  score="."
  strand=column.strand
  frame="."
 
  gene_id='gene_id '+'"'+column.repName+'"; '
  transcript_id='transcript_id '+'"'+column.repName+'dup'+str(name_dict[column.repName])+'"; '
  name_dict[column.repName]+=1
  family_id='family_id '+'"'+column.repFamily+'"; '
  class_id='class_id '+'"'+column.repClass+'"; '
  id_info=gene_id+transcript_id+family_id+class_id
  f.write(str(chromosome)+"\t"+str(program)+"\t"+str(attribute)+"\t"+str(start_pos)+"\t"+str(end_pos)+"\t"+str(score)+"\t"+str(strand)+"\t"+str(frame)+"\t"+str(id_info)+"\n")
