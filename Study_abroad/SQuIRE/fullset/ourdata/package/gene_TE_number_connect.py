import pandas as pd
import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-d', help='Directory')
parser.add_argument('-e', help='Expression of gene file')

args = parser.parse_args()
path=args.d
TE_path=path+"/DESeq2_TE_separated.txt"
gene_path=path+"/Gene.txt"
expression_path=args.e
output_path=path+"/Gene_TE_number.txt"

TE_info=pd.read_csv(TE_path,sep='\t')
gene_info=pd.read_csv(gene_path,sep='\t')
gene_exp=pd.read_csv(expression_path,sep='\t')
#sample={"Family":["Ignore"],"Class":["Ignore"],"Superfamily":["Ignore"],"TE_start":[0],"TE_end":[0],"Gene_id":["Ignore"],"Gene_start":[0],"Gene_end":[0],"Distance":[0],"Log10_distance":[0.0],"TE_log2FoldChange":[0.0],"TE_pvalue":[0.0],"Gene_log2FoldChange":[0.0],"Gene_pvalue":[0.0],"Abs_delta_LFC":[0.0],"Chr":["Ignore"],"Strand":["Ignore"],"Location":["Ignore"],"Number":[0],"Direction_number":[0],}
wantdata=pd.DataFrame(columns=["Family","Class","Superfamily","TE_start","TE_end","Gene_id","Gene_start","Gene_end","Distance","Log10_distance","TE_log2FoldChange","TE_pvalue","Gene_log2FoldChange","Gene_pvalue","Abs_delta_LFC","Chr","Strand","Location","Number","Direction_number"])
plusnumber_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
minusnumber_list=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15]

#strand_list=["+","-"]
chr_list=[]
for i in gene_info.Chr:
 if i not in chr_list:
  chr_list.append(i)
print(len(chr_list))
for chromosome in chr_list:
 print(chromosome)
 TE_chr=TE_info[TE_info.Chr==chromosome]
 gene_chr=gene_info[gene_info.Chr==chromosome]
 #for strand in strand_list:
 TE_candidates=TE_chr#[TE_chr.Strand==strand]
 gene_candidates=gene_chr#[gene_chr.Strand==strand]
 print(len(TE_candidates),len(gene_candidates))
 for i in range(len(TE_candidates)):
   TE=TE_candidates.iloc[i]
   upstream_list=[]
   downstream_list=[]
   for j in range(len(gene_candidates)):
    a_gene=gene_candidates.iloc[j]
    if(TE.Start_TE>a_gene.Gene_end):
     distance=TE.Start_TE-a_gene.Gene_end
     gene_exp_col=gene_exp[gene_exp.Gene==a_gene.Gene_id]
     if(len(gene_exp_col)==0):
      downstream_list.append(["Ignore","Ignore","Ignore",0,0,"Ignore",0,0,0,0,0,0,0.0,0.0,0.0,"Ignore","Ignore","Ignore"])
      continue
     else:
      gene_exp_col=gene_exp_col.iloc[0]
     downstream_list.append([TE.Family,TE.Class,TE.Superfamily,TE.Start_TE,TE.End_TE,a_gene.Gene_id,a_gene.Gene_start,a_gene.Gene_end,distance,math.log10(distance),TE.Log2FoldChange,TE.Pvalue,float(gene_exp_col.logFC),float(gene_exp_col.negLogPval),float(abs(TE.Log2FoldChange-gene_exp_col.logFC)),chromosome,TE.Strand,"downstream"])
    elif(TE.End_TE<a_gene.Gene_start):
     distance=a_gene.Gene_start-TE.End_TE
     gene_exp_col=gene_exp[gene_exp.Gene==a_gene.Gene_id]
     if(len(gene_exp_col)==0):
      upstream_list.append(["Ignore","Ignore","Ignore",0,0,"Ignore",0,0,0,0,0,0,0.0,0.0,0.0,"Ignore","Ignore","Ignore"])
      continue

     else:
      gene_exp_col=gene_exp_col.iloc[0]
     upstream_list.append([TE.Family,TE.Class,TE.Superfamily,TE.Start_TE,TE.End_TE,a_gene.Gene_id,a_gene.Gene_start,a_gene.Gene_end,distance,math.log10(distance),TE.Log2FoldChange,TE.Pvalue,float(gene_exp_col.logFC),float(gene_exp_col.negLogPval),float(abs(TE.Log2FoldChange-gene_exp_col.logFC)),chromosome,TE.Strand,"upstream"])
    else:
     downstream_list.append(["Ignore","Ignore","Ignore",0,0,"Ignore",0,0,0,0,0,0,0.0,0.0,0.0,"Ignore","Ignore","Ignore"])
   if(len(upstream_list)>0):
    upstream_list=pd.DataFrame(upstream_list,columns=["Family","Class","Superfamily","TE_start","TE_end","Gene_id","Gene_start","Gene_end","Distance","Log10_distance","TE_log2FoldChange","TE_pvalue","Gene_log2FoldChange","Gene_pvalue","Abs_delta_LFC","Chr","Strand","Location"])
    upstream_list=upstream_list.sort_values(by=["Distance"])
    upstream_list=upstream_list.reset_index()
    upstream_list=upstream_list.drop("index",axis=1)
    if(len(upstream_list)>15):
     upstream_list=upstream_list[:15]
    upstream_list["Number"]=plusnumber_list[:len(upstream_list)]
    upstream_list["Direction_number"]=plusnumber_list[:len(upstream_list)]
    wantdata=wantdata.append(upstream_list)

   if(len(downstream_list)>0):
    downstream_list=pd.DataFrame(downstream_list,columns=["Family","Class","Superfamily","TE_start","TE_end","Gene_id","Gene_start","Gene_end","Distance","Log10_distance","TE_log2FoldChange","TE_pvalue","Gene_log2FoldChange","Gene_pvalue","Abs_delta_LFC","Chr","Strand","Location"])
    downstream_list=downstream_list.sort_values(by=["Distance"])
    downstream_list=downstream_list.reset_index()
    downstream_list=downstream_list.drop("index",axis=1)
    if(len(downstream_list)>15):
     downstream_list=downstream_list[:15]
    downstream_list["Number"]=plusnumber_list[:len(downstream_list)]
    downstream_list["Direction_number"]=minusnumber_list[:len(downstream_list)]
    wantdata=wantdata.append(downstream_list)
wantdata=wantdata[wantdata.Family!="Ignore"]
wantdata.to_csv(output_path,index=False,sep='\t')
