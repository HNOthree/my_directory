import pandas as pd
data=pd.read_csv("/home/smiyake/sho/Fullset/txt/two_results_merge.txt",sep="\t")
ave_data=[]
for i in range(len(data)):
 col_data=data.iloc[i]
 name=col_data.Name
 TEtranscripts_lfc=col_data.Log2FoldChange_TEtranscripts
 TEtools_lfc=col_data.Log2FoldChange_TEtools
 Average=(TEtranscripts_lfc+TEtools_lfc)/2
 ave_data.append([name,col_data.Family,col_data.Class,Average])

ave_data=pd.DataFrame(ave_data,columns=["Name","Family","Class","Log2FoldChange_ave"])
list_number=50
top_data=ave_data.sort_values("Log2FoldChange_ave",ascending=False).head(list_number)
bottom_data=ave_data.sort_values("Log2FoldChange_ave").head(list_number)

top_data.to_csv("LFC_top{}.txt".format(list_number),sep="\t",index=False)
bottom_data.to_csv("LFC_bottom{}.txt".format(list_number),sep="\t",index=False)
