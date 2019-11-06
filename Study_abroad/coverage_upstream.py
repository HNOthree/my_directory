#calculate TE coverage

import pandas as pd
import matplotlib.pyplot as plt
#threshold is xlim in figure
threshold=10000
bins=50
sample=[0,0]
#Data that contains an infomation about which TE is upstream of each gene
upstream_data=pd.read_csv("/home/smiyake/sho/Fullset/txt/merge_transcript_TE_upstream_50000.txt",sep='\t')
print(upstream_data.head(5))
print(len(upstream_data))
index_list=["Class"]
for i in range(0,threshold,threshold/bins):
 index_list.append(i)

Class_list=["DNA","DNA?","LINE","LTR","nonLTR","RC","Retro","SINE","Unknown","Unspecified"]

Class_coverage=[]
for Class in Class_list:
 input_data=[Class]
 for i in range(bins):
  input_data.append(0.0)
 Class_coverage.append(input_data)

Class_coverage=pd.DataFrame(Class_coverage,columns=index_list)
Class_coverage=Class_coverage.set_index("Class")
data_count=float(len(upstream_data)*len(Class_coverage))
print(data_count)
for i in range(len(upstream_data)):
 if(i%100000==0):
  print(i)
 col=upstream_data.iloc[i]
 if(col.Distance<threshold):
  Class=col.TE_Class
  start_distance=col.Distance
  end_distance=(col.TE_end-col.TE_start)+start_distance
  start_position=int(start_distance/(threshold/bins))*(threshold/bins)
  end_position=int(end_distance/(threshold/bins)+1)*(threshold/bins)
  #print(col.Strand,start_position,end_position,start_distance,end_distance,col.TE_end-col.TE_start)
  start=start_distance 
  for k in range(start_position,end_position,threshold/bins):
   if(k>=threshold):
    break
   elif(end_distance<k+(threshold/bins)):
    end=end_distance
   else:
    end=k+(threshold/bins)
   Class_coverage.at[Class,k]+=float(end-start)/(threshold/bins)*100
   if(float(end-start)/(threshold/bins)*100>100):
    print("k start_pos end_pos start end ")
    print(k,start_position,end_position,end-start,float(end-start)/(threshold/bins)*100)
   start=end
for i in range(len(Class_coverage)):
 for j in range(bins):
  Class_coverage.iat[i,j]=Class_coverage.iat[i,j]/(data_count)
print(Class_coverage)
Class_coverage_T=Class_coverage.T
Class_coverage_T.plot.bar(width=1,stacked=True)
plt.xlabel('Distance')
plt.ylabel('Percentage')
plt.savefig("TE_coverage.png",dpi=300)
print(sample)
#plt.show()
#plt.hist(upstream_data[upstream_data.Distance<10000].Distance,bins=20)
#plt.xlim(0,10000)
#plt.savefig("b.png",dpi=300)
  #Class_coverage.at[Class,int(col.Distance/(threshold/bins))*(threshold/bins)]+=1
