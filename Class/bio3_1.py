import os
text = input()
if (os.path.exists("./{}".format(text)) !=True):
    print("ERROR")
else:
    f=open(text,'r')
    row=1
    for i in f.readlines():
        i.strip()
        if("\n" in i ):
            figure=str(row)+": "+i[:-1]
        else:
            figure=str(row)+": "+i
        print(figure)
        row+=1
    f.close()
