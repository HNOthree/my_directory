import sys
import re

def counting(motif,seq,name):

    if (seq=="0"):
        return "0"
    else:
        count=0
        while(True):
            seq=seq.replace("\n","")
            location =seq.find(motif)
            if(location==-1):
                break  
            else:
                seq=seq[location+1:]
                count+=1
        print("{}: {}".format(name,count))
        return "0"


motif = input()
all_data = sys.stdin.readlines()

seq_name=""
seq=""
for data in all_data:
    if(len(data)==0):
        continue
    elif (">" in data):
        seq=counting(motif,seq,seq_name)
        seq_name=data.split(" ")
        seq_name=seq_name[0]
        seq_name=seq_name.replace(">","")
        seq_name=seq_name.replace("\n","")

    else:
        seq =seq[:-1]+data
#print(motif,seq,seq_name)
counting(motif,seq,seq_name)
