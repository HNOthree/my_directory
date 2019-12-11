import pandas as pd

def mergedata(merge_data):
 gene_list=[]
 for i in merge_data.Gene_id:
  if i not in gene_list:
   gene_list.append(i)
 want_data=[]
 for gene in gene_list:
  gene_data=merge_data[merge_data.Gene_id==gene]
  start=gene_data.groupby("Gene_id").min().iloc[0].Transcript_start
  end=gene_data.groupby("Gene_id").max().iloc[0].Transcript_end
  for j in range(0,len(gene_data)):
   each_info=gene_data.iloc[j]
   if(each_info.Location=="upstream" and each_info.Strand=="+"):
    distance=start-each_info.TE_end
   elif(each_info.Location=="upstream" and each_info.Strand=="-"):
    distance=each_info.TE_start-end
   elif(each_info.Location=="downstream" and each_info.Strand=="+"):
    distance=each_info.TE_start-end
   elif(each_info.Location=="downstream" and each_info.Strand=="-"):
    distance=start-each_info.TE_end
   else:
    print("ERROR")
   want_data.append([gene,distance,start,end,each_info.TE_name,each_info.TE_Class,each_info.TE_family,each_info.TE_start,each_info.TE_end,each_info.Gene_log2FoldChange,each_info.TE_log2FoldChange,each_info.TE_log2FoldChange-each_info.Gene_log2FoldChange,each_info.Location,each_info.Strand])
 want_data=pd.DataFrame(want_data,columns=["Gene_id","Distance","Gene_start","Gene_end","Family","Class","Superfamily","TE_start","TE_end","Gene_log2FoldChange","TE_log2FoldChange","Delta_LFC","Location","Strand"])
 return want_data


def main():
 upstream_data=pd.read_csv("/mnt/SQ_upstream_TE_lfc.txt",sep='\t')
 downstream_data=pd.read_csv("/mnt/SQ_downstream_TE_lfc.txt",sep='\t')
 upstream_data=upstream_data.loc[:,["Gene_id","Transcript_start","Transcript_end","Chr","Strand","TE_name","TE_Class","TE_family","TE_start","TE_end","Distance","Gene_log2FoldChange","TE_log2FoldChange"]]
 upstream_data["Location"]="upstream"
 downstream_data=downstream_data.loc[:,["Gene_id","Transcript_start","Transcript_end","Chr","Strand","TE_name","TE_Class","TE_family","TE_start","TE_end","Distance","Gene_log2FoldChange","TE_log2FoldChange"]]
 downstream_data["Location"]="downstream"
 data1=mergedata(upstream_data)
 data2=mergedata(downstream_data)
 data=data1.append(data2)
 data=data[~data.duplicated()]
 data.to_csv("SQuIRE_gene_TE_distance.txt",sep='\t',index=False)
main()
