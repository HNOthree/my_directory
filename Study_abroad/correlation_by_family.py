import pandas as pd
import numpy
#it is the data from data purify 2
# it contains each log2 fold change of TE and gene, distance and TE infomation 
data=pd.read_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/SQ_downstream_TE_lfc.txt",sep='\t')
family_list=[]
for i in data.TE_name:
 if i not in family_list:
  family_list.append(i)
distance_list=[1000,5000,10000,25000,50000,100000,500000]
minimum=0
corre_list=[]
# between minumum and max

for distance in distance_list:
 for family in family_list:
  subset=data[data.TE_name==family]
  subset=subset[subset.Distance>minimum]
  subset=subset[subset.Distance<distance]
  subset=subset.loc[:,["Gene_log2FoldChange","TE_log2FoldChange"]]
  #eliminate duplicated data
  subset=subset[~subset.duplicated()]
  if(len(subset)>2):
   CC=subset.corr().iat[0,1]
   if(numpy.isnan(CC)==False):
    string=str(minimum+1)+" ~ "+str(distance)
    corre_list.append([family,string,len(subset),CC])
 minimum=distance
corre_list=pd.DataFrame(corre_list,columns=['Family',"Distance","Data","Correlation_coefficient"])
corre_list.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/downstream_family_CC_between.txt",sep='\t',index=False)

corre_list=[]
#less than distance
for distance in distance_list:
 for family in family_list:
  subset=data[data.TE_name==family]
  subset=subset[subset.Distance<distance]
  subset=subset.loc[:,["Gene_log2FoldChange","TE_log2FoldChange"]]
  subset=subset[~subset.duplicated()]
  if(len(subset)>2):
   CC=subset.corr().iat[0,1]
   if(numpy.isnan(CC)==False):
    string="0 ~ "+str(distance)
    corre_list.append([family,string,len(subset),CC])
corre_list=pd.DataFrame(corre_list,columns=['Family',"Distance","Data","Correlation_coefficient"])
corre_list.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/downstream_family_CC_LessThan.txt",sep='\t',index=False)
