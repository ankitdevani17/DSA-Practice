def inversionCount(self, arr, n):

        inv_cnt = 0
        if len(arr)>1:
            mid = len(arr)//2
            L=  arr[:mid]
            R = arr[mid:]
            inv_cnt+=self.inversionCount(L,len(L))
            inv_cnt+=self.inversionCount(R,len(R))
            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i]<=R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                    inv_cnt+=mid-i
                k+=1
                
            while i<len(L):
                arr[k] = L[i]
                i+=1
                k+=1
            while j<len(R):
                arr[k] = R[j]
                j+=1
                k+=1
        return inv_cnt


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))