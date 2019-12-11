read_name="/home/smiyake/sho/Fullset/FvsM__gene_TE_analysis.txt"
write_name="/home/smiyake/sho/Fullset/FvsM_gene_TE_analysis_Name_separated.txt"
with open(write_name,"w")as f_w:
 f_r=open(read_name,"r")
 line=f_r.readline()
 
 while line:
  write_data=line.replace(":","\t")
  print(write_data)
  f_w.write(write_data)
  line=f_r.readline()

 f_r.close()
