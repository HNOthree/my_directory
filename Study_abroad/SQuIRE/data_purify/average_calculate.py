
with open("/mnt/Result/SQuIRE_Male_vs_Female_Full_ourdata_gene_TE_counttabl_TE.txt")as f:
 line=f.readline()
 line=f.readline()
 while line:
 #for i in range(10):
  line=line.replace('\n','')
  read=line.split('\t')
  read=read[1:]
  #print(read)
  length=0
  sumation=0
  for j in read:
   sumation+=float(j)
   if(j!="0"):
    length+=1
  thres=sumation/length
  if(thres<=5):
   print(line)
   print(thres)
  line=f.readline()
