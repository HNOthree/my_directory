import sys



all_data = sys.stdin.readlines()
printlist=[]
for a in all_data:
    if(">" in a):
        if("Chr" in a):
            a=a.split(" ")
            gene=a[1]
            Ch=a[4]
            sentence=gene+",Chr "+Ch
            printlist.append(sentence)
        else:
            a=a.split(" ")
            gene=a[1]
            gene=gene.replace(">","")
            sentence=gene+",plasmid"
            printlist.append(sentence)
for i in printlist:
    print(i)


# while(True):
#     a=input()
#     if(a==""):
#         break
#     if(">" in a):
#         if("Chr" in a):
#             a=a.split(" ")
#             gene=a[0]
#             gene=gene.replace(">","")
#             Ch=a[4]
#             sentence=gene+",Chr "+Ch
#             printlist.append(sentence)
#         else:
#             a=a.split(" ")
#             gene=a[0]
#             gene=gene.replace(">","")
#             sentence=gene+",Chr plasmid"
#             printlist.append(sentence)
# for i in printlist:
#     print(i)
