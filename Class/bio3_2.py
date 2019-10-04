import os
file_name=input()
search_term=input()
output_name=input()
if (os.path.exists("./{}".format(file_name)) !=True):
    print("ERROR")
else:
    f=open(file_name,'r')
    w=open(output_name,"w")
    row=1
    count=1
    for i in f.readlines():
        if( search_term in i):
            w.write("line {}, hit #{}: {}".format(row,count,i))
            #w.write("line "+str(row)+", hit #"+str(count)+":"+i)
            count+=1
        row+=1
    f.close()
    w.close()