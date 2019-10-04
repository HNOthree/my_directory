import re
while(True):
    a=input()
    if("added" in a):
        a=a.split(" ")
        a=a[5]
        print(a)
        break