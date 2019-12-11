import pandas as pd
import argparse 
parser = argparse.ArgumentParser()
parser.add_argument('-e', help='interaction file')
parser.add_argument('-i',help='output directory')
args = parser.parse_args()
enrichment_file=args.e
out_dir=args.i
gene_file=out_dir+'/Gene_TE_distance_ref.txt'


TE_gene=pd.read_csv(gene_file,sep='\t')
enrich=pd.read_csv(enrichment_file,sep='\t',header=None,names=("Chr","Start_region","End_region","Sexuality"))

chroms=[]
for i in enrich.Chr:
 if i not in chroms:
  chroms.append(i)

for chrom in chroms:
 chrom_data=TE_gene[TE_gene.Chr==chrom]
 chrom_data.to_csv("{}/{}_GENE_TE_distance_ref.txt".format(out_dir,chrom),sep='\t',index=False)
