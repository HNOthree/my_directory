index=input()
import sys
if len(sys.argv)<=1:
    print("ERROR")
    sys.exit(1)


def calculate(sequence,index,gene):
    count=0
    for i in range(0,len(sequence)-len(index)+1):
        for j in range(0,len(index)+1):
            if(j==len(index)):
                count+=1
                break
            elif(sequence[i+j]==index[j]):
                continue
            else:
                break
    print(gene+": "+str(count))

input_file_name=sys.argv[1]

j=0
sequence=""
gene_list=""
with open(input_file_name,"r") as f:
    for i in f.readlines():
        if (j==0):
             index=i
             index=index.replace("\n","")
             j+=1
        elif (">"in i):
            if sequence!="":
                calculate(sequence,index,gene_list)
                sequence=""
            i=i.split(" ")
            i=i[0]
            i=i.replace(">","")
            i=i.replace("\n","")
            gene_list=i
            j+=1
        else:
            i=i.replace("\n","")
            sequence+=i
        
calculate(sequence,index,gene_list)

