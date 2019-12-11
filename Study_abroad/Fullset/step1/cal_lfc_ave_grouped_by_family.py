import pandas as pd
data=pd.read_csv("/home/smiyake/sho/Fullset/txt/two_results_merge.txt",sep="\t")
family_list=[]
for i in data.Family:
 if i not in family_list:
  family_list.append(i)

family_lfc_list=[]
for i in family_list:
 sub_data=data[data["Family"] ==i]
 Ttran_sum=sub_data.Log2FoldChange_TEtranscripts.sum()
 Ttools_sum=sub_data.Log2FoldChange_TEtools.sum()
 T_ave=(Ttran_sum+Ttools_sum)/2
 family_lfc_list.append([i,sub_data.iloc[0].Class,len(sub_data),T_ave/len(sub_data)])

family_lfc_list=pd.DataFrame(family_lfc_list,columns=["Family","Class","Counts","Log2FoldChange_ave"])

family_lfc_list.to_csv("/home/smiyake/sho/Fullset/txt/lfc_groupedby_family.txt",sep="\t",index=False)
