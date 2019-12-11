names=["up","down"]

for name in names:
 read_name="/mnt/Results/{}stream_transcripts_TE.txt".format(name)
 write_name="/mnt/Results/{}stream_transcripts_TE_separate_info.txt".format(name)

 with open(write_name,"w")as f_w:
  f_r=open(read_name,"r")
  line=f_r.readline()
  line=f_r.readline()
  f_w.write("Gene_name\tTE_name\tTranscript_name\tTranscript_start\tTranscript_end\tChr\tStrand\tTE_start\tTE_end\tTE_class\tTE_family\tDistance\n")
  while line:
   data_seq=[]
   write_data=line.split("\t")
   for seq in write_data:
    split_seq=seq.replace(";","")
    split_seq=split_seq.split('"')
    for data in split_seq:
     if(len(data)!=0 and data!=" "):
      data_seq.append(data)
   want_data=[data_seq[5],data_seq[12],data_seq[7],data_seq[1],data_seq[2],data_seq[0],data_seq[3],data_seq[8],data_seq[9],data_seq[18],data_seq[16],data_seq[-1]]
   print(want_data[-1])
   input_sentence=want_data[0]
   for i in want_data[1:]:
    input_sentence+="\t"+i
   #input_sentence+=("\n")
   f_w.write(input_sentence)
   line=f_r.readline()

  f_r.close()
