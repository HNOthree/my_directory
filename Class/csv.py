From =int(input())-1
To=int(input())-1

import sys



all_data = sys.stdin.readlines()
print_list=[]
for data in all_data:
    data=data.replace("\n","")
    data=data.split(",")
    ref=data[To]
    data[To]=data[From]
    data[From]=ref
    print_list.append(data)

for i in print_list:
          sen=""
          for j in i:
              sen=sen+j+","
          sen=sen[:-1]
          print(sen)

