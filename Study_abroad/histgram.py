import pandas as pd
import matplotlib as plt
import numpy as np
plt.use('Agg')
#separated means that TE infomation(family,superfamily,location...) is separated.
data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/DESeq2_TE_separated.txt",sep='\t')


import matplotlib.pyplot as plt
plt.hist(data.Log2FoldChange.dropna(),bins=50)
plt.xlabel("Log2 Fold Change")
plt.ylabel("Count")
plt.xlim(-10,10)
plt.title("The distribution of TE logFC")
plt.savefig("/home/smiyake/sho/Fullset/SQuIRE/image/SQUIRE_TE_hist.png",dpi=300)

