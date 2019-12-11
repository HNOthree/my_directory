import pandas as pd

min_data=5
all_data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/include_unknown/analysis/Gene_TE_number.txt",sep='\t')
family_list=[]

for i in all_data.Family:
 if i not in family_list:
  family_list.append(i)

wantdata=[]
for family in family_list:
 a_family_data=all_data[all_data.Family==family]
 if(len(a_family_data)>min_data):
  input_line=[family,len(a_family_data[a_family_data.Number==1])]
  for thres in range(1,11):
   thres_family_data=a_family_data[a_family_data.Number==thres]
   if(len(thres_family_data)>0):
    thres_family_data=thres_family_data[["Gene_log2FoldChange","TE_log2FoldChange"]]
    CC=thres_family_data.corr().iloc[0,1]
    input_line.append(CC)
   else:
    input_line.append(-2)
  wantdata.append(input_line)
wantdata=pd.DataFrame(wantdata,columns=["Family","nearest_count","CC1","CC2","CC3","CC4","CC5","CC6","CC7","CC8","CC9","CC10"])
wantdata=wantdata.sort_values("CC1")
wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/nearest_lfc_CC.txt",sep='\t',index=False)
