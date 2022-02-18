
def minSwap (arr, n, k) : 
    swap_count = 0
    count = 0
    low = 0
    for i in arr:
        if i <= k:
            count += 1
    
    for i in range(count):
        if arr[i] > k:
            swap_count += 1
    
    min_swap = swap_count
    i += 1
    while i < n:
        if arr[low] > k:
            swap_count -= 1
        if arr[i] > k:
            swap_count += 1
        if min_swap > swap_count:
            min_swap = swap_count
        i += 1
        low += 1
    
    return min_swap


#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
    