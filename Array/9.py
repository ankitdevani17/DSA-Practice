def getMinDiff(self, arr, n, k):
        arr.sort()
        ans=arr[n-1]-arr[0]
        
        for i in range(1,n):
            if arr[i]>=k:
                maxi=max(arr[i-1]+k,arr[n-1]-k)
                mini=min(arr[0]+k,arr[i]-k)
                ans=min(ans,maxi-mini)
        return ans

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

