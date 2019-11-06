import pandas as pd
result=pd.read_csv("/mnt/Results/upstream_transcripts_TE_overlap_lfc.txt",sep='\t')
TE_list=["ERV1","LTR","Gypsy","TcMar-Tc1","LINE"]
extract_list=result[result.TE_family==TE_list[0]]
print(len(extract_list))
for i in TE_list[1:]:
 data=result[result.TE_family==i]
 print(len(data))
 extract_list=extract_list.append(data)
 print(len(extract_list))
print(extract_list.head(10))

for i in range(len(extract_list)):
 transcript_col=extract_list.iloc[i]
 transcript_start=transcript_col.Transcript_start
 transcript_chr=transcript_col.Chr
 transcript_strand=transcript_col.Strand
 with open("/mnt/Reference/{}.fasta".format(transcript_chr)) as f:
  sequence=f.readline()
  sequence=f.readline()
  sequence=sequence.upper()
  if(transcript_strand=="+"):
   for i in range(transcript_start,transcript_col.Transcript_end):
    if(sequence[i]=="A" and sequence[i+1]=="T" and sequence[i+2]=="G"):
     print(transcript_col.TE_family,transcript_start,i,transcript_col.TE_start,transcript_col.TE_end)
     if(transcript_col.TE_start<i and transcript_col.TE_end>=i):
      print("#################################################")
     break
