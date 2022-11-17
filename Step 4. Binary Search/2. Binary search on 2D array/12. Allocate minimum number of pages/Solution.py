class Solution:
    def findPages(self,A, N, M):
        def possible(target):
            pages=0
            students=1
            for i in A:
                if i>target:
                    return False
                if pages + i > target:
                    pages= i
                    students+=1
                else:
                    pages+=i
            if students>M:
                return False
            else:
                return True
        low= min(A)
        high= sum(A)
        res=-1
        while low<=high:
            mid= (low+high)>>1
            if possible(mid):
                res= mid
                high= mid-1
            else:
                low= mid+1
        if N<M:
            return -1
        else:
            return res
        
#{ 
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends
