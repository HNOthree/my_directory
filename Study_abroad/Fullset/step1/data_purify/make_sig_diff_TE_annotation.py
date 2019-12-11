import pandas as pd

TE_annotation=pd.read_csv("/mnt/Annotation/TE_only_Latipes_annotation.txt",sep='\t')
sig_diff_list=pd.read_csv("/mnt/Results/FvsM_sigdiff_TE_separated.txt",sep='\t')
sig_diff_TE_list=[]

for i in sig_diff_list.TE_name:
 if i not in sig_diff_list:
  sig_diff_TE_list.append(i)

sig_annotation=[]

for i in range(len(TE_annotation)):
 if(i%1000==0):
  print(i,len(TE_annotation))
 col=TE_annotation.iloc[i]
 name=col.TE_name
 if name in sig_diff_TE_list:
  input_line=[]
  for j in col:
   input_line.append(j)
  sig_annotation.append(input_line)

indexes=[]
for i in TE_annotation:
 indexes.append(i)
sig_annotation_pd=pd.DataFrame(sig_annotation,columns=indexes)
sig_annotation_pd.to_csv("/mnt/Annotation/TE_only_Latipes_annotation_sig_diff.txt",sep='\t',index=False)
