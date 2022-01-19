class Solution:
    def maxSubArraySum(self,arr,N):
        curr=arr[0]
        maxe=arr[0]
        for i in range(1,N):
            curr=max(arr[i],arr[i]+curr)
            if maxe<curr:
                maxe=curr
        return maxe


import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
