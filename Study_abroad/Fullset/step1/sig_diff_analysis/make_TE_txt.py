with open("/home/smiyake/sho/Fullset/txt/FvsM_sigdiff_TE.txt") as f_r:
 line=f_r.readline()
 with open("/home/smiyake/sho/Fullset/txt/FvsM_sigdiff_TE_separated.txt","w")as f_w:
  line=f_r.readline()
  f_w.write("Name\tTE_family\tTE_class\tbaseMean\tlog2FoldChange\tlfcSE\tstat\tpvalue\tpadj\n")
  while line:
   line=line.split("\t")
   TE_info=line[0]
   TE_info=TE_info.split(":")
   input_line=TE_info[0]
   for i in TE_info[1:]:
    input_line+='\t'+str(i)
   for i in line[1:]:
    input_line+='\t'+str(i)
   f_w.write(input_line)
   line=f_r.readline()
