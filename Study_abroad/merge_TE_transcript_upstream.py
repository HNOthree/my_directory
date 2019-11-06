import pandas as pd

#TE annotation data and gene annotation data
# Required 
#TE start position as TE_start
#TE end position as TE_end
#transcript start position as Transcript_start
#transcript end position as Transcript_end
# both strand as TE_strand Transcript_strand
transcript=pd.read_csv("/mnt/Annotation/Latipes_merged_transcript.txt",sep='\t')
TE_sigdiff=pd.read_csv("/mnt/Annotation/TE_only_Latipes_annotation.txt",sep='\t')
#print(transcript.head(3))
#print(TE_sigdiff.head(3))

threshold=500000

#make a list of chrmosome
chr_list=[]
for i in transcript.Chr:
 if i not in chr_list:
  chr_list.append(i)

#print(chr_list)
strands=["+","-"]

want_data=[]
for chr_i in chr_list:#each chromosome
 transcript_chr_i=transcript[transcript.Chr==chr_i]
 TE_chr_i=TE_sigdiff[TE_sigdiff.Chr==chr_i]
 for strand in strands:#each strand
  transcript_chri_strand=transcript_chr_i[transcript_chr_i.Strand==strand]
  TE_chri_strand=TE_chr_i[TE_chr_i.Strand==strand]
  #sort each start position
  transcript_chri_strand=transcript_chri_strand.sort_values("Transcript_start")
  TE_chri_strand=TE_chri_strand.sort_values("TE_start")
  #print(TE_chri_strand.TE_start.head(5))
  #print(transcript_chri_strand.Transcript_start.head(5))
  
  start_pos=0 #position in order to reduce the number of calculation
  print(chr_i,strand)
  for i in range(len(transcript_chri_strand)):
   transcript_col=transcript_chri_strand.iloc[i]
#   print(transcript_col)
#   print(TE_chri_strand.iloc[start_pos+1])
   for j in range(start_pos,len(TE_chri_strand)):
    TE_col=TE_chri_strand.iloc[j]
    if(int(transcript_col.Transcript_start-TE_col.TE_end)>threshold):#shakutori
     start_pos=j
     continue
    elif(TE_col.TE_start>transcript_col.Transcript_start):#finish if TE start site exceed Transcript start site
     break
    ##not overlapped
    if(transcript_col.Transcript_start>TE_col.TE_end):
     input_line=[]
     for k in transcript_col:
      input_line.append(k)
     for k in TE_col[0:5]:
      input_line.append(k)
     ##distance
     input_line.append(transcript_col.Transcript_start-TE_col.TE_end)
     want_data.append(input_line)

index_list=[]
for i in transcript:
 index_list.append(i)
for i in TE_sigdiff:
 index_list.append(i)
index_list=index_list[:-1]
index_list=index_list[:-1]
index_list.append("Distance")
want_data_pd=pd.DataFrame(want_data,columns=index_list)
want_data_pd.to_csv("/mnt/Results/merge_transcript_TE_upstream.txt",sep='\t',index=False)

