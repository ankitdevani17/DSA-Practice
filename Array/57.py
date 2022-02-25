s= "1225556"
snew=""
current = s[0]
count=1
for i in range(1,len(s)):
        if s[i]==current:
            count+=1
        else:
            snew+=str(count)+current
            current=s[i]
            count=1
print(snew)
