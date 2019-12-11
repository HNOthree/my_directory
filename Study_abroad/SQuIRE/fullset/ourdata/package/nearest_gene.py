import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='input directory')

args = parser.parse_args()
path=args.i
input_path=path+"/Gene_TE_number.txt"
output_path=path+"/TE_nearest_gene.txt"

data=pd.read_csv(input_path,sep='\t')
#data=data.head(1000)
near_gene=data[data.Number==1]

i_near_gene = near_gene.groupby(["Family","TE_start"])
nearest=near_gene.loc[i_near_gene['Distance'].idxmin(),:]
print(nearest)
nearest.to_csv(output_path,sep='\t',index=False)
