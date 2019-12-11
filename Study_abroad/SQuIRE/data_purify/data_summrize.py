import pandas as pd

data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/Result/DESeq2_TE_separated.txt",sep='\t')
sup
super_family=input()
want_data=[]
subset=data[data.Superfamily==super_family]
summary=subset["Log2FoldChange"].describe()
print(summary)
super_family=input()
subset=data[data.Superfamily==super_family]
input_col=[]
for i in summary:
 input_col.append(i)
want_data.append(input_col)
summary.append(subset["Log2FoldChange"].describe())
print(summary)
