want_gene=[]
with open("/home/smiyake/shares/Sho/data/refGenes.list") as f:
 line=f.readline()
 while line:
  line=line.replace("\n","")
  want_gene.append(line)
  line=f.readline()

print(want_gene[1:10])

with open("/home/smiyake/shares/Sho/data/Annotation/Latipes_merged.gtf") as f_r:
 with open("/home/smiyake/sho/Fullset/Latipes_merged_listed_gene.gtf","w") as f_w:
  line=f_r.readline()
  while line:
   gene=line.split("\t")
   gene=gene[-1]
   gene=gene.replace('"','')
   gene=gene.split(" ")
   gene=gene[1]
   gene=gene.replace(";","")
#   print(gene)
   if gene in want_gene:
#    print(gene)
    f_w.write(line)
   line=f_r.readline()
