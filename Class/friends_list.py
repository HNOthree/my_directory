name_dict={}
name_list=[]
name=[]
while True:
    name.append(input())
    name.append(input())
    if(name[1]=="END" and name[0]=="END"):
        break
    else:
        for na in name:
            if (na not in name_list):
                name_list.append(na)
                name_dict[na]=1
            else :
                name_dict[na]+=1

    name=[]
max_key = max(name_dict, key=name_dict.get)
max_value = max(name_dict.values())

print(max_key,max_value)