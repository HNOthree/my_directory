import pandas as pd
data=pd.read_csv("~/sho/Fullset/txt/FvsM_gene_TE_analysis_Name_separated_only_TE.txt",sep='\t')
male=data[data.log2foldchange>1]
male=male[male.pvalue<0.05]
female=data[data.log2foldchange<-1]
female=female[female.pvalue<0.05]

count_male=male.groupby(["Class","Family"]).count()
count_female=female.groupby(["Class","Family"]).count()

count_male.to_csv("~/sho/Fullset/txt/sigdiff_TE_male.txt",sep='\t')
count_female.to_csv("~/sho/Fullset/txt/sigdiff_TE_female.txt",sep='\t')
