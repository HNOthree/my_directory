import sys



all_data = sys.stdin.readlines()
print_list=[]
for data in all_data:
    if '"' in data:
        col=""
        quote_count=0
        for term in data:
            if(term=='"'):
                quote_count+=1
                continue
            if(quote_count%2==0 and term==","):
                col=col+"\t"
            else:
                col=col+term
        col=col.replace("\n","")   
        print_list.append(col)

    
    else:
        data=data.replace(',',"\t")
        data=data.replace('\n',"")
        print_list.append(data)

for data in print_list:
    print(data)