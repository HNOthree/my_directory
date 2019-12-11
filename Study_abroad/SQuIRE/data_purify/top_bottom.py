import pandas as pd
data=pd.read_csv("/mnt/Result/DESeq2_TE_separated.txt",sep='\t')
data.sort_values("Log2FoldChange").head(100).to_csv("/mnt/Result/DESeq2_TE_female_top100.txt",index=False,sep='\t')

data.sort_values("Log2FoldChange",ascending=False).head(100).to_csv("/mnt/Result/DESeq2_TE_male_top100.txt",index=False,sep='\t')


