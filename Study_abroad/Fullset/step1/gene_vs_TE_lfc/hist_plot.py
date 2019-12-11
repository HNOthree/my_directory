import pandas as pd
import matplotlib.pyplot as plt

def hist_plot(location,family_list,data_pd):
  for j in family_list:
   family_data=data_pd[data_pd.TE_family==j]
   plt.hist(family_data.Distance,bins=50,cumulative=False)
   plt.xlim(0,500000)
   plt.xlabel("Distance")
   plt.ylabel("Counts")
   plt.savefig("{}_{}hist.png".format(location,j),dpi=300,x_inches='tight')
   plt.figure()

names=["up","down"]
family_list=[]
for i in names:
 data=pd.read_csv("/home/smiyake/sho/Fullset/txt/{}stream_Gene_TE_merge_data.txt".format(i),sep="\t")
 data.head(5)
 class_list=[]
 #family_list=[]
 for j in data.TE_class:
  if j not in class_list:
   class_list.append(j)
 
 for j in data.TE_family:
  if j not in family_list:
   family_list.append(j)
 all_list=[]
print(len(family_list))
print(family_list)
 #hist_plot(i,family_list,data)
