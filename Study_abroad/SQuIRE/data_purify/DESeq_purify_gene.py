def write_file(sequence,fw):
 sentence=sequence[0]
 for i in sequence[1:]:
  sentence+="\t"+i
 fw.write(sentence)

input_file="/mnt/Result/DESeq2_RefSeq_only.txt"
output_file="/mnt/Result/DESeq2_RefSeq_separated.txt"
index_list=["Gene","Strand","BaseMean","Log2FoldChange","LfcSE","Stat","Pvalue","Padj\n"]
with open(input_file) as fr:
 with open(output_file,"w") as fw:
  write_file(index_list,fw)
  line=fr.readline()
  line=fr.readline()
  while line:
   line=line.split("\t")
   input_line=[]
   for i in line:
    i=i.split(",")
    for j in i:
      input_line.append(j)
   write_file(input_line,fw)
   line=fr.readline()
