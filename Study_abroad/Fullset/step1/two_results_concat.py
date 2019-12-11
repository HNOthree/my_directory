import pandas as pd

data_1=pd.read_csv("/home/smiyake/sho/Fullset/FvsM_gene_TE_analysis_Name_separated_only_TE.txt",sep="\t")
data_2=pd.read_csv("/home/smiyake/shares/Sho/data/all_TE~condition.csv")
data_1=data_1.rename(columns={"Basemean":"Basemean_TEtranscripts",\
"log2foldchange":"Log2FoldChange_TEtranscripts","lfcSE":"LfcSE_TEtranscripts",\
"stat":"Stat_TEtranscripts","pvalue":"Pvalue_TEtranscripts","padj":"Padj_TEtranscripts"})
data_2=data_2.rename(columns={"Nomna":"Name","baseMean":"BaseMean_TEtools",\
"log2FoldChange":"Log2FoldChange_TEtools","lfcSE":"LfcSE_TEtools",\
"stat":"Stat_TEtools","pvalue":"Pvalue_TEtools","padj":"Padj_TEtools",\
"condition":"Condition_TEtools","TE":"TE_TEtools","BH":"BH_TEtools",\
"signif":"Signif_TEtools"})
print(data_1.head(10))
print(data_2.head(10))
data=pd.merge(data_1,data_2,on="Name")
data.to_csv("~/sho/Fullset/two_results_merge.txt",sep="\t",index=False)
