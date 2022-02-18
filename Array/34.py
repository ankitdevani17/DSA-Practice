def pal(num):
    temp =str(num)
    if temp==temp[::-1]:
        return True
    return False    
def PalinArray(arr ,n):
    for x in arr:
        if not pal(x):
            return 0
    return 1        
    

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)