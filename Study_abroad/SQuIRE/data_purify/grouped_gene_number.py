import pandas as pd

data=pd.read_csv("Gene_TE_distance_lfc.txt",sep='\t')
indexes=[]
wantdata=[]
for i in data:
 indexes.append(i)
indexes.append("Number")
indexes.append("Direction_number")
TE_list=[]
for i in data.Family:
 if i not in TE_list:
  TE_list.append(i)

locations=["upstream","downstream"]

for location in locations:
 d_data=data[data.Location==location]
 for TE in TE_list:
  TE_data=d_data[d_data.Family==TE]
  start_list=[]
  for i in TE_data.TE_start:
   if i not in start_list:
    start_list.append(i)

  for start in start_list:
   start_data=TE_data[TE_data.TE_start==start]
   sort_startdata=start_data.sort_values("Distance")
   for i in range(0,len(sort_startdata)):
    columns=sort_startdata.iloc[i]
    col=[]
    for j in columns:
     col.append(j)
    col.append(i+1)
    if(location=="upstream"):
     col.append(i+1)
    else:
     col.append(-(i+1))
    wantdata.append(col)

wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv("Gene_TE_number.txt",index=False,sep='\t')
