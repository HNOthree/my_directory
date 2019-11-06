import pandas as pd

TE_annotation=pd.read_csv("/mnt/Annotation/TE_only_Latipes_annotation.txt",sep='\t')
TE_list=["ERV1","LTR","Gypsy"]
extract_list=TE_annotation[TE_annotation.TE_family==TE_list[0]]
print(len(extract_list))
for i in TE_list[1:]:
 data=TE_annotation[TE_annotation.TE_family==i]
 print(len(data))
 extract_list=extract_list.append(data)
 print(len(extract_list))
extract_list.to_csv("/mnt/Annotation/TE_three_family.txt",sep='\t',index=False)
