import pandas as pd

transcript=pd.read_csv("/mnt/Annotation/Latipes_merged_transcript.txt",sep='\t')
TE_sigdiff=pd.read_csv("/mnt/Annotation/TE_only_Latipes_annotation.txt",sep='\t')
#print(transcript.head(3))
#print(TE_sigdiff.head(3))


chr_list=[]
for i in transcript.Chr:
 if i not in chr_list:
  chr_list.append(i)

#print(chr_list)
strands=["+","-"]

want_data=[]
for chr_i in chr_list:
 transcript_chr_i=transcript[transcript.Chr==chr_i]
 TE_chr_i=TE_sigdiff[TE_sigdiff.Chr==chr_i]
 for strand in strands:
  transcript_chri_strand=transcript_chr_i[transcript_chr_i.Strand==strand]
  TE_chri_strand=TE_chr_i[TE_chr_i.Strand==strand]
  transcript_chri_strand=transcript_chri_strand.sort_values("Transcript_start")
  TE_chri_strand=TE_chri_strand.sort_values("TE_start")
  #print(TE_chri_strand.TE_start.head(5))
  #print(transcript_chri_strand.Transcript_start.head(5))
  
  start_pos=0
  print(chr_i,strand)
  for i in range(len(transcript_chri_strand)):
   transcript_col=transcript_chri_strand.iloc[i]
#   print(transcript_col)
#   print(TE_chri_strand.iloc[start_pos+1])
   for j in range(start_pos,len(TE_chri_strand)):
    TE_col=TE_chri_strand.iloc[j]
    if(transcript_col.Transcript_start>TE_col.TE_end):#shakutori
     start_pos=j
     continue
    elif(TE_col.TE_start>transcript_col.Transcript_start):#finish if TE start site exceed Transcript start site
     break
    ##overlapped
    if(transcript_col.Transcript_start>TE_col.TE_start):
     input_line=[]
     for k in transcript_col:
      input_line.append(k)
     for k in TE_col[0:5]:
      input_line.append(k)
     want_data.append(input_line)

index_list=[]
for i in transcript:
 index_list.append(i)
for i in TE_sigdiff:
 index_list.append(i)
index_list=index_list[:-1]
index_list=index_list[:-1]
want_data_pd=pd.DataFrame(want_data,columns=index_list)
want_data_pd.to_csv("/mnt/Results/merge_transcript_TE_upstream_overlap.txt",sep='\t',index=False)

