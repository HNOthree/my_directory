def write_file(sequence,fw):
 sentence=sequence[0]
 for i in sequence[1:]:
  sentence+="\t"+i
 fw.write(sentence)

input_file="/mnt/Result/DESeq2_TE_only.txt"
output_file="/mnt/Result/DESeq2_TE_separated.txt"
strand=["+,.","-,."]
index_list=["Chr","Start_TE","End_TE","Family","Superfamily","Class","number","Strand","BaseMean","Log2FoldChange","LfcSE","Stat","Pvalue","Padj\n"]
with open(input_file) as fr:
 with open(output_file,"w") as fw:
  write_file(index_list,fw)
  line=fr.readline()
  line=fr.readline()
  while line:
   line=line.split("\t")
   input_line=[]
   for i in line:
    i=i.split("|")
    for j in i:
     j=j.split(":")
     for k in j:
      if k in strand:
       input_line.append(k[0])
      else:
       input_line.append(k)
   write_file(input_line,fw)
   line=fr.readline()
