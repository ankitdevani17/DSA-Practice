
class Solution:
    def merge(self, arr1, arr2, n, m): 
        def function(a1,a2):
            i = len(a1)-1
            j = 0
            while( i>=0 and j<=len(a2)-1):
                if( a1[i] >= a2[j] ):
                    temp = a1[i]
                    a1[i] = a2[j]
                    a2[j] = temp
                    i-=1
                    j+=1
                else:
                    i-=1
                    j+=1
                
            a1.sort()
            a2.sort()
        function(arr1,arr2)

if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
