a =[6,9,9]
am = min(a[0],a[len(a)-1])
sum=0
for i in range(1,len(a)-1):
    temp = am-a[i]
    sum=sum+temp
if sum >0:
    print(sum)
else:
    print(0)