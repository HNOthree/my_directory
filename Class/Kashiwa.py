import sys

# if len(sys.argv)<=1:
#     print("ERROR")
#     sys.exit(1)

column=int(input())
word=input()
index=input()
match=[]
all_data=sys.stdin.readlines()
print_list=[]
for data in all_data:
    if(word in data):
        data=data.replace("\n","")
        match.append(data)

    
print(index)
for i in match:
    print(i)

# while(True):
#     a=input()
#     if(a==""):
#         break
#     else:
#         if(word in a):
#             match.append(a)
#     a=a.split(" ")
# print(index)
# for i in match:
#     print(i)
