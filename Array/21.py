    
def subArrayExists( self , A , n ):
        
        S = set()
        
        x = 0
        
        for i in A:
            
            x += i
            
            if x == 0 or x in S:
                
                return 1
                
            S.add( x )
            
        return 0




def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()

        
        
