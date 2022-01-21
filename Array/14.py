arr = [[1,3],[2,6],[8,10]]
i=0
while i<=len(arr)+1:
    if arr[i+1][0] >= arr[i][1]:
        arr[i]= [arr[i][0],arr[i+1][1]]
        i=i-1

print(arr)