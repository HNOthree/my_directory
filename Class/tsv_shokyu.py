import sys

all_data = sys.stdin.readlines()
print_list=[]
chr_list=[]
count_dic={}
sum_dic={}
for data in all_data:
    data=data.split("\t")
    
    if("211" in data[0] or "Unmapped" in data[0]):
        continue
    if("gene"==data[2]):
        #print(data)
        if(data[0] not in chr_list):
            chr_list.append(data[0])
            count_dic[data[0]]=1
            sum_dic[data[0]]=int(data[4])-int(data[3])+1
        else:
            count_dic[data[0]]=count_dic[data[0]]+1
            sum_dic[data[0]]+=(int(data[4])-int(data[3]))+1

chr_list.sort()
print("Chromosome,Gene Count,Avg Size")

for chr in chr_list:
    print("{}\t{}\t{}".format(chr,count_dic[chr],int(sum_dic[chr]/count_dic[chr])))