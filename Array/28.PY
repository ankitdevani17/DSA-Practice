arr =  [1,4,45,6,10,8]
x=13

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(x-(i+j)) in arr:
            print("1")
            exit()