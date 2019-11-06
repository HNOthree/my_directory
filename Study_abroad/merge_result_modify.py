import pandas as pd
windows=[500,1000,5000,10000,50000]
for window in windows:
 print(window)
 need=[]
 with open("/mnt/Results/upstream{}bp_transcripts_TE.txt".format(window),"r") as rf:
  line=rf.readline()
  line=rf.readline()
  while line:
   aline=line.split('"')
   a=[]    
   a.append([aline[0],aline[3],aline[7],aline[10],aline[13],aline[17],aline[21],aline[25]])
   need_line=[]
   a=a[0]
   for b in a:
    c=b.split("\t")
    for d in c:
     need_line.append(d)
   need_line=[need_line[5],need_line[0],need_line[1],need_line[2],need_line[3],need_line[6],need_line[12],need_line[15],need_line[14],need_line[8],need_line[9]]
   need.append(need_line)
   line=rf.readline()
  need=pd.DataFrame(need,columns=["Gene__name","Chr","Transcript_start","Transcript_end","Strand","Transcript_name","TE_name","TE_Class","TE_family","TE_start","TE_end"])
  need.to_csv("/mnt/Results/upstream{}bp_transcripts_TE_data.txt".format(window),sep="\t",index=False)
