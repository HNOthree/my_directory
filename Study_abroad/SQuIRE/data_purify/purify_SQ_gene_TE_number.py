import math
import pandas as pd


data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_number.txt",sep='\t')

indexes=[]
for i in data:
 indexes.append(i)
indexes.append("Abs_delta_LFC")
indexes.append("log10_Distance")
wantdata=[]
for i in range(0,len(data)):
 col=data.iloc[i]
 A_delta=abs(col.Delta_LFC)
 logdist=math.log10(col.Distance)
 input_line=[]
 for i in col:
  input_line.append(i)
 input_line.append(A_delta)
 input_line.append(logdist)
 wantdata.append(input_line)

wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/Gene_TE_number_purified.txt",index=False,sep='\t')
