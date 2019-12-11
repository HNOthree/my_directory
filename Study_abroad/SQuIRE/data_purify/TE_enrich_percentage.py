import pandas as pd
threshold="25"
TE_data=pd.read_csv("/home/smiyake/shares/Sho/Results/SQuIRE/txt/TE_in_enrichregion_{}k_all.txt".format(threshold),sep='\t')

familylist=[]
for i in TE_data.Family:
 if i not in familylist:
  familylist.append(i)

p_wantdata=[]
c_wantdata=[]
for family in familylist:
 familydata=TE_data[TE_data.Family==family]
 male=familydata[familydata.Sexuality=="male"]
 female=familydata[familydata.Sexuality=="female"]
 other=familydata[familydata.Sexuality=="Other"]
 all_length=float(len(male)+len(female)+len(other))
 p_wantdata.append([family,familydata.iloc[0].Superfamily,familydata.iloc[0].Class,int(all_length),len(male)/all_length,len(female)/all_length,len(other)/all_length])
 c_wantdata.append([family,familydata.iloc[0].Superfamily,familydata.iloc[0].Class,int(all_length),len(male),len(female),len(other)])

p_wantdata=pd.DataFrame(p_wantdata,columns=["Family","Superfamily","Class","Count","Male","Female","Other"])
c_wantdata=pd.DataFrame(c_wantdata,columns=["Family","Superfamily","Class","Count","Male","Female","Other"])
p_wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/family_percentage_enrich_{}k_percentage.txt".format(threshold),index=False,sep='\t')
c_wantdata.to_csv("/home/smiyake/sho/Fullset/SQuIRE/txt/family_percentage_enrich_{}k_count.txt".format(threshold),index=False,sep='\t')
