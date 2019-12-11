import pandas as pd
new=[]
female=[]
male=[]
TE_id=[]
for i in range(1,4):
 print(i)
 data=pd.read_csv("/mnt/SQUIRE_all/squire_count/Clean{}latF_Fullset_TEcounts.txt".format(i),sep='\t')
 #data=data.head(100)
 for ID in data.TE_ID:
   if ID not in new:
    new.append(ID)
   female.append([ID,1])
   TE_id.append([ID,1])
#TE_id=pd.DataFrame(TE_id,columns=["ID","Count"])

for i in range(4,7):
 print(i)
 data=pd.read_csv("/mnt/SQUIRE_all/squire_count/Clean{}latM_Fullset_TEcounts.txt".format(i),sep='\t')
 #data=data.head(100)
 for ID in data.TE_ID:
   if ID not in new:
    new.append(ID)
   male.append([ID,1])
   TE_id.append([ID,1])
TE_id=pd.DataFrame(TE_id,columns=["ID","Count"])
male=pd.DataFrame(male,columns=["ID","Count"])
female=pd.DataFrame(female,columns=["ID","Count"])

TE_id_group=TE_id.groupby("ID").count()
male=male.groupby("ID").count()
female=female.groupby("ID").count()


TE_id_group.to_csv("/mnt/Result/TE_count_experiment.txt",sep='\t',index=True)
common=TE_id_group[TE_id_group.Count==6]
print('Male common',len(male[male.Count==3]))
male.to_csv("/mnt/Result/TE_count_male.txt",sep='\t',index=True)
print('Female common',len(female[female.Count==3]))
female.to_csv("/mnt/Result/TE_count_female.txt",sep='\t',index=True)

#common=common.reset_index()
#print(common)
print(len(common))
common.to_csv("/mnt/Result/common_experiment.txt",sep='\t',index=True)
print("all kinds",len(new))
print("male kinds",len(male))
print("female kinds",len(female))

