import pandas as pd 

def convert(sequence,strand):
 newseq=""
 for i in sequence:
  if(i=="a"):
   newseq+="A"
  elif(i=="t"):
   newseq+="T"
  elif(i=="g"):
   newseq+="G"
  elif(i=="c"):
   newseq+="C"
  else:
   newseq+=i
 if(strand=="-"):
  newseq=newseq[::-1]
 return newseq

data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/Olat_helitron1.txt",sep='\t')
chromosomes=[]
for i in data.Chr:
 if i not in chromosomes:
  chromosomes.append(i)
with open("/home/smiyake/sho/Fullset/SQuIRE/Olat_helitron1.fasta","w") as f_w:
 for chrom in chromosomes:
  data_chrom=data[data.Chr==chrom]
  with open("/home/smiyake/shares/Sho/data/Genome/GCF_002234675.1_ASM223467v1_genomic.fasta") as f_r:
   while True:
    sentence=f_r.readline()
    can_chrom=sentence[1:20]
    if(chrom in can_chrom):
     sequence=f_r.readline()
     while True:
      can=f_r.readline()
      if(">" in can):
       break
      else:
       can=can.replace("\n","")
       sequence+=can
     break
   for j in range(len(data_chrom)):
    TE=data_chrom.iloc[j]
    TE_seq=sequence[TE.Start_TE:TE.End_TE]
    input_TE_seq=convert(TE_seq,TE.Strand)
    header=">"+str(TE.Start_TE)+chrom+"\n"
    f_w.write(header)
    input_TE_seq+='\n'
    f_w.write(input_TE_seq)
