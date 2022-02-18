arr =[1,9,3,10,4,20,2]
marr = max(arr)
minarr = min(arr)
cnt=0
temp2=0
temp = minarr - 1
for i in range(minarr,marr+1):
    if i == temp+1 & i in arr:
        cnt = cnt +1
        temp = i
    else :
        if cnt>temp2:
            temp2=cnt
        cnt = 0
print(temp2)


