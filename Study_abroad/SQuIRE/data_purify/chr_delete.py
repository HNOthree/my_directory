with open("/mnt/squire_fetch/TE_only_Latipes_annotation_file.unknown.ucsc") as f_r:
 line=f_r.readline()
 with open("/mnt/squire_fetch/TE_only_Latipes_annotation_file_unknown.txt","w") as f_w:
  while line:
   line=line.replace("chr","")
   f_w.write(line)
   line=f_r.readline()
