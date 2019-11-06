import pandas as pd
exon_data_pd=pd.read_csv("/mnt/Annotation/Latipes_merged_exon.txt",sep='\t')
transcript_data_pd=pd.read_csv("/mnt/Annotation/Latipes_merged_transcript.txt",sep='\t')

intron_all_data=[]
for i in range(len(transcript_data_pd)):
  transcript_col=transcript_data_pd.iloc[i]
 want_exon_data=exon_data_pd[exon_data_pd.Transcript_id==transcript_col.Transcript_id]
 
 if(len(want_exon_data)>0):
  pre_col=want_exon_data.iloc[0]
  intron_number=1
  for j in range(1,len(want_exon_data)):
   input_data=[]
   current_col=want_exon_data.iloc[j]
   intron_start=pre_col.Exon_end+1
   intron_end=current_col.Exon_start-1
   intron_all_data.append([transcript_col.Transcript_id,\
    transcript_col.Transcript_start,\
    transcript_col.Transcript_end,\
    transcript_col.Gene_id,\
    transcript_col.Chr,\
    transcript_col.Strand,\
    intron_start,\
    intron_end,\
    intron_number])
   pre_col=current_col
   intron_number+=1
intron_all_data_pd=pd.DataFrame(intron_all_data,columns=["Transcript_id","Transcript_start","Transcript_end","Gene_id","Chr","Strand","Intron_start","Intron_end","Intron_number"]) 

intron_all_data_pd.to_csv("/mnt/Annotation/Latipes_merged_intron.txt",sep='\t',index=False)

