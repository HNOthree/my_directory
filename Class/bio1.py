i = int(input())
j = int(input())

for k in range(i,j+1):
    if(k%3==0 and k %5==0):
        print("Fizz Buzz")
    elif (k%3==0):
        print("Fizz")
    elif(k%5==0):
        print("Buzz")
    else:
        print(k)