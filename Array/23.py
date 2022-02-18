import numpy
class Solution:


    def maxProduct(self,arr, N):
        # code here
        '''pro=numpy.prod(arr)
        k=1
        for k in range(1,N):
            i=0
            j=0
            pro1=1
            while(j<N):
                pro1*=arr[j]
                if(j-i+1==k):
                    pro=max(pro,pro1)
                    pro1-=arr[i]
                    i+=1
                j+=1
        return pro'''
        ans = arr[0]
        mx = arr[0]
        mn = arr[0]
        for i in range(1,n):
            if(arr[i] < 0):
                mx,mn=mn,mx
            mx = max(arr[i],mx*arr[i])
            mn = min(arr[i],mn*arr[i])
            ans = max(ans,mx)
        return (ans)




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1