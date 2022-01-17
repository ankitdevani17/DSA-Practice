class Solution:
    def minJumps(self, arr, n):
        i=0
        ans=0
        if len(arr)==1:
            return 0
        while i<len(arr):
            mx=0
           
            if arr[i]==0:
                return -1
            if arr[i]+1+i>n-1:
                return ans+1
            for j in range(i+1,arr[i]+1+i,1):
                
                if arr[j]+j>mx:
                    mx=arr[j]+j
                    i=j
                
            ans+=1
        return ans
            

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
