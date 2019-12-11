import pandas as pd

directory="/home/smiyake/sho/Fullset/SQuIRE/txt/"

category=["Male","Female","Other"]
indexes=["Family","Superfamily","Class","Data_count","CC1","Pvalue","CC2","CC3","CC4","CC5","CC6","CC7","CC8","CC9","CC10"]
wantdata=[]
enrich_TE=pd.DataFrame()

cc_data=pd.read_csv("{}../csv/nearest_lfc_CC.csv".format(directory))

for i in category:
 data=pd.read_csv("{}ALLTE_enrichment_{}.txt".format(directory,i),sep='\t')
 can=data[data.Pchoice==True]
 enrich_TE=enrich_TE.append(can)

for i in range(len(enrich_TE)):
 TE_col=enrich_TE.iloc[i]
 if(len(cc_data[cc_data.Family==TE_col.Family])>0):
  f_data=cc_data[cc_data.Family==TE_col.Family].iloc[0]
  wantdata.append([TE_col.Family,TE_col.Superfamily,TE_col.Class,f_data.nearest_count,f_data.CC1,f_data.pvalue,f_data.CC2,f_data.CC3,f_data.CC4,f_data.CC5,f_data.CC6,f_data.CC7,f_data.CC8,f_data.CC9,f_data.CC10])
 else:
  wantdata.append([TE_col.Family,TE_col.Superfamily,TE_col.Class,0,0,0])
wantdata=pd.DataFrame(wantdata,columns=indexes)
wantdata.to_csv("{}/CC_enrich.txt".format(directory),sep='\t',index=False)
